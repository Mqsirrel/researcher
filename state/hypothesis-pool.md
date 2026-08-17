# Hypothesis Pool

Maintain multiple competing explanations with explicit predictions, falsifiers, and calibrated novelty/confidence rankings.

| ID | Hypothesis | Target Observation | Evidence Base | Decisive Vulnerabilities / Unsupported Edges | Novelty Level | Confidence | Status / Final Verdict |
|---|---|---|---|---|---|---|---|
| **H-001** | **Nutritional Sparing & Compensatory Drive Model** | Universal Pica | Widespread correlation with low ferritin, response to iron therapy. | Fails for pagophagia (ice has 0 Fe) and geophagy (binds Fe). | **N0 (Established)** | Moderate | Active (Baseline) |
| **H-002** | **Striatal Tyrosine Hydroxylase / D2 Hypoactivity Model** | Restlessness / Compulsive Seeking | Iron is an essential cofactor for TH; iron deficiency reduces D2 density and dopamine synthesis in striatum. | Explains chronic compulsive restlessness, but does not explain rapid $<24$h pagophagia cessation (striatal iron recovery takes weeks). | **N1 (Proposed)** | **Moderate-High** | **Active (Leading Bio-behavioral)** |
| **H-003** | **Trigeminal / Cerebral Perfusion Hypoxia Model** | Pagophagia (Ice) | Ice chewing improves cognitive test performance in anemic subjects (Hunt 2014); IV iron resolves pagophagia rapidly. | Cerebral blood flow was never measured by Hunt et al.; BMEC TfR1 vasodilatory cascade is unproven; does not explain compulsive craving. | **N2 (Under-investigated)** | **Moderate (~35%)** | **PLAUSIBLE BUT UNPROVEN** |
| **H-004** | **GI Mucosal Coating & Enterotoxin Sequestration Model** | Geophagy (Clay) | Smectite/kaolin clays bind bacterial toxins and plant tannins; colobus monkeys prefer clay-rich over iron-rich soils. | Explains geophagy as adaptive barrier protection, but fails for non-toxic pregnancy or ice pica. | **N1 (Proposed)** | **High (for Geophagy)** | Active (Subtype Specific) |
| **H-005R** | **7p15.3 / NPVF Proximal Locus Genetic Model** | Blood Donor Genetic Risk | Direct statistical GWAS association of `rs73277282` (REDS-III, AoU replication); fine-mapping isolates 17.5 kb LD block containing active enhancer `ENSR7_9D2JJ` 15.7 kb from *NPVF*. | Bulk GTEx lacks eQTL due to cell-type rarity; direct human hypothalamic CRISPRi/snRNA-seq proof is pending. | **N1 (Published GWAS Candidate)** | **Moderate (~35%)** | **PLAUSIBLE BUT UNPROVEN** |
| **H-006** | **Olfactory Glomerular Disinhibition & Desiderosmia Model** | Geosminophilia & Geophagia | Geosminophilia present in 93.8% of geophagia patients (PMID 38222205); iron deficiency impairs dopaminergic periglomerular lateral inhibition in rodents (PMID 29520328). | General IDA patients display hyposmia on Sniffin' Sticks; concept linking olfactory craving to geophagy already published (PMID 42152139). | **N1 (Previously Proposed / Dispersed)** | **Moderate-High (~45%)** | **UNDER-INVESTIGATED BUT NOT NOVEL** |
| **H-007** | **Hepatic Portal Vagal Transferrin Sensor Circuit** | Ultra-rapid $<24$h Pica Extinction | IV iron rapidly saturates circulating transferrin ($TSAT > 80\%$ in 1–4h) and clears via hepatic periportal hepatocytes; vagus modulates hepcidin/sickness behavior (PMID 37661330). | Zero electrophysiological evidence that vagal afferents possess transferrin-sensitive ion channels or fire in response to acute transferrin saturation. | **N4 (Unproposed Cross-Field Connection)** | **Low-Moderate (~30%)** | **SURVIVES — NEEDS MORE EVIDENCE** |
| **H-008** | **Salivary Amylase (*AMY1*) CNV & Gestational Starch Counter-Regulation Model** | **Amylophagy Failure to Resolve with IV Iron (REVAMP 2025 RCT)** | Direct clinical trial proof that IV iron fails to resolve amylophagy ($PR=0.93, p=0.31$, PMID 40368302); *AMY1* CNV determines salivary amylase and pre-absorptive glycemic curve; pregnancy induces insulin resistance. | Assumption that low *AMY1* specifically provokes compulsive non-food starch craving rather than generic carbohydrate intake. | **N4 (Unproposed Cross-Field Connection)** | **Moderate-High (~45%)** | **POTENTIALLY NOVEL — READY FOR EXPERIMENTAL DESIGN** |

---

## Detailed Audit Summary: Hypothesis H-008

```
[Prior-Art Audit] ──► 0 papers linking AMY1 CNV to pica, amylophagia, or non-food starch cravings.
[Causal Edges]    ──► AMY1 -> Salivary Amylase: DIRECTLY DEMONSTRATED
                  ──► Amylase -> Starch Liquefaction: DIRECTLY DEMONSTRATED
                  ──► Digestion -> Metabolic Glycemia: INDIRECTLY SUPPORTED
                  ──► Glycemia -> Compulsive Craving: PLAUSIBLE
                  ──► Compulsive Craving -> Amylophagy: SPECULATIVE (Weakest Edge)
[Counterevidence] ──► Sub-Saharan populations have intermediate AMY1 copy numbers; reflux buffering is competing driver.
[Novelty]         ──► POTENTIALLY NOVEL (Genuinely unproposed in pica literature).
[Decisive Test]   ──► Droplet digital PCR (ddPCR) of AMY1 copy number in REVAMP trial biobank.
[Status]          ──► POTENTIALLY NOVEL — READY FOR EXPERIMENTAL DESIGN
```
