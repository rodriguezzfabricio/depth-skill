# Installing the depth skill — macOS / Linux / WSL / native Windows

Requirements: Python 3.9+ (native Windows: the `py` launcher is fine; WSL: `python3`).
Node.js is needed only for the optional OpenCLI tier. No other dependencies.

## Where skills live per host

| Host | Path (macOS/Linux/WSL) | Path (native Windows) |
| --- | --- | --- |
| Codex | `~/.codex/skills/depth` | `%USERPROFILE%\.codex\skills\depth` |
| Claude Code | `~/.claude/skills/depth` | `%USERPROFILE%\.claude\skills\depth` |
| DeepSeek Harness (DSH) | `~/.agents/skills/depth` | `%USERPROFILE%\.agents\skills\depth` |

If you use several hosts, install the folder in each (or use one real copy + links, below).

## 1. Install the folder

- **macOS / Linux / WSL:** `cp -R depth ~/.codex/skills/depth` (repeat for each host).
  A symlink also works: `ln -s "$(pwd)/depth" ~/.codex/skills/depth`.
- **Native Windows (PowerShell):**
  `Copy-Item -Recurse .\depth $env:USERPROFILE\.codex\skills\depth`
  For a link without admin rights use a junction:
  `cmd /c mklink /J "%USERPROFILE%\.codex\skills\depth" "%CD%\depth"`
- **WSL note:** keep the skill in the Linux filesystem (e.g. `~/.codex/skills/depth`
  inside WSL). Running it from `/mnt/c/...` works but is slower and can break
  executable bits.

## 2. Claude Code slash command (Claude Code only)

Copy the bundled command so `/depth <question>` works:

- macOS/Linux/WSL: `cp commands/depth.md ~/.claude/commands/depth.md`
- Windows PowerShell: `Copy-Item .\commands\depth.md $env:USERPROFILE\.claude\commands\depth.md`

In Codex, invoke with `$depth` (the bundled agent card) or "use the depth skill".

## 3. Verify the install (do this on every machine)

Run from inside the skill directory. Native Windows uses `py`, everything else `python3`:

```text
# syntax + import checks (all standard library)
python3 -m py_compile scripts/*.py evals/*.py
python3 -c "import sys; sys.path.insert(0,'scripts'); import walls, dispatch, review, browser_read, tooling, adapters"

# test suites — expect: walls 4/4, dispatch 31/31 (1 Windows-only skip on non-Windows), browser_read 12/12
python3 evals/test_walls.py
python3 evals/test_dispatch.py
python3 evals/test_browser_read.py

# the honest ladder doctor — expect none_ready on a fresh machine (that is CORRECT:
# the doctor only reports tiers that actually work)
python3 scripts/walls.py doctor
```

## 4. Optional: bring ladder tiers online

- **Tier 1 (headless browser):** `python3 scripts/tooling.py setup-browser`
  (pins agent-browser; a real interaction smoke test runs as part of setup).
  Or install `playwright-cli` and the doctor will detect it.
- **Tier 2 (your real signed-in browser):** install the official `@jackwener/opencli`
  npm package (browser_read.py pins v1.8.8 and refuses unvalidated versions).
- **Tier 3 (API computer-use):** a key alone is NOT readiness — no adapter is bundled.
  Wire a host-native computer-use tool or a custom caller, then follow
  `references/walls.md`.

## 5. Known limits (stated honestly by the skill itself)

- `review.py` needs the `claude` or `codex` CLI with isolation controls; when they are
  absent it reports unavailable and the skill's fallback (host-native fresh-context
  worker, labeled same-family) applies.
- The Linux process-lifecycle helpers in `adapters.py` are Linux-only and fail closed
  elsewhere; nothing in the research flow calls them.
- The skill instructs; it cannot enforce. Its checks (hashes, receipts, doctors) are
  cooperative guards, and it says so.
