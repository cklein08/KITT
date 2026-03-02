# KITT MCP Configuration

## Setup

1. Copy `mcp.json.example` to `mcp.json`:
   ```bash
   cp .cursor/mcp.json.example .cursor/mcp.json
   ```

2. Edit `.cursor/mcp.json` and fill in your tokens:
   - **EASYMCP_TOKEN**: Get from [easymcp.net](https://easymcp.net). Enable Adobe Wiki Confluence.
   - **OPENAI_API_KEY**: Your OpenAI API key (for KITT voice TTS).

## MCP Servers

| Server | Purpose |
|--------|---------|
| EasyMCP-Adobe-Wiki-Confluence | Primary source for use-case doc lookup. Search and fetch wiki pages. |
| tts-mcp | KITT voice (text-to-speech). Speak or read aloud in KITT's voice. |

## KITT Voice

For KITT's voice, tts-mcp uses:
- **Voice:** onyx (authoritative) or echo (slightly synthetic)
- **Model:** tts-1-hd
- **Speed:** Normal (1.0) - KITT speaks at normal pace

See `content/kitt-voice-reference.md` for details.
