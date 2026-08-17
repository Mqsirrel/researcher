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

Target: not a plausible narrative, but an unusual connection that survives prior-art and adversarial causal review and produces a clear testable prediction.

## Repo architecture
- `GEMINI.md` — methodology
- `.agents/hooks.json` — lifecycle enforcement
- `.agents/hooks/research_gate.py` — lightweight research/stop gate
- `state/` — Gemini's persistent research state
- `research/SEARCH_POLICY.md` — token-efficient search policy
- `SUPERVISOR_MEMORY.md` — **ChatGPT/supervisor-only; Gemini must not modify**

## Token strategy
User has finite Gemini quota. Optimize for **information gained per token**, not autonomous runtime or broad literature completeness.
Use: `state → targeted search → synonyms → citation traversal → adjacent field → deeper search only if ranking can change`.
Prefer killing/demoting candidates cheaply over accumulating support. Do not generate a new hypothesis while a promising candidate has an unresolved high-information falsification/design question.

## Important previous failures
### H-005 / NPVF
Initially overpromoted. Forensic audit found causal NPVF regulation unproven, proximity insufficient, cortisol evidence overgeneralized, RF9 characterization incorrect, novelty overstated.
Current H-005R: **PLAUSIBLE BUT UNPROVEN**.

### U-002 / pagophagia
Gemini prematurely promoted endothelial/TfR1/eNOS/TRPM8 to Very High and marked resolved. Audit showed rapid symptom resolution constrains timescale but does not identify mechanism.
Current chain remains unproven: `IV iron → transferrin saturation → BMEC TfR1 → endothelial/eNOS → cerebral perfusion → cold-mastication benefit → pagophagia`.

### H-006
Adversarial novelty audit: **UNDER-INVESTIGATED BUT NOT NOVEL**. Correctly rejecting a candidate is a successful research outcome.

## Current hypotheses
### H-003 — Trigeminal / Cerebral Perfusion Hypoxia Compensation
**N2 / ~35% / PLAUSIBLE BUT UNPROVEN**. Rapid pagophagia time course is useful, but endothelial/eNOS/perfusion chain remains unproven.

### H-005R — 7p15.3 / NPVF Proximal Locus
**N1 / ~35% / PLAUSIBLE BUT UNPROVEN**. Causal gene/mechanism unresolved.

### H-007 — Hepatic Portal Vagal Transferrin Sensor
**SURVIVES — NEEDS MORE EVIDENCE / ~30%**.
Proposed chain: `IV iron → rapid TSAT increase → hepatic/periportal sensing → hepatic vagal afferents → NTS/PBN → pica-drive suppression`.
Critical weakness: zero electrophysiological evidence that vagal afferents directly sense transferrin/acute iron changes. Do not promote until missing transduction mechanism has stronger evidence or a defensible intermediate is identified.

### H-008 — AMY1 CNV & Gestational Starch Counter-Regulation / Amylophagy
Latest Gemini commit: **e057a9c — NEEDS PILOT DATA FIRST (~40%)**.

Core proposition: `AMY1 CNV → salivary amylase → pre-absorptive starch handling/glycemic signaling → selective persistent starch craving`, potentially interacting with pregnancy insulin resistance.
Core observation: cited REVAMP 2025 RCT reportedly found IV iron failed to resolve amylophagy while geophagy improved.

The key unproven edge is **AMY1 copy number → compulsive non-food starch craving/amylophagia**. Established AMY1 digestion biology is not evidence for this edge.

The statistical/design audit correctly moved H-008 from "ready for experimental design" to **pilot first** because there is no reliable prior effect-size/variance information in the relevant pregnancy population and there may be GERD/reflux and ancestry/population confounding.

Gemini currently proposes a 90-person feasibility pilot: 30 persistent amylophagy, 30 resolved geophagy, 30 healthy controls; duplex AMY1/RPP30 ddPCR on REVAMP biobank DNA. Treat this as a draft, NOT a validated design.

Important problems still to resolve:
- "resolved geophagy" may be a poor primary control for an AMY1/amylophagia hypothesis; persistent amylophagy should likely be compared primarily with appropriate matched controls without persistent amylophagia, with geophagy as a secondary comparator.
- N=90 has not yet been justified by reliable prior effect-size data; a pilot may be for variance/assay/phenotype estimation rather than formal hypothesis testing.
- Gemini's proposed equivalence interval OR 0.90–1.10 is not automatically defensible; it needs scientific justification or should be replaced by a pilot-estimation framework.
- `p > 0.05` alone must never be treated as falsification.
- "cases have higher AMY1 CNV" is evidence against the specific low-copy-number direction but does not automatically eliminate every possible AMY1 mechanism.
- Do not use arbitrary AMY1 copy thresholds (e.g. ≤4) without evidence.

## Current ranking
1. **H-008** — strongest current candidate; potentially novel and testable, but needs pilot/design revision.
2. **H-007** — interesting/potentially novel, but missing critical sensor/transduction evidence.

Do NOT generate H-009 yet.

## Current highest-value task
Run a **final design audit of H-008 only**, not another broad literature review.

Audit:
1. Whether REVAMP phenotype is suitable and how persistent amylophagia should be defined (binary vs frequency/severity/duration).
2. Whether persistent amylophagia vs appropriate matched non-amylophagia controls is a better primary comparison than resolved geophagy; use geophagy as secondary if appropriate.
3. Inclusion/exclusion criteria and which variables should be matched vs adjusted.
4. Whether N=90 has a defensible purpose; do not assume conventional power without a credible effect size.
5. Best AMY1 CNV measurement method and whether CNV should be continuous or categorical.
6. Primary statistical model and confounders: ancestry/population structure, age, BMI, parity, gestational stage, diet/carbohydrate exposure, socioeconomic factors, iron status/treatment response, GERD/reflux, and other relevant factors.
7. Which causal edges the human pilot can actually test versus merely associate.
8. At least two competing explanations and discriminating measurements.
9. A defensible decision rule. Do not use p>0.05 alone; do not invent an equivalence interval.
10. What the pilot can establish, what it cannot, and whether a larger confirmatory study would be justified.
11. Choose the highest information per sample/cost/token.

Final status must be exactly one:
- READY FOR PILOT
- NEEDS DESIGN REVISION
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
1. Check evidence against claims.
2. Find weakest causal edge.
3. Give Gemini the smallest high-value next task.
4. Prefer falsification over confirmation.
5. Treat correctly rejected hypotheses as successful research.
6. Check canonical state/report consistency.
7. Avoid unnecessary searches/token-heavy prompts.
8. Distinguish resolving a question from choosing the most plausible explanation.
9. If evidence cannot discriminate, keep **UNRESOLVED**.
10. Only spend quota when the next action can materially change ranking.

## Resume instruction
When this file is supplied in a new ChatGPT conversation, inspect the latest repo commits/state first. Then give the user the **single highest-information next action** rather than restarting the research.
