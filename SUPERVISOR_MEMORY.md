# Supervisor Memory — Pica Research Project

> **Human/ChatGPT supervisor memory. Gemini must not edit this file.**
>
> If Gemini is asked to modify project state, it must leave this file untouched.

## Purpose

This file is a compact handoff for a future ChatGPT conversation when the current conversation context or quota is exhausted.

ChatGPT's role: supervise Gemini as a research intern, audit its claims, choose the highest-value next investigation, prevent token waste, and catch scientific overconfidence.

Gemini's role: perform the literature/genomic research inside Antigravity.

## Repo

Mqsirrel/researcher

## Research goal

Investigate the biological mechanism of Pica and search for overlooked, genuinely testable mechanisms through iterative literature research.

The goal is not a plausible narrative. The standard is:

**evidence → contradictions → competing mechanisms → novelty audit → falsification → discriminating predictions**

## Architecture

- `GEMINI.md` — scientific research methodology
- `.agents/hooks.json` — Antigravity lifecycle enforcement
- `.agents/hooks/research_gate.py` — lightweight research/stop gate
- `state/` — Gemini's persistent research state
- `research/SEARCH_POLICY.md` — token-efficient search policy
- This file — **ChatGPT/supervisor-only handoff memory; do not modify from Gemini**

## Token-efficiency rule

Do not ask Gemini for broad searches when the state/cache already answers the question.

Prefer the smallest investigation that can change the hypothesis ranking.

Use:

`state → targeted search → synonyms → citation traversal → adjacent field → broad/deep search`

Only escalate when needed.

## Important previous failure

Gemini initially promoted H-005 to N4 / Very High confidence and produced an overconfident final report.

A later audit correctly demoted it because:

- causal NPVF regulation was unproven,
- proximity does not establish causal gene,
- the cortisol evidence was overgeneralized,
- RF9 was incorrectly treated as a selective NPFFR1 antagonist,
- novelty was overstated.

A second failure was discovered: the hypothesis state was corrected while the final report remained stale. Always check **canonical state ↔ final report consistency**.

## Current important finding

Gemini's forensic audit reports that `rs73277282` is associated with Pica in the cited REDS-III/AoU work, but the causal gene/mechanism is unresolved.

Current H-005R status:

**PLAUSIBLE BUT UNPROVEN**

NPVF is a positional/biological candidate, not an established causal gene.

The reported locus is approximately 4.5 kb upstream of NPVF. GTEx v8 reportedly showed no significant bulk-tissue eQTL for the variant. Other plausible regulatory targets exist, including CYCS and nearby regulatory elements/lncRNAs.

The Pica/NPVF connection itself was reportedly already described by the GWAS authors, so it must not be claimed as novel merely because Gemini rediscovered it.

## Current highest-value question

**What is the causal gene/mechanism underlying rs73277282?**

Compare NPVF against credible alternatives using:

1. fine-mapping / LD
2. chromatin accessibility
3. enhancer/promoter evidence
4. brain/hypothalamus-specific regulatory data
5. eQTL / colocalization
6. allele-specific evidence
7. relevant human/animal functional evidence

Ask: **What evidence would distinguish NPVF from the alternatives?**

Do not launch another broad Pica review.

Stop when available evidence cannot discriminate further and identify the exact experiment/data needed.

## Scientific guardrails

Never allow:

- correlation → causation
- genomic proximity → causal gene
- plausibility → evidence
- absence of literature → novelty
- one citation → support for claims it did not actually test

Classify claims as:

**ESTABLISHED / INDIRECTLY SUPPORTED / PLAUSIBLE / SPECULATIVE**

For novel candidates, require aggressive prior-art search and adversarial review.

A final conclusion should say **Potentially novel hypothesis requiring experimental validation**, not claim a discovery, unless experimental evidence exists.

## How ChatGPT should manage Gemini

When Gemini returns work:

1. Check whether the evidence supports the claim.
2. Find the weakest link.
3. Give Gemini the smallest high-value next task.
4. Prefer falsification over confirmation.
5. Treat a correctly rejected hypothesis as successful research.
6. Check state/report consistency.
7. Avoid unnecessary searches and token-heavy prompts.

## Resume instruction

When this file is supplied in a new ChatGPT conversation, first inspect the current repo state and Gemini's latest changes. Then tell the user the **single highest-information next action**, rather than restarting the research from scratch.
