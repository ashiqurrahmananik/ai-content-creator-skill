# Example: Grandparent Passes Down a Trade

A lightweight worked example from a real run. It shows the inputs the skill produces before a film engine takes over.

| File | What it is |
|---|---|
| `work/BRIEF.md` | Filled production brief: research sources, original angle, engine, style, voice source, constraints |
| `work/script.txt` | Clean narration used for timing |
| `work/script_elevenlabs.txt` | Same words with `[ ]` emotion tags |
| `work/script_full.txt` | Director's copy with `[[[ ]]]` character/prop/setting notes and tags |
| `work/voices.json` | Narrator and dialogue voice map plus `he`/`she`/`I` attribution map |
| `TREATMENT.md` | The director's shot list, beat sheet, cue map and sound design handed to `lemo-opuscar` |

Audio and video are intentionally not included: generated `voice.mp3`, `voice.wav`, the contact sheet and the final MP4 are media binaries and are excluded by the repository `.gitignore`.

To reproduce the audio from this example:

```sh
# from this example folder's parent, with the skill installed
python "<skill>/scripts/auto_voice.py" "<absolute path to this example folder>" --preview 3
# approve the preview, then:
python "<skill>/scripts/auto_voice.py" "<absolute path to this example folder>"
```

The final film in the original run was 1080×1920, 30 fps, 145.6 s, produced in `paper-popup` style with free offline Kokoro voices.
