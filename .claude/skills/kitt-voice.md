---
name: kitt-voice
description: Speak or read aloud using KITT's voice (calm, authoritative, slightly synthetic) via TTS. Invoke when the user wants text spoken in KITT's voice. Playback uses the system default speakers.
---

# KITT Voice (Text-to-Speech)

Speak text aloud using **KITT's voice**: calm, authoritative, professional, slightly synthetic—like Knight Rider's KITT (William Daniels). Uses the tts-mcp server (OpenAI TTS) with voice **onyx** or **echo** and normal-speed delivery. **Playback always uses the default speakers** of the machine where it runs (no specific output device).

## When to Use

Claude Code should invoke this skill when:
- User says "read this aloud," "read it aloud," or "speak this"
- User asks to "say it in KITT's voice," "use KITT voice," "speak as KITT," or "in KITT's voice"
- User wants a response or a piece of text read out in KITT's voice

## How It Works

1. **Identify the text to speak**  
   Use the content the user indicated: the last message, a selected block, a file, or the assistant's previous reply. If ambiguous, ask what to speak.

2. **Call the TTS MCP tool**  
   Use the **text-to-speech** tool from the **tts-mcp** server with:
   - **text:** The content to speak (required).
   - **speed:** Use normal speed (1.0) for KITT's efficient delivery—not slow like MARVIN.
   - **instructions:** If the tool supports it, pass something like: "Speak in a calm, efficient, professional tone—slightly synthetic, like KITT from Knight Rider."

   The tts-mcp server is configured with voice **onyx** (authoritative male) or **echo** (slightly synthetic); no need to pass voice if the server is fixed.

3. **Play through default speakers (required)**  
   - If the tool returns an audio file path, you **must run a terminal command** to play that file. Do not only show the path—the user will not hear anything until the file is played.
   - **Run the play command yourself:** On macOS use `afplay <path>`, on Linux `aplay <path>` or `paplay <path>`, on Windows `Start-Process -FilePath "<path>"` or `start <path>`. Use no output-device flag so playback goes to the system default speakers.
   - Wait for the command to finish (playback completes), then confirm to the user that it played. If the tool plays audio automatically, confirm that it played.

## Example

```
User: "Read my last message aloud in KITT's voice."
Claude: [invokes kitt-voice, gets the user's last message text, calls text-to-speech with KITT-style instructions, then plays the returned file via default speakers (e.g. afplay on macOS)]
Result: "Done. Played through your default speakers."
```

## Notes

- **Requires:** tts-mcp MCP server enabled in `.cursor/mcp.json` and `OPENAI_API_KEY` set in that server's `env` (or in your environment). See CLAUDE.md and `content/kitt-voice-reference.md`.
- **Voice reference:** We approximate KITT's voice with onyx or echo + normal-speed, calm, professional delivery. See `content/kitt-voice-reference.md` for details.
- **Default speakers:** Always play the generated audio through the system default output so it is heard on whatever speakers or headphones are currently default where the command runs.

## Troubleshooting: "I can't hear the voice"

- **tts-mcp not available:** If the **text-to-speech** tool isn't available, Cursor isn't loading tts-mcp. Check Settings → MCP: tts-mcp should be listed and have `OPENAI_API_KEY` in its `env` in `.cursor/mcp.json`. Restart Cursor and try again.
- **No play command run:** You must **run** the play command (e.g. `afplay <path>`) in the terminal after getting the file path. If the agent only replied with the path and didn't run a command, run it yourself: e.g. `afplay /path/to/file.mp3` (macOS).
- **Volume and output:** Check system volume and that the correct output device is set as default (e.g. built-in speakers or your headset) in system sound settings.
