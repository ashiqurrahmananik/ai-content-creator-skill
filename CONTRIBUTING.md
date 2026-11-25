# Contributing

Thanks for helping improve the pipeline.

## Setup

```sh
git clone https://github.com/ashiqurrahmananik/ai-content-creator-skill.git
cd ai-content-creator-skill
python -m py_compile opencode/skills/ai-content-creator/scripts/auto_voice.py
python -m py_compile claude/skills/ai-content-creator/scripts/auto_voice.py
```

To test a skill change locally, copy the relevant folder into `~/.config/opencode/skills/` or `~/.claude/skills/` as described in [README.md](README.md), then restart the host.

## Ground rules

- Keep `SKILL.md` under 500 lines. Put detailed material in `references/`.
- OpenCode and Claude versions should stay in sync. If you change behavior, update both `SKILL.md` files and any affected reference.
- Never commit API keys, tokens, generated voice files or final videos. `.gitignore` already excludes media.
- Preserve the hard rules: direct Shorts links, sourced numbers, original characters, unchanged user voice, preview before full TTS, contact sheet before render.
- Use lowercase kebab-case for new files and folders.

## Pull request checklist

- [ ] Both provider variants updated (OpenCode and Claude), if behavior changed.
- [ ] `auto_voice.py` syntax-checked.
- [ ] README updated if install steps or features changed.
- [ ] No secrets, personal paths or generated media included.
- [ ] Commit message explains the user-visible change.

## Good first issues

Look for issues labelled `good first issue` in the issue tracker. Small documentation fixes, tests for `auto_voice.py`, and install scripts are especially welcome.
