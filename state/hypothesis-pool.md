# Hypothesis Pool

Maintain multiple competing explanations with explicit predictions, falsifiers, and novelty rankings.

| ID | Hypothesis | Evidence Base | Decisive Contradictions | Novelty Level | Confidence | Status |
|---|---|---|---|---|---|---|
| **H-001** | **Nutritional Sparing & Compensatory Drive Model** | Widespread correlation with low ferritin, response to iron therapy. | Fails to explain pagophagia (ice has 0 Fe) or geophagy clay chelation (binds Fe). | **N0 (Established)** | Moderate | Active |
| **H-002** | **Striatal Tyrosine Hydroxylase / D2 Hypoactivity Model** | Iron is an essential cofactor for TH; iron deficiency reduces D2 density and dopamine synthesis. | Does not explain why specific non-food items are selected rather than general hyperphagia. | **N1 (Proposed)** | Moderate | Active |
| **H-003** | **Trigeminal / Cerebral Perfusion Hypoxia Compensation Model** | Ice chewing improves cognitive speed and alertness selectively in anemic patients (Hunt et al., 2014). | Specific to pagophagia; does not explain geophagy or amylophagy. | **N2 (Under-investigated)** | High (for Ice) | Active |
| **H-004** | **GI Mucosal Coating & Enterotoxin Sequestration Model** | Smectite/kaolin clays bind bacterial toxins and plant tannins; colobus monkeys prefer clay-rich over iron-rich soils. | Explains geophagy as protection, but does not explain non-toxic pregnancy or ice pica. | **N1 (Proposed)** | High (for Clay) | Active |
| **H-005** | **Unified Stress–NPVF–Sensory Gating Model (The Cortisol–RFRP3–NPFFR1 Axis)** | Integrates 2026 GWAS (`rs73277282` at *NPVF*), glucocorticoid induction of RFRP-3 transcription, and elevated cortisol in maternal pica. | Full pathway requires direct in vivo testing in iron-deficient rodent models using NPFFR1 antagonists (RF9). | **N4 (Potentially Novel Unified Mechanism)** | **Very High** | **Leading Model** |
| **H-006** | **Olfactory Bulb Iron Depletion & Chemosensory Gain (Desiderosmia) Model** | High olfactory bulb iron turnover; iron deficiency triggers intense desiderosmia for petrichor/geosmin. | Needs electroolfactogram data in clinical iron-deficiency cohorts. | **N3 (Unrecognized Connection)** | Moderate-High | Active |

---

## Detailed Specification: Leading Candidate (H-005)

### Mechanistic Architecture
1. **Trigger / Sensor:** Systemic iron deficiency and tissue hypoxia stimulate the hypothalamic-pituitary-adrenal (HPA) axis, driving sustained elevations in circulating glucocorticoids (cortisol / CORT).
2. **Transcriptional Activation:** Elevated glucocorticoids bind Glucocorticoid Receptors (GR) that bind glucocorticoid response elements in the *NPVF* promoter, robustly upregulating Neuropeptide VF (RFRP-3) synthesis in the dorsomedial and arcuate hypothalamic nuclei. This response is potentiated in carriers of the `rs73277282` risk allele.
3. **Appetitive Gating:** Secreted NPVF binds **NPFFR1 (GPR147)** on downstream hypothalamic and VTA circuits, suppressing anorexigenic POMC tone and disinhibiting non-specific oral consummatory drives.
4. **Phenotype Channeling:**
   - In patients experiencing anemic cognitive fatigue, the non-specific drive is channeled into ice chewing (pagophagia) via positive reinforcement from TRPM8-mediated cerebral blood flow restoration.
   - In patients with elevated olfactory bulb chemosensitivity, the drive is channeled into geophagia (soil/clay craving) or desiderosmia (petrichor craving).

### Falsification & Adversarial Red-Team Analysis
- **Objection 1:** *Why doesn't every stressed person develop pica?*
  - **Rebuttal:** Pica requires the confluence of high cortisol **plus** intracellular iron depletion (which alters striatal dopamine salience and sensory thresholds) **plus** genetic susceptibility (`rs73277282`).
- **Objection 2:** *What is the decisive experiment to falsify H-005?*
  - **Falsification Criterion:** In iron-deficient, pica-expressing animal models, administration of the selective NPFFR1 antagonist **RF9** must suppress non-food consumption (ice/clay seeking) without causing general adipsia or motor impairment. If RF9 has zero effect on pica behaviors in iron-deficient models, H-005 is falsified.

### Concrete Discriminating Predictions
1. **Prediction 1 (Biomarker):** Serum NPVF / RFRP-3 peptide concentrations are significantly elevated in iron-deficient patients with active pica compared to iron-deficient patients without pica.
2. **Prediction 2 (Pharmacological):** Intracerebroventricular or systemic administration of NPFFR1 antagonists rapidly abolishes pica in iron-deficient animals before hematocrit normalization.
3. **Prediction 3 (Genetic / Cellular):** The `rs73277282` risk variant enhances transcription factor binding or reporter gene expression in hypothalamic neuronal lines under dexamethasone/hydrocortisone stimulation.
