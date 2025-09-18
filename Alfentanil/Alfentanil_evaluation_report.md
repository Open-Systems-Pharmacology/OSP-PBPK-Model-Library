# Building and Evaluation of a PBPK Model for alfentanil in Adults

| Version                                         | 3.0-OSP12.1                                                   |
| ----------------------------------------------- | ------------------------------------------------------------ |
| based on *Model Snapshot* and *Evaluation Plan* | https://github.com/Open-Systems-Pharmacology/Alfentanil-Model/releases/tag/v3.0 |
| OSP Version                                     | 12.1                                                          |
| Qualification Framework Version                 | 3.4                                                          |

This evaluation report and the corresponding PK-Sim project file are filed at:

https://github.com/Open-Systems-Pharmacology/OSP-PBPK-Model-Library/

# Table of Contents

 * [1 Introduction](#introduction)
 * [2 Methods](#methods)
   * [2.1 Modeling Strategy](#modeling-strategy)
   * [2.2 Data](#data)
   * [2.3 Model Parameters and Assumptions](#model-parameters-and-assumptions)
 * [3 Results and Discussion](#results-and-discussion)
   * [3.1 Final input parameters](#final-input-parameters)
   * [3.2 Diagnostics Plots](#diagnostics-plots)
   * [3.3 Concentration-Time Profiles](#ct-profiles)
     * [3.3.1 Model Building](#model-building)
     * [3.3.2 Model Verification](#model-verification)
 * [4 Conclusion](#conclusion)
 * [5 References](#main-references)

# 1 Introduction<a id="introduction"></a>

Alfentanil is a potent analgesic synthetic opioid. It is fast but short-acting and used for anesthesia during surgery. Alfentanil is metabolized solely by CYP3A4 ([Phimmasone 2001](#5-references)). Like midazolam, alfentanil is not a substrate for P-gp ([Wandel 2002](#5-references)) and less than 1% of an alfentanil dose is excreted unchanged in urine ([Meuldermans 1988](#5-references)).

Although in clinical use alfentanil is always administered intravenously (iv), some DDI studies published plasma concentration-time profiles of alfentanil following oral ingestion. The presented alfentanil model was established using clinical PK data of 8 publications, covering iv and oral (po) administration and a dosing range from 0.015 to 0.075 mg/kg as well as absolute doses of 1 mg iv and 4 mg po. The established model is based on the model developed by Hanke *et al.* ([Hanke 2018](#5-references)) and applies metabolism by CYP3A4 and glomerular filtration.  

# 2 Methods<a id="methods"></a>

## 2.1 Modeling Strategy<a id="modeling-strategy"></a>

The general concept of building a PBPK model has previously been described by e.g. Kuepfer et al. ([Kuepfer 2016](#5-references)). The relevant anthropometric (height, weight) and physiological information (e.g. blood flows, organ volumes, binding protein concentrations, hematocrit, cardiac output) in adults was gathered from the literature and has been previously published ([Willmann 2007](#5-references)). This information was incorporated into PK-Sim® and was used as default values for the simulations in adults.

Variability of plasma proteins and CYP3A4 are integrated into PK-Sim® and described in the publicly available PK-Sim® Ontogeny Database Version 7.3 ([PK-Sim Ontogeny Database Version 7.3](#5-references)) or otherwise referenced for the specific process.

First, a base mean model was built using clinical data including selected single dose studies with intravenous and oral applications (solution) of alfentanil to find an appropriate structure to describe the pharmacokinetics in plasma. The mean PBPK model was developed using a typical European individual. The relative tissue specific expressions of enzymes predominantly being involved in the metabolism of alfentanil were included in the model as described elsewhere ([Meyer 2012](#5-references)).

Unknown parameters (see below) were identified using the Parameter Identification module provided in PK-Sim®. Structural model selection was mainly guided by visual inspection of the resulting description of data and biological plausibility.

Details about input data (physicochemical, *in vitro* and clinical) can be found in [Section 2.2](#22-data).

Details about the structural model and its parameters can be found in [Section 2.3](#23-model-parameters-and-assumptions).

## 2.2 Data<a id="data"></a>

### 2.2.1 In vitro / physicochemical Data

A literature search was performed to collect available information on physicochemical properties of alfentanil. The obtained information from literature is summarized in the table below. 

| **Parameter**   | **Unit** | **Value**  | Source                            | **Description**                                           |
| :-------------- | -------- | ---------- | --------------------------------- | --------------------------------------------------------- |
| MW              | g/mol    | 416.52     | [DrugBank DB00802](#5-references) | Molecular weight                                          |
| pK<sub>a</sub>  |          | 6.5 (base) | [Jansson 2008](#5-references)     | Acid dissociation constant                                |
| Solubility (pH) | mg/L     | 992 (6.5)  | [Baneyx 2014](#5-references)      | Solubility                                                |
| logD            |          | 2.1        | [Baneyx 2014](#5-references)      | Partition coefficient between octanol and water at pH 7.4 |
|                 |          | 2.2        | [Jansson 2008](#5-references)     | Partition coefficient between octanol and water           |
| fu              | %        | 8.6        | [Gertz 2010](#5-references)       | Fraction unbound in plasma                                |
|                 |          | 10.0       | [Edginton 2008](#5-references)    | Fraction unbound in plasma                                |
|                 |          | 12.0       | [Almond 2016](#5-references)      | Fraction unbound in plasma                                |

### 2.2.2 Clinical Data

A literature search was performed to collect available clinical data on alfentanil in healthy adults.

#### 2.2.2.1 Model Building

The following studies were used for model building:

| Publication                      | Arm / Treatment / Information used for model building        |
| :------------------------------- | :----------------------------------------------------------- |
| [Ferrier 1985](#5-references)    | Healthy subjects with a single iv dose of 0.05 mg/kg         |
| [Kharasch 1997](#5-references)   | Healthy subjects with a single iv dose of 0.02 mg/kg         |
| [Kharasch 2004](#5-references)   | Healthy subjects with a single iv dose of 0.015 mg/kg, healthy subjects with a single oral dose of 0.06 mg/kg |
| [Kharasch 2011](#5-references)   | Healthy subjects with a single iv dose of 0.015 mg/kg, healthy subjects with a single oral dose of 0.075 mg/kg |
| [Kharasch 2011b](#5-references)  | Healthy subjects with an iv dose of 1 mg, healthy subjects with an oral dose of 1 mg. Publication compares sequential and simultaneous dosing of oral deuterated and intravenous unlabeled alfentanil. Furthermore, IV and oral administration of alfentanil is combined with grapefruit juice. Grapefruit juice is considered to have no effect on hepatic clearance, and, hence, no effect on IV administered alfentanil |
| [Kharasch 2012](#5-references)   | Healthy subjects with a single iv dose of 0.02 mg/kg, healthy subjects with a single oral dose of 0.043 mg/kg |
| [Meistelman 1987](#5-references) | Healthy subjects with a single iv dose of 0.02 mg/kg         |
| [Phimmasone 2001](#5-references) | Healthy subjects with a single iv dose of 0.015 mg/kg        |

## 2.3 Model Parameters and Assumptions<a id="model-parameters-and-assumptions"></a>

### 2.3.1 Absorption

Absorption observed in clinical studies can be fully explained by passive absorption.

### 2.3.2 Distribution

After testing the available organ-plasma partition coefficient and cell permeability calculation methods built in PK-Sim, observed clinical data was best described by choosing the partition coefficient calculation by `Rodgers and Rowland` and cellular permeability calculation by `PK-Sim Standard`. 

### 2.3.3 Metabolism and Elimination

Alfentanil is metabolized solely by CYP3A4. The tissue-specific CYP3A4 expression implemented in the model is based on high-sensitive real-time RT-PCR ([Nishimura 2013](#5-references)). 

The first model simulations showed that gut wall metabolization was too low in the PBPK model. In order to increase gut wall metabolization, the “mucosa permeability on basolateral side” (jointly the model parameters in the mucosa: ``P (interstitial->intracellular)`` and ``P (intracellular->interstitial)``) was estimated. This may lead to higher gut wall concentrations and, in turn, to a higher gut wall elimination.

### 2.3.4 Automated Parameter Identification

This is the result of the final parameter identification:

| Model Parameter            | Optimized Value | Unit |
| -------------------------- | --------------- | ---- |
| `Lipophilicity` | 1.846           |        |
| `Specific intestinal permeability`                           | 5.737E-4        | cm/min |
| `Specific organ permeability` | 6.875E-3        | cm/min |
| Basolateral mucosa permeability<br />(``P (interstitial->intracellular)``, ``P (intracellular->interstitial)``) | 5.415E-4        | cm/min |
| `CYP3A4 - 1st order CL - intrinsic clearance` | 0.527           | l/min  |

# 3 Results and Discussion<a id="results-and-discussion"></a>

The PBPK model for alfentanil was developed and evaluated using publically available, clinical pharmacokinetic data from studies listed in [Section 2.2.2](#222-clinical-data).

The next sections show:

1. the final model parameters for the building blocks: [Section 3.1](#31-final-input-parameters).
2. the overall goodness of fit: [Section 3.2](#32-diagnostics-plots).
3. simulated vs. observed concentration-time profiles for the clinical studies used for model building and for model verification: [Section 3.3](#33-concentration-time-profiles).

## 3.1 Final input parameters<a id="final-input-parameters"></a>

The compound parameter values of the final PBPK model are illustrated below.

### Compound: Alfentanil

#### Parameters

Name                                             | Value                   | Value Origin                                                                                                          | Alternative | Default
------------------------------------------------ | ----------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------- | -------
Solubility at reference pH                       | 992 mg/l                | Publication-Hanke 2018                                                                                                | Baneyx 2014 | True   
Reference pH                                     | 6.5                     | Publication-Hanke 2018                                                                                                | Baneyx 2014 | True   
Lipophilicity                                    | 1.8463211883 Log Units  | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 4' on 2019-09-06 11:28 | Fit         | True   
Fraction unbound (plasma, reference value)       | 0.1                     | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 4' on 2019-09-06 11:28 | Healthy     | True   
Permeability                                     | 0.0068752756625 cm/min  | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 4' on 2019-09-06 11:28 | Optimized   | True   
Specific intestinal permeability (transcellular) | 0.00057373577138 cm/min | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 4' on 2019-09-06 11:28 | Optimized   | True   
Is small molecule                                | Yes                     |                                                                                                                       |             |        
Molecular weight                                 | 416.52 g/mol            | Publication-Drugbank                                                                                                  |             |        
Plasma protein binding partner                   | α1-acid glycoprotein    |                                                                                                                       |             |        

#### Calculation methods

Name                    | Value              
----------------------- | -------------------
Partition coefficients  | Rodgers and Rowland
Cellular permeabilities | PK-Sim Standard    

#### Processes

##### Metabolizing Enzyme: CYP3A4-1st order CL

Species: Human

Molecule: CYP3A4

###### Parameters

Name                | Value              | Value Origin                                                                                                         
------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------
Intrinsic clearance | 0.5272297928 l/min | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 4' on 2019-09-06 11:28

##### Systemic Process: Glomerular Filtration-GFR

Species: Human

###### Parameters

Name         | Value | Value Origin          
------------ | -----:| ----------------------
GFR fraction |  0.06 | Publication-Hanke 2018

### Formulation: Solution

Type: Dissolved

## 3.2 Diagnostics Plots<a id="diagnostics-plots"></a>

Below you find the goodness-of-fit visual diagnostic plots for the PBPK model performance of all data used presented in [Section 2.2.2](#222-clinical-data).

The first plot shows observed versus simulated plasma concentration, the second weighted residuals versus time. 

<a id="table-3-1"></a>

**Table 3-1: GMFE for Goodness of fit plot for concentration in plasma**

|Group                      |GMFE |
|:--------------------------|:----|
|Intravenous administration |1.26 |
|Oral administration        |1.45 |
|All                        |1.32 |

<br>
<br>

<a id="figure-3-1"></a>

![](images/006_section_results-and-discussion/008_section_diagnostics-plots/2_gof_plot_predictedVsObserved.png)

**Figure 3-1: Goodness of fit plot for concentration in plasma**

<br>
<br>

<a id="figure-3-2"></a>

![](images/006_section_results-and-discussion/008_section_diagnostics-plots/3_gof_plot_residualsOverTime.png)

**Figure 3-2: Goodness of fit plot for concentration in plasma**

<br>
<br>

## 3.3 Concentration-Time Profiles<a id="ct-profiles"></a>

Simulated versus observed concentration-time profiles of all data listed in [Section 2.2.2](#222-clinical-data) are presented below.

### 3.3.1 Model Building<a id="model-building"></a>

<a id="figure-3-3"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/1_time_profile_plot_Alfentanil_Ferrier_1985__Alfentanil_iv_0_05_mg_kg.png)

**Figure 3-3: Ferrier 1985, Alfentanil iv 0.05 mg/kg - log**

<br>
<br>

<a id="figure-3-4"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/2_time_profile_plot_Alfentanil_Ferrier_1985__Alfentanil_iv_0_05_mg_kg.png)

**Figure 3-4: Ferrier 1985, Alfentanil iv 0.05 mg/kg - linear**

<br>
<br>

<a id="figure-3-5"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/3_time_profile_plot_Alfentanil_Kharasch_1997__Alfentanil_iv_0_02_mg_kg.png)

**Figure 3-5: Kharasch 1997, Alfentanil iv 0.02 mg/kg - log**

<br>
<br>

<a id="figure-3-6"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/4_time_profile_plot_Alfentanil_Kharasch_1997__Alfentanil_iv_0_02_mg_kg.png)

**Figure 3-6: Kharasch 1997, Alfentanil iv 0.02 mg/kg - lin**

<br>
<br>

<a id="figure-3-7"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/5_time_profile_plot_Alfentanil_Kharasch_2004__Alfentanil_iv_0_015_mg_kg.png)

**Figure 3-7: Kharasch 2004, Alfentanil iv 0.015 mg/kg - log**

<br>
<br>

<a id="figure-3-8"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/6_time_profile_plot_Alfentanil_Kharasch_2004__Alfentanil_iv_0_015_mg_kg.png)

**Figure 3-8: Kharasch 2004, Alfentanil iv 0.015 mg/kg - lin**

<br>
<br>

<a id="figure-3-9"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/7_time_profile_plot_Alfentanil_Kharasch_2004__Alfentanil_po_0_06_mg_kg.png)

**Figure 3-9: Kharasch 2004, Alfentanil po 0.06 mg/kg - log**

<br>
<br>

<a id="figure-3-10"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/8_time_profile_plot_Alfentanil_Kharasch_2004__Alfentanil_po_0_06_mg_kg.png)

**Figure 3-10: Kharasch 2004, Alfentanil po 0.06 mg/kg - lin**

<br>
<br>

<a id="figure-3-11"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/9_time_profile_plot_Alfentanil_Kharasch_2011__Alfentanil_iv_0_015_mg_kg.png)

**Figure 3-11: Kharasch 2011, Alfentanil iv 0.015 mg/kg - log**

<br>
<br>

<a id="figure-3-12"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/10_time_profile_plot_Alfentanil_Kharasch_2011__Alfentanil_iv_0_015_mg_kg.png)

**Figure 3-12: Kharasch 2011, Alfentanil iv 0.015 mg/kg - lin**

<br>
<br>

<a id="figure-3-13"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/11_time_profile_plot_Alfentanil_Kharasch_2011__Alfentanil_po_0_075_mg_kg.png)

**Figure 3-13: Kharasch 2011, Alfentanil po 0.075 mg/kg - log**

<br>
<br>

<a id="figure-3-14"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/12_time_profile_plot_Alfentanil_Kharasch_2011__Alfentanil_po_0_075_mg_kg.png)

**Figure 3-14: Kharasch 2011, Alfentanil po 0.075 mg/kg - lin**

<br>
<br>

<a id="figure-3-15"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/13_time_profile_plot_Alfentanil_Kharasch_2011b__Alfentanil_IV_1_mg.png)

**Figure 3-15: Kharasch 2011b, Alfentanil IV 1 mg - log**

<br>
<br>

<a id="figure-3-16"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/14_time_profile_plot_Alfentanil_Kharasch_2011b__Alfentanil_IV_1_mg.png)

**Figure 3-16: Kharasch 2011b, Alfentanil IV 1 mg - lin**

<br>
<br>

<a id="figure-3-17"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/15_time_profile_plot_Alfentanil_Kharasch_2011b__Alfentanil_PO_4_mg.png)

**Figure 3-17: Kharasch 2011b, Alfentanil PO 4 mg - log**

<br>
<br>

<a id="figure-3-18"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/16_time_profile_plot_Alfentanil_Kharasch_2011b__Alfentanil_PO_4_mg.png)

**Figure 3-18: Kharasch 2011b, Alfentanil PO 4 mg - lin**

<br>
<br>

<a id="figure-3-19"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/21_time_profile_plot_Alfentanil_Meistelman_1987__20_g_kg__adult_male_individual.png)

**Figure 3-19: Meistelman 1987, 20µg/kg, adult male individual - log**

<br>
<br>

<a id="figure-3-20"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/22_time_profile_plot_Alfentanil_Meistelman_1987__20_g_kg__adult_male_individual.png)

**Figure 3-20: Meistelman 1987, 20µg/kg, adult male individual - lin**

<br>
<br>

<a id="figure-3-21"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/23_time_profile_plot_Alfentanil_Phimmasone_2001__Alfentanil_iv_0_015_mg_kg.png)

**Figure 3-21: Phimmasone 2001, Alfentanil iv 0.015 mg/kg - log**

<br>
<br>

<a id="figure-3-22"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/24_time_profile_plot_Alfentanil_Phimmasone_2001__Alfentanil_iv_0_015_mg_kg.png)

**Figure 3-22: Phimmasone 2001, Alfentanil iv 0.015 mg/kg - lin**

<br>
<br>

### 3.3.2 Model Verification<a id="model-verification"></a>

<a id="figure-3-23"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/17_time_profile_plot_Alfentanil_Kharasch_2012__Alfentanil_iv_0_02_mg_kg.png)

**Figure 3-23: Kharasch 2012, Alfentanil iv 0.02 mg/kg - log**

<br>
<br>

<a id="figure-3-24"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/18_time_profile_plot_Alfentanil_Kharasch_2012__Alfentanil_iv_0_02_mg_kg.png)

**Figure 3-24: Kharasch 2012, Alfentanil iv 0.02 mg/kg - lin**

<br>
<br>

<a id="figure-3-25"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/19_time_profile_plot_Alfentanil_Kharasch_2012__Alfentanil_po_0_043_mg_kg.png)

**Figure 3-25: Kharasch 2012, Alfentanil po 0.043 mg/kg - log**

<br>
<br>

<a id="figure-3-26"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/20_time_profile_plot_Alfentanil_Kharasch_2012__Alfentanil_po_0_043_mg_kg.png)

**Figure 3-26: Kharasch 2012, Alfentanil po 0.043 mg/kg - lin**

<br>
<br>

# 4 Conclusion<a id="conclusion"></a>

The herein presented PBPK model adequately describes the pharmacokinetics of alfentanil after iv and oral administration of a variety of doses to healthy adults. Parameters that were optimized during parameter identification are in a close range to the measured or calculated values and, consistent with literature, no additional active processes were needed to describe the PK of alfentanil.

In conclusion, the presented alfentanil PBPK model is well-suited to be applied in drug-drug-interaction scenarios to predict the interaction potential. 

# 5 References<a id="main-references"></a>

**Almond 2016** Almond, L.M. et al. Prediction of drug-drug interactions arising from CYP3A induction using a physiologically based dynamic model. Drug Metab. Dispos. 44, 821–32 (2016).

**Baneyx 2014** Baneyx, G., Parrott, N., Meille, C., Iliadis, A. & Lavé, T. Physiologically based pharmacokinetic modeling of CYP3A4 induction by rifampicin in human: influence of time between substrate and inducer administration. Eur. J. Pharm. Sci. 56, 1–15 (2014).

**DrugBank DB00802** https://www.drugbank.ca/drugs/DB00802, accessed 05-15-2020.

**Edginton 2008** Edginton, A.N. & Willmann, S. Physiology-based simulations of a pathological condition: prediction of pharmacokinetics in patients with liver cirrhosis. Clin. Pharmacokinet. 47, 743–52 (2008).

**Ferrier 1985** Ferrier, C. et al. Alfentanil pharmacokinetics in patients with cirrhosis. Anesthesiology 62, 480–484 (1985).

**Gertz 2010** Gertz, M., Harrison, A., Houston, J. B., & Galetin, A. (2010). Prediction of human intestinal first-pass metabolism of 25 CYP3A substrates from in vitro clearance and permeability data. Drug Metab. Dispos. 38, 1147-1158 (2010).

**Hanke 2018** Hanke N, Frechen S, Moj D, Britz H, Eissing T, Wendl T, Lehr T. PBPK  Models for CYP3A4 and P-gp DDI Prediction: A Modeling Network of  Rifampicin, Itraconazole, Clarithromycin, Midazolam, Alfentanil, and  Digoxin. CPT Pharmacometrics Syst Pharmacol. 2018 Oct;7(10):647-659. doi: 10.1002/psp4.12343. Epub 2018 Sep 7.

**Jansson 2008** Jansson, R., Bredberg, U. & Ashton, M. Prediction of drug tissue to plasma concentration ratios using a measured volume of distribution in combination with lipophilicity. J. Pharm. Sci. 97, 2324–39 (2008).

**Kharasch 1997** Kharasch, E.D. et al. The role of cytochrome P450 3A4 in alfentanil clearance. Implications for interindividual variability in disposition and perioperative drug interactions. Anesthesiology 87, 36–50 (1997).

**Kharasch 2004** Kharasch, E.D., Walker, A., Hoffer, C. & Sheffels, P. Intravenous and oral alfentanil as in vivo probes for hepatic and first-pass cytochrome P450 3A activity: noninvasive assessment by use of pupillary miosis. Clin. Pharmacol. Ther. 76, 452–66 (2004).

**Kharasch 2011** Kharasch, E.D. et al. Sensitivity of intravenous and oral alfentanil and pupillary miosis as minimal and noninvasive probes for hepatic and first-pass CYP3A induction. Clin. Pharmacol. Ther. 90, 100–8 (2011).

**Kharasch 2011b** Kharasch ED, Vangveravong S, Buck N, London A, Kim T, Blood J, Mach RH. Concurrent assessment of hepatic and intestinal cytochrome P450 3A activities using deuterated alfentanil. Clin Pharmacol Ther. 2011 Apr;89(4):562-70. doi: 10.1038/clpt.2010.313. Epub 2011 Feb 23. 

**Kharasch 2012** Kharasch ED, Whittington D, Ensign D, Hoffer C, Bedynek PS, Campbell S, Stubbert K, Crafford A, London A, Kim T. Mechanism of efavirenz influence on methadone pharmacokinetics and pharmacodynamics. Clin Pharmacol Ther. 2012 Apr;91(4):673-84. doi: 10.1038/clpt.2011.276. Epub 2012 Mar 7.

**Kuepfer 2016** Kuepfer L, Niederalt C, Wendl T, Schlender JF, Willmann S, Lippert J, Block M, Eissing T, Teutonico D. Applied Concepts in PBPK Modeling: How to Build a PBPK/PD Model.CPT Pharmacometrics Syst Pharmacol. 2016 Oct;5(10):516-531. doi: 10.1002/psp4.12134. Epub 2016 Oct 19.

**Meistelman 1987** Meistelman C, Saint-Maurice C, Lepaul M, Levron JC, Loose JP, Mac Gee K. A comparison of alfentanil pharmacokinetics in children and adults. Anesthesiology. 1987 Jan;66(1):13-6. PubMed PMID: 3099603.

**Meuldermans 1988** Meuldermans, W. et al. Alfentanil pharmacokinetics and metabolism in humans. Anesthesiology 69, 527–534 (1988).

**Meyer 2012** Meyer M, Schneckener S, Ludewig B, Kuepfer L, Lippert J. Using expression data for quantification of active processes in physiologically based pharmacokinetic modeling. Drug Metab Dispos. 2012 May;40(5):892-901.

**Nishimura 2013** Nishimura M, Yaguti H, Yoshitsugu H, Naito S, Satoh T. Tissue distribution of mRNA expression of human cytochrome P450 isoforms assessed by high-sensitivity real-time reverse transcription PCR. Yakugaku Zasshi. 2003 May;123(5):369-75.

**Phimmasone 2001** Phimmasone, S. & Kharasch, E.D. A pilot evaluation of alfentanil-induced miosis as a noninvasive probe for hepatic cytochrome P450 3A4 (CYP3A4) activity in humans. Clin. Pharmacol. Ther. 70, 505–17 (2001).

**PK-Sim Ontogeny Database Version 7.3** (https://github.com/Open-Systems-Pharmacology/OSPSuite.Documentation/blob/38cf71b384cfc25cfa0ce4d2f3addfd32757e13b/PK-Sim%20Ontogeny%20Database%20Version%207.3.pdf)	

**Wandel 2002** Wandel, C., Kim, R., Wood, M. & Wood, A. Interaction of morphine, fentanyl, sufentanil, alfentanil, and loperamide with the efflux drug transporter P-glycoprotein. Anesthesiology 96, 913–920 (2002).

**Willmann 2007** Willmann S, Höhn K, Edginton A, Sevestre M, Solodenko J, Weiss W, Lippert J, Schmitt W. Development of a physiology-based whole-body population model for assessing the influence of individual variability on the pharmacokinetics of drugs. J Pharmacokinet Pharmacodyn. 2007, 34(3): 401-431.

