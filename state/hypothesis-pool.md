# Hypothesis Pool

Maintain multiple competing explanations with explicit predictions, falsifiers, and calibrated novelty/confidence rankings.

| ID | Hypothesis | Evidence Base | Decisive Contradictions / Major Vulnerabilities | Novelty Level | Confidence | Status |
|---|---|---|---|---|---|---|
| **H-001** | **Nutritional Sparing & Compensatory Drive Model** | Widespread correlation with low ferritin, response to iron therapy. | Fails to explain pagophagia (ice has 0 Fe) or geophagy clay chelation (binds Fe). | **N0 (Established)** | Moderate | Active (Baseline) |
| **H-002** | **Striatal Tyrosine Hydroxylase / D2 Hypoactivity Model** | Iron is an essential cofactor for TH; iron deficiency reduces D2 density and dopamine synthesis in striatum; strong clinical overlap with RLS. | Does not explain substance-specific sensory selection (ice vs. clay) without peripheral gating. | **N1 (Proposed)** | **High** | **Leading Model (Bio-behavioral)** |
| **H-003** | **Trigeminal / Cerebral Perfusion Hypoxia Compensation Model** | Ice chewing improves cognitive speed and alertness selectively in anemic patients (Hunt et al., 2014); TRPM8/sympathetic activation increases MCA blood flow velocity. | Highly specific to pagophagia; does not explain geophagy or amylophagy. | **N2 (Under-investigated)** | **High (for Pagophagia)** | **Leading Model (Subtype Specific)** |
| **H-004** | **GI Mucosal Coating & Enterotoxin Sequestration Model** | Smectite/kaolin clays bind bacterial toxins and plant tannins; colobus monkeys prefer clay-rich over iron-rich soils. | Explains geophagy as adaptive barrier protection, but fails for non-toxic pregnancy or ice pica. | **N1 (Proposed)** | **High (for Geophagy)** | Active (Subtype Specific) |
| **H-005** | **Hypothalamic NPVF Genetic Vulnerability / Appetite Multiplier Model (Refactored)** | REDS-III GWAS (`rs73277282` at 7p15.3 near *NPVF*, replicated in All of Us); NPVF is an orexigenic peptide acting via NPFFR1. | `rs73277282` is in a non-coding gene desert (functional eQTL unproven); NPVF stimulates caloric chow, not non-food pica; RF9 is an unselective KISS1R agonist; cortisol link is weak/confounded. | **N2 (Under-investigated Genetic Candidate)** | **Low-Moderate (25-30%)** | **Demoted / Refactored** |
| **H-006** | **Olfactory Bulb Iron Depletion & Chemosensory Gain (Desiderosmia) Model** | Olfactory bulb has highest brain iron turnover; iron deficiency triggers intense desiderosmia for petrichor/geosmin. | Needs electroolfactogram data in clinical iron-deficiency cohorts; doesn't explain ice. | **N3 (Unrecognized Connection)** | Moderate | Active |

---

## Adversarial Audit & Refactoring: H-005

### 1. What Failed the Audit
- **Universal Cortisol / HPA Drive:** Conflated a small, exploratory pregnant cohort ($N=34$, PMID 38050975) with general pica etiology. Blood donors with pica lack evidence of systemic hypercortisolemia.
- **RF9 as a Selective Antagonist:** RF9 is a known potent agonist at **KISS1R (GPR54)** and lacks in vivo selectivity for NPFFR1. It cannot be used as a definitive test of NPFFR1 blockade.
- **Direct Causal Attribution of `rs73277282`:** The SNP lies in an intergenic region on 7p15.3 flanked by super-enhancers that could regulate other neighboring or distant genes (*MIR148A*, *NFE2L3*, *HOXA*).
- **Novelty Rating Inflation:** Labeling H-005 as N4 / Very High Confidence was an error. Linking a known GWAS candidate (*NPVF*) to its existing literature is N2 at best.

### 2. The Surviving Refactored Model (H-005R)
`rs73277282` acts as a regulatory modifier in the 7p15.3 locus that enhances hypothalamic *NPVF* orexigenic responsiveness under metabolic/anemic stress. Elevated NPVF signaling lowers the general threshold for consummatory seeking, which is then shaped into pica by striatal dopamine depletion (H-002) and peripheral sensory feedback (H-003, H-004, H-006).

---

## Discriminating Predictions (H-005R vs. H-002/H-003)

1. **Prediction 1 (Genotype Stratification in Severe IDA):**
   - *H-005R:* In severe iron deficiency (ferritin $<10$ ng/mL), pica will be significantly enriched in `rs73277282` risk allele carriers, whereas non-carriers will exhibit anemia and fatigue without non-food cravings.
   - *H-002/H-003:* Pica penetrance depends strictly on the degree of striatal iron depletion or cerebral hypoperfusion, regardless of `rs73277282`.
2. **Prediction 2 (Hypothalamic *Npffr1* Knockdown in Rodents):**
   - *H-005R:* Targeted viral knockdown of *Npffr1* in the DMH/arcuate nucleus will attenuate non-food ingestion in iron-deficient rodents without restoring systemic iron or hematocrit.
   - *H-002:* Only dopamine D2/D3 receptor agonists (e.g. pramipexole) will suppress pica; *Npffr1* knockdown will have no effect.
3. **Prediction 3 (Caloric Food vs. Non-Food Satiation):**
   - *H-005R:* Ingestion of high-calorie food will activate standard satiety circuits and suppress NPVF-driven pica urges.
   - *H-003:* Caloric food will fail to relieve pagophagia, which requires oral cold (TRPM8) to restore cerebral perfusion velocity.
