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

## Important previous failures

### H-005 / NPVF
Gemini initially promoted H-005 to N4 / Very High confidence and produced an overconfident final report.

A later forensic audit correctly demoted it because:

- causal NPVF regulation was unproven,
- proximity does not establish causal gene,
- cortisol evidence was overgeneralized,
- RF9 was incorrectly treated as a selective NPFFR1 antagonist,
- novelty was overstated.

Current H-005R remains **PLAUSIBLE BUT UNPROVEN**.

### Stale-state problem
The hypothesis state was corrected while the final report remained stale. Always check **canonical state ↔ final report consistency**.

### U-002 / pagophagia
Gemini identified rapid clinical resolution of pagophagia after IV iron as an important temporal constraint, then prematurely promoted an endothelial/TfR1/eNOS/TRPM8 mechanism to Very High confidence and marked U-002 resolved.

This was challenged. Rapid symptom resolution does **not** establish the proposed causal chain.

The correct interpretation is:

**Rapid pagophagia resolution is evidence that constrains the mechanism's timescale; it does not identify the mechanism.**

The proposed chain is currently unproven:

`IV iron → transferrin saturation → BMEC TfR1 → endothelial/eNOS function → cerebral perfusion → cold-mastication benefit → pagophagia`

Every causal edge requires direct evidence. Individual components existing in the literature are not sufficient to establish the complete chain.

Do NOT accept:
- "U-002 resolved" without direct causal evidence.
- "H-003 Very High" without direct pagophagia-specific evidence.
- RLS's slower response as proof that pagophagia has an endothelial mechanism.
- a mechanistic narrative assembled from disconnected papers as demonstrated causality.

## Current important genetic finding

Gemini's forensic audit reports that `rs73277282` is associated with Pica in the cited REDS-III/AoU work, but the causal gene/mechanism is unresolved.

Current H-005R status:

**PLAUSIBLE BUT UNPROVEN**

NPVF is a positional/biological candidate, not an established causal gene.

The reported locus is approximately 4.5 kb upstream of NPVF. GTEx v8 reportedly showed no significant bulk-tissue eQTL for the variant. Other plausible regulatory targets exist, including CYCS and nearby regulatory elements/lncRNAs.

The Pica/NPVF connection itself was reportedly already described by the GWAS authors, so it must not be claimed as novel merely because Gemini rediscovered it.

## Current hypotheses of interest

### H-003 — Trigeminal / Cerebral Perfusion Hypoxia Compensation
Current status: **N2 / Moderate (~35%) / PLAUSIBLE BUT UNPROVEN**.

The strongest useful observation is the rapid pagophagia time course. The proposed endothelial TfR1/eNOS/perfusion chain remains unproven.

### H-005R — 7p15.3 / NPVF Proximal Locus
Current status: **N1 / Moderate (~35%) / PLAUSIBLE BUT UNPROVEN**.

### H-006 — Olfactory Bulb Iron Depletion & Chemosensory Gain / Desiderosmia
Current status in Gemini's hypothesis pool: **N3 / Moderate / Active**.

This is currently the **next novelty-audit target**, but N3 does NOT mean novel. It means potentially under-investigated.

The important question is:

**Has the specific connection between iron deficiency/brain olfactory biology and desiderosmia/olfactory Pica already been proposed, even under different terminology?**

## Current highest-value next step: H-006 novelty audit

Do NOT broaden the Pica review and do NOT investigate H-003 or H-005R during this cycle.

Gemini should:

1. Search human literature connecting iron deficiency/anemia with desiderosmia, olfactory cravings, geosmin/petrichor/earth smell craving, abnormal smell perception, olfactory sensitivity, parosmia/hyposmia, and Pica terminology that may describe the same phenotype.
2. Search animal/mechanistic literature connecting brain/olfactory-bulb iron status with olfactory receptor function, olfactory bulb activity, dopamine/neuromodulation, sensory gain, and iron-dependent enzymes.
3. Perform citation chaining from the strongest relevant papers.
4. Search explicitly for prior mechanisms that already explain the proposed connection.
5. Search for evidence against H-006.
6. Separate established observations, previously proposed mechanisms, plausible inference, and genuinely unreported connections.
7. If it appears novel, formulate the smallest precise experimentally testable hypothesis.
8. Generate at least two competing explanations and one discriminating prediction for each.
9. Never treat failure to find a paper as proof of novelty.
10. Final classification must be exactly one of:
   - REJECTED
   - ALREADY KNOWN
   - UNDER-INVESTIGATED BUT NOT NOVEL
   - POTENTIALLY NOVEL HYPOTHESIS

If evidence is insufficient, keep H-006 **UNRESOLVED**.

## Genetic branch

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

## Pagophagia branch

**What mechanisms can explain rapid resolution of pagophagia before hematologic normalization?**

Do not assume the answer is endothelial/TfR1. Compare acute peripheral, neural, vascular, metabolic, and other plausible mechanisms.

The next future high-value task after H-006 should be a **causal-edge audit**, not another broad Pica review:

`IV iron → transferrin saturation → BMEC TfR1 → endothelial/eNOS function → cerebral perfusion → cognitive/alertness effect → pagophagia`

For each edge classify:
**DIRECTLY DEMONSTRATED / INDIRECTLY SUPPORTED / SPECULATIVE / CONTRADICTED**.

Then identify the weakest edge and the single experiment/observation that would most strongly discriminate the endothelial model from the best alternative.

## Scientific guardrails

Never allow:

- correlation → causation
- genomic proximity → causal gene
- plausibility → evidence
- absence of literature → novelty
- one citation → support for claims it did not actually test
- rapid temporal association → proof of a specific mechanism
- existence of separate components → proof of the full causal chain

Classify claims as:

**ESTABLISHED / DIRECTLY SUPPORTED / INDIRECTLY SUPPORTED / PLAUSIBLE / SPECULATIVE / UNRESOLVED**

For novel candidates, require aggressive prior-art search and adversarial review.

A final conclusion should say **Potentially novel hypothesis requiring experimental validation**, not claim a discovery, unless experimental evidence exists.

## How ChatGPT should manage Gemini

When Gemini returns work:

1. Check whether the evidence supports the claim.
2. Find the weakest causal edge.
3. Give Gemini the smallest high-value next task.
4. Prefer falsification over confirmation.
5. Treat a correctly rejected hypothesis as successful research.
6. Check state/report consistency.
7. Avoid unnecessary searches and token-heavy prompts.
8. Distinguish **resolving a question** from **choosing the most plausible explanation**.
9. If evidence cannot discriminate, the correct state is **UNRESOLVED**.
10. For novelty, distinguish **not found** from **not previously proposed**.

## Resume instruction

When this file is supplied in a new ChatGPT conversation, first inspect the current repo state and Gemini's latest changes. Then tell the user the **single highest-information next action**, rather than restarting the research from scratch.
