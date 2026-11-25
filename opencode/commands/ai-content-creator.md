---
description: Research viral topics, recommend one, write a script, then make the video from your voiceover
agent: ai-content-creator
---
Load the `ai-content-creator` skill with the skill tool and follow it from Stage 0. Offer the research scope choice (`Cartoon-ready` for `cartoon-audio-short` / `lemo-opuscar`, or `All videos`) and always return direct `youtube.com/shorts/<ID>` links after research. Scripts come with ElevenLabs `[ ]` emotion tags and `[[[ ]]]` character notes when needed. Audio can be auto-generated: ElevenLabs if a key is set, otherwise the free built-in voice, with narrator and dialogue voices.

User request: $ARGUMENTS
