# Building and evaluation of a PBPK model for alprazolam in healthy adults





| Version                                         | 1.0-OSP9.1                                                   |
| ----------------------------------------------- | ------------------------------------------------------------ |
| based on *Model Snapshot* and *Evaluation Plan* | https://github.com/Open-Systems-Pharmacology/Alprazolam-Model/releases/tag/v1.0 |
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
  * [4 Conclusion](#4-conclusion)
  * [5 References](#5-references)
# 1 Introduction
The presented model building and evaluation report evaluates the performance of a PBPK model for alprazolam in healthy adults.

Alprazolam, sold under the trade names Xanax and Solanax, among others, belongs to the group of benzodiazepines and is commonly used in short term management of anxiety disorders. It is generally administered orally as immediate release or extended release tablet, but other forms are also available, e.g. solution or sublingual tablet.

Following oral administration, alprazolam is rapidly absorbed with an absolute bioavailability ranging from 80% to 100% ([Greenblatt 1993](#5-References)). Absorption is independent of the dose and the relative bioavailability of solid and liquid dosage forms has been observed to be similar ([Dawson 1984](#5-References)). Alprazolam is widely distributed throughout the body and its free fraction in plasma, averaging around 30%, is not influenced by total alprazolam concentrations within the tested range of 0.01 to 10 mg/L ([Moschitto 1983](#5-References)). Alprazolam is extensively metabolized to various metabolites ([von Moltke 1993](#5-References)). The two major metabolites, α-hydroxy-alprazolam and 4-hydroxy-alprazolam, are formed through oxidation catalyzed by CYP3A ([Eberts 1980](#5-References), [von Moltke 1993](#5-References)). Within 72 h of a 2 mg oral dose of <sup>14</sup>C-alprazolam, 20% of the dose have been observed to be excreted unchanged in urine ([Eberts 1980](#5-References)). Alprazolam displays dose linear pharmacokinetics and does not accumulate during multiple dose treatment ([Dawson 1984](#5-References), [Greenblatt 1993](#5-References)). Because of the predominant role of CYP3A4 in alprazolam elimination, alprazolam is often used as victim compound in drug-drug interaction (DDI) studies.

The presented alprazolam PBPK model was developed for intravenous (IV) administration and oral (PO) administration of the immediate release tablet (Xanax) or extended-release formulation (Solanax) given in fasted state in healthy, non-obese adults; administration in fed state was not addressed here.




# 2 Methods

## 2.1 Modeling Strategy
The general workflow for building an adult PBPK model has been described by Kuepfer et al. ([Kuepfer 2016](#5-References)). Relevant information on the anthropometry (height, weight) was gathered from the respective clinical study, if reported. Information on physiological parameters (e.g. blood flows, organ volumes, hematocrit) in adults was gathered from the literature and has been incorporated in PK-Sim<sup>®</sup>) as described previously ([Willmann 2007](#5-References)). The  applied activity and variability of plasma proteins and active processes that are integrated into PK-Sim® are described in the publicly available 'PK-Sim<sup>®</sup> Ontogeny Database Version 7.3' ([PK-Sim Ontogeny Database Version 7.3](#5-References)).

The PBPK model was developed based on clinical data of healthy, non-obese, adult subjects obtained from the literature, covering different single doses of alprazolam administered via the intravenous (IV) or oral (PO) route in the fasted state. Several oral dosage forms were included in the model building process, such as Xanax<sup>®</sup> and Solanax<sup>®</sup> tablets. Comparison of the reported alprazolam plasma concentration-time profiles following administration of Xanax<sup>®</sup> and Solanax<sup>®</sup> tablets indicated that the latter oral dosage form yields a larger t<sub>max</sub> than the Xanax<sup>®</sup> immediate release formulation. Therefore, different dissolution kinetics were developed for these two oral dosage forms. The reported PK profiles following administration of Solanax<sup>®</sup> tablets were measured in Japanese subjects ([Yasui 1996](#5-References), [Yasui 1998](#5-References), [Yasui 2000](#5-References)). To account for ethnicity-related differences in anatomical and physiological model parameters, the European Standard Individual used per default in the simulations was scaled to a Japanese individual and the reference concentration of CYP3A4 in this individual was optimized to better match the clinical data. Finally, mass balance information on urinary excretion of unchanged <sup>14</sup>C-alprazolam after PO administration reported by  Eberts et al. ([Eberts 1980](#5-References)) was also accounted for during the model building process. 

Unknown parameters were simultaneously optimized using all available PK data, in particular:

-  2 plasma concentration-time profiles following single IV administration of 0.25 mg
-  2 plasma concentration-time profiles following single IV administration of 0.5 mg
-  3 plasma concentration-time profiles following single IV administration of 1 mg
-  1 plasma concentration-time profile following single IV administration of 1 mg followed by 1.576 mg over 8 h
-  2 plasma concentration-time profiles following single IV administration of 2 mg
-  3 plasma concentration-time profiles following single IV administration of 4 mg
- 2 plasma concentration-time profiles following single PO administration of 0.5 mg
- 3 plasma concentration-time profiles following single PO administration of Solanax<sup>®</sup> tablets containing 0.8 mg alprazolam to Japanese subjects
- 12 plasma concentration-time profiles following single PO administration of 1 mg
- 1 plasma concentration-time profile following single PO administration of 2 mg
- 1 dose fraction excreted unchanged in urine following single PO administration of 2 mg

Structural model selection was mainly guided by visual inspection of the resulting description of data and biological plausibility. The following parameters were identified using the Parameter Identification module provided in PK-Sim<sup>®</sup> and MoBi<sup>®</sup> ([Open Systems Pharmacology Documentation](#5-References)):

- `Dissolution time (50% dissolved)`
- `Dissolution shape`
- `Specific intestinal permeability`
- `Mucosa permeability (interstitial<->intracellular)`
- `Lipophilicity`
- `Metabolizing Enzyme - CYP3A4 - kcat`
- `Reference concentration CYP3A4` (only for Japanese subjects)
- `GFR fraction`

Details about input data (physicochemical, *in vitro* and clinical) can be found in [Section 2.2](#22-Data).

Details about the structural model and its parameters can be found in [Section 2.3](#23-Model-Parameters-and-Assumptions).






## 2.2 Data
### 2.2.1 In vitro / physicochemical data

A literature search was carried out to collect available information on physicochemical properties of alprazolam. The obtained information from the literature is summarized in the table below and is used for model building.

| **Parameter**             | **Unit** | **Literature**                                               | **Description**                                              |
| :------------------------ | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Molecular weight          | g/mol    | 308.765 ([drugbank.ca](#5-References))                       | Molecular weight                                             |
| pK<sub>a</sub> (basic)    |          | 2.40 ([Cho 1983](#5-References), [Raymond 1986](#5-References)); 2.48 ± 0.01 ([Manchester 2018](#5-References)) | Acid dissociation constant                                   |
| logP                      |          | 2.19 ([Machatha 2004](#5-References))                        | Partition coefficient between octanol and water              |
| logD                      |          | 1.26 ([Greenblatt 1983](#5-References))                      | Partition coefficient between octanol and water at physiological pH |
| f<sub>u</sub>             |          | 0.20 ([Eberts 1980](#5-References)); 0.233 ± 0.028<sup>a</sup> ([Schmith 1991](#5-References)); 0.270 ± 0.017<sup>a</sup> ([Scavone 1988](#5-References)); 0.284 ± 0.017<sup>a</sup> ([Scavone 1988](#5-References)); 0.290 ± 0.025<sup>a</sup> ([Juhl 1984](#5-References)); 0.298 [0.259 - 0.316]<sup>b</sup> ([Abernethy 1983](#5-References)); 0.311 ± 0.026<sup>a</sup> ([Ochs 1986](#5-References)); 0.316<sup>c</sup> ([Moschitto 1983](#5-References)) | Fraction unbound in human plasma of healthy adults           |
| Water solubility (pH 1.2) | mg/L     | 12 ([drugbank.ca](#5-References))                            | Estimated solubility in water at pH 1.2                      |
| Water solubility (pH 7.0) | mg/L     | 40 ([drugbank.ca](#5-References))                            | Estimated solubility in water at pH 7.0                      |
| Water solubility          | mg/L     | 73 ([Loftsson 2006](#5-References))                          | Experimentally measured solubility in water at 22°C - 24°C   |

<sup>a</sup> mean ± SD

<sup>b</sup> mean [range]

<sup>c</sup> mean

### 2.2.2 Clinical data

A literature search was carried out to collect alprazolam PK data in healthy adults. 

The following publications were found and used for model building and evaluation:

| Publication                            | Study description                                            |
| :------------------------------------- | :----------------------------------------------------------- |
| [Adams 1984](#5-References)            | IV single dose administration of 0.25 mg and 4 mg            |
| [Bertz 1997](#5-References)           | IV single dose administration of 2 mg (young subjects group) |
| [Eberts 1980](#5-References)          | PO single dose administration of 2 mg <sup>14</sup>C-alprazolam (no plasma concentration-time profile was reported, but the dose fraction excreted unchanged in urine was quantified) |
| [Eller 1990](#5-References)           | PO single dose administration of 1 mg (Treatment C: IR tablet in fasted state) |
| [Fleishaker 1989](#5-References)      | IV single dose administration of 1 mg (Treatment A)          |
| [Fleishaker 1994](#5-References)      | PO multiple dose administration of 1 mg four times daily at irregular time intervals for 4 days (Control phase) |
| [Friedman 1991](#5-References)        | PO single dose administration of 1 mg                        |
| [Greenblatt 1988](#5-References)      | PO single dose administration of 1 mg                        |
| [Greenblatt 1992](#5-References)      | PO single dose administration of 1 mg (Control phase)        |
| [Greenblatt 1998](#5-References)      | PO single dose administration of 1 mg (Trial A)              |
| [Greenblatt 2000](#5-References)      | PO single dose administration of 1 mg (Control group)        |
| [Juhl 1984](#5-References)            | PO single dose administration of 1 mg (Healthy control group) |
| [Kaplan 1998](#5-References)          | PO single dose administration of 1 mg (young subjects group) |
| [Kirkwood 1991](#5-References)        | PO single dose administration of 1 mg                        |
| [Kroboth 1988](#5-References)         | IV single dose administration of 0.5 mg, 1 mg followed by 72 µg over 8 h, and 2 mg |
| [Lin 1988](#5-References)             | IV single dose administration of 0.5 mg and PO single dose administration of 0.5 mg |
| [Schmider 1999](#5-References)        | PO single dose administration of 1 mg (Control phase)        |
| [Schmith 1991](#5-References)         | PO single dose administration of 0.5 mg and 2 mg (normal subjects group) |
| [Smith 1984](#5-References)           | IV single dose administration of 1 mg and PO single dose administration of 1 mg |
| [Venkatakrishnan 2005](#5-References) | IV single dose administration of 1 mg                        |
| [Wennerholm 2005](#5-References)      | PO single dose administration of 1 mg                        |
| [Yasui 1996](#5-References)           | PO single dose administration of 0.8 mg (Control phase)      |
| [Yasui 1998](#5-References)           | PO single dose administration of 0.8 mg (Control phase)      |
| [Yasui 2000](#5-References)           | PO single dose administration of 0.8 mg (Control phase)      |


## 2.3 Model Parameters and Assumptions
### 2.3.1 Dissolution and absorption

Dissolution of the immediate release tablet of alprazolam was described by a Weibull function with the two parameters `Dissolution shape` and `Dissolution time (50% dissolved)` being fitted to observed PK data. As described in [Section 2.1](#21-Modeling-Strategy), different dissolution kinetics were developed for Xanax<sup>®</sup> and Solanax<sup>®</sup> formulations to allow a slower dissolution of the latter yielding a larger t<sub>max</sub>. Although alprazolam is sparingly soluble in water, no solubility limitation was observed in the model using a solubility value of 40 mg/L (pH 7.0). `Specific intestinal permeability (transcellular)` was also optimized to better match the observed PK data.

### 2.3.2 Distribution

In the model, the `fraction unbound (plasma, reference value)` was set to 0.233 which is the average value measured in young male subjects ([Schmith 1991](#5-References)). Slightly higher values around 0.30 have been reported for mid-aged subjects ([Juhl 1984](#5-References), [Ochs 1986](#5-References)) which have not been applied in the current model. `Lipophilicity` was optimized within the range of reported values for logP or logD, namely 1.26 ([Greenblatt 1983](#5-References)) - 2.19 ([Machatha 2004](#5-References)), to better match the observed PK data. The observed PK data were found to be best described using the model for estimating intracellular-to-plasma partition coefficients according to the method by `Rodgers and Rowland` ([Rodgers 2005](#5-References), [Rodgers 2006](#5-References)). Cellular permeabilities were automatically calculated using the method `PK-Sim Standard` ([Open Systems Pharmacology Documentation](#5-References)).  

### 2.3.3 Elimination

Alprazolam is extensively metabolized via CYP3A to give two major metabolites, α-hydroxy-alprazolam and 4-hydroxy-alprazolam. In the model, these two biotransformation pathways were described by Michaelis-Menten kinetics. The `Km` values for each pathway were fixed to reported literature values, namely 269 µmol/L for the α-OH pathway and 704 µmol/L for the 4-OH pathway ([Hirota 2001](#5-References)), and the `kcat` values were optimized to better match the observed PK data while keeping the ratio between both values constant (by selecting the option `Use as Factor`). The gene expression profile of CYP3A4 was loaded from the internal PK-Sim<sup>®</sup> database using the expression data quantified by RT-PCR ([Open Systems Pharmacology Documentation](#5-References)). As described in [Section 2.1](#21-Modeling-Strategy), the European Standard Individual used per default in the simulations was scaled to a Japanese individual with the `Reference concentration CYP3A4` being fitted to observed data reported by Yasui et al. ([Yasui 1996](#5-References), [Yasui 1998](#5-References), [Yasui 2000](#5-References)) to account for ethnicity-related differences in anatomical and physiological model parameters. 

Following oral administration of <sup>14</sup>C-alprazolam, 20% of the dose have been recovered unchanged in urine ([Eberts 1980](#5-References)). This information was accounted for in the model by implementing a glomerular filtration process and optimizing the `GFR fraction` to match the observed dose fraction excreted unchanged in urine. 
# 3 Results and Discussion
The PBPK model for alprazolam was developed and verified with clinical pharmacokinetic data.

The next sections show:

1. the final model parameters for the building blocks: [Section 3.1](#31-Final-Input-Parameters).
2. the overall goodness of fit: [Section 3.2](#32-Diagnostics-Plots).
3. simulated vs. observed concentration-time profiles for the clinical studies used for model building: [Section 3.3](#33-Concentration-Time-Profiles).


## 3.1 Final input parameters
The compound parameter values of the final PBPK model are illustrated below. 


### Compound: Alprazolam

#### Parameters

Name                                             | Value                  | Value Origin                                                                                                            | Alternative | Default
------------------------------------------------ | ---------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------- | -------
Solubility at reference pH                       | 40 mg/l                |                                                                                                                         | Measurement | True   
Reference pH                                     | 7                      |                                                                                                                         | Measurement | True   
Lipophilicity                                    | 2.0799268917 Log Units | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 3.4' on 2020-03-25 13:19 | Optimized   | True   
Fraction unbound (plasma, reference value)       | 0.233                  | Publication-In Vivo-PMID: 1880224                                                                                       | Measurement | True   
Specific intestinal permeability (transcellular) | 7.6146060669 cm/min    | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 3.4' on 2020-03-25 13:19 | Optimized   | True   
Cl                                               | 1                      |                                                                                                                         |             |        
Is small molecule                                | Yes                    |                                                                                                                         |             |        
Molecular weight                                 | 308.765 g/mol          |                                                                                                                         |             |        
Plasma protein binding partner                   | Unknown                |                                                                                                                         |             |        
#### Calculation methods

Name                    | Value              
----------------------- | -------------------
Partition coefficients  | Rodgers and Rowland
Cellular permeabilities | PK-Sim Standard    
#### Processes

##### Metabolizing Enzyme: CYP3A4-alpha-OH pathway

Molecule: CYP3A4
###### Parameters

Name                               | Value                          | Value Origin                                                                                                           
---------------------------------- | ------------------------------ | -----------------------------------------------------------------------------------------------------------------------
In vitro Vmax for liver microsomes | 0.131 nmol/min/mg mic. protein | Publication-In Vitro-PMID: 11745908                                                                                    
Km                                 | 269 µmol/l                     | Publication-In Vitro-PMID: 11745908                                                                                    
kcat                               | 0.8066945978 1/min             | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 3.4' on 2020-03-25 13:19
##### Systemic Process: Glomerular Filtration-GFR

Species: Human
###### Parameters

Name         |        Value | Value Origin                                                                                                           
------------ | ------------:| -----------------------------------------------------------------------------------------------------------------------
GFR fraction | 0.5461456402 | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 3.4' on 2020-03-25 13:19
##### Metabolizing Enzyme: CYP3A4-4-OH pathway

Molecule: CYP3A4
###### Parameters

Name                               | Value                         | Value Origin                                                                                                           
---------------------------------- | ----------------------------- | -----------------------------------------------------------------------------------------------------------------------
In vitro Vmax for liver microsomes | 2.23 nmol/min/mg mic. protein | Publication-In Vitro-PMID: 11745908                                                                                    
Km                                 | 704 µmol/l                    | Publication-In Vitro-PMID: 11745908                                                                                    
kcat                               | 13.7322820855 1/min           | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 3.4' on 2020-03-25 13:19

### Formulation: Solanax

Type: Weibull
#### Parameters

Name                             | Value             | Value Origin                                                                                                           
-------------------------------- | ----------------- | -----------------------------------------------------------------------------------------------------------------------
Dissolution time (50% dissolved) | 35.8519725483 min | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 3.4' on 2020-03-25 13:19
Lag time                         | 0 min             |                                                                                                                        
Dissolution shape                | 0.92              | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 3.4' on 2020-03-25 13:19
Use as suspension                | Yes               |                                                                                                                        

### Formulation: Xanax_IR

Type: Weibull
#### Parameters

Name                             | Value             | Value Origin                                                                                                           
-------------------------------- | ----------------- | -----------------------------------------------------------------------------------------------------------------------
Dissolution time (50% dissolved) | 12.1060809908 min | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 3.4' on 2020-03-25 13:19
Lag time                         | 0 min             |                                                                                                                        
Dissolution shape                | 0.92              | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 3.4' on 2020-03-25 13:19
Use as suspension                | Yes               |                                                                                                                        

## 3.2 Diagnostics Plots
Below you find the goodness-of-fit visual diagnostic plots for the PBPK model performance of all data used presented in [Section 2.2.2](#222-Clinical-Data).

The first plot shows observed versus simulated plasma concentration, the second weighted residuals versus time. 


![001_plotGOFMergedPredictedVsObserved.png](images/003_3_Results_and_Discussion/002_3_2_Diagnostics_Plots/001_plotGOFMergedPredictedVsObserved.png)

![002_plotGOFMergedResidualsOverTime.png](images/003_3_Results_and_Discussion/002_3_2_Diagnostics_Plots/002_plotGOFMergedResidualsOverTime.png)

GMFE = 1.181425 

## 3.3 Concentration-Time Profiles
Simulated versus observed concentration-time profiles of all data listed in [Section 2.2.2](#222-Clinical-data) are presented below.


![001_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/001_plotTimeProfile.png)

![002_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/002_plotTimeProfile.png)

![003_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/003_plotTimeProfile.png)

![004_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/004_plotTimeProfile.png)

![005_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/005_plotTimeProfile.png)

![006_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/006_plotTimeProfile.png)

![007_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/007_plotTimeProfile.png)

![008_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/008_plotTimeProfile.png)

![009_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/009_plotTimeProfile.png)

![010_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/010_plotTimeProfile.png)

![011_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/011_plotTimeProfile.png)

![012_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/012_plotTimeProfile.png)

![013_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/013_plotTimeProfile.png)

![014_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/014_plotTimeProfile.png)

![015_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/015_plotTimeProfile.png)

![016_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/016_plotTimeProfile.png)

![017_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/017_plotTimeProfile.png)

![018_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/018_plotTimeProfile.png)

![019_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/019_plotTimeProfile.png)

![020_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/020_plotTimeProfile.png)

![021_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/021_plotTimeProfile.png)

# 4 Conclusion
The final alprazolam PBPK model applies metabolism by CYP3A4, modelled as two separate pathways catalyzed by the same enzyme yielding α-hydroxy-alprazolam and 4-hydroxy-alprazolam as metabolites, and glomerular filtration. Overall, the model adequately describes the pharmacokinetics of alprazolam in healthy, non-obese adults receiving different single doses of alprazolam via the IV route or oral route as immediate release tablet in the fasted state.




# 5 References
**Abernethy 1983** Abernethy DR, Greenblatt DJ, Divoll M, Moschitto LJ, Harmatz JS, Shader RI. Interaction of cimetidine with the triazolobenzodiazepines alprazolam and triazolam. *Psychopharmacology (Berl)* 1983, 80(3): 275-278.

**Adams 1984** Adams WJ, Bombardt PA, Brewer JE. Normal-phase liquid chromatographic determination of alprazolam in human serum. *Anal Chem* 1984, 56(9): 1590-1594.

**Bertz 1997** Bertz RJ, Kroboth PD, Kroboth FJ, Reynolds IJ, Salek F, Wright CE, Smith RB. Alprazolam in young and elderly men: sensitivity and tolerance to psychomotor, sedative and memory effects. *J Pharmacol Exp Ther* 1997, 281(3): 1317-1329.

**Cho 1983** Cho MJ, Scahill TA, Hester JB Jr. Kinetics and equilibrium of the reversible alprazolam ring-opening reaction. *J Pharm Sci* 1983, 72(4): 356-362.

**Dawson 1984** Dawson GW, Jue SG, Brogden RN. Alprazolam: a review of its pharmacodynamic properties and efficacy in the treatment of anxiety and depression. *Drugs* 1984, 27(2): 132-147.

**drugbank.ca**. (https://www.drugbank.ca/drugs/DB00404), accessed on 11-19-2019.

**Eberts 1980** Eberts FS, Philopoulos Y, Reineke LM, Vliek RW. Disposition of 14-C-alprazolam, a new anxiolytic-antidepressant, in man. *Pharmacologist* 1980, 22(3): 279.

**Eller 1990** Eller MG, Della‐Coletta AA. Absence of effect of food on alprazolam absorption from sustained release tablets. *Biopharm Drug Dispos* 1990, 11(1): 31-37.

**Fleishaker 1989** Fleishaker JC, Phillips JP, Eller MG, Smith RB. Pharmacokinetics and pharmacodynamics of alprazolam following single and multiple oral doses of a sustained‐release formulation. *J Clin Pharmacol* 1989, 29(6): 543-549.

**Fleishaker 1994** Fleishaker JC, Hulst LK. A pharmacokinetic and pharmacodynamic evaluation of the combined administration of alprazolam and fluvoxamine. *Eur J Clin Pharmacol.* 1994, 46(1): 35-39.

**Friedman 1991** Friedman H, Redmond DE, Greenblatt DJ. Comparative pharmacokinetics of alprazolam and lorazepam in humans and in African Green Monkeys. *Psychopharmacology (Berl)* 1991, 104(1): 103-105.

**Greenblatt 1983** Greenblatt DJ, Arendt RM, Abernethy DR, Giles HG, Sellers EM, Shader RI. In vitro quantitation of benzodiazepine lipophilicity: relation to in vivo distribution. *Br J Anaesth* 1983, 55(10): 985-989.

**Greenblatt 1988** Greenblatt DJ, Harmatz JS, Dorsey C, Shader RI. Comparative single‐dose kinetics and dynamics of lorazepam, alprazolam, prazepam, and placebo. *Clin Pharmacol Ther* 1988, 44(3): 326-334.

**Greenblatt 1992** Greenblatt DJ, Preskorn SH, Cotreau MM, Horst WD, Harmatz JS. Fluoxetine impairs clearance of alprazolam but not of clonazepam. *Clin Pharmacol Ther* 1992, 52(5): 479-486.

**Greenblatt 1993** Greenblatt DJ, Wright CE. Clinical pharmacokinetics of alprazolam. Therapeutic implications. *Clin Pharmacokinet* 1993, 24(6): 453-471.

**Greenblatt 1998** Greenblatt DJ, Wright CE, von Moltke LL, Harmatz JS, Ehrenberg BL, Harrel LM, Corbett K, Counihan M, Tobias S, Shader RI. Ketoconazole inhibition of triazolam and alprazolam clearance: differential kinetic and dynamic consequences. *Clin Pharmacol Ther* 1998, 64(3): 237-247.

**Greenblatt 2000** Greenblatt DJ, von Moltke LL, Harmatz JS, Durol ALB, Daily JP, Graf JA, Mertzanis P, Hoffman JL, Shader RI. Alprazolam‐ritonavir interaction: implications for product labeling. *Clin Pharmacol Ther* 2000, 67(4): 335-341.

**Hirota 2001** Hirota N, Ito K, Iwatsubo T, Green CE, Tyson CA, Shimada N, Suzuki H, Sugiyama Y. In vitro/in vivo scaling of alprazolam metabolism by CYP3A4 and CYP3A5 in humans. *Biopharm Drug Dispos* 2001, 22(2): 53-71.

**Juhl 1984** Juhl RP, Van Thiel DH, Dittert LW, Smith RB. Alprazolam pharmacokinetics in alcoholic liver disease. *J Clin Pharmacol* 1984, 24(2-3): 113-119.

**Kaplan 1998** Kaplan GB, Greenblatt DJ, Ehrenberg BL, Goddard JE, Harmatz JS, Shader RI. Single‐dose pharmacokinetics and pharmacodynamics of alprazolam in elderly and young subjects. *J Clin Pharmacol* 1998, 38(1): 14-21.

**Kirkwood 1991** Kirkwood C, Moore A, Hayes P, DeVane CL, Pelonero A. Influence of menstrual cycle and gender on alprazolam pharmacokinetics. *Clin Pharmacol Ther* 1991, 50(4): 404-409.

**Kroboth 1988** Kroboth PD, Smith RB, Erb RJ. (1988). Tolerance to alprazolam after intravenous bolus and continuous infusion: psychomotor and EEG effects. Clinical Pharmacology & Therapeutics, 43(3), 270-277.

**Kuepfer 2016** Kuepfer L, Niederalt C, Wendl T, Schlender JF, Willmann S, Lippert J, Block M, Eissing T, Teutonico D. Applied concepts in PBPK modeling: how to build a PBPK/PD model. *CPT Pharmacometrics Syst Pharmacol* 2016, 5(10): 516-531.

**Lin 1988** Lin KM, Lau JK, Smith R, Phillips P, Antal E, Poland RE. Comparison of alprazolam plasma levels in normal Asian and Caucasian male volunteers. *Psychopharmacology (Berl)* 1988, 96(3): 365-369.

**Loftsson 2006** Loftsson T, Hreinsdôttir D. Determination of aqueous solubility by heating and equilibration: a technical note. *AAPS PharmSciTech* 2006, 7(1): E29-E32.

**Machatha 2004** Machatha SG, Yalkowsky SH. Estimation of the ethanol/water solubility profile from the octanol/water partition coefficient. *Int J Pharm* 2004, 286(1-2): 111-115.

**Manchester 2018** Manchester KR, Maskell PD, Waters L. Experimental versus theoretical log D7.4, pKa and plasma protein binding values for benzodiazepines appearing as new psychoactive substances. *Drug Test Anal* 2018, 10(8): 1258-1269.

**Moschitto 1983** Moschitto LJ, Greenblatt DJ. Concentration-independent plasma protein binding of benzodiazepines. *J Pharm Pharmacol* 1983, 35(3): 179-180.

**Ochs 1986** Ochs HR, Greenblatt DJ, Labedzki L, Smith RB. Alprazolam kinetics in patients with renal insufficiency. *J Clin Psychopharmacol* 1986, 6(5): 292-294.

**Open Systems Pharmacology Documentation**. (https://docs.open-systems-pharmacology.org/), accessed on 07-30-2019.

**PK-Sim Ontogeny Database Version 7.3**. (https://github.com/Open-Systems-Pharmacology/OSPSuite.Documentation/blob/38cf71b384cfc25cfa0ce4d2f3addfd32757e13b/PK-Sim%20Ontogeny%20Database%20Version%207.3.pdf), accessed on 07-30-2019.

**Raymond 1986** Raymond GG, Born JL. An updated pKa listing of medicinal compounds. *Drug Intell Clin Pharm* 1986, 20(9): 683-686.

**Scavone 1988** Scavone JM, Greenblatt DJ, Locniskar A, Shader RI. Alprazolam pharmacokinetics in women on low-dose oral contraceptives. *J Clin Pharmacol* 1988, 28(5): 454-457.

**Schmider 1999** Schmider J, Brockmöller J, Arold G, Bauer S, Roots I. Simultaneous assessment of CYP3A4 and CYP1A2 activity in vivo with alprazolam and caffeine. *Pharmacogenetics* 1999, 9(6): 725-734.

**Schmith 1991** Schmith VD, Piraino B, Smith RB, Kroboth PD. Alprazolam in end-stage renal disease: I. Pharmacokinetics. *J Clin Pharmacol* 1991, 31(6): 571-579.

**Smith 1984** Smith RB, Kroboth PD, Vanderlugt JT, Phillips JP, Juhl RP. Pharmacokinetics and pharmacodynamics of alprazolam after oral and IV administration. *Psychopharmacology (Berl)* 1984, 84(4): 452-456.

**Venkatakrishnan 2005** Venkatakrishnan K, Culm KE, Ehrenberg BL, Harmatz JS, Corbett KE, Fleishaker JC, Greenblatt DJ. Kinetics and dynamics of intravenous adinazolam, n‐desmethyl adinazolam, and alprazolam in healthy volunteers. *J Clin Pharmacol* 2005, 45(5): 529-537.

**von Moltke 1993** von Moltke LL, Greenblatt DJ, Harmatz JS, Shader RI. Alprazolam metabolism in vitro: studies of human, monkey, mouse, and rat liver microsomes. *Pharmacology* 1993, 47(4): 268-276.

**Wennerholm 2005** Wennerholm A, Allqvist A, Svensson JO, Gustafsson LL, Mirghani RA, Bertilsson L. Alprazolam as a probe for CYP3A using a single blood sample: pharmacokinetics of parent drug, and of α-and 4-hydroxy metabolites in healthy subjects. *Eur J Clin Pharmacol* 2005, 61(2): 113-118.

**Willmann 2007** Willmann S, Höhn K, Edginton A, Sevestre M, Solodenko J, Weiss W, Lippert J, Schmitt W. Development of a physiology-based whole-body population model for assessing the influence of individual variability on the pharmacokinetics of drugs. *J Pharmacokinet Pharmacodyn* 2007, 34(3): 401-431.

**Yasui 1996** Yasui N, Otani K, Kaneko S, Ohkubo T, Osanai T, Sugawara K, Chiba K, Ishizaki T. A kinetic and dynamic study of oral alprazolam with and without erythromycin in humans: in vivo evidence for the involvement of CYP3A4 in alprazolam metabolism. *Clin Pharmacol Ther.* 1996, 59(5): 514-519.

**Yasui 1998** Yasui N, Kondo T, Otani K, Furukori H, Kaneko S, Ohkubo T, Nagasaki T, Sugawara K. Effect of itraconazole on the single oral dose pharmacokinetics and pharmacodynamics of alprazolam. *Psychopharmacology* 1998, 139(3): 269-273.

**Yasui 2000** Yasui N, Kondo T, Furukori H, Kaneko S, Ohkubo T, Uno T, Osanai T, Sugawara K, Otani K. Effects of repeated ingestion of grapefruit juice on the single and multiple oral-dose pharmacokinetics and pharmacodynamics of alprazolam. *Psychopharmacology* 2000, 150(2): 185-190.
