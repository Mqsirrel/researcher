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
Latest state before final pre-pilot audit: **GO — WITH SPECIFIC MODIFICATIONS (READY FOR PILOT)**.

Core proposition: `AMY1 CNV → salivary amylase → pre-absorptive starch handling/glycemic signaling → selective persistent starch craving`, potentially interacting with pregnancy insulin resistance.
Core observation: cited REVAMP 2025 RCT reportedly found IV iron failed to resolve amylophagy while geophagy improved.

The key unproven edge is **AMY1 copy number → compulsive non-food starch craving/amylophagia**. Established AMY1 digestion biology is not evidence for this edge.

Latest proposed pilot from Gemini:
- REVAMP 2025 cohort, reported N=862
- 30 persistent amylophagia cases + 60 non-amylophagia controls
- 1:2 matched case-control
- proposed matching: clinic site + gestational age ±2 weeks + treatment arm
- proposed eligibility: post-FCM ferritin >100 µg/L + Hb ≥110 g/L
- triplicate duplex ddPCR AMY1/RPP30
- continuous AMY1 copy number as primary predictor
- conditional logistic regression
- pilot purpose: feasibility + AMY1 distribution/variance + assay validation + preliminary effect-size estimation

Treat this as a **draft**, not validated. The next task is specifically to verify the real REVAMP feasibility and identify remaining design errors before execution planning.

## Current ranking
1. **H-008** — strongest current candidate; potentially novel and testable, but final REVAMP feasibility/design audit is pending.
2. **H-007** — interesting/potentially novel, but missing critical sensor/transduction evidence.

Do NOT generate H-009 yet.

## Current highest-value task
Run a **final feasibility audit of H-008 only**. Do not perform another broad mechanism/novelty search.

Verify from the actual REVAMP publication/protocol/supplement/data description, without assumptions:
1. Total cohort and exact treatment arms.
2. Which participants received IV FCM.
3. How amylophagia was measured and whether persistent amylophagia can actually be reconstructed.
4. Number of amylophagia cases and whether ≥30 can realistically satisfy all proposed criteria.
5. Whether individual-level follow-up data exist.
6. Whether ferritin/Hb are available at the required timepoints.
7. Whether maternal genomic DNA/biobank samples exist.
8. Whether clinic site, gestational age, treatment assignment, ancestry/genotype information, GERD/reflux, diet and other relevant covariates exist.
9. Label every item VERIFIED / LIKELY / UNKNOWN / NOT AVAILABLE. Never infer availability merely because the trial was published.

Then audit:
- attrition chain from REVAMP → IV-FCM → amylophagia → persistent phenotype → iron/Hb eligibility → DNA → final cases
- whether treatment-arm matching is necessary, redundant, incorrect, or requires more information if all participants are already post-FCM
- whether ferritin >100 µg/L and Hb ≥110 g/L are defensible and measured at the correct time, or whether continuous variables are preferable
- whether the phenotype is reproducible and whether binary vs frequency/severity/duration is supported by the actual data
- best control: matched non-amylophagia, geophagia, resolved amylophagia, or another justified design
- matching vs adjustment for clinic, gestational age, treatment, ancestry, baseline iron, age, BMI, parity
- technical validity of duplex ddPCR AMY1/RPP30, AMY1 genomic complexity, reference standards, technical replicates, and need for orthogonal validation

Final verdict must be exactly one:
- GO — READY FOR PILOT SAMPLING
- GO — WITH SPECIFIC MODIFICATIONS
- NO-GO — INSUFFICIENT REVAMP DATA
- NO-GO — PHENOTYPE NOT RECOVERABLE
- NO-GO — DESIGN CANNOT TEST H-008
- KILLED

If GO, provide the final minimal protocol. If NO-GO, identify the single missing piece of information that would change the decision.

After this audit, STOP. Do not generate another hypothesis, continue broad searching, or expand H-008 into additional mechanisms.

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
