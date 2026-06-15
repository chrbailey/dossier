#!/usr/bin/env python3
"""
Signal Database v2 for Dossier Pulse — validated computation.

Replaces signal_db.py:
- Sentiment thresholds stored in pulse_config table (not hardcoded)
- Thresholds logged with every pulse export
- All real computation preserved (weighted sentiment, momentum, coverage)

Usage:
    python signal_db_v2.py init <domain>
    python signal_db_v2.py import-accounts <domain> <social-signals-x.md>
    python signal_db_v2.py add-signal <domain> '<json>'
    python signal_db_v2.py update-pulse <domain>
    python signal_db_v2.py export <domain> [output_path]
    python signal_db_v2.py summary <domain>
    python signal_db_v2.py config <domain> [key] [value]
"""

import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


DB_DIR = "output"


def get_db_path(domain: str) -> str:
    return os.path.join(DB_DIR, domain, "signals.db")


def get_conn(domain: str) -> sqlite3.Connection:
    db_path = get_db_path(domain)
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db(domain: str):
    conn = get_conn(domain)
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS accounts (
            handle TEXT PRIMARY KEY,
            name TEXT,
            category TEXT,
            relevance INTEGER DEFAULT 0,
            followers TEXT,
            signal_summary TEXT,
            added_at TEXT DEFAULT (datetime('now')),
            last_seen TEXT,
            active INTEGER DEFAULT 1
        );

        CREATE TABLE IF NOT EXISTS signals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            handle TEXT NOT NULL,
            content TEXT,
            source_url TEXT,
            sentiment REAL DEFAULT 0.0,
            relevance REAL DEFAULT 0.5,
            category TEXT,
            signal_type TEXT,
            detected_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (handle) REFERENCES accounts(handle)
        );

        CREATE TABLE IF NOT EXISTS pulse (
            domain TEXT NOT NULL,
            metric TEXT NOT NULL,
            value REAL,
            label TEXT,
            updated_at TEXT DEFAULT (datetime('now')),
            PRIMARY KEY (domain, metric)
        );

        CREATE TABLE IF NOT EXISTS history (
            domain TEXT NOT NULL,
            date TEXT NOT NULL,
            metric TEXT NOT NULL,
            value REAL,
            signal_count INTEGER DEFAULT 0,
            PRIMARY KEY (domain, date, metric)
        );

        CREATE TABLE IF NOT EXISTS pulse_config (
            key TEXT PRIMARY KEY,
            value REAL,
            source TEXT DEFAULT 'default_uncalibrated',
            updated_at TEXT DEFAULT (datetime('now'))
        );

        CREATE INDEX IF NOT EXISTS idx_signals_handle ON signals(handle);
        CREATE INDEX IF NOT EXISTS idx_signals_detected ON signals(detected_at);
        CREATE INDEX IF NOT EXISTS idx_signals_sentiment ON signals(sentiment);
    """)

    defaults = [
        ("bullish_threshold", 0.3),
        ("slight_bullish_threshold", 0.1),
        ("slight_bearish_threshold", -0.1),
        ("bearish_threshold", -0.3),
        ("bullish_pct_threshold", 0.2),
        ("bearish_pct_threshold", -0.2),
    ]
    for key, value in defaults:
        conn.execute("""
            INSERT OR IGNORE INTO pulse_config (key, value, source)
            VALUES (?, ?, 'default_uncalibrated')
        """, (key, value))

    conn.commit()
    conn.close()
    print(json.dumps({"status": "initialized", "domain": domain, "db": get_db_path(domain)}))


def get_config(conn: sqlite3.Connection) -> dict:
    config = {}
    for row in conn.execute("SELECT key, value, source FROM pulse_config"):
        config[row["key"]] = {"value": row["value"], "source": row["source"]}
    return config


def get_threshold(config: dict, key: str, default: float) -> float:
    if key in config:
        return config[key]["value"]
    return default


def set_config(domain: str, key: str, value: float):
    conn = get_conn(domain)
    conn.execute("""
        INSERT OR REPLACE INTO pulse_config (key, value, source, updated_at)
        VALUES (?, ?, 'user_configured', datetime('now'))
    """, (key, value))
    conn.commit()
    conn.close()
    print(json.dumps({"status": "config_updated", "key": key, "value": value}))


def show_config(domain: str):
    conn = get_conn(domain)
    config = get_config(conn)
    conn.close()
    print(json.dumps(config, indent=2))


def import_accounts(domain: str, md_path: str):
    text = Path(md_path).read_text(encoding="utf-8")
    conn = get_conn(domain)

    imported = 0
    in_table = False
    header_found = False

    for line in text.split("\n"):
        line = line.strip()
        if not line.startswith("|"):
            if in_table and header_found:
                break
            continue

        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) < 5:
            continue

        if all(re.match(r"^[-:]+$", c) for c in cols):
            header_found = in_table
            continue

        if any("rank" in c.lower() for c in cols) and any("handle" in c.lower() for c in cols):
            in_table = True
            continue

        if in_table and header_found:
            try:
                handle = cols[1].strip() if len(cols) > 1 else ""
                name = cols[2].strip() if len(cols) > 2 else ""
                category = cols[3].strip() if len(cols) > 3 else "Other"

                relevance_str = cols[4] if len(cols) > 4 else "0"
                rel_match = re.search(r"(\d+)", relevance_str)
                relevance = int(rel_match.group(1)) if rel_match else 0

                followers = cols[5].strip() if len(cols) > 5 else ""
                signal = cols[6].strip() if len(cols) > 6 else ""

                if handle and handle.startswith("@"):
                    conn.execute("""
                        INSERT OR REPLACE INTO accounts
                        (handle, name, category, relevance, followers, signal_summary, last_seen)
                        VALUES (?, ?, ?, ?, ?, ?, datetime('now'))
                    """, (handle, name, category, relevance, followers, signal))
                    imported += 1
            except (ValueError, IndexError):
                continue

    conn.commit()
    conn.close()
    print(json.dumps({"status": "imported", "domain": domain, "accounts": imported}))


def add_signal(domain: str, signal_json: str):
    data = json.loads(signal_json)
    conn = get_conn(domain)

    conn.execute("""
        INSERT INTO signals (handle, content, source_url, sentiment, relevance, category, signal_type)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("handle", ""),
        data.get("content", ""),
        data.get("source_url", ""),
        data.get("sentiment", 0.0),
        data.get("relevance", 0.5),
        data.get("category", ""),
        data.get("signal_type", "post"),
    ))

    conn.execute("""
        UPDATE accounts SET last_seen = datetime('now') WHERE handle = ?
    """, (data.get("handle", ""),))

    conn.commit()
    conn.close()
    print(json.dumps({"status": "added", "handle": data.get("handle")}))


def update_pulse(domain: str):
    conn = get_conn(domain)
    config = get_config(conn)
    now = datetime.utcnow()
    day_ago = (now - timedelta(days=1)).isoformat()
    week_ago = (now - timedelta(days=7)).isoformat()
    month_ago = (now - timedelta(days=30)).isoformat()

    metrics = {}

    for period_name, cutoff in [("24h", day_ago), ("7d", week_ago), ("30d", month_ago)]:
        row = conn.execute("""
            SELECT
                COALESCE(SUM(sentiment * relevance) / NULLIF(SUM(relevance), 0), 0) as weighted_sentiment,
                COUNT(*) as signal_count,
                COALESCE(AVG(sentiment), 0) as avg_sentiment
            FROM signals
            WHERE detected_at >= ?
        """, (cutoff,)).fetchone()

        metrics[f"sentiment_{period_name}"] = round(row["weighted_sentiment"], 3)
        metrics[f"signals_{period_name}"] = row["signal_count"]

    categories = conn.execute("""
        SELECT category,
               COALESCE(AVG(sentiment), 0) as avg_sentiment,
               COUNT(*) as count
        FROM signals
        WHERE detected_at >= ?
        GROUP BY category
    """, (week_ago,)).fetchall()

    for cat in categories:
        safe_name = re.sub(r"[^a-zA-Z0-9]", "_", cat["category"].lower())
        metrics[f"cat_{safe_name}_sentiment"] = round(cat["avg_sentiment"], 3)
        metrics[f"cat_{safe_name}_count"] = cat["count"]

    two_days_ago = (now - timedelta(days=2)).isoformat()
    recent = conn.execute("""
        SELECT COALESCE(AVG(sentiment), 0) as avg
        FROM signals WHERE detected_at >= ?
    """, (day_ago,)).fetchone()["avg"]

    previous = conn.execute("""
        SELECT COALESCE(AVG(sentiment), 0) as avg
        FROM signals WHERE detected_at >= ? AND detected_at < ?
    """, (two_days_ago, day_ago)).fetchone()["avg"]

    metrics["momentum"] = round(recent - previous, 3)

    total_accounts = conn.execute("SELECT COUNT(*) as n FROM accounts WHERE active = 1").fetchone()["n"]
    active_accounts = conn.execute("""
        SELECT COUNT(DISTINCT handle) as n FROM signals WHERE detected_at >= ?
    """, (week_ago,)).fetchone()["n"]
    metrics["account_coverage"] = round(active_accounts / max(total_accounts, 1), 3)
    metrics["total_accounts"] = total_accounts

    bullish_thresh = get_threshold(config, "bullish_pct_threshold", 0.2)
    bearish_thresh = get_threshold(config, "bearish_pct_threshold", -0.2)

    metrics["bullish_pct"] = conn.execute("""
        SELECT COALESCE(ROUND(100.0 * COUNT(*) / NULLIF((SELECT COUNT(*) FROM signals WHERE detected_at >= ?), 0), 1), 0)
        FROM signals WHERE detected_at >= ? AND sentiment > ?
    """, (week_ago, week_ago, bullish_thresh)).fetchone()[0]

    metrics["bearish_pct"] = conn.execute("""
        SELECT COALESCE(ROUND(100.0 * COUNT(*) / NULLIF((SELECT COUNT(*) FROM signals WHERE detected_at >= ?), 0), 1), 0)
        FROM signals WHERE detected_at >= ? AND sentiment < ?
    """, (week_ago, week_ago, bearish_thresh)).fetchone()[0]

    metrics["neutral_pct"] = round(100 - metrics["bullish_pct"] - metrics["bearish_pct"], 1)

    now_str = now.isoformat()

    bull_t = get_threshold(config, "bullish_threshold", 0.3)
    sbull_t = get_threshold(config, "slight_bullish_threshold", 0.1)
    sbear_t = get_threshold(config, "slight_bearish_threshold", -0.1)
    bear_t = get_threshold(config, "bearish_threshold", -0.3)

    for metric, value in metrics.items():
        label = ""
        if metric == "sentiment_7d":
            if value > bull_t:
                label = "BULLISH"
            elif value > sbull_t:
                label = "SLIGHTLY BULLISH"
            elif value > sbear_t:
                label = "NEUTRAL"
            elif value > bear_t:
                label = "SLIGHTLY BEARISH"
            else:
                label = "BEARISH"

        conn.execute("""
            INSERT OR REPLACE INTO pulse (domain, metric, value, label, updated_at)
            VALUES (?, ?, ?, ?, ?)
        """, (domain, metric, value, label, now_str))

    today = now.strftime("%Y-%m-%d")
    for metric in ["sentiment_24h", "sentiment_7d", "signals_24h"]:
        conn.execute("""
            INSERT OR REPLACE INTO history (domain, date, metric, value, signal_count)
            VALUES (?, ?, ?, ?, ?)
        """, (domain, today, metric, metrics.get(metric, 0), metrics.get("signals_24h", 0)))

    conn.commit()

    uncalibrated = [k for k, v in config.items() if v["source"] == "default_uncalibrated"]

    result = {
        "status": "pulse_updated",
        "domain": domain,
        "metrics": metrics,
        "thresholds_used": {k: v for k, v in config.items()},
        "uncalibrated_thresholds": uncalibrated,
    }

    conn.close()
    print(json.dumps(result, indent=2))


def export_pulse(domain: str, output_path: str = None):
    if output_path is None:
        output_path = os.path.join(DB_DIR, domain, "pulse.json")

    conn = get_conn(domain)
    config = get_config(conn)

    pulse = {}
    for row in conn.execute("SELECT metric, value, label, updated_at FROM pulse WHERE domain = ?", (domain,)):
        pulse[row["metric"]] = {
            "value": row["value"],
            "label": row["label"] or "",
            "updated_at": row["updated_at"],
        }

    accounts = []
    for row in conn.execute("""
        SELECT handle, name, category, relevance, followers, signal_summary
        FROM accounts WHERE active = 1 ORDER BY relevance DESC LIMIT 100
    """):
        accounts.append(dict(row))

    recent_signals = []
    for row in conn.execute("""
        SELECT s.handle, s.content, s.sentiment, s.relevance, s.category,
               s.signal_type, s.detected_at, a.name, a.followers
        FROM signals s
        LEFT JOIN accounts a ON s.handle = a.handle
        ORDER BY s.detected_at DESC LIMIT 50
    """):
        recent_signals.append(dict(row))

    history = []
    for row in conn.execute("""
        SELECT date, metric, value, signal_count
        FROM history WHERE domain = ?
        ORDER BY date DESC LIMIT 90
    """, (domain,)):
        history.append(dict(row))

    categories = []
    for row in conn.execute("""
        SELECT category, COUNT(*) as count, ROUND(AVG(sentiment), 3) as avg_sentiment
        FROM signals
        GROUP BY category
        ORDER BY count DESC
    """):
        categories.append(dict(row))

    uncalibrated = [k for k, v in config.items() if v["source"] == "default_uncalibrated"]

    export = {
        "domain": domain,
        "generated_at": datetime.utcnow().isoformat(),
        "pulse": pulse,
        "accounts": accounts,
        "recent_signals": recent_signals,
        "history": history,
        "categories": categories,
        "sentiment_config": {k: v for k, v in config.items()},
        "calibration_status": "UNCALIBRATED" if uncalibrated else "CALIBRATED",
        "uncalibrated_thresholds": uncalibrated,
    }

    Path(output_path).write_text(json.dumps(export, indent=2), encoding="utf-8")
    conn.close()
    print(json.dumps({
        "status": "exported",
        "path": output_path,
        "accounts": len(accounts),
        "signals": len(recent_signals),
        "calibration_status": "UNCALIBRATED" if uncalibrated else "CALIBRATED",
    }))


def summary(domain: str):
    conn = get_conn(domain)

    accounts = conn.execute("SELECT COUNT(*) as n FROM accounts WHERE active = 1").fetchone()["n"]
    signals = conn.execute("SELECT COUNT(*) as n FROM signals").fetchone()["n"]

    pulse_data = {}
    for row in conn.execute("SELECT metric, value, label FROM pulse WHERE domain = ?", (domain,)):
        pulse_data[row["metric"]] = {"value": row["value"], "label": row["label"]}

    config = get_config(conn)
    uncalibrated = [k for k, v in config.items() if v["source"] == "default_uncalibrated"]

    result = {
        "domain": domain,
        "total_accounts": accounts,
        "total_signals": signals,
        "pulse": pulse_data,
        "calibration_status": "UNCALIBRATED" if uncalibrated else "CALIBRATED",
        "uncalibrated_thresholds": uncalibrated,
    }

    conn.close()
    print(json.dumps(result, indent=2))


def main():
    if len(sys.argv) < 3:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1]
    domain = sys.argv[2]

    if command == "init":
        init_db(domain)
    elif command == "import-accounts":
        if len(sys.argv) < 4:
            print("Usage: signal_db_v2.py import-accounts <domain> <social-signals-x.md>", file=sys.stderr)
            sys.exit(1)
        import_accounts(domain, sys.argv[3])
    elif command == "add-signal":
        if len(sys.argv) < 4:
            print("Usage: signal_db_v2.py add-signal <domain> '<json>'", file=sys.stderr)
            sys.exit(1)
        add_signal(domain, sys.argv[3])
    elif command == "update-pulse":
        update_pulse(domain)
    elif command == "export":
        output_path = sys.argv[3] if len(sys.argv) > 3 else None
        export_pulse(domain, output_path)
    elif command == "summary":
        summary(domain)
    elif command == "config":
        if len(sys.argv) >= 5:
            set_config(domain, sys.argv[3], float(sys.argv[4]))
        else:
            show_config(domain)
    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
