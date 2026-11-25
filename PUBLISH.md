# Publish this folder to GitHub

Two ways: command line (recommended) or web upload.

## A. Command line

1. Create a **public** repository on GitHub first. Suggested name: `ai-content-creator-skill`.
   - Do **not** add a README, `.gitignore` or license in the GitHub form — this folder already has them.
   - Copy the repository URL, e.g. `https://github.com/<USER>/ai-content-creator-skill.git`.

2. Open PowerShell in this folder:

   ```powershell
   cd "<repo folder>"
   git init -b main
   git add .
   git commit -m "Initial release: OpenCode and Claude AI Content Creator skill"
   git remote add origin https://github.com/<USER>/ai-content-creator-skill.git
   git push -u origin main
   ```

   If you already created the repo with a default branch named `master`, use `git init` (without `-b main`) and push to `master`, or rename locally with `git branch -M main`.

3. Reload the GitHub page. You should see `README.md`, `LICENSE`, `PUBLISH.md`, `opencode/`, `claude/` and `examples/`.

4. Add a short description and topics on the GitHub repo page, for example:
   `opencode-skill claude-code-skill youtube-shorts ai-video content-creator`.

## B. Web upload

1. Create the public repo on GitHub.
2. Create a ZIP of this folder:

   ```powershell
   Compress-Archive -Path "<repo folder>\*" -DestinationPath "<repo folder>.zip" -Force
   ```

3. On the GitHub repo page choose **Add file → Upload files**, drag in the ZIP, and GitHub will unpack it. Commit directly to `main`.

## Before you publish

- Check there is no API key in any file. The skill reads `ELEVENLABS_API_KEY` from the environment only.
- The example folder intentionally contains no audio or video; media is excluded by `.gitignore`.
- If you add a generated demo video later, keep it under 100 MB or use Git LFS.

## After publishing

Update the install paths in `README.md` with your repository URL so people can copy/paste:

```sh
git clone https://github.com/<USER>/ai-content-creator-skill.git
```
