# Non-English narration timing

## Choose the engine

Prefer `lemo-opuscar` for non-English narration: its handoff explicitly
includes the narration language and it provides a voice tier. Check that
the selected voice provider supports the requested language.

Use `cartoon-audio-short` when its fixed-voiceover story workflow is
preferred and reviewed word timestamps are available. Its English
syllable-based fallback is unsuitable for reliable non-English timing.

Whisper timestamps are estimates, not guaranteed exact alignments.
Listen to the narration and check them before planning shots.


Work in `~/shorts/<slug>`, outside this repository.

Keep the final narration as `voice.mp3` and its exact spoken text as
`work/script.txt`. Exclude emotion tags and director notes from the clean
script. Do not change the recording's speed, pitch, level or pauses.

Use the final audio for transcription. If the recording changes,
regenerate and review its timestamps.

## Generate multilingual Whisper output

Prerequisites: Python, ffmpeg on PATH, and `openai-whisper` installed in
a dedicated Python environment:

```bash
python -m pip install openai-whisper
```

The first transcription downloads the selected model.

From the narration project's root, run this Bengali example:

```bash
python -m whisper voice.mp3 --model base --language bn --task transcribe --word_timestamps True --output_format json --output_dir work/whisper
```

Replace `bn` with the narration's language code, such as `ur` for Urdu,
`hi` for Hindi, or `es` for Spanish.

Use a multilingual model such as `base`, not the English-only `base.en`.
Keep `--task transcribe`: translation would replace the original-language
words with English.

Whisper writes `work/whisper/voice.json`. Its word timestamps are nested
under `segments[].words[]`; this is not yet the engine's flat word list.

## Create work/words.json

Save the following as `work/extract-whisper-words.py` inside the narration
project:

```python
import json
import math
from pathlib import Path

source = Path("work/whisper/voice.json")
transcript = json.loads(source.read_text(encoding="utf-8"))
words = []

for segment in transcript["segments"]:
    for item in segment.get("words", []):
        text = item["word"].strip()
        if not text:
            continue
        start = float(item["start"])
        end = float(item["end"])
        if not (
            math.isfinite(start)
            and math.isfinite(end)
            and 0 <= start <= end
        ):
            raise ValueError(f"Invalid word timing: {item!r}")
        words.append({"w": text, "s": start, "e": end})

if not words:
    raise ValueError("No word timestamps found; enable --word_timestamps True")

Path("work/words.json").write_text(
    json.dumps(words, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)
print(f"Wrote {len(words)} entries to work/words.json")
```

Run it from the narration project's root:

```bash
python work/extract-whisper-words.py
```

Each entry contains `w` (spoken text), `s` (start in seconds), and `e`
(end in seconds), relative to the beginning of the unchanged audio.

## Worked example

Suppose `work/script.txt` contains this Bengali narration:

```text
আজ আকাশ পরিষ্কার।
```

Record those words as `voice.mp3`, run the Bengali Whisper command above,
then run the conversion script.

The resulting structure looks like this. These times are illustrative,
not measured output; use the timestamps generated from your recording.

```json
[
  {"w": "আজ", "s": 0.2, "e": 0.55},
  {"w": "আকাশ", "s": 0.6, "e": 1.1},
  {"w": "পরিষ্কার।", "s": 1.15, "e": 1.9}
]
```

## Review and handoff

- Compare recognized words with `work/script.txt` while listening.
  Check omissions, repetitions, names, code-switching and long pauses.
- Check word order and timestamps against the recording's duration.
  Word segmentation can differ between languages.
- For poor recognition, try a larger multilingual model and review again.
  Do not invent timings for missing words.
- Keep reviewed `work/words.json` alongside `voice.mp3` and the clean script.
- Tell the cartoon engine to use these reviewed timings. Check its
  installed timing workflow before running helpers: regenerating timing
  files can overwrite this file or use an English-only model.
- For lemo, include the language, original audio path and clean script
  path in the handoff described in [handoff.md](handoff.md).
- Word timings do not authorize captions. Preserve the contact-sheet
  approval gate before rendering.

## Reference

[OpenAI Whisper documentation and CLI source](https://github.com/openai/whisper)