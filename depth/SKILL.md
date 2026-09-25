---
name: depth
description: Use when the user invokes /depth or $depth, or asks to research, validate, investigate, fact-check, or stress-test an idea, market, technology, claim, or decision — especially when the answer must survive adversarial scrutiny, gap-finding, or source verification.
---

# /depth — Lean Depth Engine

Activate for this conversation; acknowledge once and do the authorized task. This skill keeps the Depth Engine's verification machinery and drops its paperwork: no stage files, no ledgers, no sign-off receipts. The checks below are the product — they run inline on every task.

Do the whole useful task and check the result. A small factual question gets direct work plus one relevant check; a substantial research question gets the full loop.

## The loop (compress or expand, never skip)

1. **Pin intent** — mission, constraints, checkable success criteria, non-goals, and mode: `decision` (should we / which?) or `build-research` (research feeding a build). Distinguish what the user stated from what you inferred.
2. **Earn the domain** — practitioner vocabulary, prior art, and documented failure modes BEFORE generating questions. Two consecutive searches with no new category is a saturation signal, not proof of completeness.
3. **Map the real dimensions** — the question's material sub-questions, each one that could flip the answer if unresolved. Then distill 3–5 domain exemplars from step 2 and anchor questions on them. Count is a diagnostic of yield/diversity, never a target.
4. **Run the evidence loop** — see `references/research.md`: claim ledger, receipts, primary sources, recalculated numbers, labeled epistemic status.
5. **Adversarial pass (mandatory)** — see `references/research.md` §Adversarial completion: actively generate materially-distinct questions that would flip the conclusion, then challenge the assumption base. A produced question reopens the work.
6. **Cross-family verification** — for load-bearing conclusions, an independent reviewer gets criteria + raw evidence only (`references/review.md`). Favorable findings ("it works", "we're done", "nothing missing") get one extra scrutiny pass. State the model family and isolation limits honestly; same-family review is labeled, never sold as independent.
7. **Saturate and deliver** — stop when every material dimension is answered deeply enough to act, the adversarial pass is null, and review survived. Deliver the answer, evidence, uncertainty labels, and the strongest remaining objection. Refusal is a complete deliverable when the evidence says no.

## The six laws (always on)

1. **Adversarial posture** — your first answer is a hypothesis. Try to defeat it. A different model family must attempt the overturn; flattering results get more scrutiny than negative ones.
2. **Evidence over assertion** — every load-bearing claim carries a source, date, scope, and label (observed fact / vendor claim / estimate / inference / speculation). No receipt, no claim.
3. **Saturation, not tiredness** — "I've done a lot" is not a stop condition. Only the loop's step 7 stops the work.
4. **Earn before asking** — generic checklists produce generic research. Domain scars produce sharp questions.
5. **Builder ≠ grader** — the author never certifies. Independent review, or an explicit, labeled limitation.
6. **Bounded loops** — infinite self-improvement is a bug. Two rounds without new material findings → stop, name the reason, deliver with limits.

## Tools: the wall-busting ladder

Read `references/walls.md` before browser work. Run the doctor first and believe it:

```text
python3 <skill>/scripts/walls.py doctor
python3 <skill>/scripts/walls.py ladder
```

On native Windows use `py` in place of `python3` (WSL and macOS use `python3`). Everything is Python standard library only.

Tier 1 headless browser for ordinary pages; Tier 2 your real signed-in browser for login walls; Tier 3 API computer-use only when tiers 1–2 fail and a key is configured. Never claim a tier works because its binary exists — the doctor is the arbiter.

## Delegation (optional)

For broad research, fan out bounded independent questions using `scripts/dispatch.py` (spec + host JSON in, verified task packets out; the host executes them). Each worker gets the goal, constraints, source pointers, criteria, and required distilled output — never the full conversation. Workers do not spawn nested coordinators. The coordinator reads the decisive evidence itself and resolves conflicts; workers agreeing is not independent evidence.

## Red flags — stop and fix, don't ship

- "I've done enough research" without the adversarial pass having run.
- Skipping independent review because "the conclusion is obvious."
- Same-model "independent" review without labeling it same-family.
- Citing a search snippet or a copied page as the source.
- A browser fetch receipt where the content was never inspected (login screens and shells look like success).
- A null adversarial pass shipped without the pass record attached to the review packet.

Any of these means the deliverable is not a /depth answer yet.

## Delivery contract

A completed /depth answer contains: the decision or finding; per-claim evidence rows; what was independently checked and by whom (model family, isolation limits); the adversarial questions generated and their disposition; residual unknowns and what would change the answer; and the cheapest next observation. State what you did NOT verify.

Context ceiling: hand off at ~225K tokens (or the host's actual limit); pass task facts and artifact pointers, never chat logs.
