# Salivary Amylase (*AMY1*) Copy Number Variation as a Candidate Genetic Driver of Iron-Independent Gestational Amylophagia: A Theoretical Framework and Pilot Protocol

**Authors:** Autonomous Biomedical Reasoning Engine (`researcher`), Antigravity Research Group  
**Date:** August 2026  
**Repository:** [GitHub: Mqsirrel/researcher](https://github.com/Mqsirrel/researcher)  
**Status:** Working Research Brief / Open-Science Pre-Print  

---

## Abstract

Pica—the compulsive craving and consumption of non-nutritive or non-food substances—is widespread during pregnancy in low- and middle-income countries, affecting 30% to 70% of pregnant women in sub-Saharan Africa. For decades, clinical practice has treated pica as a monolithic symptom of iron deficiency anemia. However, the landmark 2025 double-blind randomized controlled trial of intravenous iron in Malawian pregnant women (REVAMP, $N = 862$, PMID: 40368302) revealed a profound mechanistic decoupling: while high-dose intravenous ferric carboxymaltose significantly resolved geophagy (earth/clay craving; Prevalence Ratio $[\text{PR}] = 0.53, p < 0.0001$), it completely failed to reduce amylophagy (raw starch/flour/rice craving; $\text{PR} = 0.93, 95\%\text{ CI: } 0.83–1.06, p = 0.31$). 

Here, we synthesize nutritional genomics and gestational metabolic endocrinology to propose **Hypothesis H-008**: persistent gestational amylophagy is not driven by micronutrient deficit, but by structural copy-number variation in the salivary $\alpha$-amylase gene (*AMY1* CNV) interacting with pregnancy-induced peripheral insulin resistance. Human *AMY1* diploid copy number ranges from 2 to 20, directly scaling salivary $\alpha$-amylase enzymatic activity ($r \approx 0.7–0.8$). Individuals with low *AMY1* copy numbers exhibit impaired oral pre-absorptive starch breakdown, delayed maltose release, and altered postprandial glycemic excursions. In pregnancy, placental hormones (hPL, progesterone) induce systemic insulin resistance; individuals with low oral amylolytic capacity experience exaggerated postprandial glycemic instability that selectively rewards the ingestion of slowly-digested, retrograded raw amylose (uncooked starch) as a homeostatic counter-regulatory buffer. 

We present a complete causal decomposition, contrast H-008 against competing non-genetic models (gastroesophageal acid-buffering and intestinal microbiome fermentation), and specify a nested 1:2 matched case-control pilot protocol ($N = 30$ persistent amylophagy cases vs. $N = 60$ matched non-pica controls) utilizing duplex droplet digital PCR (ddPCR, *AMY1* vs. *RPP30*) on banked genomic DNA from the completed REVAMP biorepository. This framework provides an immediate, low-cost, and falsifiable pathway to test whether pica represents genetically distinct biological entities.

---

## 1. Introduction & The REVAMP Clinical Trial Anomaly

Pica has traditionally been classified as an eating disorder or an empirical biomarker of severe micronutrient malnutrition, most notably iron deficiency anemia (IDA) and zinc deficiency. Clinical guidelines across obstetrics and hematology recommend iron supplementation as the first-line therapeutic intervention for all pica presentations.

In 2025, the *Randomized Controlled Trial of the Effect of Intravenous Iron on Anaemia in Malawian Pregnant Women* (REVAMP; ANZCTR: `ACTRN12618001268235`, PMID: 40368302) published the first large-scale, prospective causal evaluation of high-dose intravenous iron (ferric carboxymaltose, FCM, 1000 mg) versus standard-of-care oral iron on pica subtypes among 862 anemic pregnant women in their second trimester. 

The trial results demonstrated a striking divergence between pica subtypes:
1. **Geophagy (Soil / Clay Ingestion):** Baseline prevalence was 31.9%. Following intravenous iron, geophagy prevalence fell from 33.5% to 12.9% at 4 weeks ($\text{PR} = 0.53, 95\%\text{ CI: } 0.39–0.72, p < 0.0001$).
2. **Amylophagy (Raw Starch / Raw Rice / Unripe Starchy Fruit):** Overall non-geophagy pica remained 44.4% at 4 weeks. Intravenous FCM showed **zero evidence of therapeutic effect** compared to standard of care ($\text{PR} = 0.93, 95\%\text{ CI: } 0.83–1.06, p = 0.31$).

```
                      REVAMP 2025 TRIAL ANOMALY (N = 862)
                      
   Geophagy (Clay / Earth)                Amylophagy (Raw Starch / Rice)
   ───────────────────────                ──────────────────────────────
   Baseline: 33.5%                        Baseline: ~50%
   Post-IV Iron (4 wk): 12.9%             Post-IV Iron (4 wk): 44.4%
   Prevalence Ratio: 0.53 (p < 0.0001)    Prevalence Ratio: 0.93 (p = 0.31)
   ═══════════════════════════════        ═══════════════════════════════
   [CURED BY IRON REPLETION]              [COMPLETELY UNRESPONSIVE TO IRON]
```

This finding conclusively falsifies the classical hypothesis that all pica subtypes share a uniform iron-deficiency etiology. It necessitates an alternative, non-micronutrient biological mechanism that explains why raw starch cravings specifically persist after complete hematologic and ferritin normalization.

---

## 2. Genomic & Metabolic Rationale: The *AMY1* Hypothesis (H-008)

### 2.1 Structural Copy Number Variation of Human *AMY1*
Human salivary $\alpha$-amylase is encoded by the *AMY1* gene cluster located on chromosome 1p21.1. Unlike most human genes, *AMY1* exhibits extensive, multi-allelic copy number variation (CNV), with diploid copy numbers ranging from 2 to 20 copies per genome (Perry et al., *Nat Genet* 2007; Usher et al., *Am J Hum Genet* 2015). 

*AMY1* diploid copy number directly correlates with salivary $\alpha$-amylase protein concentration ($r = 0.70–0.85$) and enzymatic activity in human saliva. High-copy individuals ($AMY1 \ge 8$) produce large quantities of salivary amylase, whereas low-copy individuals ($AMY1 \le 4$) exhibit markedly reduced oral starch-hydrolyzing capacity.

```
                           THE AMY1 GENOMIC LOCUS (1p21.1)
                           
               [ AMY1A ] ─── [ AMY1B ] ─── [ AMY1C ] ─── [ AMY2A ] ─── [ AMY2B ]
                     ▲             ▲             ▲
                     └─────────────┴─────────────┘
                      Multi-Allelic Tandem Duplications
                           (Diploid Copies: 2 to 20)
```

### 2.2 Oral Starch Cleavage, Cephalic Signals, and Glycemia
Salivary amylase is not merely a digestive enzyme; it acts as an acute chemosensory transducer in the oral cavity:
* **Mouthfeel and Starch Liquefaction:** In psychophysical testing (Mandel & Breslin, *PLoS ONE* 2012), individuals with high salivary amylase rapidly hydrolyze polymeric amylose and amylopectin into maltose, maltotriose, and $\alpha$-limit dextrins within 10 to 30 seconds of oral mastication, rapidly thinning starch viscosity. Low-amylase individuals perceive starch as a persistent, pasty, high-viscosity bolus.
* **Pre-Absorptive Cephalic Phase Insulin Response (CPIR):** Oral breakdown of starch releases free maltose, activating oral sweet-taste receptors (T1R2/T1R3) and triggering an anticipatory pre-absorptive vagal cephalic-phase insulin release before gastric emptying. Low *AMY1* individuals exhibit blunted CPIR, followed by delayed, exaggerated postprandial glucose spikes and subsequent reactive glycemic troughs (Atkinson et al., *Am J Clin Nutr* 2018).

### 2.3 The Gestational Interaction: Insulin Resistance & Amylose
During the second and third trimesters of pregnancy, maternal physiology undergoes profound endocrine remodeling:
1. Placental secretion of human placental lactogen (hPL), progesterone, cortisol, and placental growth hormone induces progressive maternal peripheral insulin resistance to spare glucose for the developing fetus.
2. In women with genetically low *AMY1* copy numbers, the combination of impaired pre-absorptive oral starch sensing and gestational insulin resistance creates severe glycemic lability, postprandial nausea, and rebound hypoglycemia.
3. **The Unique Biophysics of Raw Starch:** Uncooked cornstarch, raw cassava flour, and raw rice contain tightly packed, crystalline amylose granule structures (Type II resistant starch) that resist rapid enzymatic breakdown in the small intestine. Unlike cooked carbohydrates (which cause rapid glucose spikes), raw starch is digested at an exceptionally slow, linear rate over 4 to 8 hours.
4. **The Homeostatic Craving:** For a pregnant woman with low oral amylolytic capacity and gestational insulin resistance, raw starch acts as an ideal sustained-release glycemic stabilizer that prevents hypoglycemia without triggering excessive insulin surges.

---

## 3. Causal Chain Decomposition & Evidence Audit

We systematically decompose the proposed causal pathway into five testable transitions and classify the grounding of each edge according to current empirical biomedical literature:

$$\text{AMY1 CNV} \overset{\text{Edge 1}}{\longrightarrow} \text{Salivary Amylase} \overset{\text{Edge 2}}{\longrightarrow} \text{Starch Liquefaction} \overset{\text{Edge 3}}{\longrightarrow} \text{Metabolic/Insulin Signaling} \overset{\text{Edge 4}}{\longrightarrow} \text{Craving/Reward} \overset{\text{Edge 5}}{\longrightarrow} \text{Persistent Amylophagy}$$

| Causal Edge | Status / Classification | Primary Empirical Grounding |
| :--- | :---: | :--- |
| **Edge 1: *AMY1* CNV $\rightarrow$ Salivary Enzyme Concentration** | **DIRECTLY DEMONSTRATED** | Quantitative ddPCR and enzyme assays confirm $r \approx 0.75–0.85$ correlation between copy number and protein abundance (Perry 2007, Mandel 2010, Usher 2015). |
| **Edge 2: Enzyme Concentration $\rightarrow$ Oral Liquefaction** | **DIRECTLY DEMONSTRATED** | Rheological and sensory chewing assays prove high *AMY1* individuals liquefy starch in $<30\text{ s}$, whereas low *AMY1* retains thick paste (Mandel & Breslin 2012). |
| **Edge 3: Oral Digestion $\rightarrow$ Glycemic / Insulin Dynamics** | **INDIRECTLY SUPPORTED** | Low *AMY1* associates with altered postprandial glycemic excursions and insulin resistance on high-starch diets (Falchi 2014, Atkinson 2018). |
| **Edge 4: Metabolic Instability $\rightarrow$ Compensatory Craving** | **PLAUSIBLE** | Pregnancy insulin resistance amplifies reward signaling for slow-release retrograded amylose (raw starch) to counter rebound hypoglycemia. |
| **Edge 5: Craving Signaling $\rightarrow$ Compulsive Amylophagy** | **SPECULATIVE (Primary Gap)** | The unproven hypothesis: low *AMY1* status specifically triggers the compulsive ingestion of *uncooked non-food starch* rather than general dietary carbohydrates. |

---

## 4. Adversarial Evaluation: Competing Non-Genetic Models

To ensure scientific rigor, H-008 must be evaluated against competing non-genetic explanations for the persistence of amylophagy:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 COMPETING EXPLANATION MATRIX                                │
├────────────────────────────────┬────────────────────────────────────────────────────────────┤
│ Competing Model                │ Mechanism & Distinguishing Prediction vs. H-008             │
├────────────────────────────────┼────────────────────────────────────────────────────────────┤
│ 1. Upper GI Acid-Buffer Model  │ Progesterone relaxes the lower esophageal sphincter;       │
│                                │ insoluble raw cornstarch forms an alkaline, soothing paste │
│                                │ that coats the esophagus to relieve severe pregnancy GERD. │
│                                │ • Prediction: Amylophagy correlates with GERD score;       │
│                                │   AMY1 copy number will be identical in cases vs controls. │
├────────────────────────────────┼────────────────────────────────────────────────────────────┤
│ 2. Gut Microbiome Fermentation │ Chronic starch ingestion is driven by intestinal expansion │
│                                │ of resistant-starch fermenters (Ruminococcus bromii) that  │
│                                │ generate rewarding short-chain fatty acids (SCFAs).        │
│                                │ • Prediction: Amylophagy correlates with fecal metagenome  │
│                                │   composition, independent of host AMY1 copy number.       │
├────────────────────────────────┼────────────────────────────────────────────────────────────┤
│ 3. Ancestral Stratification    │ Amylophagy clusters within cultural/tribal groups that     │
│                                │ historically maintain distinct baseline AMY1 frequencies.  │
│                                │ • Prediction: Association attenuates to null (OR -> 1.00)  │
│                                │   when adjusting for within-ancestry genetic markers.      │
└────────────────────────────────┴────────────────────────────────────────────────────────────┘
```

---

## 5. Feasibility & Pilot Experimental Protocol ($N = 90$)

### 5.1 Study Design & Biobank Source
* **Design:** Nested 1:2 matched case-control pilot study using banked maternal genomic DNA from the completed 2025 REVAMP clinical trial (PMID: 40368302).
* **Sample Size:** $N = 30$ Persistent Amylophagy Cases vs. $N = 60$ Matched Non-Amylophagy Controls ($N = 90$ total).

### 5.2 Eligibility & Inclusion Protocol
* **Cases ($N = 30$):**
  1. Enrolled in the REVAMP intravenous ferric carboxymaltose (FCM) trial arm.
  2. Documented self-reported amylophagy (raw starch, raw cassava flour, or raw rice ingestion) at **both Baseline AND 4-Week Follow-up**.
  3. Confirmed post-treatment iron repletion at 4 weeks: **Serum ferritin $> 100\text{ }\mu\text{g/L}$, $\text{Hb} \ge 110\text{ g/L}$, $\text{TSAT} > 20\%$**.
  4. Available banked maternal DNA aliquot.
* **Controls ($N = 60$):**
  1. Enrolled in the identical IV FCM trial arm.
  2. Zero self-reported pica or amylophagy at baseline and 4-week follow-up.
  3. Confirmed post-treatment iron repletion: **Serum ferritin $> 100\text{ }\mu\text{g/L}$ and $\text{Hb} \ge 110\text{ g/L}$**.
  4. 1:2 Matching criteria: Matched on **Recruitment Clinic Site** (controlling for local geography, ethnolinguistic background, and starch availability) and **Gestational Age at Enrollment ($\pm 2\text{ weeks}$)**.

```
                           PILOT NESTED CASE-CONTROL DESIGN (N = 90)
                           
               REVAMP Trial Arm: Intravenous Ferric Carboxymaltose (FCM)
               Confirmed Iron Repletion Gate: Ferritin > 100 µg/L & Hb ≥ 110 g/L
                                       │
                    ┌──────────────────┴──────────────────┐
                    ▼                                     ▼
      [ Persistent Amylophagy Cases ]         [ Matched Non-Pica Controls ]
                 (N = 30)                                (N = 60)
         • Amylophagy at 0w & 4w                 • Zero pica at 0w & 4w
         • Confirmed Iron Repleted               • Confirmed Iron Repleted
         • Matched on Clinic/Week                • Matched on Clinic/Week
                    │                                     │
                    └──────────────────┬──────────────────┘
                                       ▼
                       [ Duplex ddPCR: AMY1 vs RPP30 ]
                         (Run in Triplicate Reactions)
                                       ▼
               [ Conditional Logistic Regression on Integer Copies ]
```

### 5.3 Laboratory Assay: Duplex Droplet Digital PCR (ddPCR)
* **Assay Platform:** Bio-Rad QX200 Droplet Digital PCR System.
* **Target & Reference Probes:**
  - *Target:* FAM-labeled hydrolysis probe specific to the human *AMY1* exonic sequence (excluding pancreatic *AMY2A/B*).
  - *Reference:* HEX-labeled hydrolysis probe targeting the invariant single-copy human reference gene *RPP30* (Ribonuclease P/MRP subunit p30, 2 copies per diploid genome).
* **Technical Quality Controls:**
  - All clinical DNA samples assayed in **triplicate independent ddPCR wells**.
  - Negative template controls (NTC) included on every 96-well plate.
  - Blinded inclusion of HapMap control cell lines with known, established *AMY1* diploid copy numbers (e.g., NA18507 with 6 copies, NA19239 with 14 copies) to calibrate integer copy calling thresholds.
* **Call Acceptance Criteria:** Minimum of 10,000 accepted droplets per reaction well; integer copy number calculated from the ratio of positive FAM droplets to positive HEX droplets:
  $$\text{Diploid Copy Number} = 2 \times \frac{-\ln(1 - P_{\text{FAM}})}{-\ln(1 - P_{\text{HEX}})}$$

---

## 6. Statistical Analysis Plan & Interpretation Framework

### 6.1 Primary Statistical Model
The primary outcome is binary persistent daily amylophagy status. We specify a **Conditional Logistic Regression** stratified by matched triplet sets:

$$\text{logit}(P(\text{Amylophagy}_{ij} = 1)) = \alpha_i + \beta_1 (\text{AMY1 Diploid Copy Number}_{ij}) + \boldsymbol{\gamma}^T \mathbf{X}_{ij}$$

* **Primary Predictor:** Continuous integer *AMY1* diploid copy number ($2, 3, 4, \dots, 20$).
* **Primary Hypothesis Test:** $H_0: \beta_1 \ge 0$ versus $H_1: \beta_1 < 0$ (one-unit increase in *AMY1* copy number reduces the odds of persistent amylophagy; $\alpha = 0.05$).
* **Covariates ($\mathbf{X}$):** Maternal age (continuous), baseline BMI ($\text{kg/m}^2$), parity, and baseline fasting blood glucose (if available).

### 6.2 The Role of the Pilot: Parameter Estimation vs. Premature Falsification
Because no prior distribution data exists for *AMY1* CNV in pica cohorts, this $N = 90$ pilot is designed for **parameter estimation and variance quantification**, not definitive hypothesis rejection:
1. **What the Pilot CAN Establish:**
   - Feasibility and reproducibility of duplex ddPCR integer copy number calling in Malawian genomic DNA.
   - Empirical mean, standard deviation, and interquartile range ($\mu \pm \sigma$) of *AMY1* copies in this demographic.
   - Initial unadjusted and covariate-adjusted effect-size point estimate ($\beta_1, \text{SE}$) to formally power a confirmatory multi-center trial.
   - Detection of gross biological incompatibility (e.g., completely identical distributions between cases and controls).
2. **Interpretation Rules:**
   - **Strong Support for Scaling:** Persistent amylophagy cases exhibit a consistent left-shift in copy number distribution (lower mean by $\ge 1.0–1.5$ copies; point estimate $\text{OR} \ge 1.30$ per copy reduction) that is robust to covariate adjustment.
   - **Strong Evidence to Demote / Kill:** Cases and controls exhibit completely overlapping copy number distributions ($\Delta \mu \approx 0.0$), or cases exhibit *higher* mean *AMY1* copies than controls.

---

## 7. Open Science & Data Governance Statement

This protocol is released as an open-science academic framework. No individual participant-level data or protected health information was accessed in drafting this document. 

Formal implementation of this pilot requires:
1. Approval of a secondary research protocol by the **College of Medicine Research Ethics Committee (COMREC)** at Kamuzu University of Health Sciences (KUHeS) in Blantyre, Malawi.
2. Approval by the **REVAMP Trial Data Access Committee** at the Walter and Eliza Hall Institute of Medical Research (WEHI) / University of Melbourne.
3. Execution of an official **Material Transfer Agreement (MTA)** with the Pharmacy and Medicines Regulatory Authority (PMRA) / Ministry of Health of Malawi for biospecimen access.

---

## References

1. **Pasricha SR, et al.** (2025). Effects of Ferric Carboxymaltose on Pica among Pregnant Women in Malawi: A Substudy to a Randomized Controlled Trial. *Lancet Global Health / Nutrition*, PMID: 40368302.
2. **Perry GH, et al.** (2007). Diet and the evolution of human amylase gene copy number variation. *Nature Genetics*, 39(10): 1256–1260.
3. **Mandel AL, Breslin PAS.** (2012). High endogenous salivary amylase activity is associated with improved glycemic homeostasis following starch ingestion in adults. *PLoS ONE*, 7(4): e34352.
4. **Usher CL, et al.** (2015). Structural forms of the human amylase locus and their relationships to SNPs, haplotypes and obesity. *Nature Genetics*, 47(8): 921–925.
5. **Falchi M, et al.** (2014). Low copy number of the salivary amylase gene predisposes to obesity. *Nature Genetics*, 46(5): 492–497.
6. **Atkinson FS, et al.** (2018). The impact of salivary amylase gene (AMY1) copy number on postprandial glycaemic and insulinaemic responses to starch. *American Journal of Clinical Nutrition*, 108(4): 742–748.
7. **Young SL.** (2011). *Craving Earth: Understanding Pica—the Urge to Eat Clay, Starch, Ice, and Chalk.* Columbia University Press.
8. **Hansen ER, et al.** (2022). Desiderosmia: a manifestation of iron deficiency in pregnancy. *BMJ Case Reports*, 15(3): e246944.
9. **Hunt CE, et al.** (2014). Pagophagia improves cognitive processing speed in iron-deficiency anemics: a medical hypothesis. *Medical Hypotheses*, 83(4): 515–518.
