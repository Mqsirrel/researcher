# Supervisor Memory — Pica Research Project

> **Human/ChatGPT supervisor memory. Gemini must not edit this file.**
> If Gemini is asked to modify project state, it must leave this file untouched.

## Purpose

Compact handoff for future ChatGPT conversations when context/quota runs out.

ChatGPT supervises Gemini as a research intern: audit claims, choose the highest-information next action, prevent token waste, and catch scientific overconfidence.

Gemini performs literature/genomic research inside Antigravity.

## Research goal

Investigate biological mechanisms of Pica and search for overlooked, genuinely testable mechanisms through iterative literature research.

Standard:
**evidence → contradictions → competing mechanisms → novelty audit → falsification → discriminating predictions**

The target is not a plausible narrative. A successful candidate should be an unusual connection that survives prior-art and adversarial causal review and produces a clear testable prediction.

## Repo architecture

- `GEMINI.md` — methodology
- `.agents/hooks.json` — lifecycle enforcement
- `.agents/hooks/research_gate.py` — lightweight research/stop gate
- `state/` — Gemini's persistent research state
- `research/SEARCH_POLICY.md` — token-efficient search policy
- `SUPERVISOR_MEMORY.md` — **ChatGPT/supervisor-only; Gemini must not modify**

## Token strategy

User has finite Gemini quota. Do NOT optimize for long autonomous runtime or broad literature completeness.

Optimize for **information gained per token**.

Use:
`state → targeted search → synonyms → citation traversal → adjacent field → deeper search only if ranking can change`

Prefer killing/demoting candidates cheaply over accumulating supporting papers.
Do not generate a new hypothesis while a promising candidate still has an unresolved high-information falsification/design question.

## Important previous failures

### H-005 / NPVF
Initially promoted to N4 / Very High with overconfident claims. Later forensic audit found causal NPVF regulation unproven, proximity insufficient, cortisol evidence overgeneralized, RF9 characterization incorrect, and novelty overstated.

Current H-005R: **PLAUSIBLE BUT UNPROVEN**. The Pica/NPVF connection was reportedly already described by the GWAS authors and must not be called novel merely because Gemini rediscovered it.

### U-002 / pagophagia
Gemini prematurely promoted endothelial/TfR1/eNOS/TRPM8 to Very High and marked it resolved. Audit showed rapid symptom resolution constrains timescale but does not identify mechanism.

Current chain remains unproven:
`IV iron → transferrin saturation → BMEC TfR1 → endothelial/eNOS → cerebral perfusion → cold-mastication benefit → pagophagia`

Do not accept a mechanistic narrative assembled from disconnected papers as demonstrated causality.

### H-006
Adversarial novelty audit classified H-006 as **UNDER-INVESTIGATED BUT NOT NOVEL**. This was a successful falsification/novelty result, not a project failure.

Lesson: failure to find an exact paper is not novelty; alternative terminology and citation chaining matter.

## Current hypotheses

### H-003 — Trigeminal / Cerebral Perfusion Hypoxia Compensation
**N2 / Moderate (~35%) / PLAUSIBLE BUT UNPROVEN**.
Rapid pagophagia time course is useful, but the endothelial/eNOS/perfusion chain is unproven.

### H-005R — 7p15.3 / NPVF Proximal Locus
**N1 / Moderate (~35%) / PLAUSIBLE BUT UNPROVEN**.
Causal gene/mechanism unresolved.

### H-007 — Hepatic Portal Vagal Transferrin Sensor
Latest adversarial audit: **SURVIVES — NEEDS MORE EVIDENCE**, ~30%.

The candidate explains ultra-rapid post-IV-iron pica extinction through:
`IV iron → rapid TSAT increase → hepatic/periportal sensing → hepatic vagal afferents → NTS/PBN → pica-drive suppression`

Critical weakness discovered by Gemini: **zero electrophysiological evidence that vagal afferents directly sense transferrin/acute iron changes**. Liver-vagus signaling, hepcidin regulation, and appetite circuitry separately existing do not prove this complete mechanism.

Do not promote H-007 to experimental-ready until the missing transduction mechanism has stronger evidence or a more defensible testable intermediate is identified.

### H-008 — AMY1 CNV & Gestational Starch Counter-Regulation / Amylophagy
Latest adversarial audit: **POTENTIALLY NOVEL — READY FOR EXPERIMENTAL DESIGN**, ~45%, but this now requires a statistical/experimental-design audit before any further promotion.

Core observation:
IV iron reportedly failed to resolve amylophagy in the cited REVAMP 2025 RCT while geophagy improved. Gemini proposes:
`AMY1 CNV → salivary amylase → pre-absorptive starch handling/glycemic signaling → selective persistent starch craving`, potentially interacting with pregnancy insulin resistance.

Important caveat: established AMY1 biology is NOT evidence that AMY1 causes amylophagy. The unproven edge is specifically:
**AMY1 copy number → compulsive non-food starch craving/amylophagia.**

Proposed test must not assume arbitrary copy-number thresholds or effect sizes. The relevant human phenotype, measurement method, confounders, power, and falsification criterion must be justified prospectively.

## Current ranking

1. **H-008** — strongest current candidate; potentially novel and experimentally testable, pending design/statistical audit.
2. **H-007** — interesting and potentially novel, but critical sensor/transduction evidence is missing.

Do NOT generate H-009 yet.

## Current highest-value task

Perform a **statistical + experimental-design audit of H-008 only**.

Do NOT spend tokens on another broad literature review unless a specific finding is needed to resolve a design question.

Audit:
1. Whether the REVAMP phenotype is suitable for testing H-008 and how persistent amylophagia should be defined.
2. Whether binary amylophagia is adequate versus frequency/severity/duration.
3. Whether any proposed sample size is actually powered; do not assume N=60/group.
4. What effect sizes are defensible and what sample size can detect them.
5. Best AMY1 CNV measurement method (ddPCR/qPCR/sequencing/other validated methods).
6. Whether CNV should be modeled continuously or categorically; no arbitrary ≤4 threshold without evidence.
7. Appropriate primary statistical model and major confounders: ancestry/population structure, age, BMI, parity, gestational stage, diet/carbohydrate exposure, socioeconomic factors, iron status and treatment response, and other relevant variables.
8. Which causal edges the human study can actually test versus merely associate.
9. At least two competing explanations and measurements that discriminate them.
10. A real falsification criterion using effect-size confidence intervals, meaningful pre-specified effects, power, and equivalence testing if appropriate. Never use p>0.05 alone as proof of falsification.
11. Whether an existing biobank, a pilot, or a new cohort gives the highest information per sample/cost.

Final verdict must be exactly one of:
- READY FOR A REAL-WORLD EXPERIMENT
- NEEDS PILOT DATA FIRST
- NEEDS MORE MECHANISTIC EVIDENCE
- DEMOTED
- KILLED

Do not call H-008 a discovery without experimental validation.

## Scientific guardrails

Never allow:
- correlation → causation
- genomic proximity → causal gene
- plausibility → evidence
- absence of literature → novelty
- one citation → support for claims it did not test
- rapid temporal association → proof of mechanism
- separate known components → proof of a complete causal chain
- arbitrary statistical thresholds → evidence
- p > 0.05 alone → proof of no effect

Classify claims as:
**ESTABLISHED / DIRECTLY SUPPORTED / INDIRECTLY SUPPORTED / PLAUSIBLE / SPECULATIVE / UNRESOLVED**.

For novelty, distinguish **not found** from **not previously proposed**.

## How ChatGPT should manage Gemini

When Gemini returns work:
1. Check whether evidence supports the claim.
2. Find the weakest causal edge.
3. Give Gemini the smallest high-value next task.
4. Prefer falsification over confirmation.
5. Treat correctly rejected hypotheses as successful research.
6. Check canonical state/report consistency.
7. Avoid unnecessary searches and token-heavy prompts.
8. Distinguish resolving a question from choosing the most plausible explanation.
9. If evidence cannot discriminate, keep it **UNRESOLVED**.
10. Only spend additional quota on a candidate when the next search/analysis can materially change its ranking.

## Resume instruction

When this file is supplied in a new ChatGPT conversation, inspect the latest repo commits/state first. Then give the user the **single highest-information next action** rather than restarting the research.
