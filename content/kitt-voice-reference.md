# KITT Voice Reference

Short reference for the KITT TTS voice: **Knight Rider's KITT** (William Daniels) and how this project approximates it. Playback uses the **default speakers** of the machine where it runs.

## Voice: Knight Rider's KITT

We use **William Daniels'** voice as KITT from Knight Rider: calm, authoritative, professional, slightly synthetic—efficient and reassuring. There is no official TTS or voice clone for him; we approximate with a deep male voice (onyx) or slightly robotic voice (echo) plus delivery instructions.

For this project, "KITT voice" means: **calm, efficient, professional, slightly synthetic—like Knight Rider's KITT**.

## How We Approximate It

- **TTS provider:** tts-mcp (OpenAI TTS).
- **Voice:** **onyx** (authoritative male) or **echo** (slightly synthetic/robotic), set in `.cursor/mcp.json` for the tts-mcp server.
- **Model:** tts-1-hd.
- **Delivery:** When calling the TTS tool, use normal speed (1.0) and, if supported, instructions like: "Speak in a calm, efficient, professional tone—slightly synthetic, like KITT from Knight Rider."

## Playback: Default Speakers

Audio is always played through the **system default audio output** (the default speakers or headphones of the machine where the command runs). Do not specify a particular device—use the OS default (e.g. `afplay <path>` on macOS, `aplay`/`paplay` on Linux, or the default player on Windows) so playback follows the user's current default device.

## Setup

- Add **tts-mcp** to `.cursor/mcp.json` (see CLAUDE.md).
- Set **OPENAI_API_KEY** in the tts-mcp server's `env` in `.cursor/mcp.json`, or in your environment.
- Use `--voice onyx` or `--voice echo` for KITT-style output.

## Optional Alternatives

- **ElevenLabs** or **Hume Octave**: for a closer match to a specific voice, use a provider that supports voice descriptions or cloning; different API and setup.
