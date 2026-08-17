# Hypothesis Pool

Maintain multiple competing explanations with explicit predictions, falsifiers, and calibrated novelty/confidence rankings.

| ID | Hypothesis | Evidence Base | Decisive Contradictions / Major Vulnerabilities | Novelty Level | Confidence | Status / Final Verdict |
|---|---|---|---|---|---|---|
| **H-001** | **Nutritional Sparing & Compensatory Drive Model** | Widespread correlation with low ferritin, response to iron therapy. | Fails to explain pagophagia (ice has 0 Fe) or geophagy clay chelation (binds Fe). | **N0 (Established)** | Moderate | Active (Baseline) |
| **H-002** | **Striatal Tyrosine Hydroxylase / D2 Hypoactivity Model** | Iron is an essential cofactor for TH; iron deficiency reduces D2 density and dopamine synthesis in striatum; strong clinical overlap with RLS. | Does not explain substance-specific sensory selection (ice vs. clay) without peripheral gating. | **N1 (Proposed)** | **High** | **Leading Model (Bio-behavioral)** |
| **H-003** | **Trigeminal / Cerebral Perfusion Hypoxia Compensation Model** | Ice chewing improves cognitive speed and alertness selectively in anemic patients (Hunt et al., 2014); TRPM8/sympathetic activation increases MCA blood flow velocity. | Highly specific to pagophagia; does not explain geophagy or amylophagy. | **N2 (Under-investigated)** | **High (for Pagophagia)** | **Leading Model (Subtype Specific)** |
| **H-004** | **GI Mucosal Coating & Enterotoxin Sequestration Model** | Smectite/kaolin clays bind bacterial toxins and plant tannins; colobus monkeys prefer clay-rich over iron-rich soils. | Explains geophagy as adaptive barrier protection, but fails for non-toxic pregnancy or ice pica. | **N1 (Proposed)** | **High (for Geophagy)** | Active (Subtype Specific) |
| **H-005R** | **7p15.3 / NPVF Proximal Locus Genetic Vulnerability Model** | Direct statistical GWAS association of `rs73277282` in blood donors (REDS-III, AoU replication); fine-mapping isolates a 17.5 kb LD block containing active enhancer `ENSR7_9D2JJ` (disrupted by proxy `rs111374644`) located 15.7 kb from *NPVF* TSS. | Bulk GTEx lacks eQTL due to cell-type rarity; direct human hypothalamic CRISPRi/snRNA-seq proof is pending. | **N1 (Published GWAS Candidate)** | **Moderate (~40%)** | **PLAUSIBLE BUT UNPROVEN** |
| **H-006** | **Olfactory Bulb Iron Depletion & Chemosensory Gain (Desiderosmia) Model** | Olfactory bulb has highest brain iron turnover; iron deficiency triggers intense desiderosmia for petrichor/geosmin. | Needs electroolfactogram data in clinical iron-deficiency cohorts; doesn't explain ice. | **N3 (Unrecognized Connection)** | Moderate | Active |

---

## Functional Genomic Resolution: 7p15.3 Credible Set & Candidate Comparison

```
                    chr7:25,080,179               chr7:25,224,570-25,228,486       chr7:25,244,170-25,244,675
                      [ CYCS ]                            [ NPVF (-) ]                  [ ENSR7_9D2JJ Enhancer ]
                    (164 kb away)                         (15.7 kb away)                    (Contains rs111374644)
                         ▲                                      ▲                                     ▲
                         │                                      │                                     │
─────────────────────────┴──────────────────────────────────────┴─────────────────────────────────────┴─────────────
                                                                                         ▲
                                                                                   [ rs73277282 ]
                                                                                   chr7:25,233,039
```

### Systematic Gene Target Comparison at 7p15.3

| Evaluation Criterion | Candidate 1: `NPVF` | Candidate 2: `CYCS` | Candidate 3: `SPMIP4` | Candidate 4: `lncRNAs` |
| :--- | :--- | :--- | :--- | :--- |
| **1. Distance to LD Block** | **15.7 kb (Proximal)** | 164 kb (Distant) | 109.5 kb (Distant) | 10.3 kb (Proximal) |
| **2. Enhancer Overlap** | Proximal to `ENSR7_9D2JJ` | Outside loop domain | Outside loop domain | Downstream flank |
| **3. Tissue Expression** | **Hypothalamic neurons (DMH)** | Ubiquitous (Housekeeping) | Testis-specific | Negligible / Uncharacterized |
| **4. Functional Repertoire** | **Orexigenic peptide / Feeding** | Mitochondrial electron chain | Sperm motility | Unknown |
| **5. Knockout Phenotype** | Altered energy balance/feeding | Embryonic lethal / Myopathy | Male subfertility | No phenotype |
| **6. Overall Plausibility** | **High (Leading Target)** | Low (Housekeeping) | Inactive in Brain | Low |

### The Decisive Experiment to Resolve Causality:
- **Human CRISPRi in Hypothalamic Neurons:** Targeted repression of enhancer `ENSR7_9D2JJ` in hiPSC-derived hypothalamic neurons to measure allele-specific transcription of *NPVF* vs. *CYCS*.
- **Murine Behavioral Validation:** Iron-deficiency dietary challenge in *Npvf* knockout mice to test if non-food consumption is abolished.
