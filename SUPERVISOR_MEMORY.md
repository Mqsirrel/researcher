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

### H-008 — AMY1 CNV & Gestational Starch Counter-Regulation / Amylophagia
Latest state: **POTENTIALLY NOVEL + TESTABLE candidate, but NOT validated and feasibility remains UNKNOWN**.

Latest Gemini commit `fddfab7` created a 223-line H-008 research brief / working pre-print. It decomposes the hypothesis into:
`AMY1 CNV → salivary amylase → oral starch processing → metabolic/insulin dynamics → craving/reward → persistent amylophagia`.

Important: the brief is a DRAFT, not a discovery or validated causal model. The strongest/weakest link is the final causal transition from metabolic state to selective compulsive raw-starch/amylophagia behavior. This is currently **SPECULATIVE**.

The brief proposes that low AMY1 CNV may interact with pregnancy-induced insulin resistance, but this interaction and the selective craving mechanism remain unproven.

REVAMP observation motivating H-008:
- reported N=862 anemic pregnant women in Malawi
- randomized IV ferric carboxymaltose vs standard oral iron
- geophagy improved with IV iron while non-geophagy/amylophagy did not show a clear therapeutic effect
- phenotype details must be verified against the original publication before using exact substance labels in any external request

Critical corrections retained:
- Aggregate 44.4% prevalence does NOT establish ≥30 eligible persistent cases after all filters and usable DNA.
- Do not assume ancestry PCs 1–5 exist; genome-wide ancestry genotype data are unverified.
- Do not assume ddPCR AMY1/RPP30 can generate ancestry PCs.
- Proposed ferritin/Hb/TSAT gates and N=30+60 design are **proposed**, not verified feasibility facts.
- Do not call amylophagia "completely unresponsive" unless the original trial's confidence interval supports that wording.

### Current proposed pilot concept — still unvalidated
- 30 persistent amylophagia cases + 60 non-amylophagia controls
- controls from the same IV-FCM arm
- clinic site / gestational-age matching
- proposed post-FCM iron-repletion criteria, subject to methodological justification
- triplicate duplex ddPCR AMY1/RPP30
- continuous AMY1 copy number as primary predictor
- pilot framed as feasibility, assay validation, distribution/variance, and preliminary effect-size estimation—not causal proof

## Current ranking
1. **H-008** — strongest current candidate; potentially novel and testable, but its key causal edge and practical feasibility remain unresolved.
2. **H-007** — interesting/potentially novel, but missing critical sensor/transduction evidence.

Do NOT generate H-009 yet.

## Legal/ethical access status
Gemini previously produced a legal-access pathway for REVAMP, but the user is not currently positioned as an institutional biomedical researcher and does not want to overstate credentials. Therefore **do not initiate external contact yet**.

If access ever becomes appropriate, first use only official/public routes and ask for aggregate feasibility information, not PHI or biospecimens. Never claim IRB approval, institutional affiliation, authorization, or existing access unless actually provided.

## Current highest-value task
**Final adversarial scientific audit of H-008 before any external contact.**

Gemini's next task:
1. Search specifically for prior work connecting AMY1 CNV/salivary amylase with amylophagia, pica, starch craving, pregnancy, insulin resistance, glycemic variability, and reward/craving.
2. Distinguish exact prior hypothesis vs closely related hypothesis vs component biology vs genuinely new connection. Absence of the exact phrase is NOT novelty.
3. Audit every causal edge and identify the strongest supporting and limiting/contradictory evidence.
4. Attack the central claim that low AMY1 could specifically favor raw/non-food starch consumption rather than ordinary carbohydrate craving.
5. Verify the REVAMP phenotype definitions and treatment-effect interpretation directly from the original paper before preserving exact wording.
6. Audit every pilot number and eligibility gate as observed vs derived vs assumed vs unknown.
7. Find the single most discriminating and information-efficient test against GERD/acid-buffering, microbiome, cultural/behavioral, and generalized carbohydrate-craving models.
8. Give one final classification: `POTENTIALLY NOVEL + STRONGLY TESTABLE`, `POTENTIALLY NOVEL BUT WEAKLY GROUNDED`, `UNDER-INVESTIGATED BUT NOT NOVEL`, `PLAUSIBLE BUT ALREADY KNOWN`, or `FALSIFIED / ABANDON`.
9. Do not contact researchers, request data/biospecimens, generate H-009, or rewrite the research brief before the audit.

The key question is:
**Is H-008 actually a novel biological hypothesis worth pursuing, or did Gemini merely combine known AMY1 biology with an unexplained pica phenotype?**

## Legal/ethical guardrails
Only use legitimate, documented access routes. Public aggregate information first. Restricted individual-level data and biospecimens only through formal governance. No bypassing access controls, scraping private systems, fabricated authorization, or unnecessary PHI requests.

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
