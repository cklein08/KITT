---
description: Show available commands and integrations
---

# /help - KITT Help

Show the user what KITT can do and what integrations are available.

## Instructions

### 1. Show Available Commands

Display this reference:

```
## Slash Commands

| Command   | What It Does                                    |
|-----------|-------------------------------------------------|
| /start    | Start a session with a briefing                 |
| /end      | End session and save everything                 |
| /update   | Quick checkpoint (save progress)                 |
| /match    | Run use-case matching (search wiki, validate, rank) |
| /check    | Run guardrail/risk check on use case           |
| /dossier  | Generate 1-page dossier with top-3 architectures |
| /help     | Show this help guide                            |
```

### 2. Show Current Integrations

Check what MCP servers are configured by running:
```bash
claude mcp list
```

Then display something like:

```
## Your Integrations

These are the tools KITT can currently access:

| Integration              | What It Does                                      |
|--------------------------|---------------------------------------------------|
| EasyMCP Adobe Wiki        | Search and fetch use-case docs, Confluence pages  |
| TTS (KITT voice)         | Speak or read aloud in KITT's voice               |

(List only what's actually configured based on the mcp list output)
```

If no integrations are configured, say:
```
## Your Integrations

No integrations configured yet. Just say "Help me connect to Adobe Wiki" and I'll walk you through it!
```

### 3. Show Available Integrations

Display what integrations can be added:

```
## Available Integrations

Just ask me to set one up! For example: "Help me connect to Adobe Wiki"

| Integration              | What It Does                              |
|--------------------------|-------------------------------------------|
| EasyMCP Adobe Wiki       | Primary source for use-case docs, Confluence |
| TTS (KITT voice)         | Speak or read aloud in KITT's voice; requires tts-mcp and OPENAI_API_KEY |
| Parallel Search          | Web search capabilities                   |
```

### 4. Offer Next Steps

End with:

```
---

Want me to help you set up an integration, run use-case matching, or learn more about what I can do?

Otherwise, hit **Esc** to get back to work.
```

Wait for the user to respond or exit.
