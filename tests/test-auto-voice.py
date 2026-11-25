"""Regression tests for both shipped auto_voice helpers."""

from contextlib import redirect_stdout
import importlib.util
from io import StringIO
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
HOSTS = ("claude", "opencode")


def load_helper(host):
    path = ROOT / host / "skills" / "ai-content-creator" / "scripts" / "auto_voice.py"
    spec = importlib.util.spec_from_file_location(f"auto_voice_{host}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class AutoVoiceTests(unittest.TestCase):
    def test_splits_and_attributes_dialogue_in_spoken_order(self):
        script = (
            '[[[ Production note with "unspoken dialogue" ]]]\n'
            '\n'
            '[ worried ][ quiet ] At the stairs, "Wait," she said.\n'
            'He answered, “Coming.”\n'
            '“I know,” I said.\n'
            '“A voice without an attribution.”\n'
        )
        config = {"pronouns": {"he": "leo", "she": "maya", "i": "jo"}}
        expected = [
            ("At the stairs", "narrator", ["worried", "quiet"], 3),
            ("Wait", "maya", ["worried", "quiet"], 3),
            ("she said.", "narrator", ["worried", "quiet"], 3),
            ("He answered", "narrator", [], 4),
            ("Coming.", "leo", [], 4),
            ("I know", "jo", [], 5),
            ("I said.", "narrator", [], 5),
            ("A voice without an attribution.", "narrator", [], 6),
        ]

        with TemporaryDirectory() as temp:
            path = Path(temp) / "script.txt"
            path.write_text(script, encoding="utf-8")
            for host in HOSTS:
                with self.subTest(host=host):
                    self.assertEqual(
                        load_helper(host).segments_from_script(path, config), expected
                    )

    def test_preview_uses_same_line_and_next_line_gaps(self):
        script = '[soft] At the stairs, "Wait,"\nThe door opened.\nLater that day.\n'
        expected_manifest = [
            {"id": 1, "text": "At the stairs", "speaker": "narrator",
             "emotion": ["soft"], "line": 1, "provider": "kokoro"},
            {"id": 2, "text": "Wait", "speaker": "narrator",
             "emotion": ["soft"], "line": 1, "provider": "kokoro"},
            {"id": 3, "text": "The door opened.", "speaker": "narrator",
             "emotion": [], "line": 2, "provider": "kokoro"},
        ]

        for host in HOSTS:
            with self.subTest(host=host), TemporaryDirectory() as temp:
                helper = load_helper(host)
                project = Path(temp)
                work = project / "work"
                work.mkdir()
                (work / "script_full.txt").write_text(script, encoding="utf-8")
                (work / "voices.json").write_text("{}", encoding="utf-8")

                args = [
                    str(helper.__file__), str(project), "--provider", "kokoro", "--preview", "3"
                ]
                with (
                    patch.object(sys, "argv", args),
                    patch.object(helper, "generate_elevenlabs"),
                    patch.object(helper, "generate_kokoro"),
                    patch.object(helper, "assemble") as assemble,
                    patch.object(helper, "run"),
                    patch.object(helper, "duration_of", return_value=1.0),
                    redirect_stdout(StringIO()),
                ):
                    helper.main()

                assemble.assert_called_once()
                _, gaps, wav = assemble.call_args.args
                self.assertEqual(gaps.get(2), 0.06)
                self.assertEqual(gaps.get(3), 0.18)
                self.assertEqual(wav, work / "preview_voice.wav")
                manifest = json.loads((work / "voice_segments.json").read_text(encoding="utf-8"))
                self.assertEqual(manifest, expected_manifest)


if __name__ == "__main__":
    unittest.main()
