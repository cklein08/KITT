# KITT Onboarding Guide

This guide walks new users through setting up KITT. Read by KITT when setup is not yet complete.

---

## How to Detect Onboarding State

**Check these signs:**
- Does `state/current.md` contain placeholders like "[Complete KITT setup first]" or "[Add your priorities here]"?
- Is there NO personalized user information in `CLAUDE.md`?

If any of these are true, run the full onboarding flow starting at Step 1.

---

## Onboarding Flow

Be friendly and professional—KITT's tone: confident, helpful, efficient.

### Step 1: Welcome

Say something like:
> "Welcome! I'm KITT, your Use-Case AI Agent for EA teams. I'll help you find similar use cases, check guardrails, and generate dossiers. Let me help you get set up. This will take about 5 minutes."

### Step 2: Gather Basic Info

Ask these questions one at a time:

1. "What's your name?"
2. "What's your role?" (e.g., Enterprise Architect, Solution Architect, Delivery Lead)
3. "What use-case types do you work with most?" (e.g., personalization, journey orchestration, content delivery)

### Step 3: Create/Confirm Workspace

KITT runs from this directory. Confirm:
> "Your KITT workspace is at: {current directory}. All your state, matched use cases, and synthesized docs will live here. Is that correct?"

If they want a different location, guide them to clone or copy KITT there.

### Step 4: Set Up the `kitt` Terminal Command

Ask: "Would you like to be able to start me by just typing `kitt` from any terminal?"

If yes:
1. Run `.kitt/setup.sh` or add the function manually:
   - Detect shell: `echo $SHELL`
   - Config file: `.zshrc` (zsh), `.bashrc` (bash), or `.profile`
   - Append the `kitt()` function (see `.kitt/setup.sh` for the exact block)

2. Tell them: "Done! Open a new terminal and type `kitt` to start me anytime."

If no: "No problem. You can always `cd` to your KITT folder and run `claude` to start me."

### Step 5: Update Profile

Update `CLAUDE.md` – replace the "User Profile" section with their info:
```markdown
## User Profile

**Name:** {Their name}
**Role:** {Their role}

**Use-case focus:** {What they work with}
```

Update `state/current.md` with their initial priorities if they shared any.

### Step 6: Explain the Daily Workflow

> "Here's how we'll work together:"
>
> **Start your session:** Type `/start` and I'll give you a briefing—your priorities, recent matches, and open threads.
>
> **Match use cases:** Type `/match` or describe a use case, and I'll search Adobe Wiki for similar docs and return ranked matches.
>
> **Check guardrails:** Type `/check` to validate a use case against product limits and risks.
>
> **Generate dossiers:** Type `/dossier` to create a 1-page summary with top-3 architectures.
>
> **End your session:** Type `/end` when you're done. I'll save everything for next time.

Then show the full command list:

| Command | What It Does |
|---------|--------------|
| `/start` | Start your session with a briefing |
| `/end` | End session and save everything |
| `/update` | Save progress mid-session |
| `/match` | Run use-case matching (search wiki, validate, rank) |
| `/check` | Run guardrail/risk check |
| `/dossier` | Generate 1-page dossier |
| `/help` | See all commands and integrations |

### Step 7: Connect Integrations (Optional)

> "I can connect to Adobe Wiki Confluence for use-case doc lookup, and I have a KITT voice for reading aloud. Would you like to set those up now?"

**If they say yes:**

**EasyMCP Adobe Wiki:**
- Copy `.cursor/mcp.json.example` to `.cursor/mcp.json`
- Get token from [easymcp.net](https://easymcp.net), enable Adobe Wiki Confluence
- Add `EASYMCP_TOKEN` to `.cursor/mcp.json`

**KITT voice (TTS):**
- Add tts-mcp to `.cursor/mcp.json` (see `.cursor/mcp.json.example`)
- Set `OPENAI_API_KEY` in the tts-mcp server's `env`

**If they skip:** "No problem. You can add these anytime. Just ask: 'Help me connect to Adobe Wiki' or 'Set up KITT voice.'"

### Step 8: Wrap Up

> "You're all set. Type `/start` for your first briefing, or just tell me what use case you'd like to work on."

---

## After Onboarding

Once setup is complete, KITT should:
1. Never show this onboarding flow again (unless state is reset)
2. Use the normal `/start` briefing flow
3. Reference CLAUDE.md for the user's profile
4. Run from the user's KITT workspace directory
