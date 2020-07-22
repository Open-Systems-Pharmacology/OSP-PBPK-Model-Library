# Building and evaluation of a PBPK model for triazolam in healthy adults


| Version                                         | 1.0-OSP9.1                                                   |
| ----------------------------------------------- | ------------------------------------------------------------ |
| based on *Model Snapshot* and *Evaluation Plan* | https://github.com/Open-Systems-Pharmacology/Triazolam-Model/releases/tag/v1.0 |
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
The presented model building and evaluation report evaluates the performance of a PBPK model for triazolam in healthy adults.

Triazolam, sold under the trade name Halcion, among others, belongs to the group of benzodiazepines and is used for short-term treatment of insomnia and circadian rhythm sleep disorders. It is generally administered orally as immediate release tablet, but other forms of administrations, e.g. intravenously or as sublingual tablet, exist as well.

Following oral administration, triazolam is rapidly absorbed with an absolute bioavailability of 44 ± 24% (mean ± standard deviation, [Kroboth 1995](#5-References)). Triazolam is widely distributed throughout the body. Its fraction unbound in human plasma averages around 17% and is, within the range of 20 to 1000 ng/mL, not influenced by total triazolam concentrations ([Eberts 1981](#5-References)). Triazolam is extensively metabolized via CYP3A4 to α-hydroxy-alprazolam and 4-hydroxy-alprazolam ([Eberts 1981](#5-References), [Kronbach 1989](#5-References)) and is therefore often used as victim compound in drug-drug interaction (DDI) studies.

The presented triazolam PBPK model was developed for intravenous (IV) administration and oral (PO) administration of the immediate release tablet given in fasted state in healthy, non-obese adults. 



# 2 Methods
 
## 2.1 Modeling Strategy
The general workflow for building an adult PBPK model has been described by Kuepfer et al. ([Kuepfer 2016](#5-References)). Relevant information on the anthropometry (height, weight) was gathered from the respective clinical study, if reported. Information on physiological parameters (e.g. blood flows, organ volumes, hematocrit) in adults was gathered from the literature and has been incorporated in PK-Sim<sup>®</sup>) as described previously ([Willmann 2007](#5-References)). The  applied activity and variability of plasma proteins and active processes that are integrated into PK-Sim® are described in the publicly available 'PK-Sim<sup>®</sup> Ontogeny Database Version 7.3' ([PK-Sim Ontogeny Database Version 7.3](#5-References)).

The PBPK model was developed based on clinical data of healthy, non-obese, adult subjects obtained from the literature, covering different single doses of triazolam administered intravenously or orally as immediate release tablet in the fasted state. 

Unknown parameters were simultaneously optimized using all available PK data, in particular:

-  6 data sets following single IV administration of 5 different doses of triazolam (0.125 mg, 0.25 mg, 0.5 mg, 0.75 mg, 1 mg)
- 22 data sets following single PO administration of 3 different doses of triazolam as immediate release tablet (0.125 mg, 0.25 mg, 0.5 mg)

Structural model selection was mainly guided by visual inspection of the resulting description of data and biological plausibility. The following parameters were identified using the Parameter Identification module provided in PK-Sim<sup>®</sup> and MoBi<sup>®</sup> ([Open Systems Pharmacology Documentation](#5-References)):

- `Dissolution time (50% dissolved)`
- `Dissolution shape`
- `Specific intestinal permeability`
- `Mucosa permeability (interstitial<->intracellular)`
- `Lipophilicity`
- `Metabolizing Enzyme - CYP3A4 - kcat`

Details about input data (physicochemical, *in vitro* and clinical) can be found in [Section 2.2](#22-Data).

Details about the structural model and its parameters can be found in [Section 2.3](#23-Model-Parameters-and-Assumptions).



## 2.2 Data
### 2.2.1 In vitro / physicochemical data

A literature search was carried out to collect available information on physicochemical properties of triazolam. The obtained information from the literature is summarized in the table below and is used for model building.

| **Parameter**          | **Unit** | **Literature**                                               | **Description**                                              |
| :--------------------- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Molecular weight       | g/mol    | 343.21 ([drugbank.ca](#5-References))                       | Molecular weight                                             |
| pK<sub>a</sub> (basic) |          | 1.52 ([Konishi 1982](#5-References))                        | Acid dissociation constant                                   |
| logP                   |          | 2.42 ([drugbank.ca](#5-References))                         | Partition coefficient between octanol and water              |
| logD                   |          | 1.63 ([Greenblatt 1983a](#5-References))                    | Partition coefficient between octanol and water at physiological pH |
| f<sub>u</sub>          |          | 0.099 ± 0.015<sup>a</sup> ([Jochemsen 1983](#5-References)); 0.11 ([Eberts 1981](#5-References)); 0.174 ± 0.020<sup>a</sup> ([Friedman 1988](#5-References)); 0.188 ± 0.139<sup>a</sup> ([Ochs 1987](#5-References)); 0.213 [0.193 - 0.264]<sup>b</sup> ([Greenblatt 1983b](#5-References)); 0.229 [0.204 - 0.259]<sup>c</sup> ([Greenblatt 1983b](#5-References)) | Fraction unbound in human plasma of healthy adults           |
| Water solubility       | mg/L     | 4.53 ([drugbank.ca](#5-References))                         | Estimated solubility in water                                |

<sup>a</sup> mean ± standard deviation

<sup>b</sup> mean [range] in young males

<sup>c</sup> mean [range] in young females

### 2.2.2 Clinical data

A literature search was carried out to collect triazolam PK data in healthy adults. 

The following publications were found and used for model building and evaluation:

| Publication                            | Study description                                            |
| :------------------------------------- | :----------------------------------------------------------- |
| [Friedman 1986](#5-References)        | PO single dose administration of 0.5 mg                      |
| [Friedman 1988](#5-References)        | PO single dose administration of 0.5 mg                      |
| [Greenblatt 1989](#5-References)      | PO single dose administration of 0.25 mg                     |
| [Greenblatt 1991](#5-References)      | PO single dose administration of 0.125 mg                    |
| [Greenblatt 2000](#5-References)      | PO single dose administration of 0.25 mg                     |
| [Greenblatt 2004](#5-References)      | PO single dose administration of 0.25 mg                     |
| [Hukkinen 1995](#5-References)        | PO single dose administration of 0.25 mg                     |
| [Lilja 2000](#5-References)           | PO single dose administration of 0.25 mg                     |
| [Kroboth 1985](#5-References)         | IV single dose administration of 0.25 mg and PO single dose administration of 0.25 mg |
| [O'Connor-Semmes 2001](#5-References) | PO single dose administration of 0.25 mg                     |
| [Ochs 1984](#5-References)            | PO single dose administration of 0.5 mg                      |
| [Phillips 1986](#5-References)        | PO single dose administration of 0.5 mg                      |
| [Smith 1987](#5-References)           | IV single dose administration of 0.125 mg, 0.25 mg, 0.5 mg, 0.75 mg, and 1 mg |
| [Varhe 1994](#5-References)           | PO single dose administration of 0.25 mg                     |
| [Varhe 1996a](#5-References)          | PO single dose administration of 0.25 mg                     |
| [Varhe 1996b](#5-References)          | PO single dose administration of 0.25 mg                     |
| [Varhe 1996c](#5-References)          | PO single dose administration of 0.25 mg                     |
| [Villikka 1997](#5-References)        | PO single dose administration of 0.5 mg                      |
| [Villikka 1998](#5-References)        | PO single dose administration of 0.5 mg                      |
| [von Moltke 1996](#5-References)      | PO single dose administration of 0.125 mg                    |


## 2.3 Model Parameters and Assumptions
### 2.3.1	Dissolution and absorption

Dissolution of the immediate release tablet of triazolam was described by a Weibull function with the two parameters `Dissolution shape` and `Dissolution time (50% dissolved)` being fitted, together with the other parameters listed in [Section 2.1](#21-Modeling-Strategy), to observed PK data to better match the observations. `Specific intestinal permeability (transcellular)` was also optimized together with the parameters listed in [Section 2.1](#2.1 Modeling Strategy).
### 2.3.2	Distribution

In the model, the `fraction unbound (plasma, reference value)` was set to 0.174 which is the reported mean value measured in 19 healthy male and female volunteers aged 20 to 45 years ([Friedman 1988](#5-References)). This value is also the approximate average of all pooled values reported in several studies ([Jochemsen 1983](#5-References), [Eberts 1981](#5-References), [Greenblatt 1983](#5-References),  [Friedman 1988](#5-References), [Ochs 1987](#5-References)). `Lipophilicity` was optimized together with the other parameters listed in [Section 2.1](#2.1 Modeling Strategy) to better match observed PK data. The observed PK data were found to be best described using the model for estimating intracellular-to-plasma partition coefficients according to the method by `Rodgers and Rowland` ([Rodgers 2005](#5-References), [Rodgers 2006](#5-References)). Cellular permeabilities were automatically calculated using the method `PK-Sim Standard` ([Open Systems Pharmacology Documentation](#5-References)).  

### 2.3.3	Elimination

Triazolam is extensively metabolized via CYP3A to the two metabolites α-hydroxy-triazolam and 4-hydroxy-triazolam. In the model, these two biotransformation pathways were separately described via Michaelis-Menten kinetics. The `Km` values for each pathway were fixed to reported literature values, namely 74.2 µmol/L for the α-OH pathway and 305 µmol/L for the 4-OH pathway ([von Moltke 1996](#5-References)). Together with the other parameters listed in [Section 2.1](#21-Modeling-Strategy), the `kcat` values were optimized while keeping the ratio between both values constant (by selecting the option `Use as Factor`). The gene expression profile of CYP3A4 was loaded from the internal PK-Sim<sup>®</sup> database using the expression data quantified by RT-PCR ([Open Systems Pharmacology Documentation](#5-References)).



# 3 Results and Discussion
The PBPK model for triazolam was developed and verified with clinical PK data.

The next sections show:

1. the final model parameters for the building blocks: [Section 3.1](#31-Final-Input-Parameters).
2. the overall goodness of fit: [Section 3.2](#32-Diagnostics-Plots).
3. simulated vs. observed concentration-time profiles for the clinical studies used for model building: [Section 3.3](#33-Concentration-Time-Profiles).


## 3.1 Final input parameters
The compound parameter values of the final PBPK model are illustrated below. 


### Formulation: Halcion

Type: Weibull
#### Parameters

Name                             | Value            | Value Origin                                                                                        
-------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------
Dissolution time (50% dissolved) | 1.7958147418 min | Parameter Identification-Parameter Identification-Value updated from 'IV + Oral' on 2018-11-13 16:52
Lag time                         | 0 min            |                                                                                                     
Dissolution shape                | 2.5169993312     | Parameter Identification-Parameter Identification-Value updated from 'IV + Oral' on 2018-11-13 16:52
Use as suspension                | Yes              |                                                                                                     

### Compound: Triazolam

#### Parameters

Name                                             | Value                   | Value Origin                                                                                         | Alternative | Default
------------------------------------------------ | ----------------------- | ---------------------------------------------------------------------------------------------------- | ----------- | -------
Solubility at reference pH                       | 4.53 mg/l               | Unknown-drugbank.ca                                                                                  | Measurement | True   
Reference pH                                     | 7                       | Unknown-drugbank.ca                                                                                  | Measurement | True   
Lipophilicity                                    | 1.897007419 Log Units   | Parameter Identification-Parameter Identification-Value updated from 'IV + Oral' on 2018-11-13 16:52 | Optimized   | True   
Fraction unbound (plasma, reference value)       | 0.174                   | Publication-In Vivo-PMID: 3360971                                                                    | Measurement | True   
Specific intestinal permeability (transcellular) | 7.0220146601E-05 cm/min | Parameter Identification-Parameter Identification-Value updated from 'IV + Oral' on 2018-11-13 16:52 | Optimized   | True   
Cl                                               | 2                       |                                                                                                      |             |        
Is small molecule                                | Yes                     |                                                                                                      |             |        
Molecular weight                                 | 343.21 g/mol            |                                                                                                      |             |        
Plasma protein binding partner                   | Unknown                 |                                                                                                      |             |        
#### Calculation methods

Name                    | Value              
----------------------- | -------------------
Partition coefficients  | Rodgers and Rowland
Cellular permeabilities | PK-Sim Standard    
#### Processes

##### Metabolizing Enzyme: CYP3A4-alpha-OH pathway

Molecule: CYP3A4
###### Parameters

Name                               | Value                         | Value Origin                                                                                        
---------------------------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------
In vitro Vmax for liver microsomes | 2.36 nmol/min/mg mic. protein | Publication-In Vitro-PMID: 8632299                                                                  
Km                                 | 74.2 µmol/l                   | Publication-In Vitro-PMID: 8632299                                                                  
kcat                               | 4.0317206142 1/min            | Parameter Identification-Parameter Identification-Value updated from 'IV + Oral' on 2018-11-13 16:52
##### Metabolizing Enzyme: CYP3A4-4-OH pathway

Molecule: CYP3A4
###### Parameters

Name                               | Value                          | Value Origin                                                                                        
---------------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------
In vitro Vmax for liver microsomes | 10.27 nmol/min/mg mic. protein | Publication-In Vitro-PMID: 8632299                                                                  
Km                                 | 305 µmol/l                     | Publication-In Vitro-PMID: 8632299                                                                  
kcat                               | 17.5448180963 1/min            | Parameter Identification-Parameter Identification-Value updated from 'IV + Oral' on 2018-11-13 16:52

## 3.2 Diagnostics Plots
Below you find the goodness-of-fit visual diagnostic plots for the PBPK model performance of all data used presented in [Section 2.2.2](#222-Clinical-data).

The first plot shows observed versus simulated plasma concentration, the second weighted residuals versus time. 


![001_plotGOFMergedPredictedVsObserved.png](images/003_3_Results_and_Discussion/002_3_2_Diagnostics_Plots/001_plotGOFMergedPredictedVsObserved.png)

![002_plotGOFMergedResidualsOverTime.png](images/003_3_Results_and_Discussion/002_3_2_Diagnostics_Plots/002_plotGOFMergedResidualsOverTime.png)

GMFE = 1.272636 

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

# 4 Conclusion
The final triazolam PBPK model applies metabolism by CYP3A4, modelled as two separate pathways yielding α-hydroxy-triazolam and 4-hydroxy-triazolam as metabolites. Overall, the model adequately describes the observed PK of triazolam in healthy, non-obese adults receiving different single IV or PO doses of triazolam. The model is deemed fit for purpose to be applied as victim drug for the investigation of CYP3A4 drug-drug interactions.

# 5 References
**drugbank.ca**. (https://www.drugbank.ca/drugs/DB00897), accessed on 11-19-2019.

**Eberts  1981** Eberts FS Jr, Philopoulos Y, Reineke LM, Vliek RW. Triazolam disposition. *Clin Pharmacol Ther* 1981, 29(1): 81-93.

**Friedman 1986** Friedman H, Greenblatt DJ, Burstein ES, Harmatz JS, Shader RI. Population study of triazolam pharmacokinetics. *Br J Clin Pharmacol* 1986, 22(6): 639-642.

**Friedman 1988** Friedman H, Greenblatt DJ, Burstein ES, Scavone JM, Harmatz JS, Shader RI.  kinetics: interaction with cimetidine, propranolol, and the combination. *J Clin Pharmacol* 1988, 28(3): 228-233.

**Greenblatt 1983a** Greenblatt DJ, Arendt RM, Abernethy DR, Giles HG, Sellers EM, Shader RI. In vitro quantitation of benzodiazepine lipophilicity: relation to in vivo distribution. *Br J Anaesth* 1983, 55(10): 985-989.

**Greenblatt 1983** Greenblatt DJ, Divoll M, Abernethy DR, Moschitto LJ, Smith RB, Shader RI. Reduced clearance of triazolam in old age: relation to antipyrine oxidizing capacity. *Br J Clin Pharmacol* 1983, 15(3): 303-309.

**Greenblatt 1989** Greenblatt DJ, Harmatz JS, Engelhardt N, Shader RI. Pharmacokinetic determinants of dynamic differences among three benzodiazepine hypnotics. Flurazepam, temazepam, and triazolam. *Arch Gen Psychiatry* 1989, 46(4): 326-332.

**Greenblatt 1991** Greenblatt DJ, Harmatz JS, Shapiro L, Engelhardt N, Gouthro TA, Shader RI. Sensitivity to triazolam in the elderly. *N Engl J Med* 1991, 324(24): 1691-1698.

**Greenblatt 2000** Greenblatt DJ, Harmatz JS, von Moltke LL, Wright CE, Durol AL, Harrel-Joseph LM, Shader RI. Comparative kinetics and response to the benzodiazepine agonists triazolam and zolpidem: evaluation of sex-dependent differences. *J Pharmacol Exp Ther* 2000, 293(2): 435-443.

**Greenblatt 2004** Greenblatt DJ, Harmatz JS, von Moltke LL, Wright CE, Shader RI. Age and gender effects on the pharmacokinetics and pharmacodynamics of triazolam, a cytochrome P450 3A substrate. *Clin Pharmacol Ther* 2004, 76(5): 467-479.

**Hukkinen 1995** Hukkinen SK, Varhe A, Olkkola KT, Neuvonen PJ. Plasma concentrations of triazolam are increased by concomitant ingestion of grapefruit juice. *Clin Pharmacol Ther* 1995, 58(2): 127-131.

**Jochemsen 1983** Jochemsen R, Wesselman JG, van Boxtel CJ, Hermans J, Breimer DD. Comparative pharmacokinetics of brotizolam and triazolam in healthy subjects. *Br J Clin Pharmacol* 1983, 16 Suppl 2: 291S-297S.

**Konishi 1982** Konishi M, Hirai K, Mori Y. Kinetics and mechanism of the equilibrium reaction of triazolam in aqueous solution. *J Pharm Sci* 1982, 71(12): 1328-1334.

**Kroboth 1995** Kroboth PD, McAuley JW, Kroboth FJ, Bertz RJ, Smith RB. Triazolam pharmacokinetics after intravenous, oral, and sublingual administration. *J Clin Psychopharmacol* 1995, 15(4): 259-262.

**Kronbach 1989** Kronbach T, Mathys D, Umeno M, Gonzalez FJ, Meyer UA. Oxidation of midazolam and triazolam by human liver cytochrome P450IIIA4. *Mol Pharmacol* 1989, 36(1): 89-96.

**Kuepfer 2016** Kuepfer L, Niederalt C, Wendl T, Schlender JF, Willmann S, Lippert J, Block M, Eissing T, Teutonico D. Applied concepts in PBPK modeling: how to build a PBPK/PD model. *CPT Pharmacometrics Syst Pharmacol* 2016, 5(10): 516-531.

**Lilja 2000** Lilja JJ, Kivistö KT, Backman JT, Neuvonen PJ. Effect of grapefruit juice dose on grapefruit juice-triazolam interaction: repeated consumption prolongs triazolam half-life. *Eur J Clin Pharmacol* 2000, 56(5): 411-415.

**O'Connor-Semmes 2001** O'Connor-Semmes RL, Kersey K, Williams DH, Lam R, Koch KM. Effect of ranitidine on the pharmacokinetics of triazolam and alpha-hydroxytriazolam in both young (19-60 years) and older (61-78 years) people. *Clin Pharmacol Ther* 2001, 70(2): 126-131.

**Ochs 1984** Ochs HR, Greenblatt DJ, Arendt RM, Hübbel W, Shader RI. Pharmacokinetic noninteraction of triazolam and ethanol. *J Clin Psychopharmacol* 1984, 4(2): 106-107.

**Ochs 1987** Ochs HR, Greenblatt DJ, Burstein ES. Lack of influence of cigarette smoking on triazolam pharmacokinetics. *Br J Clin Pharmacol* 1987, 23(6): 759-763.

**Open Systems Pharmacology Documentation**. (https://docs.open-systems-pharmacology.org/), accessed on 07-30-2019.

**Phillips 1986** Phillips JP, Antal EJ, Smith RB. A pharmacokinetic drug interaction between erythromycin and triazolam. *J Clin Psychopharmacol* 1986, 6(5): 297-299.

**PK-Sim Ontogeny Database Version 7.3**. (https://github.com/Open-Systems-Pharmacology/OSPSuite.Documentation/blob/38cf71b384cfc25cfa0ce4d2f3addfd32757e13b/PK-Sim%20Ontogeny%20Database%20Version%207.3.pdf), accessed on 07-30-2019.

**Smith 1987** Smith RB, Kroboth PD, Varner PD. Pharmacodynamics of triazolam after intravenous administration. *J Clin Pharmacol* 1987, 27(12): 971-979.

**Varhe 1994** Varhe A, Olkkola KT, Neuvonen PJ. Oral triazolam is potentially hazardous to patients receiving systemic antimycotics ketoconazole or itraconazole. *Clin Pharmacol Ther* 1994, 56(6 Pt 1): 601-607.

**Varhe 1996a** Varhe A, Olkkola KT, Neuvonen PJ. Fluconazole, but not terbinafine, enhances the effects of triazolam by inhibiting its metabolism. *Br J Clin Pharmacol* 1996, 41(4): 319-323.

**Varhe 1996b** Varhe A, Olkkola KT, Neuvonen PJ. Diltiazem enhances the effects of triazolam by inhibiting its metabolism. *Clin Pharmacol Ther* 1996, 59(4): 369-375.

**Varhe 1996c** Varhe A, Olkkola KT, Neuvonen PJ. Effect of fluconazole dose on the extent of fluconazole-triazolam interaction. *Br J Clin Pharmacol* 1996, 42(4): 465-470.

**Villikka 1997** Villikka K, Kivistö KT, Backman JT, Olkkola KT, Neuvonen PJ. Triazolam is ineffective in patients taking rifampin. *Clin Pharmacol Ther* 1997, 61(1): 8-14.

**Villikka 1998** Villikka K, Kivistö KT, Neuvonen PJ. The effect of dexamethasone on the pharmacokinetics of triazolam. *Pharmacol Toxicol* 1998, 83(3): 135-138.

**von Moltke 1996** von Moltke LL, Greenblatt DJ, Harmatz JS, Duan SX, Harrel LM, Cotreau-Bibbo MM, Pritchard GA, Wright CE, Shader RI. Triazolam biotransformation by human liver microsomes in vitro: effects of metabolic inhibitors and clinical confirmation of a predicted interaction with ketoconazole. *J Pharmacol Exp Ther* 1996, 276(2): 370-379.

**Willmann 2007** Willmann S, Höhn K, Edginton A, Sevestre M, Solodenko J, Weiss W, Lippert J, Schmitt W. Development of a physiology-based whole-body population model for assessing the influence of individual variability on the pharmacokinetics of drugs. *J Pharmacokinet Pharmacodyn* 2007, 34(3): 401-431.
