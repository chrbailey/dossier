#!/usr/bin/env python3
"""WHOIS lookup → JSON stdout.

Usage: python whois_lookup.py example.com
Output: JSON with registrar, dates, nameservers, contacts.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime
from typing import Any

import whois


def serialize(obj: Any) -> Any:
    """Handle datetime and list-of-datetime serialization."""
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, list):
        return [serialize(item) for item in obj]
    return obj


def lookup(domain: str) -> dict:
    w = whois.whois(domain)
    raw = dict(w)
    # Normalize all values for JSON serialization
    return {k: serialize(v) for k, v in raw.items() if v is not None}


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: whois_lookup.py <domain>", file=sys.stderr)
        sys.exit(1)

    domain = sys.argv[1]
    try:
        result = lookup(domain)
        json.dump(result, sys.stdout, indent=2, default=str)
        print()  # trailing newline
    except Exception as e:
        json.dump({"error": str(e), "domain": domain}, sys.stdout, indent=2)
        print()
        sys.exit(1)


if __name__ == "__main__":
    main()
