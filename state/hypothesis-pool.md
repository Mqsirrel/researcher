# Hypothesis Pool

Maintain multiple competing explanations with explicit predictions, falsifiers, and calibrated novelty/confidence rankings.

| ID | Hypothesis | Evidence Base | Decisive Contradictions / Major Vulnerabilities | Novelty Level | Confidence | Status / Final Verdict |
|---|---|---|---|---|---|---|
| **H-001** | **Nutritional Sparing & Compensatory Drive Model** | Widespread correlation with low ferritin, response to iron therapy. | Fails to explain pagophagia (ice has 0 Fe) or geophagy clay chelation (binds Fe). | **N0 (Established)** | Moderate | Active (Baseline) |
| **H-002** | **Striatal Tyrosine Hydroxylase / D2 Hypoactivity Model** | Iron is an essential cofactor for TH; iron deficiency reduces D2 density and dopamine synthesis in striatum; strong clinical overlap with RLS. | Explains chronic compulsive restlessness, but does not explain rapid $<24$h pagophagia cessation (striatal iron recovery takes weeks). | **N1 (Proposed)** | **Moderate-High** | **Active (Leading Bio-behavioral)** |
| **H-003** | **Trigeminal / Cerebral Perfusion Hypoxia Compensation Model (Hunt et al., 2014)** | Ice chewing improves cognitive test performance in anemic subjects (Hunt 2014); IV iron resolves pagophagia rapidly. | **Cerebral blood flow was never measured by Hunt et al.**; BMEC TfR1 vasodilatory cascade is purely speculative; does not explain compulsive craving intensity. | **N2 (Under-investigated)** | **Moderate (~35%)** | **PLAUSIBLE BUT UNPROVEN** |
| **H-004** | **GI Mucosal Coating & Enterotoxin Sequestration Model** | Smectite/kaolin clays bind bacterial toxins and plant tannins; colobus monkeys prefer clay-rich over iron-rich soils. | Explains geophagy as adaptive barrier protection, but fails for non-toxic pregnancy or ice pica. | **N1 (Proposed)** | **High (for Geophagy)** | Active (Subtype Specific) |
| **H-005R** | **7p15.3 / NPVF Proximal Locus Genetic Vulnerability Model** | Direct statistical GWAS association of `rs73277282` in blood donors (REDS-III, AoU replication); fine-mapping isolates 17.5 kb LD block containing active enhancer `ENSR7_9D2JJ` (disrupted by proxy `rs111374644`), 15.7 kb from *NPVF*. | Bulk GTEx lacks eQTL due to cell-type rarity; direct human hypothalamic CRISPRi/snRNA-seq proof is pending. | **N1 (Published GWAS Candidate)** | **Moderate (~35%)** | **PLAUSIBLE BUT UNPROVEN** |
| **H-006** | **Olfactory Bulb Iron Depletion & Chemosensory Gain (Desiderosmia) Model** | Olfactory bulb has highest brain iron turnover; iron deficiency triggers intense desiderosmia for petrichor/geosmin. | Needs electroolfactogram data in clinical iron-deficiency cohorts; doesn't explain ice. | **N3 (Unrecognized Connection)** | Moderate | Active |

---

## Causal Edge Audit of H-003 (Pagophagia Mechanism)

```
[IV Iron]
   │
   ▼ (DIRECTLY DEMONSTRATED: Serum Fe & TSAT spike in 1-4h)
[Transferrin Saturation ↑]
   │
   ▼ (DIRECTLY DEMONSTRATED: Diferric Tf binds BMEC surface TfR1)
[BMEC TfR1 Binding & Endocytosis]
   │
   ▼ (SPECULATIVE: No direct proof that TfR1 triggers acute eNOS activation)
[Endothelial eNOS Activation & Vasodilation]
   │
   ▼ (INDIRECTLY SUPPORTED: eNOS general vascular role; unproven in this context)
[Cerebral Microvascular Perfusion Normalization]
   │
   ▼ (SPECULATIVE: Hunt 2014 measured reaction time, NEVER cerebral blood flow)
[Abolition of Need for TRPM8 Cold Mastication Alertness Boost]
   │
   ▼ (INDIRECTLY SUPPORTED: Fails to explain compulsive craving drive)
[Resolution of Compulsive Pagophagia]
```

### The Decisive Experiment to Settle H-003:
- **Design:** Transcranial Doppler (TCD) of Middle Cerebral Artery (MCA) in iron-deficient anemic pagophagia patients during randomized ice chewing vs. room-temperature water chewing vs. sham dry mastication before and 24h after IV ferric carboxymaltose.
- **Falsification Threshold:** If ice chewing does not produce a significant, cold-dependent increase in MCA flow velocity ($V_m$) compared to room-temperature water in anemic patients, H-003 is falsified.
