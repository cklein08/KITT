#!/usr/bin/env python3
"""
KITT Use-Case Search Script (Vector DB Spike)

Searches the ChromaDB collection for use cases similar to the query.

Usage:
  pip install chromadb openai
  export OPENAI_API_KEY=your_key
  python scripts/search_use_cases.py "real-time personalization for logged-in users"
  python scripts/search_use_cases.py "AEP RPS limits" --n 5
"""

import os
import sys
from pathlib import Path

try:
    import chromadb
    from chromadb.config import Settings
except ImportError:
    print("Install chromadb: pip install chromadb")
    sys.exit(1)

try:
    from openai import OpenAI
except ImportError:
    print("Install openai: pip install openai")
    sys.exit(1)


def get_embedding(client, text: str, model: str = "text-embedding-3-small") -> list[float]:
    response = client.embeddings.create(input=text, model=model)
    return response.data[0].embedding


def main():
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else ""
    if not query:
        print("Usage: python search_use_cases.py \"your search query\" [--n 5]")
        sys.exit(1)

    n = 5
    if "--n" in sys.argv:
        idx = sys.argv.index("--n")
        if idx + 1 < len(sys.argv):
            n = int(sys.argv[idx + 1])
        sys.argv = [s for i, s in enumerate(sys.argv) if i not in (idx, idx + 1)]
        query = " ".join(sys.argv[1:])

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Set OPENAI_API_KEY environment variable")
        sys.exit(1)

    script_dir = Path(__file__).parent
    kitt_root = script_dir.parent
    chroma_path = kitt_root / ".chroma"

    if not chroma_path.exists():
        print("No vector DB found. Run scripts/ingest_use_cases.py first.")
        sys.exit(1)

    client = OpenAI(api_key=api_key)
    db = chromadb.PersistentClient(path=str(chroma_path), settings=Settings(anonymized_telemetry=False))
    collection = db.get_collection("use_cases")

    embedding = get_embedding(client, query)
    results = collection.query(query_embeddings=[embedding], n_results=min(n, collection.count()))

    if not results["ids"][0]:
        print("No matches found.")
        sys.exit(0)

    print(f"\nTop {len(results['ids'][0])} matches for: \"{query}\"\n")
    for i, (uid, doc, dist) in enumerate(
        zip(results["ids"][0], results["documents"][0], results["distances"][0]), 1
    ):
        print(f"--- Match {i} (id: {uid}, distance: {dist:.4f}) ---")
        print(doc[:500] + "..." if len(doc) > 500 else doc)
        print()


if __name__ == "__main__":
    main()
