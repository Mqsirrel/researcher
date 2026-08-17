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
Latest state after final feasibility audit: **UNKNOWN — REQUIRES BIOBANK ACCESS**.

Core proposition: `AMY1 CNV → salivary amylase → pre-absorptive starch handling/glycemic signaling → selective persistent starch craving`, potentially interacting with pregnancy insulin resistance.
Core observation: cited REVAMP 2025 RCT reportedly found IV iron failed to resolve amylophagy while geophagy improved.

The key unproven edge is **AMY1 copy number → compulsive non-food starch craving/amylophagia**. Established AMY1 digestion biology is not evidence for this edge.

Verified/claimed REVAMP facts from latest Gemini audit:
- cohort reported as N=862 anemic pregnant women in Malawi
- randomized 1:1 IV ferric carboxymaltose vs standard oral iron
- amylophagy measured by self-reported craving/consumption of raw starch, raw rice, or unripe mango over the prior 2 weeks at baseline and 4 weeks
- banked maternal whole blood/buffy coat biorepository reportedly exists
- Hb and serum ferritin measured baseline and 4 weeks
- age, gestational age, parity, clinic site documented
- granular GERD/heartburn and genome-wide ancestry data remain UNKNOWN/unconfirmed in public materials

Important correction:
Gemini previously inferred that >30 eligible cases could be obtained from aggregate 44.4% prevalence. This was rejected. Aggregate prevalence alone does NOT establish ≥30 eligible persistent-amylophagia cases after all filters and usable DNA.
Gemini also previously proposed ancestry PCs 1–5 despite ancestry genotype data being unverified. This was rejected. Do not assume ddPCR AMY1/RPP30 can generate ancestry PCs.

Current proposed pilot concept, still unvalidated:
- 30 persistent amylophagia cases + 60 non-amylophagia controls
- controls from the same IV-FCM arm
- matching mainly on recruitment clinic site and gestational age ±2 weeks
- proposed post-FCM ferritin >100 µg/L and Hb ≥110 g/L gate, subject to further methodological justification
- triplicate duplex ddPCR AMY1/RPP30
- continuous AMY1 copy number as primary predictor
- conditional logistic regression
- pilot framed as feasibility, assay validation, AMY1 distribution/variance, and preliminary effect-size estimation—not causal proof or formal falsification

## Current ranking
1. **H-008** — strongest current candidate; potentially novel and testable, but feasibility is currently UNKNOWN pending legitimate biobank feasibility/access.
2. **H-007** — interesting/potentially novel, but missing critical sensor/transduction evidence.

Do NOT generate H-009 yet.

## Current highest-value task
Determine the **legal and ethical access pathway** for H-008 feasibility information. Do NOT attempt to obtain restricted/private participant data or biospecimens directly.

Gemini's next task:
1. Identify the official REVAMP study/publication/protocol/repository and investigators/institution.
2. Identify the official mechanism for individual-level data access and for biospecimen/DNA access.
3. Determine requirements such as institutional affiliation, IRB/REC approval, data-use agreement, MTA, research proposal, PI/repository approval, etc.
4. First seek the minimum feasible query: aggregate counts of eligible persistent-amylophagia cases, controls, relevant missingness, and DNA/biospecimen availability.
5. Do NOT request names, addresses, direct identifiers, or unnecessary clinical data.
6. Do NOT claim IRB approval, institutional affiliation, authorization, or existing access unless actually provided.
7. Do NOT send protected health information through ordinary email or bypass authentication/access controls.
8. If aggregate feasibility can answer whether ≥30 cases + ≥60 controls exist, stop there before requesting participant-level data or biospecimens.
9. Draft a short professional feasibility request using only the official access/contact route.

The target feasibility question is:
**Can we verify that ≥30 eligible persistent-amylophagia cases and ≥60 eligible non-amylophagia controls with usable DNA exist before proposing an AMY1 experiment?**

## Legal/ethical guardrails
Only use legitimate, documented access routes. Public aggregate information first. Restricted individual-level data and biospecimens only through the study's formal governance process. No bypassing access controls, scraping private systems, fabricated authorization, or unnecessary PHI requests.

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
