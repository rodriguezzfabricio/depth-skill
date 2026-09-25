# depth — Lean Depth Engine (research skill)

A lean research skill that carries the Depth Engine's verification machinery — adversarial
gap-finding, evidence claim ledger, cross-family review, negative controls, bounded loops —
without the stage files, ledgers, or gate paperwork. Plus a 3-tier browser/computer-control
ladder with an honest doctor.

## Quick install

1. Copy the `depth/` folder to a skills root for your host:
   - **Codex:** `~/.codex/skills/depth` (Windows: `%USERPROFILE%\.codex\skills\depth`)
   - **Claude Code:** `~/.claude/skills/depth` (Windows: `%USERPROFILE%\.claude\skills\depth`)
   - **DeepSeek Harness (DSH):** `~/.agents/skills/depth`
2. Claude Code only: copy `commands/depth.md` to `~/.claude/commands/depth.md`
   (Windows: `%USERPROFILE%\.claude\commands\depth.md`) for the `/depth` slash command.
3. Verify (see INSTALL.md): run the test suites and the walls doctor.

Windows notes: on native Windows use `py` instead of `python3`. Prefer copying the folder
over symlinks; if you want a link, use `mklink /J` (junction — no admin rights needed).
Everything is Python standard library only; Node.js is needed only for the optional
OpenCLI tier.

## What's inside

- `SKILL.md` — the whole workflow in one screen (loop, six laws, red flags, delivery contract)
- `references/research.md` — evidence loop, claim ledger, the mandatory adversarial
  completion pass (binary teeth), saturation stop, domain exemplars, negative controls
- `references/review.md` — independent review, favorable-result asymmetry, host fallback
- `references/walls.md` — the 3-tier wall-busting ladder and its rules
- `scripts/` — 7 Python programs (standard library only): walls.py (ladder doctor),
  dispatch.py (verified task packets), review.py (fresh-process reviewer), browser_read.py
  (OpenCLI receipt reader), tooling.py + adapters.py (agent-browser setup/doctors)
- `evals/` — 47 tests + the A/B evaluation protocol
- `registry.json` — SHA-256 integrity pins for every file
- `agents/openai.yaml` — Codex agent registration (`$depth`)

## Verification record

This build was verified with a planted-trap A/B probe and negative controls; see the
`GRADING.md` verification record shipped alongside this skill.

## Attribution

Mechanisms ported from the Depth Engine by Endegena Assefa
(github.com/endegenaassefa/depth-engine); implementation base from the NoCatch
depthengine skill (github.com/rodriguezzfabricio/NoCatch); tool integrations per their
upstream projects (OpenCLI, agent-browser). See INSTALL.md for setup details.
