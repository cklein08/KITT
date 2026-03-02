# KITT - Use-Case AI Agent for EA Teams

**KITT** = Knight Rider Intelligent Technology Team

An AI agent that serves as a canonical, living use-case library and advisor for Enterprise Architecture teams. KITT ingests documented use cases, product guardrails, entitlements, RFPs and implementation notes to (a) surface best-fit patterns, (b) flag risks/limits early (latency, RPS, licensing), (c) propose tailored solution sketches and (d) generate artifacts (dossiers, RFP drafts, slides, Lucid diagrams).

## Why KITT?

KITT extends Claude Code with capabilities designed for EA use-case workflows:

- **Use-case matching** - Search Adobe Wiki Confluence, validate, and return ranked matches with supporting links
- **Guardrail checking** - Flag product limits, licensing gaps, and risks before implementation
- **Artifact generation** - 1-page dossier, top-3 architectures, RFP drafts, slide summaries
- **Session continuity** - Pick up where you left off, even days later
- **KITT personality** - Confident, professional, efficient (like Knight Rider's KITT)

## Quick Start

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_ORG/KITT.git
   cd KITT
   ```

2. Open in Claude Code:
   ```bash
   claude
   ```

   Or use the `kitt` command from any terminal (after setup):
   ```bash
   kitt
   ```

3. Ask KITT to help you set up:
   > "Help me set up KITT"

That's it. KITT walks you through the rest: your profile, workspace location, and optional integrations.

## The `kitt` Terminal Command

After setup, type `kitt` from any directory to launch KITT:

```bash
kitt
```

The setup script (`.kitt/setup.sh`) or onboarding flow adds a `kitt()` function to your shell config (`.zshrc`, `.bashrc`, or `.profile`). It changes to the KITT workspace and runs `claude`.

## Commands

| Command | What It Does |
|---------|--------------|
| `/start` | Start your session with a briefing |
| `/end` | End session and save everything |
| `/update` | Quick checkpoint (save progress) |
| `/match` | Run use-case matching (search wiki, validate, rank) |
| `/check` | Run guardrail/risk check on use case |
| `/dossier` | Generate 1-page dossier with top-3 architectures |
| `/help` | Show all commands and integrations |

## Integrations

| Integration | What It Provides |
|-------------|------------------|
| **EasyMCP Adobe Wiki Confluence** | Primary source for use-case docs. Search and fetch wiki pages. Extract Lucid diagrams. |
| **TTS (KITT voice)** | Speak or read aloud in KITT's voice (calm, authoritative). |
| **Parallel Search** | Web search capabilities |

## Data Sources

- **Adobe Wiki Confluence** (primary) - Use-case docs, product guardrails, RFPs via EasyMCP
- **SharePoint** (Phase 2) - Word, PowerPoint, Excel
- **PPT and PNG (Lucid diagrams)** (Phase 2) - Standalone file ingestion

## Optional: Vector DB (Semantic Search)

For improved use-case matching with a local use-case library, you can ingest JSON use cases into ChromaDB:

```bash
pip install chromadb openai
export OPENAI_API_KEY=your_key
python scripts/ingest_use_cases.py    # Ingest from content/use-case-examples/
python scripts/search_use_cases.py "your query"
```

See `scripts/README.md` for details.

## Workspace Structure

```
KITT/
├── CLAUDE.md               # KITT profile and preferences
├── state/                  # Current state, matched use cases
├── sessions/               # Daily session logs
├── content/                # Canonical template, schema, guardrails
├── scripts/                # Vector DB ingestion and search (optional)
└── .claude/                # Commands, agents, skills
```

## About

KITT is named after the AI from Knight Rider. Confident, professional, and always ready to assist.
