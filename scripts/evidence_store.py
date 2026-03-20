"""Evidence store for Dossier Loop.

Manages evidence across 6 durability tiers with promotion gates.
Uses SQLite for local-first persistence.

Tiers (from ResearchLoopContract):
  raw -> working -> verified -> promoted -> training -> locked

Usage:
  from scripts.evidence_store import EvidenceStore
  store = EvidenceStore()  # uses default path: data/evidence.db
  store.insert("RLC.001", "source-1", "content here", {"key": "val"})
  store.promote("RLC.001", "<hash>", "working", confidence=0.5)
"""
from __future__ import annotations

import hashlib
import json
import math
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

SCHEMA = """
CREATE TABLE IF NOT EXISTS evidence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hash TEXT UNIQUE NOT NULL,
    contract_id TEXT NOT NULL,
    tier TEXT NOT NULL DEFAULT 'raw',
    source_id TEXT NOT NULL,
    content TEXT NOT NULL,
    metadata TEXT,
    confidence REAL DEFAULT 0.0,
    corroboration_count INTEGER DEFAULT 0,
    created_at TEXT NOT NULL,
    updated_at TEXT,
    promoted_at TEXT,
    expires_at TEXT,
    cycle_number INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS signals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    evidence_id INTEGER REFERENCES evidence(id),
    contract_id TEXT NOT NULL,
    dimension TEXT NOT NULL,
    score REAL NOT NULL,
    scorer TEXT NOT NULL,
    cycle_number INTEGER NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS cycles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contract_id TEXT NOT NULL,
    cycle_number INTEGER NOT NULL,
    phase TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending',
    started_at TEXT,
    completed_at TEXT,
    artifacts TEXT,
    notes TEXT
);

CREATE INDEX IF NOT EXISTS idx_evidence_contract ON evidence(contract_id);
CREATE INDEX IF NOT EXISTS idx_evidence_tier ON evidence(tier);
CREATE INDEX IF NOT EXISTS idx_evidence_source ON evidence(source_id);
CREATE INDEX IF NOT EXISTS idx_signals_evidence ON signals(evidence_id);
CREATE INDEX IF NOT EXISTS idx_cycles_contract ON cycles(contract_id, cycle_number);
"""

TIERS = ["raw", "working", "verified", "promoted", "training", "locked"]

DEFAULT_DB = Path(__file__).parent.parent / "data" / "evidence.db"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _hash_content(source_id: str, content: str) -> str:
    """SHA-256 hash of source + content for dedup."""
    return hashlib.sha256(f"{source_id}:{content}".encode()).hexdigest()[:16]


class EvidenceStore:
    """SQLite-backed evidence store with tier promotion."""

    def __init__(self, db_path: Union[str, Path, None] = None):
        self.db_path = Path(db_path) if db_path else DEFAULT_DB
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)

    def close(self):
        self.conn.close()

    def insert(
        self,
        contract_id: str,
        source_id: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None,
        cycle_number: int = 0,
    ) -> Optional[str]:
        """Insert raw evidence. Returns hash, or None if duplicate."""
        h = _hash_content(source_id, content)
        try:
            self.conn.execute(
                """INSERT INTO evidence
                   (hash, contract_id, source_id, content, metadata,
                    created_at, cycle_number)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (h, contract_id, source_id, content,
                 json.dumps(metadata) if metadata else None,
                 _now(), cycle_number),
            )
            self.conn.commit()
            return h
        except sqlite3.IntegrityError:
            # Duplicate — increment corroboration
            self.conn.execute(
                """UPDATE evidence
                   SET corroboration_count = corroboration_count + 1,
                       updated_at = ?
                   WHERE hash = ?""",
                (_now(), h),
            )
            self.conn.commit()
            return None

    def get(self, evidence_hash: str) -> Optional[Dict[str, Any]]:
        """Get evidence by hash."""
        row = self.conn.execute(
            "SELECT * FROM evidence WHERE hash = ?", (evidence_hash,)
        ).fetchone()
        return dict(row) if row else None

    def query(
        self,
        contract_id: str,
        tier: Optional[str] = None,
        source_id: Optional[str] = None,
        cycle_number: Optional[int] = None,
        limit: int = 100,
    ) -> List[Dict[str, Any]]:
        """Query evidence with optional filters."""
        sql = "SELECT * FROM evidence WHERE contract_id = ?"
        params: list = [contract_id]
        if tier:
            sql += " AND tier = ?"
            params.append(tier)
        if source_id:
            sql += " AND source_id = ?"
            params.append(source_id)
        if cycle_number is not None:
            sql += " AND cycle_number = ?"
            params.append(cycle_number)
        sql += " ORDER BY created_at DESC LIMIT ?"
        params.append(limit)
        return [dict(r) for r in self.conn.execute(sql, params).fetchall()]

    def promote(
        self,
        contract_id: str,
        evidence_hash: str,
        target_tier: str,
        confidence: Optional[float] = None,
    ) -> bool:
        """Promote evidence to a higher tier. Returns success."""
        if target_tier not in TIERS:
            return False
        row = self.get(evidence_hash)
        if not row or row["contract_id"] != contract_id:
            return False
        current_idx = TIERS.index(row["tier"])
        target_idx = TIERS.index(target_tier)
        if target_idx <= current_idx:
            return False  # Can only promote upward
        updates = {"tier": target_tier, "promoted_at": _now(), "updated_at": _now()}
        if confidence is not None:
            updates["confidence"] = confidence
        set_clause = ", ".join(f"{k} = ?" for k in updates)
        self.conn.execute(
            f"UPDATE evidence SET {set_clause} WHERE hash = ?",
            list(updates.values()) + [evidence_hash],
        )
        self.conn.commit()
        return True

    def add_signal(
        self,
        evidence_id: int,
        contract_id: str,
        dimension: str,
        score: float,
        scorer: str,
        cycle_number: int,
    ) -> int:
        """Record a signal score for evidence."""
        cur = self.conn.execute(
            """INSERT INTO signals
               (evidence_id, contract_id, dimension, score, scorer,
                cycle_number, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (evidence_id, contract_id, dimension, score, scorer,
             cycle_number, _now()),
        )
        self.conn.commit()
        return cur.lastrowid

    def record_cycle(
        self,
        contract_id: str,
        cycle_number: int,
        phase: str,
        status: str = "pending",
    ) -> int:
        """Record a cycle phase execution."""
        cur = self.conn.execute(
            """INSERT INTO cycles
               (contract_id, cycle_number, phase, status, started_at)
               VALUES (?, ?, ?, ?, ?)""",
            (contract_id, cycle_number, phase, status, _now()),
        )
        self.conn.commit()
        return cur.lastrowid

    def complete_cycle(self, cycle_id: int, status: str, notes: Optional[str] = None):
        """Mark a cycle phase as complete."""
        self.conn.execute(
            """UPDATE cycles SET status = ?, completed_at = ?, notes = ?
               WHERE id = ?""",
            (status, _now(), notes, cycle_id),
        )
        self.conn.commit()

    def source_entropy(self, contract_id: str) -> float:
        """Shannon entropy of source distribution. Anti-recursion guard."""
        rows = self.conn.execute(
            """SELECT source_id, COUNT(*) as cnt
               FROM evidence WHERE contract_id = ?
               GROUP BY source_id""",
            (contract_id,),
        ).fetchall()
        if not rows:
            return 0.0
        total = sum(r["cnt"] for r in rows)
        entropy = 0.0
        for r in rows:
            p = r["cnt"] / total
            if p > 0:
                entropy -= p * math.log2(p)
        return round(entropy, 3)

    def self_citation_ratio(self, contract_id: str) -> float:
        """Fraction of evidence sourced from own prior outputs. Anti-recursion guard."""
        total = self.conn.execute(
            "SELECT COUNT(*) FROM evidence WHERE contract_id = ?",
            (contract_id,),
        ).fetchone()[0]
        if total == 0:
            return 0.0
        self_refs = self.conn.execute(
            """SELECT COUNT(*) FROM evidence
               WHERE contract_id = ? AND source_id LIKE 'self:%'""",
            (contract_id,),
        ).fetchone()[0]
        return round(self_refs / total, 3)

    def tier_counts(self, contract_id: str) -> Dict[str, int]:
        """Count evidence per tier."""
        rows = self.conn.execute(
            """SELECT tier, COUNT(*) as cnt FROM evidence
               WHERE contract_id = ? GROUP BY tier""",
            (contract_id,),
        ).fetchall()
        return {r["tier"]: r["cnt"] for r in rows}

    def score_evidence(
        self,
        contract_id: str,
        evidence_hash: str,
        scores: Dict[str, float],
        scorer: str,
        cycle_number: int,
    ) -> Optional[float]:
        """Batch-score evidence across multiple dimensions.

        Args:
            scores: Dict mapping dimension name to score (0.0-1.0).
            scorer: Who scored (e.g., 'llm', 'rule', 'hybrid').

        Returns:
            Composite score (weighted average) or None if evidence not found.
            Weights are equal unless caller pre-weights the scores dict.
        """
        row = self.get(evidence_hash)
        if not row or row["contract_id"] != contract_id:
            return None
        eid = row["id"]
        for dim, score in scores.items():
            self.add_signal(eid, contract_id, dim, score, scorer, cycle_number)
        composite = sum(scores.values()) / len(scores) if scores else 0.0
        # Update evidence confidence to composite score
        self.conn.execute(
            "UPDATE evidence SET confidence = ?, updated_at = ? WHERE hash = ?",
            (round(composite, 3), _now(), evidence_hash),
        )
        self.conn.commit()
        return round(composite, 3)

    def query_signals(
        self,
        contract_id: str,
        cycle_number: Optional[int] = None,
        dimension: Optional[str] = None,
        evidence_id: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """Query signals with optional filters."""
        sql = "SELECT * FROM signals WHERE contract_id = ?"
        params: list = [contract_id]
        if cycle_number is not None:
            sql += " AND cycle_number = ?"
            params.append(cycle_number)
        if dimension:
            sql += " AND dimension = ?"
            params.append(dimension)
        if evidence_id is not None:
            sql += " AND evidence_id = ?"
            params.append(evidence_id)
        sql += " ORDER BY created_at DESC"
        return [dict(r) for r in self.conn.execute(sql, params).fetchall()]

    def compute_corroboration(self, contract_id: str) -> Dict[str, int]:
        """Compute cross-source corroboration for all evidence.

        Two evidence items corroborate each other when they share topic tags
        but come from different sources. For each item, corroboration_count =
        number of distinct OTHER sources with overlapping topic tags.

        Returns dict of {hash: new_corroboration_count}.
        """
        evidence = self.query(contract_id, limit=10000)
        # Build tag -> set of (source_id, hash) mapping
        tag_sources: Dict[str, List[tuple]] = {}
        item_tags: Dict[str, List[str]] = {}
        for e in evidence:
            tags = []
            if e["metadata"]:
                try:
                    meta = json.loads(e["metadata"]) if isinstance(e["metadata"], str) else e["metadata"]
                    tags = meta.get("topic_tags", [])
                except (json.JSONDecodeError, AttributeError):
                    pass
            item_tags[e["hash"]] = tags
            for tag in tags:
                tag_sources.setdefault(tag, []).append((e["source_id"], e["hash"]))

        # For each item, count distinct sources sharing any tag (excluding self)
        results = {}
        for e in evidence:
            other_sources = set()
            for tag in item_tags.get(e["hash"], []):
                for src_id, h in tag_sources.get(tag, []):
                    if src_id != e["source_id"]:
                        other_sources.add(src_id)
            count = len(other_sources)
            if count != e["corroboration_count"]:
                self.conn.execute(
                    "UPDATE evidence SET corroboration_count = ?, updated_at = ? WHERE hash = ?",
                    (count, _now(), e["hash"]),
                )
            results[e["hash"]] = count
        self.conn.commit()
        return results

    def get_silence_events(
        self,
        contract_id: str,
        cycle_number: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """Get silence evidence (metadata.type == 'silence').

        Silence events are regular evidence items with metadata containing:
        - type: "silence"
        - last_seen: ISO timestamp of last known activity
        - days_silent: integer
        - confidence: 0.0-1.0 (how confident we are this is real silence vs search artifact)
        """
        sql = """SELECT * FROM evidence
                 WHERE contract_id = ? AND metadata LIKE '%"type": "silence"%'"""
        params: list = [contract_id]
        if cycle_number is not None:
            sql += " AND cycle_number = ?"
            params.append(cycle_number)
        sql += " ORDER BY created_at DESC"
        return [dict(r) for r in self.conn.execute(sql, params).fetchall()]
