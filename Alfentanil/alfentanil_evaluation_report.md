# Building and Evaluation of a PBPK Model for alfentanil in Adults



| Version                                         | 2.1-OSP9.1                                                   |
| ----------------------------------------------- | ------------------------------------------------------------ |
| based on *Model Snapshot* and *Evaluation Plan* | https://github.com/Open-Systems-Pharmacology/Alfentanil-Model/releases/tag/v2.1 |
| OSP Version                                     | 9.1                                                          |
| Qualification Framework Version                 | 2.2                                                          |





This evaluation report and the corresponding PK-Sim project file are filed at:

https://github.com/Open-Systems-Pharmacology/OSP-PBPK-Model-Library/
# Table of Contents
  * [1 Introduction](#1-introduction)
  * [2 Methods](#2-methods)
    * [2.1 Modeling Strategy](#21-modeling-strategy)
    * [2.2 Data](#22-data)
    * [2.3 Model Parameters and Assumptions](#23-model-parameters-and-assumptions)
  * [3 Results and Discussion](#3-results-and-discussion)
    * [3.1 Final input parameters](#31-final-input-parameters)
    * [3.2 Diagnostics Plots](#32-diagnostics-plots)
    * [3.3 Concentration-Time Profiles](#33-concentration-time-profiles)
      * [3.3.1 Model Building](#331-model-building)
      * [3.3.2 Model Verification](#332-model-verification)
  * [4 Conclusion](#4-conclusion)
  * [5 References](#5-references)
# 1 Introduction
Alfentanil is a potent analgesic synthetic opioid. It is fast but short-acting and used for anesthesia during surgery. Alfentanil is metabolized solely by CYP3A4 ([Phimmasone 2001](#5-References)). Like midazolam, alfentanil is not a substrate for P-gp ([Wandel 2002](#5-References)) and less than 1% of an alfentanil dose is excreted unchanged in urine ([Meuldermans 1988](#5-References)).

Although in clinical use alfentanil is always administered intravenously (iv), some DDI studies published plasma concentration-time profiles of alfentanil following oral ingestion. The presented alfentanil model was established using clinical PK data of 8 publications, covering iv and oral (po) administration and a dosing range from 0.015 to 0.075 mg/kg as well as absolute doses of 1 mg iv and 4 mg po. The established model is based on the model developed by Hanke *et al.* ([Hanke 2018](#5-References)) and applies metabolism by CYP3A4 and glomerular filtration.  

# 2 Methods


## 2.1 Modeling Strategy
The general concept of building a PBPK model has previously been described by e.g. Kuepfer et al. ([Kuepfer 2016](#5-References)). The relevant anthropometric (height, weight) and physiological information (e.g. blood flows, organ volumes, binding protein concentrations, hematocrit, cardiac output) in adults was gathered from the literature and has been previously published ([Willmann 2007](#5-References)). This information was incorporated into PK-Sim® and was used as default values for the simulations in adults.

Variability of plasma proteins and CYP3A4 are integrated into PK-Sim® and described in the publicly available PK-Sim® Ontogeny Database Version 7.3 ([PK-Sim Ontogeny Database Version 7.3](#5-References)) or otherwise referenced for the specific process.

First, a base mean model was built using clinical data including selected single dose studies with intravenous and oral applications (solution) of alfentanil to find an appropriate structure to describe the pharmacokinetics in plasma. The mean PBPK model was developed using a typical European individual. The relative tissue specific expressions of enzymes predominantly being involved in the metabolism of alfentanil were included in the model as described elsewhere ([Meyer 2012](#5-References)).

Unknown parameters (see below) were identified using the Parameter Identification module provided in PK-Sim®. Structural model selection was mainly guided by visual inspection of the resulting description of data and biological plausibility.

Details about input data (physicochemical, *in vitro* and clinical) can be found in [Section 2.2](#22-Data).

Details about the structural model and its parameters can be found in [Section 2.3](#23-Model-Parameters-and-Assumptions).


## 2.2 Data
### 2.2.1 In vitro / physicochemical Data

A literature search was performed to collect available information on physicochemical properties of alfentanil. The obtained information from literature is summarized in the table below. 

| **Parameter**   | **Unit** | **Value**  | Source                            | **Description**                                           |
| :-------------- | -------- | ---------- | --------------------------------- | --------------------------------------------------------- |
| MW              | g/mol    | 416.52     | [DrugBank DB00802](#5-References) | Molecular weight                                          |
| pK<sub>a</sub>  |          | 6.5 (base) | [Jansson 2008](#5-References)     | Acid dissociation constant                                |
| Solubility (pH) | mg/L     | 992 (6.5)  | [Baneyx 2014](#5-References)      | Solubility                                                |
| logD            |          | 2.1        | [Baneyx 2014](#5-References)      | Partition coefficient between octanol and water at pH 7.4 |
|                 |          | 2.2        | [Jansson 2008](#5-References)     | Partition coefficient between octanol and water           |
| fu              | %        | 8.6        | [Gertz 2010](#5-References)       | Fraction unbound in plasma                                |
|                 |          | 10.0       | [Edginton 2008](#5-References)    | Fraction unbound in plasma                                |
|                 |          | 12.0       | [Almond 2016](#5-References)      | Fraction unbound in plasma                                |


### 2.2.2 Clinical Data

A literature search was performed to collect available clinical data on alfentanil in healthy adults.

#### 2.2.2.1 Model Building

The following studies were used for model building:

| Publication                      | Arm / Treatment / Information used for model building        |
| :------------------------------- | :----------------------------------------------------------- |
| [Ferrier 1985](#5-References)    | Healthy subjects with a single iv dose of 0.05 mg/kg         |
| [Kharasch 1997](#5-References)   | Healthy subjects with a single iv dose of 0.02 mg/kg         |
| [Kharasch 2004](#5-References)   | Healthy subjects with a single iv dose of 0.015 mg/kg, healthy subjects with a single oral dose of 0.06 mg/kg |
| [Kharasch 2011](#5-References)   | Healthy subjects with a single iv dose of 0.015 mg/kg, healthy subjects with a single oral dose of 0.075 mg/kg |
| [Kharasch 2011b](#5-References)  | Healthy subjects with an iv dose of 1 mg, healthy subjects with an oral dose of 1 mg. Publication compares sequential and simultaneous dosing of oral deuterated and intravenous unlabeled alfentanil. Furthermore, IV and oral administration of alfentanil is combined with grapefruit juice. Grapefruit juice is considered to have no effect on hepatic clearance, and, hence, no effect on IV administered alfentanil |
| [Kharasch 2012](#5-References)   | Healthy subjects with a single iv dose of 0.02 mg/kg, healthy subjects with a single oral dose of 0.043 mg/kg |
| [Meistelman 1987](#5-References) | Healthy subjects with a single iv dose of 0.02 mg/kg         |
| [Phimmasone 2001](#5-References) | Healthy subjects with a single iv dose of 0.015 mg/kg        |

## 2.3 Model Parameters and Assumptions
### 2.3.1 Absorption

Absorption observed in clinical studies can be fully explained by passive absorption.

### 2.3.2 Distribution

After testing the available organ-plasma partition coefficient and cell permeability calculation methods built in PK-Sim, observed clinical data was best described by choosing the partition coefficient calculation by `Rodgers and Rowland` and cellular permeability calculation by `PK-Sim Standard`. 

### 2.3.3 Metabolism and Elimination

Alfentanil is metabolized solely by CYP3A4. The tissue-specific CYP3A4 expression implemented in the model is based on high-sensitive real-time RT-PCR ([Nishimura 2013](#5-References)). 

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


# 3 Results and Discussion
The PBPK model for alfentanil was developed and evaluated using publically available, clinical pharmacokinetic data from studies listed in [Section 2.2.2](#222-Clinical-Data).

The next sections show:

1. the final model parameters for the building blocks: [Section 3.1](#31-Final-Input-Parameters).
2. the overall goodness of fit: [Section 3.2](#32-Diagnostics-Plots).
3. simulated vs. observed concentration-time profiles for the clinical studies used for model building and for model verification: [Section 3.3](#33-Concentration-Time-Profiles).


## 3.1 Final input parameters
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

## 3.2 Diagnostics Plots
Below you find the goodness-of-fit visual diagnostic plots for the PBPK model performance of all data used presented in [Section 2.2.2](#222-Clinical-Data).

The first plot shows observed versus simulated plasma concentration, the second weighted residuals versus time. 


![001_plotGOFMergedPredictedVsObserved.png](images/003_3_Results_and_Discussion/002_3_2_Diagnostics_Plots/001_plotGOFMergedPredictedVsObserved.png)

![002_plotGOFMergedResidualsOverTime.png](images/003_3_Results_and_Discussion/002_3_2_Diagnostics_Plots/002_plotGOFMergedResidualsOverTime.png)

GMFE = 1.316003 

## 3.3 Concentration-Time Profiles
Simulated versus observed concentration-time profiles of all data listed in [Section 2.2.2](#222-Clinical-Data) are presented below.


### 3.3.1 Model Building





![001_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/001_plotTimeProfile.png)

![002_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/002_plotTimeProfile.png)

![003_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/003_plotTimeProfile.png)

![004_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/004_plotTimeProfile.png)

![005_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/005_plotTimeProfile.png)

![006_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/006_plotTimeProfile.png)

![007_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/007_plotTimeProfile.png)

![008_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/008_plotTimeProfile.png)

![009_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/009_plotTimeProfile.png)

![010_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/010_plotTimeProfile.png)

![011_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/011_plotTimeProfile.png)

![012_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/012_plotTimeProfile.png)

![013_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/013_plotTimeProfile.png)

![014_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/014_plotTimeProfile.png)

![015_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/015_plotTimeProfile.png)

![016_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/016_plotTimeProfile.png)

![017_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/017_plotTimeProfile.png)

![018_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/018_plotTimeProfile.png)

![019_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/019_plotTimeProfile.png)

![020_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_3_3_1_Model_Building/020_plotTimeProfile.png)

### 3.3.2 Model Verification





![001_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/002_3_3_2_Model_Verification/001_plotTimeProfile.png)

![002_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/002_3_3_2_Model_Verification/002_plotTimeProfile.png)

![003_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/002_3_3_2_Model_Verification/003_plotTimeProfile.png)

![004_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/002_3_3_2_Model_Verification/004_plotTimeProfile.png)

# 4 Conclusion
The herein presented PBPK model adequately describes the pharmacokinetics of alfentanil after iv and oral administration of a variety of doses to healthy adults. Parameters that were optimized during parameter identification are in a close range to the measured or calculated values and, consistent with literature, no additional active processes were needed to describe the PK of alfentanil.

In conclusion, the presented alfentanil PBPK model is well-suited to be applied in drug-drug-interaction scenarios to predict the interaction potential. 

# 5 References
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
