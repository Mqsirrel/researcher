# Hypothesis Pool

Maintain multiple competing explanations with explicit predictions, falsifiers, and calibrated novelty/confidence rankings.

| ID | Hypothesis | Evidence Base | Decisive Contradictions / Major Vulnerabilities | Novelty Level | Confidence | Status / Final Verdict |
|---|---|---|---|---|---|---|
| **H-001** | **Nutritional Sparing & Compensatory Drive Model** | Widespread correlation with low ferritin, response to iron therapy. | Fails to explain pagophagia (ice has 0 Fe) or geophagy clay chelation (binds Fe). | **N0 (Established)** | Moderate | Active (Baseline) |
| **H-002** | **Striatal Tyrosine Hydroxylase / D2 Hypoactivity Model** | Iron is an essential cofactor for TH; iron deficiency reduces D2 density and dopamine synthesis in striatum; strong clinical overlap with RLS. | Does not explain substance-specific sensory selection (ice vs. clay) without peripheral gating. | **N1 (Proposed)** | **High** | **Leading Model (Bio-behavioral)** |
| **H-003** | **Trigeminal / Cerebral Perfusion Hypoxia Compensation Model** | Ice chewing improves cognitive speed and alertness selectively in anemic patients (Hunt et al., 2014); TRPM8/sympathetic activation increases MCA blood flow velocity. | Highly specific to pagophagia; does not explain geophagy or amylophagy. | **N2 (Under-investigated)** | **High (for Pagophagia)** | **Leading Model (Subtype Specific)** |
| **H-004** | **GI Mucosal Coating & Enterotoxin Sequestration Model** | Smectite/kaolin clays bind bacterial toxins and plant tannins; colobus monkeys prefer clay-rich over iron-rich soils. | Explains geophagy as adaptive barrier protection, but fails for non-toxic pregnancy or ice pica. | **N1 (Proposed)** | **High (for Geophagy)** | Active (Subtype Specific) |
| **H-005R** | **7p15.3 / NPVF Proximal Locus Genetic Vulnerability Model** | Direct statistical GWAS association of `rs73277282` (4.5 kb upstream of *NPVF*) with blood donor pica (REDS-III, AoU replication, PMID 41708529). | Non-coding intergenic variant; GTEx v8 lacks significant eQTL; functional eQTL in human hypothalamus unproven; potential alternative targets (*CYCS*, lncRNAs). | **N1 (Published GWAS Candidate)** | **Moderate (~35%)** | **PLAUSIBLE BUT UNPROVEN** |
| **H-006** | **Olfactory Bulb Iron Depletion & Chemosensory Gain (Desiderosmia) Model** | Olfactory bulb has highest brain iron turnover; iron deficiency triggers intense desiderosmia for petrichor/geosmin. | Needs electroolfactogram data in clinical iron-deficiency cohorts; doesn't explain ice. | **N3 (Unrecognized Connection)** | Moderate | Active |

---

## Forensic Genomic Trace: rs73277282 → 7p15.3 → NPVF

```
                    chr7:25,080,179            chr7:25,134,676           chr7:25,224,570-25,228,486
                      [ CYCS ]                   [ SPMIP4 ]                      [ NPVF (-) ]
                    (107.6 kb up)               (52.6 kb up)                   (4.5 kb away)
                         ▲                           ▲                               ▲
                         │                           │                               │
─────────────────────────┴───────────────────────────┴───────────────┬───────────────┴───────────
                                                                     │
                                                              [ rs73277282 ]
                                                            chr7:25,233,039
```

### Forensic Audit Findings:
1. **Association Reality:** **Real & Replicated.** Reached genome-wide significance ($p = 1.53 \times 10^{-8}$) in 12,157 REDS-III blood donors and replicated in *All of Us*.
2. **Phenotype:** **Directly Associated with Pica Survey Responses.** Assessed via structured health questionnaires in blood donors who developed iron depletion (2.4% prevalence).
3. **NPVF Proximity:** `rs73277282` is located **4,553 bp upstream** of the 5' transcription start site of `NPVF` on the negative strand, making *NPVF* the primary positional candidate.
4. **Functional Evidence:** **Zero Direct Proof.** GTEx v8 reports 0 significant eQTLs in bulk tissues. Direct proof of allele-specific *NPVF* transcription in human hypothalamic tissue is absent.
5. **Plausible Genomic Alternatives:** `CYCS` (Cytochrome c, essential mitochondrial heme protein, 107.6 kb away) and adjacent lncRNAs (`ENSG00000285716` at 21.9 kb).
6. **Prior Art:** The connection between `rs73277282` / *NPVF* and pica was **discovered and published by the REDS-III study group in April 2026 (Transfusion)**. It is not our novel discovery.

### Final Evaluative Verdict on H-005R:
**PLAUSIBLE BUT UNPROVEN**
