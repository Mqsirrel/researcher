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
Do not generate a new hypothesis while a promising candidate still has an unresolved high-information falsification/novelty question.

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
Latest adversarial audit: **POTENTIALLY NOVEL — READY FOR EXPERIMENTAL DESIGN**, ~45%.

Core observation:
IV iron reportedly failed to resolve amylophagy in the cited REVAMP 2025 RCT while geophagy improved. Gemini proposes:
`AMY1 CNV → salivary amylase → pre-absorptive starch handling/glycemic signaling → selective persistent starch craving`, potentially interacting with pregnancy insulin resistance.

Important caveat: established AMY1 biology is NOT evidence that AMY1 causes amylophagy. The unproven edge is specifically:
**AMY1 copy number → compulsive non-food starch craving/amylophagy.**

Proposed immediate test: genotype `AMY1` CNV in relevant clinical cohort/banked DNA and compare persistent amylophagy against geophagy and controls.

Do NOT accept an arbitrary threshold such as OR >4 unless justified prospectively. Effect sizes and statistical design must be evidence-based.

## Current ranking

1. **H-008** — strongest current candidate; potentially novel and experimentally testable.
2. **H-007** — interesting and potentially novel, but critical sensor/transduction evidence is missing.

Do NOT generate H-009 yet.

## Highest-value next step

Perform a **deep prior-art + causal/statistical design audit of H-008 only** before spending tokens on new hypotheses.

Questions:
1. Has `AMY1 CNV × starch craving × pregnancy × amylophagia` already been studied under different terminology?
2. Has any human/animal study linked AMY1 genotype or salivary amylase variation to non-food starch craving specifically?
3. Is the proposed AMY1 → craving pathway biologically defensible, or is it merely an inference from carbohydrate digestion?
4. What are the strongest alternative explanations for persistent amylophagy after iron repletion?
5. What confounders could produce an apparent AMY1/amylophagy association?
6. What sample size/effect size would make the proposed cohort test informative?
7. What result would decisively falsify H-008?
8. Does the hypothesis survive a terminology-expanded novelty search and citation chaining?

The desired endpoint is one of:
- **KILLED**
- **DEMOTED**
- **SURVIVES — NEEDS MORE EVIDENCE**
- **POTENTIALLY NOVEL — READY FOR EXPERIMENTAL DESIGN**

Do not call it a discovery without experimental validation.

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
