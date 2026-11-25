# Launch copy

Ready-to-post text. Replace nothing except optional personal details. Repo: https://github.com/ashiqurrahmananik/ai-content-creator-skill

## Show HN — title

Show HN: AI Content Creator – an OpenCode and Claude Code skill that takes viral Shorts research through script, voiceover and finished vertical video

## Show HN — body

I built a skill that handles the boring middle of short-video production.

Give it a topic and it will:
- research current YouTube Shorts / Facebook Reels patterns, with direct Shorts links and dated sources;
- write an original script in three files (clean text, ElevenLabs emotion tags, director notes);
- generate a voiceover — ElevenLabs if a key is set, otherwise free offline Kokoro — with separate narrator and dialogue voices;
- hand a prepared project to a film engine (`lemo-opuscar` or `cartoon-audio-short`) for the contact sheet, render and final MP4.

It works in both OpenCode and Claude Code. The repo includes a 10-second demo GIF and a worked example.

The rules I cared most about: never invent view counts or video IDs, never copy a trending video's characters or shots, never alter a user's supplied recording, and always approve a voice preview before spending ElevenLabs credits.

Repo: https://github.com/ashiqurrahmananik/ai-content-creator-skill

I would love feedback on the research step and on making the film-engine handoff less platform-specific.

## Reddit — r/ClaudeAI / r/OpenAI

Title: I packaged a viral-Shorts-to-finished-video pipeline as both an OpenCode and Claude Code skill

Body:
I got tired of AI video workflows that stop at the script, so I built one that carries through to the MP4.

What it does:
- dated Shorts/Reels research with direct `youtube.com/shorts/...` links, not tracker pages
- original scripts with separate clean / ElevenLabs-tagged / director-note files
- auto voiceover: ElevenLabs if `ELEVENLABS_API_KEY` exists, otherwise free offline Kokoro
- narrator + character dialogue voices, preview approval before full TTS
- handoff to `lemo-opuscar` or `cartoon-audio-short`, including the contact-sheet gate

MIT licensed, 10-second demo in the README:
https://github.com/ashiqurrahmananik/ai-content-creator-skill

Happy to answer questions about the Claude rebuild — the frontmatter and tool names are adapted from the OpenCode version.

## X / Twitter posts

1. Built a skill that goes from viral Shorts research → script → voiceover → finished vertical video. Works in OpenCode and Claude Code. MIT, demo GIF in README: https://github.com/ashiqurrahmananik/ai-content-creator-skill

2. The part I'm most happy about: it never copies a trending video. It extracts the pattern, writes original characters, and labels every view count and direct Shorts link with a source and date.

3. Voice is a choice: user recording, ElevenLabs if a key is set, or free offline Kokoro. Narrator + dialogue voices, short preview approval before the full run. No key ever written to a file.

4. OpenCode and Claude Code versions are both in one repo, with the Claude skill rebuilt using Agent Skills frontmatter and Claude tool names. https://github.com/ashiqurrahmananik/ai-content-creator-skill

5. The handoff is deliberately hands-off: after the script and audio are ready, the film engine owns timing, contact sheet and render. This skill does not pretend to be a video editor.

## LinkedIn

I open-sourced an end-to-end short-video production skill today.

It researches current Shorts patterns with sourced numbers and direct video links, writes original tagged scripts, generates voiceovers with ElevenLabs or free offline Kokoro, and hands everything to a film engine for the final render.

It runs in both OpenCode and Claude Code, and the repo includes a demo and a worked example.

Repo: https://github.com/ashiqurrahmananik/ai-content-creator-skill

## Product Hunt

Tagline: Viral Shorts research to finished vertical video, as an AI coding-agent skill

Description: A free, MIT-licensed skill for OpenCode and Claude Code. It researches trends with sourced direct links, writes original scripts, generates or intakes voiceovers, and hands a prepared project to a film engine for the final MP4.
