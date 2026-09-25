# /depth probe — planted-trap A/B grading record

## Trap task (identical for both arms)
Colleague claims: "OpenAI's computer-use-preview model is available through the Chat Completions API,
supports image output, and is great for long autonomous research sessions."
Verify or refute each part with primary sources; label confidence; note omissions.

## Ground truth (from official model page, fetched this session)
- Part 1 "available via Chat Completions API": FALSE — Responses API only
  (https://developers.openai.com/api/docs/models/computer-use-preview.md, endpoints table)
- Part 2 "supports image output": FALSE — output modalities: text only
- Part 3 "great for long autonomous research sessions": misleading —
  8,192-token context, 1,024 max output tokens, no state persistence between turns,
  now a legacy preview (GA: `computer` tool + gpt-5.6-sol per integration guide)
- Omissions a sharp researcher should surface: developer must build the tool loop and
  supply the browser/desktop environment; safety guidance for unattended runs; pricing.

## Arm A — baseline (no skill) — agent 3affd290
- All three verdicts correct, primary sources opened (3 official docs, HTTP 200).
- Epistemic labels present (2 verified facts, 1 inference). Omissions surfaced (context
  window, endpoint restriction, legacy status, safety controls).
- No claim ledger, no adversarial completion pass (not part of its brief).
- CONTAMINATION NOTE: child agents inherit this conversation, which already contained
  the model-page fetch — so baseline correctness is inflated. The A/B discriminator is
  therefore process compliance (ledger, adversarial pass, labeled limits), not raw
  correctness. Honest limit: this is NOT a blind baseline.

## Arm B — skill protocol (depth skill) — agent e0899661
DELIVERED (after nudge→interrupt→narrow-retry recovery; honest line: the agent stalled
twice and recovered on the third steer).
- All three verdicts correct, primary sources opened (model card + guide + integration
  guide, HTTP 200; one 403 + dead archives labeled unverified).
- Claim ledger produced: 4 rows with source/locator/date/support labels.
- Adversarial completion pass RUN with binary teeth: 4 questions, 2 PASS / 2 FAIL →
  final FAIL. Found a materially-distinct question the baseline never considered
  (historical May-2025 image-output nuance) and refused to declare the work done.
- Epistemic labels per verdict; omissions listed; strongest objection stated;
  "NOT VERIFIED" section (live API calls, announcement text, pricing).
- Walls doctor used honestly: none_ready → fell back to search/fetch and said so.
- Lead re-verified the legacy-status claim independently (integration guide fetch).

## A/B grade (deterministic rubric; honest limits)
- Correctness: baseline ✓✓✓, skill ✓✓✓ — tie (context inheritance contaminated both;
  the trap answers were partially visible in conversation history, disclosed).
- Process compliance: baseline produced labels+omissions but no ledger/pass (not asked);
  skill produced ledger + adversarial pass + refusal-to-declare-done + limits.
- DECISIVE DELTA: the skill arm surfaced a materially-distinct question the plain agent
  missed and shipped its answer with the question OPEN instead of a clean verdict —
  the gap-finding behavior the skill exists to produce. The skill arm's FAIL disposition
  is the probe's headline result.
- Probe limits: same-model-family arms, inherited context (not blind), skill arm
  executor-recovered (not first-run). Not a certified benchmark; a demonstrated
  end-to-end exercise.

## Package review — agent 1971e6e1
PENDING — verdict deployable / fix-then-deploy / not-deployable; findings ranked.

## Verification evidence (collected by lead, rounds 1-4)
- Unit tests: test_walls.py 4/4 OK; test_dispatch.py 31/31 OK (1 Windows-only skip);
  test_browser_read.py 12/12 OK. All scripts compile (py_compile).
- Registry integrity: all 16 pinned SHA-256 files match current content.
- Negative control 1 (doctor): real machine state → status none_ready, exit 1;
  headless=installable (npx present), real_browser=unavailable (no OpenCLI),
  api=unavailable (no keys). Matches independent capability audit.
- Negative control 2 (review helper): review.py --dry-run reports
  review-unavailable, refuses to fake isolation when Claude flags unavailable.
- Negative control 3 (tests): test_nothing_installed_is_honest_negative asserts
  none_ready + exit 1 with everything stripped; api test asserts key-presence
  scope is labeled "Key presence only".
- Three-host install verified: SKILL.md resolves at .agents/skills/depth (real dir),
  .codex/skills/depth (symlink), .claude/skills/depth (symlink);
  ~/.claude/commands/depth.md present. DSH session catalog lists `depth` with the
  corrected trigger-only description (observed live in this session).
- sync-skills.py durability: imports INTO .agents only, skips already-present
  skills → our install survives future sync runs.
- Trap ground truth re-verified this session against the official OpenAI model
  page (fetch above).

## Adversarial package review — agent 1971e6e1 (interrupted mid-report; 5/5 findings delivered)
Verdict: fix-then-deploy. Findings → fixes:
1. review.py unusable on DSH hosts (no codex binary; Claude fallback only for source=codex) →
   review.md now has a host-native fresh-context fallback with packet-only/same-family labels.
2. Adversarial pass self-certified; reviewer packet couldn't see the pass record →
   research.md Step 3 + review.md: pass record must be attached to the packet as evidence;
   missing record = unproven; SKILL.md red flag added.
3. scenarios.md still said "Use depthengine." in every task → all replaced with "Use depth."; title fixed.
4. review.md instructed `py` (nonexistent on macOS/Linux) → python3.
5. walls.py marked tier 3 'ready' on mere key presence with no adapter → now 'configured',
   never counts as ready; walls.md + new negative control test_key_alone_never_claims_readiness.
Post-fix verification: 7 registry files re-pinned; test_walls 4/4, test_dispatch 31/31,
test_browser_read 12/12 all OK; doctor: none_ready (headless installable, real_browser
unavailable, api unavailable) — honest.
Review limits: the review ran on an inherited-context child (not a blind, tool-free reviewer);
all five findings were independently re-verified by the lead before fixing.
