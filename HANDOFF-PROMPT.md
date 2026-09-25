# Handoff prompt — install the depth skill on a Windows PC (native + WSL)

Paste this into a fresh agent session on the new machine (Codex, Claude Code, or any
agent with shell access), after cloning/downloading the repo this file lives in:

---
You are installing a verified AI-agent skill package from this repo onto this machine.
The package root contains `depth/` (the skill), `commands/depth.md`, `README.md`,
`INSTALL.md`, and `GRADING.md`. Follow INSTALL.md exactly and report evidence at each step.

Task:
1. Read README.md and INSTALL.md completely first. Detect which environment you are in
   (native Windows PowerShell/CMD, WSL, or both) and confirm it out loud.
2. Install the skill for the hosts the user has on this machine. Default target: both
   Codex and Claude Code if they exist. Check which hosts are actually installed first
   (do not create config folders for hosts that are not present unless the user asks):
   - Codex → %USERPROFILE%\.codex\skills\depth
   - Claude Code → %USERPROFILE%\.claude\skills\depth, plus commands\depth.md →
     %USERPROFILE%\.claude\commands\depth.md
   - WSL: repeat inside WSL at ~/.codex/skills/depth and ~/.claude/skills/...
   Use Copy-Item or cp (copying is preferred over links on Windows; if the user wants a
   link, use `mklink /J` for a junction — it needs no admin rights).
3. VERIFY — do not skip any of these, and paste the actual output:
   a. In the skill directory: compile + import checks and all three test suites
      (py -3 on native Windows, python3 in WSL). Expected: walls 4/4, dispatch 31/31
      (1 Windows-only skip on non-Windows), browser_read 12/12.
   b. Run `scripts/walls.py doctor`. A fresh machine is expected to report none_ready —
      that is the honest negative, not a failure. If any tier reports ready, say which.
   c. Confirm the SKILL.md frontmatter is intact and registry.json hashes match
      (recompute with the same method INSTALL.md documents if you have time).
4. If the user wants ladder tiers online, offer (do not auto-install): tier 1 via
   scripts/tooling.py setup-browser, tier 2 via the official @jackwener/opencli package.
5. End with a report: environment, hosts installed, test outputs (paste them), doctor
   output, any deviation from INSTALL.md, and the exact command the user types to
   invoke the skill on each host (/depth in Claude Code, $depth or "use the depth
   skill" in Codex).
6. Do NOT modify the skill files. If something fails, report the exact error and stop;
   do not "fix" the package — the maintainer will.
---
