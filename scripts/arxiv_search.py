#!/usr/bin/env python3
"""arXiv paper search → JSON stdout.

Usage: python arxiv_search.py "query terms" [max_results]
Output: JSON array of papers with title, authors, abstract, url, published.
"""
from __future__ import annotations

import json
import sys

import arxiv


def search(query: str, max_results: int = 20) -> list:
    client = arxiv.Client()
    search_obj = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance,
    )

    papers = []
    for result in client.results(search_obj):
        papers.append({
            "title": result.title,
            "authors": [a.name for a in result.authors],
            "abstract": result.summary,
            "url": result.entry_id,
            "pdf_url": result.pdf_url,
            "published": result.published.isoformat() if result.published else None,
            "updated": result.updated.isoformat() if result.updated else None,
            "categories": result.categories,
        })

    return papers


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: arxiv_search.py <query> [max_results]", file=sys.stderr)
        sys.exit(1)

    query = sys.argv[1]
    max_results = int(sys.argv[2]) if len(sys.argv) > 2 else 20

    try:
        papers = search(query, max_results)
        json.dump(papers, sys.stdout, indent=2)
        print()
    except Exception as e:
        json.dump({"error": str(e), "query": query}, sys.stdout, indent=2)
        print()
        sys.exit(1)


if __name__ == "__main__":
    main()
