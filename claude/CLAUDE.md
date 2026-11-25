# Claude project quickstart — AI Content Creator

This project includes a Claude Code skill at `.claude/skills/ai-content-creator/SKILL.md` (or copy the `skills/ai-content-creator` folder from this repo to `~/.claude/skills/ai-content-creator`).

Invoke it with `/ai-content-creator`.

## Tool mapping

The shared references were written for OpenCode. In Claude Code, read:

- `websearch` / `webfetch` as `WebSearch` / `WebFetch`
- `shell` as `Bash`
- `question` as `AskUserQuestion`, or a single plain question message
- `skill` as `Skill`
- `Read`, `Write`, `Edit`, `Glob`, `Grep` as the same tools

## Non-negotiables

- Research is evidence, not a shot list. Never copy a trending video's characters, shots, captions, sounds or edits.
- Every number has a source and date. Every topic has a direct `youtube.com/shorts/<ID>` link, never a tracker page.
- Offer `Cartoon-ready` / `All videos` scope at intake; honour `cartoon` / `all` with a new dated report.
- Scripts: clean `script.txt`, ElevenLabs `script_elevenlabs.txt` with `[ ]` tags, and `script_full.txt` with `[[[ ]]]` production notes.
- Voice source is a choice: user recording, or auto — ElevenLabs when `ELEVENLABS_API_KEY` exists, otherwise free offline Kokoro. Generate a preview and get approval before the full run. Never store the key in a file.
- Never re-time, duck, compress or otherwise alter a user-supplied recording. Music/SFX at 50% of voice.
- Work under `~/shorts/<slug>`. Stop at the film engine's contact-sheet approval gate.

## Dependencies

The final handoff needs `lemo-opuscar` or `cartoon-audio-short` installed as Claude skills. If neither is available, stop and tell the user to install one; this repo does not bundle them.

Full instructions: [README.md](../README.md).
