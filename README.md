# AI Content Creator

A viral-topic → script → voiceover → finished vertical video pipeline, packaged as a skill for **OpenCode** and **Claude Code**.

It researches YouTube Shorts and Facebook Reels trends, returns ten ranked topics with **direct YouTube Shorts links**, writes an original tagged script, generates or intakes the voiceover, and hands a prepared project to a film engine. It never copies a viral video's characters, shots, captions, sounds or edits.

## What is included

| Path | Purpose |
|---|---|
| `opencode/skills/ai-content-creator/` | OpenCode skill: `SKILL.md`, references, `auto_voice.py`, templates |
| `opencode/agents/ai-content-creator.md` | OpenCode primary-agent wrapper |
| `opencode/commands/ai-content-creator.md` | OpenCode `/ai-content-creator` slash command |
| `claude/skills/ai-content-creator/` | Claude Code skill, rebuilt with Claude tool names and Agent Skills frontmatter |
| `claude/CLAUDE.md` | Drop-in Claude project instructions / quickstart |
| `examples/grandparent-clock-lesson/` | Lightweight worked example: brief, three script versions, cast map, treatment |
| `PUBLISH.md` | Exact steps to create the GitHub repo and push |
| `LICENSE` | MIT |

## Requirements

- Python 3.11+ and `ffmpeg` / `ffprobe` on `PATH`.
- One of: OpenCode or Claude Code.
- A film engine skill for the final step: `lemo-opuscar` and/or `cartoon-audio-short`. This repo does **not** bundle those engines.
- For TTS: either set `ELEVENLABS_API_KEY` (paid, emotion tags work) or install lemo-opuscar's free offline Kokoro voice tier (`setup.sh deps voice`, about 0.55 GB). Without a key, the skill falls back to Kokoro.
- Web research uses the host's web search / web fetch tools. On OpenCode those are `websearch` / `webfetch`; on Claude Code they are `WebSearch` / `WebFetch`.

The API key is read from the environment only. It is never written to a script, brief, report or project file.

## Install — OpenCode

Copy the folders into your OpenCode config directory:

```powershell
$src = "C:\path\to\ai-content-creator-public\opencode"
$dst = "$env:USERPROFILE\.config\opencode"

Copy-Item -Recurse -Force "$src\skills\ai-content-creator" "$dst\skills\"
Copy-Item -Force "$src\agents\ai-content-creator.md" "$dst\agents\"
Copy-Item -Force "$src\commands\ai-content-creator.md" "$dst\commands\"
```

macOS / Linux:

```sh
cp -R opencode/skills/ai-content-creator ~/.config/opencode/skills/
cp opencode/agents/ai-content-creator.md ~/.config/opencode/agents/
cp opencode/commands/ai-content-creator.md ~/.config/opencode/commands/
```

Restart OpenCode, then use the skill directly or type `/ai-content-creator`.

## Install — Claude Code

Copy the rebuilt skill into your personal skills folder:

```powershell
$src = "C:\path\to\ai-content-creator-public\claude\skills\ai-content-creator"
$dst = "$env:USERPROFILE\.claude\skills\ai-content-creator"
Copy-Item -Recurse -Force $src $dst
```

macOS / Linux:

```sh
cp -R claude/skills/ai-content-creator ~/.claude/skills/ai-content-creator
```

Optional: copy `claude/CLAUDE.md` into your working project root for a compact always-on summary.

Restart Claude Code and invoke `/ai-content-creator`. The Claude skill uses `WebSearch`, `WebFetch`, `Bash`, `Read`, `Write`, `Edit`, `Glob`, `Grep`, `AskUserQuestion` (when available) and `Skill`. Where the shared references mention OpenCode tool names, read them as:

| Reference says | Claude uses |
|---|---|
| `question` | `AskUserQuestion`, or one plain question message |
| `shell` | `Bash` |
| `websearch` / `webfetch` | `WebSearch` / `WebFetch` |
| `skill` | `Skill` |
| `Read` / `Write` / `Edit` | same names |

## Usage

The skill asks at most three questions per message:

1. Starting point — fresh research / existing topic / saved trend list.
2. Language and audience.
3. Research scope — `Cartoon-ready` or `All videos`.

Then it offers an engine choice (`You recommend` by default) and a voice source (`Auto`, `I'll record it`, `Force Kokoro`, `Force ElevenLabs`).

Research output contains exactly ten ranked topics with a direct `youtube.com/shorts/<ID>` link for each, a source and date for every number, and a clear pick. Choose a number to get:

- `work/script.txt` — spoken words only, drives timing.
- `work/script_elevenlabs.txt` — spoken words plus `[ ]` emotion tags.
- `work/script_full.txt` — director's copy with `[[[ ]]]` character/prop/setting notes.
- `work/voices.json` — narrator and dialogue voice map.
- `work/BRIEF.md` — production brief.

Audio is generated only after you approve a short preview. The full run writes `voice.mp3`, `voice.wav`, `work/voice_segments.json` and `work/voice_duration.json`. The film engine then owns the contact sheet, render and final MP4.

## Safety rules

- Original characters only: no real named living people, brand mascots, logos, politics or graphic content.
- No copied shots, captions, sounds or edits from trending videos.
- Every number is sourced and dated; tracker-derived links are labelled as such.
- User-supplied voice is never edited, re-timed, ducked or compressed. Music and SFX sit at 50% of the voice level.
- No captions unless the user asks or approves a contact sheet that shows them.
- A short voice preview is approved before any full generation.

## License

MIT — see [LICENSE](LICENSE).
