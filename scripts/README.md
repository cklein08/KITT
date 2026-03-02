# KITT Scripts

## Vector DB (Semantic Search) - Optional

For improved use-case matching, you can ingest use-case JSON files into a local vector database (ChromaDB) and run semantic search.

### Setup

```bash
pip install chromadb openai
export OPENAI_API_KEY=your_openai_key
```

### Ingest Use Cases

```bash
# Ingest from content/use-case-examples/ (add .json files there)
python scripts/ingest_use_cases.py

# Or from a specific file or directory
python scripts/ingest_use_cases.py path/to/use-cases.json
python scripts/ingest_use_cases.py path/to/use-cases-dir/
```

Use-case JSON files should conform to `content/canonical-schema.json`.

### Search

```bash
python scripts/search_use_cases.py "real-time personalization for logged-in users"
python scripts/search_use_cases.py "AEP RPS limits" --n 5
```

### Integration with KITT

The use-case-matching skill uses **Adobe Wiki Confluence** as the primary source. The vector DB is an optional enhancement for local use-case libraries. When ChromaDB is populated, the skill can optionally query it in addition to (or instead of) wiki search for improved ranking.

**TODO:** Integrate ChromaDB search into the use-case-matching skill when `.chroma` exists.
