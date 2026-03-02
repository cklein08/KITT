#!/usr/bin/env python3
"""
KITT Use-Case Ingestion Script (Vector DB Spike)

Reads canonical use-case JSON files, creates embeddings via OpenAI,
and stores them in ChromaDB for semantic search.

Usage:
  pip install chromadb openai
  export OPENAI_API_KEY=your_key
  python scripts/ingest_use_cases.py [path/to/use-cases.json] [path/to/use-cases-dir]

If no path given, reads from content/use-case-examples/ (expects .json files).
"""

import json
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


def get_embedding(client: OpenAI, text: str, model: str = "text-embedding-3-small") -> list[float]:
    """Get embedding for text via OpenAI API."""
    response = client.embeddings.create(input=text, model=model)
    return response.data[0].embedding


def use_case_to_text(uc: dict) -> str:
    """Convert use case dict to searchable text."""
    parts = []
    if uc.get("title"):
        parts.append(f"Title: {uc['title']}")
    if uc.get("summary"):
        parts.append(f"Summary: {uc['summary']}")
    if uc.get("businessContext"):
        bc = uc["businessContext"]
        if bc.get("drivers"):
            parts.append(f"Drivers: {', '.join(bc['drivers'])}")
        if bc.get("successMetrics"):
            parts.append(f"Metrics: {', '.join(bc['successMetrics'])}")
    if uc.get("desiredState"):
        ds = uc["desiredState"]
        if ds.get("productsExpected"):
            parts.append(f"Products: {', '.join(ds['productsExpected'])}")
        if ds.get("functionalScope"):
            parts.append(f"Scope: {ds['functionalScope']}")
    return "\n".join(parts) if parts else json.dumps(uc)


def load_use_cases(path: str) -> list[tuple[str, dict]]:
    """Load use cases from a file or directory. Returns [(id, use_case), ...]."""
    p = Path(path)
    results = []
    if p.is_file() and p.suffix == ".json":
        with open(p) as f:
            data = json.load(f)
            if isinstance(data, list):
                for i, uc in enumerate(data):
                    uid = uc.get("useCaseId") or f"{p.stem}-{i}"
                    results.append((uid, uc))
            else:
                uid = data.get("useCaseId") or p.stem
                results.append((uid, data))
    elif p.is_dir():
        for f in p.glob("**/*.json"):
            for id_, uc in load_use_cases(str(f)):
                results.append((id_, uc))
    return results


def main():
    script_dir = Path(__file__).parent
    kitt_root = script_dir.parent
    default_path = kitt_root / "content" / "use-case-examples"

    paths = sys.argv[1:] if len(sys.argv) > 1 else [str(default_path)]
    if not paths or not Path(paths[0]).exists():
        paths = [str(default_path)]
        if not default_path.exists():
            print(f"No use-case files found at {default_path}")
            print("Add .json use-case files there, or pass a path: python ingest_use_cases.py path/to/use-cases.json")
            sys.exit(0)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Set OPENAI_API_KEY environment variable")
        sys.exit(1)

    client = OpenAI(api_key=api_key)
    chroma_path = kitt_root / ".chroma"
    chroma_path.mkdir(exist_ok=True)

    db = chromadb.PersistentClient(path=str(chroma_path), settings=Settings(anonymized_telemetry=False))
    collection = db.get_or_create_collection("use_cases", metadata={"description": "KITT canonical use cases"})

    all_ids, all_metadatas, all_docs = [], [], []
    for path in paths:
        for uid, uc in load_use_cases(path):
            text = use_case_to_text(uc)
            all_ids.append(str(uid))
            all_metadatas.append({"title": uc.get("title", "")})
            all_docs.append(text)

    if not all_docs:
        print("No use cases to ingest.")
        sys.exit(0)

    print(f"Ingesting {len(all_docs)} use cases...")
    embeddings = [get_embedding(client, doc) for doc in all_docs]
    collection.add(ids=all_ids, embeddings=embeddings, documents=all_docs, metadatas=all_metadatas)
    print(f"Done. Stored in {chroma_path}")
    print("Use scripts/search_use_cases.py to search.")


if __name__ == "__main__":
    main()
