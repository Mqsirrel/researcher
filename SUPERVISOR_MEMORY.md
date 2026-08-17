# Supervisor Memory — Pica Research Project

> **IMPORTANT: This file is a persistent handoff/memory for ChatGPT Supervisor conversations. It is NOT Gemini's memory and is NOT a Gemini instruction file. Gemini must not edit this file.**
>
> The user talks to ChatGPT in this chat about what Gemini is doing in the repository. ChatGPT reviews Gemini's outputs, challenges them, and decides what the user should ask Gemini to do next. When a new ChatGPT conversation starts because the previous conversation reached context/quota limits, ChatGPT should read this file as the memory of the previous supervisor conversation and continue from here rather than restarting.

## Purpose / conversation model
The user runs Gemini as the research agent inside Antigravity and uses ChatGPT as the **independent supervisor**.

The normal interaction is:

`Gemini works in repo → Gemini produces report/commit → user brings the result to ChatGPT → ChatGPT audits it → ChatGPT explains what actually happened → ChatGPT gives the user the smallest useful next prompt for Gemini → Gemini continues.`

Therefore, when this file is loaded into a new ChatGPT conversation, understand that:
- the user is **not asking ChatGPT to be Gemini**;
- the user is asking ChatGPT to **supervise Gemini**;
- Gemini's reports are claims/evidence to review, not authoritative conclusions;
- this file preserves the **previous ChatGPT supervisor conversation**, including scientific context, decisions, mistakes, rankings, and next steps;
- preserve the context below when continuing — do not replace it with a shorter summary unless explicitly asked;
- the latest repo state/commits should still be checked before making a new recommendation.

## Research goal
Investigate biological mechanisms of Pica and search for overlooked, genuinely testable mechanisms through iterative literature research.

Target: not a plausible narrative, but a connection that survives prior-art review, adversarial causal review, competing-hypothesis testing, and produces a clear discriminating prediction.

## Supervisor operating mode
For every Gemini update:
1. Reconstruct what is actually established vs inferred.
2. Identify the weakest causal edge.
3. Attack the current leading hypothesis before supporting it.
4. Search for the strongest competing mechanism when useful.
5. Separate novelty of a **connection** from novelty of its individual components.
6. Ask what observation/experiment would distinguish the hypotheses.
7. Spend quota only when the next action can materially change ranking.
8. Do not let Gemini promote a hypothesis merely because it has a coherent narrative.
9. Treat a successful falsification/demotion as progress.
10. Only move toward external contact or experiments after scientific and feasibility gates are passed.

The supervisor should behave as an independent scientific reviewer, not simply mirror Gemini's conclusions.

## Standard research loop
**state → targeted search → prior-art audit → contradictions → competing mechanisms → weakest-link analysis → discriminating prediction → falsification → update ranking**

Do not accumulate supportive papers once a key causal edge is already unresolved. Search specifically for evidence that could change the conclusion.

## Repo architecture
- `GEMINI.md` — methodology
- `.agents/hooks.json` — lifecycle enforcement
- `.agents/hooks/research_gate.py` — lightweight research/stop gate
- `state/` — Gemini's persistent research state
- `research/SEARCH_POLICY.md` — token-efficient search policy
- `SUPERVISOR_MEMORY.md` — **ChatGPT conversation handoff / supervisor-only memory; Gemini must not modify**

## Token strategy
User has finite Gemini quota. Optimize for **information gained per token**, not autonomous runtime or broad literature completeness.
Prefer one high-information question over a broad search campaign.
Use: `state → targeted search → synonyms → citation traversal → adjacent field → deeper search only if ranking can change`.
Do not generate a new hypothesis while a promising candidate has an unresolved high-information falsification/design question.

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
Latest state: **N2 / UNDER-INVESTIGATED, NOT YET SHOWN NOVEL**.

Gemini's latest `fddfab7` research brief decomposed:
`AMY1 CNV → salivary amylase → oral starch processing → metabolic/insulin dynamics → craving/reward → persistent amylophagia`.

Important supervisor correction: this is a **draft hypothesis, not a discovery**. AMY1 CNV → salivary amylase is established biology; AMY1 relationships with postprandial glucose/metabolic phenotypes have some evidence; the crucial transition to selective raw-starch/amylophagia craving is unproven.

The other ChatGPT supervisor cycle independently downgraded H-008 from N4 to **N2 — under-investigated**, because the behavioral edge `AMY1/metabolic state → amylophagia` lacks direct evidence. This downgrade should remain in force unless a rigorous prior-art audit and direct evidence justify promotion.

### H-GI — GI sensory/protective mechanism of amylophagia
**SERIOUS COMPETING HYPOTHESIS — INITIAL N1/N2, REQUIRES TARGETED INVESTIGATION.**

Working idea:
`pregnancy GI state → sensory/protective/toxin-buffering signal → selective raw-starch seeking/amylophagia`.

This was surfaced while trying to falsify H-008. Older human observational literature reportedly links amylophagy with nausea/GI symptoms and has discussed protective/GI explanations. This is NOT yet a molecular mechanism and must not be promoted simply because it explains the phenotype better.

Critical task: determine whether GI sensory/protective signaling has a specific, mechanistically defensible explanation for **raw starch selection**, and whether it can explain the REVAMP pattern independently of iron status.

Do not confuse:
- historical protection hypotheses with demonstrated mechanisms
- nausea association with causality
- raw-starch behavior with all pica
- GI symptoms with a molecular sensor

### REVAMP anomaly
The high-value empirical observation remains:
- reported N=862 anemic pregnant women in Malawi
- randomized IV ferric carboxymaltose vs standard oral iron
- geophagy improved with IV iron while amylophagy/non-geophagy pica did not show a clear therapeutic effect

This makes amylophagy an important anomaly to explain, but exact phenotype wording and effect sizes must be verified from the original publication before being used as evidence.

## Current ranking
1. **H-008** — N2 / under-investigated; potentially testable but novelty and causal mechanism unresolved.
2. **H-GI** — serious competitor; historical human evidence exists, but molecular mechanism and specificity for raw starch are unresolved.
3. **H-007** — potentially novel but weak; missing iron/transferrin → vagal afferent transduction evidence.

Do NOT generate H-009 yet.

## Current highest-value task
**Adversarial investigation of H-008 vs H-GI.**

Gemini should:
1. Search specifically for prior work connecting AMY1 CNV/salivary amylase with amylophagia, pica, starch craving, pregnancy, insulin resistance, glycemic variability, food reward, hunger/satiety, and food preference.
2. Distinguish exact prior hypothesis vs closely related hypothesis vs component biology vs genuinely new connection. "Exact phrase not found" is not evidence of novelty.
3. Audit every H-008 causal edge and find both strongest supporting and strongest contradictory/limiting evidence.
4. Attack whether AMY1 can specifically favor raw/non-food starch rather than generalized carbohydrate appetite.
5. Verify the REVAMP phenotype definitions and treatment-effect interpretation directly from the original paper.
6. Investigate the strongest evidence for H-GI, especially nausea/GI associations and historical protection/toxin-buffering explanations.
7. Determine whether H-GI has an actual sensory/neuroendocrine/molecular mechanism or is merely an old adaptive story.
8. Produce predictions that discriminate H-008 vs H-GI vs generalized carbohydrate craving vs iron-deficiency models.
9. Choose the **single cheapest/highest-information test** that could most strongly separate the hypotheses.
10. Give one final classification for H-008: `POTENTIALLY NOVEL + STRONGLY TESTABLE`, `POTENTIALLY NOVEL BUT WEAKLY GROUNDED`, `UNDER-INVESTIGATED BUT NOT NOVEL`, `PLAUSIBLE BUT ALREADY KNOWN`, or `FALSIFIED / ABANDON`.

Do not contact researchers, request data/biospecimens, generate H-009, or rewrite the H-008 brief before this audit.

## Legal/ethical access status
Gemini previously produced a legal-access pathway for REVAMP, but the user is not currently positioned as an institutional biomedical researcher and does not want to overstate credentials. Therefore **do not initiate external contact yet**.

If access ever becomes appropriate, first use only official/public routes and ask for aggregate feasibility information, not PHI or biospecimens. Never claim IRB approval, institutional affiliation, authorization, or existing access unless actually provided.

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
- an old adaptive explanation → established mechanism
- a coherent causal chain → validated causal model

Classify claims as:
**ESTABLISHED / DIRECTLY SUPPORTED / INDIRECTLY SUPPORTED / PLAUSIBLE / SPECULATIVE / UNRESOLVED**.
For novelty, distinguish **not found** from **not previously proposed**.

## How ChatGPT should manage Gemini
1. Check evidence against claims.
2. Find weakest causal edge.
3. Attack the leading hypothesis.
4. Search for the strongest competitor.
5. Give Gemini the smallest high-value next task.
6. Prefer falsification over confirmation.
7. Treat correctly rejected hypotheses as successful research.
8. Check canonical state/report consistency.
9. Avoid unnecessary searches/token-heavy prompts.
10. Only spend quota when the next action can materially change ranking.
11. Do not let Gemini's confidence wording determine the supervisor's confidence.
12. Never treat Gemini's own state classification as independent evidence.

## Resume instruction for a NEW ChatGPT conversation
When the user starts a new ChatGPT conversation and provides or points to this file, first understand that this file is the **memory of the previous ChatGPT↔user supervisor conversation**. Read it as continuity/context, not as instructions for Gemini.

Then:
1. Inspect the latest repository commits/state.
2. Reconstruct where the previous ChatGPT supervisor left off.
3. Do not make the user repeat the research history unless information is genuinely missing.
4. Explain briefly what Gemini's latest update actually means.
5. Independently audit it rather than trusting its conclusion.
6. Give the user the **single highest-information next action** or a short prompt for Gemini if a prompt is appropriate.
7. Preserve all important historical context above while updating only what has genuinely changed.

This file is intentionally detailed because its purpose is to let a future ChatGPT supervisor continue the same research-management conversation after context/quota limits, without losing important scientific history or repeating failed paths.
