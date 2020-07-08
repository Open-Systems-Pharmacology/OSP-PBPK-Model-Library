# Building and evaluation of a PBPK model for atazanavir in healthy adults





| Version                                         | 1.1-OSP9.1                                                   |
| ----------------------------------------------- | ------------------------------------------------------------ |
| based on *Model Snapshot* and *Evaluation Plan* | https://github.com/Open-Systems-Pharmacology/Atazanavir-Model/releases/tag/v1.1 |
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
The presented model building and evaluation report evaluates the performance of a PBPK model for atazanavir in healthy adults.

Atazanavir, sold under the trade name Reyataz among others, is an azapeptide protease inhibitor and used as antiretroviral medication to treat and prevent HIV/AIDS. It is taken orally once a day at a dose of 300 mg, if co-administered with ritonavir 100 mg orally once a day, and 400 mg, if administered without ritonavir. 

After oral administration, atazanavir is rapidly absorbed. A positive food effect has been observed, atazanavir is recommended to be taken with food. Protein binding is relatively high (86%) and independent of the concentration of serum proteins ([US Food and Drug Administration 2002](#5-References)). Atazanavir undergoes extensive metabolism by CYP3A isoenzymes with a dose fraction excreted unchanged in urine of approximately 7% ([US Food and Drug Administration 2002](#5-References), [Le Tiec 2005](#5-References)). Previous in vitro studies suggest that atazanavir is a mechanism-based inhibitor of CYP3A ([US Food and Drug Administration 2002](#5-References), [Perloff 2005](#5-References)) as well as a competitive inhibitor of CYP1A2, CYP2C9 and UGT1A1 ([US Food and Drug Administration 2002](#5-References), [Zhang 2005](#5-References)).


# 2 Methods

## 2.1 Modeling Strategy
The general workflow for building an adult PBPK model has been described by Kuepfer et al. ([Kuepfer 2016](#5-References)). Relevant information on the anthropometry (height, weight) was gathered from the respective clinical study, if reported. Information on physiological parameters (e.g. blood flows, organ volumes, hematocrit) in adults was gathered from the literature and has been incorporated in PK-Sim® as described previously ([Willmann 2007](#5-References)). The  applied activity and variability of plasma proteins and active processes that are integrated into PK-Sim® are described in the publicly available ‘PK-Sim® Ontogeny Database Version 7.3' ([PK-Sim Ontogeny Database Version 7.3](#5-References)).

The PBPK model was developed based on clinical data of healthy adult subjects obtained from the literature, covering available dosing ranges for oral administration. Plasma concentration-time profiles following multiple-dose application and mass balance information on the urinary excretion of unchanged atazanavir were included in model development. 

First, a base mean model was built using plasma concentration-time profiles and the dose fraction excreted unchanged in urine following single dose administration of 400 mg po. The mean PK model was developed using a typical White American individual. Structural model selection was mainly guided by visual inspection of the resulting description of data and biological plausibility. The following parameters were identified using the Parameter Identification module provided in PK-Sim® and MoBi® ([Open Systems Pharmacology Documentation](#5-References)):

- `Dissolution shape`
- `Dissolution time (50% dissolved)`
- `Specific intestinal permeability (transcellular)`
- `GFR fraction`
- `CLspec/[Enzyme]`

Structural model selection was mainly guided by visual inspection of the resulting description of PK data and biological plausibility. On the basis of in vitro findings, atazanavir has been suggested to be a mechanism-based inhibitor of CYP3A ([Perloff 2005](#5-References)); however, no kinetic parameters have been reported for this interaction. Hence, to avoid non-identifiability issues, mechanism-based inhibition of CYP3A was not considered during parameter identification of the mean base model for single dose administration. All models implemented in PK-Sim for estimating the intracellular-to-plasma partition coefficient and those for estimating the permeability between interstitial and intracellular space were tested in this step. Once an appropriate structural model was identified, a second parameter identification was conducted fixing all previously optimized parameter values (except the `GFR fraction`) and including additional PK data following multiple dose administration of 200 mg, 300 mg, 400 mg, and 800 mg po. Optimized parameters were:

- `GFR fraction`
- `k_inact`
- `k_kinact_half`

Of note, since neither *in vitro* data on the kinetics of the mechanism-based inhibition of CYP3A nor *in vivo* pharmacokinetic data on drug-drug-interactions (DDI) with a CYP3A index substrate and atazanavir as CYP3A-perpetrator were available, the model should **not** be used to predict CYP3A DDI studies unless it has been verified for this purpose.

Details about input data (physicochemical, *in vitro* and clinical) can be found in [Section 2.2](#22-Data).

Details about the structural model and its parameters can be found in [Section 2.3](#23-Model-Parameters-and-Assumptions).






## 2.2 Data
### 2.2.1 In vitro / physicochemical data

A literature search was carried out to collect available information on physicochemical properties of atazanavir. The obtained information from the literature is summarized in the table below and is used for model building.

| **Parameter**          | **Unit** | **Value**                                   | **Description**                                       |
| :--------------------- | -------- | ------------------------------------------------------------ | ----------------------------------------------------- |
| Molecular weight       | g/mol    | 704.9 ([drugbank.ca](#5-References))                         | Molecular weight                                      |
| pK<sub>a</sub> (basic) |          | 4.7 ([Berlin 2015](#5-References))                           | Acid dissociation constant                            |
| logP                   |          | 2.12 ([Hyland 2008](#5-References))                          | Partition coefficient between octanol and water       |
| f<sub>u</sub>          |          | 0.14 ([US Food and Drug Administration 2002](#5-References)) | Fraction unbound in human plasma                      |
| Solubililty in FaSSIF  | µg/mL    | 2.74 ([Berlin 2015](#5-References))                          | Solubility in Fasted State Simulated Intestinal Fluid |
| Solubililty in FeSSIF  | µg/mL    | 4.13 ([Berlin 2015](#5-References))                          | Solubility in Fed State Simulated Intestinal Fluid    |

With regard to UGT1A1 inhibition, atazanavir inhibited 17β-Estradiol glucuronidation in recombinant UGT1A1 by a mixed-type mechanism (in-house data, [Jungmann 2019](#5-References)):

| **Parameter**    | **Unit** | **Value** | Source                         | **Description**                      |
| :--------------- | -------- | --------- | ------------------------------ | ------------------------------------ |
| K<sub>i</sub>    | µmol/L   | 0.22      | [Jungmann 2019](#5-References) | Inhibition constant                  |
| Alpha            |          | 4.5       | [Jungmann 2019](#5-References) | Alpha value in mixed-type inhibition |
| fu<sub>mic</sub> | %        | 0.863     | [Fricke 2020](#5-References)   | determined *in vitro* at 0.22 µmol/L |

### 2.2.2 Clinical data

A literature search was carried out to collect available PK data on atazanavir in healthy adults. 

The following publications were found and used for model building and evaluation:

| Publication                                           | Study description                                            |
| :---------------------------------------------------- | :----------------------------------------------------------- |
| [Acosta 2007](#5-References)                          | 300 mg atazanavir BID, Period 1                              |
| [Agarwala 2003](#5-References)                        | 400 mg atazanavir QD, Day 6                                  |
| [Agarwala 2005a](#5-References)                       | 400 mg atazanavir QD, 400 mg AM                              |
| [Agarwala 2005b](#5-References)                       | 400 mg atazanavir QD, 400 mg (Treatment A)                   |
| [Martin 2008](#5-References)                          | 400 mg atazanavir QD, monotherapy                            |
| [Zhu 2010](#5-References)                             | 300 mg atazanavir QD                                         |
| [Zhu 2011](#5-References)                             | 400 mg atazanavir QD, 400 mg QPM and QAM                     |
| [US Food and Drug Administration 2002](#5-References) | Study AI424-004 (p. 94): 400 mg atazanavir single dose (treatment A);<br />Study AI424-014 (p. 77): 400 mg atazanavir single dose (young females & males);<br />Study AI424-015 (p. 81): 400 mg atazanavir single dose (normal subjects);<br />Study AI424-028 (p. 128): 200, 400, and 800 mg atazanavir QD (A-D Day6);<br />Study AI424-029 (p. 47): 400 mg [<sup>14</sup>C]atazanavir single dose;<br />Study AI424-040 (p. 64): 200, 400, and 800 mg atazanavir QD;<br />Study AI424-056 (p. 134): 300 mg atazanavir QD (without ritonavir, Day 10);<br />Study AI424-076 (p. 178): 400 and 800 mg atazanavir QD |


## 2.3 Model Parameters and Assumptions
### 2.3.1 Dissolution and absorption

No PK data were available following intravenous administration of atazanavir allowing informing distribution and systemic clearance independently of dissolution and absorption. Consequently, only PK data following oral administration of atazanavir as capsule were used for model building. It was assumed that solubility is not a critical parameter for dissolution of atazanavir capsules in the GI tract; in the models, solubility was therefore fixed to a very high value (50 mg/mL) to prevent solubility being a limiting factor of dissolution. Although the equilibrium solubility of atazanavir in the biorelevant media FaSSIF and FeSSIF has been observed to be rather low (2.74 µg/mL and 4.13 µg/mL in FaSSIF and FeSSIF, respectively), dissolution of atazanavir capsules in these media yields concentrations that are considerably higher than this threshold during the complete measurement period of at least 3 h ([Berlin 2015](#5-References)). In the model, dissolution was described by a Weibull function and the two Weibull parameters, `dissolution shape` and `dissolution time (50% dissolved)`, were fitted together with the `specific intestinal permeability (transcellular)` to observed PK data as described in [Section 2.1](#21-Modeling-Strategy).  

Since no PK data following IV administration was available, a moderate correlation was observed between the fitted `dissolution time (50% dissolved)` and `GFR fraction`. Although the final model parameterization was found to slightly overestimate C<sub>max</sub> in fasted state, this was considered inconsequential since atazanavir must be taken with food and all further model applications encompassed fed state PK.

### 2.3.2 Distribution

With a fraction unbound in human plasma of approximately 0.14, atazanavir is extensively protein-bound. Equilibrium dialysis of spiked human serum or human blood samples *in vitro* showed that atazanavir is bound to serum proteins (86.5%), albumin (86.2%), α1-acid glycoprotein (88.7%), and red blood cells (29.5%). The extent of protein binding and blood cell distribution has been reported to be concentration-independent over a 100-fold range ([US Food and Drug Administration 2002](#5-References)). The observed PK data were found to be best described using the model for estimating intracellular-to-plasma partition coefficients by Rodgers et al. ([Rodgers 2005](#5-References), [Rodgers 2006](#5-References)) and the cellular permeability automatically calculated by PK-Sim® ([Open Systems Pharmacology Documentation](#5-References)). 

### 2.3.3 Elimination

Atazanavir is extensively metabolized via CYP3A isoenzymes ([Le Tiec 2005](#5-References)). Metabolism was modeled as linear process mediated by CYP3A4 (`in vitro clearance - first order`). The gene expression profile of CYP3A4 was loaded from the internal PK-Sim® database using the expression data quantified by RT-PCR ([Open Systems Pharmacology Documentation](#5-References)). 

Following oral administration of 400 mg [<sup>14</sup>C]atazanavir to healthy males, approximately 7% of the radioactive dose were recovered as unchanged drug in the urine ([US Food and Drug Administration 2002](#5-References)). Renal excretion of the unchanged drug was modeled as glomerular filtration process. The `GFR fraction` was then, together with the specific clearance via CYP3A4 normalized to the enzyme concentration (`CLspec/[Enzyme]`), fitted to observed PK data as described in [Section 2.1](#21-Modeling-Strategy).

### 2.3.2 Autoinhibition

Findings from in vitro studies indicate that atazanavir irreversibly inhibits CYP3A ([US Food and Drug Administration 2002](#5-References), [Perloff 2005](#5-References)). Since no kinetic values were reported for this mechanism-based inhibition, relevant parameters in the model (`k_kinact_half` and `k_inact`) were fitted as described in [Section 2.1](#2.1-Modeling-Strategy). An attempt to fix `k_kinact_half` to a very high value (100 µmol/L) to ensure linear inhibition kinetics while fitting `k_inact` and the `GFR faction` resulted in a slightly worse description of the observed PK in the terminal phase. Hence, both `k_kinact_half` and `k_inact were` fitted together with the `GFR fraction`. This resulted in a strong correlation between the former two parameters, but also in a reduction of the total error. Furthermore, the introduction of irreversible CYP3A4 inhibition led to a slightly worse description of clearance of the single dose PK data. Furthermore, the model was found to describe the lowest and highest dose (200 and 800 mg) less accurately. Importantly, though, the PK after multiple dose administration of 300 mg and 400 mg - the only two approved doses - could be adequately captured. 

Of note, since neither *in vitro* data on the mechanism-based inhibition of CYP3A nor *in vivo* pharmacokinetic data on drug-drug-interactions (DDI) with a CYP3A index substrate and atazanavir as CYP3A-perpetrator were available, the model should **not** be used to predict CYP3A DDI studies unless it has been verified for this purpose.


# 3 Results and Discussion
The PBPK model for dapagliflozin was developed and verified with clinical pharmacokinetic data.

The next sections show:

1. the final model parameters for the building blocks: [Section 3.1](#31-Final-Input-Parameters).
2. the overall goodness of fit: [Section 3.2](#32-Diagnostics-Plots).
3. simulated vs. observed concentration-time profiles for the clinical studies used for model building and for model verification: [Section 3.3](#33-Concentration-Time-Profiles).


## 3.1 Final input parameters
The compound parameter values of the final PBPK model are illustrated below.


### Compound: Atazanavir

#### Parameters

Name                                             | Value                   | Value Origin                            | Alternative | Default
------------------------------------------------ | ----------------------- | --------------------------------------- | ----------- | -------
Solubility at reference pH                       | 50000 mg/l              | Assumption                              | Assumption  | True   
Reference pH                                     | 7                       | Assumption                              | Assumption  | True   
Lipophilicity                                    | 2.12 Log Units          | Publication-Hyland 2008, PMID: 18647303 | Measurement | True   
Fraction unbound (plasma, reference value)       | 0.14                    | Publication-Rajoli 2015, PMID: 25523214 | Measurement | True   
Specific intestinal permeability (transcellular) | 9.8649602504E-06 cm/min | Parameter Identification                | Optimized   | True   
Is small molecule                                | Yes                     |                                         |             |        
Molecular weight                                 | 704.8555 g/mol          | Internet-drugbank.ca                    |             |        
Plasma protein binding partner                   | Unknown                 |                                         |             |        
#### Calculation methods

Name                    | Value              
----------------------- | -------------------
Partition coefficients  | Rodgers and Rowland
Cellular permeabilities | PK-Sim Standard    
#### Processes

##### Metabolizing Enzyme: CYP3A4-Optimized

Molecule: CYP3A4
###### Parameters

Name                 | Value                   | Value Origin            
-------------------- | ----------------------- | ------------------------
Enzyme concentration | 1 µmol/l                |                         
Specific clearance   | 0 1/min                 |                         
CLspec/[Enzyme]      | 1.0383524966 l/µmol/min | Parameter Identification
##### Systemic Process: Glomerular Filtration-Clinical Pharmacology Review

Species: Human
###### Parameters

Name         |       Value | Value Origin            
------------ | -----------:| ------------------------
GFR fraction | 2.014495446 | Parameter Identification
##### Inhibition: CYP3A4-Perloff2005

Molecule: CYP3A4
###### Parameters

Name          | Value                 | Value Origin            
------------- | --------------------- | ------------------------
kinact        | 0.0033009852632 1/min | Parameter Identification
K_kinact_half | 0.1292581489 µmol/l   | Parameter Identification
##### Inhibition: UGT1A1-PH-41095

Molecule: UGT1A1
###### Parameters

Name | Value          | Value Origin                                          
---- | -------------- | ------------------------------------------------------
Ki_c | 0.18986 µmol/l | In Vitro-Calculated from reported Ki and fu,mic       
Ki_u | 0.85437 µmol/l | In Vitro-Calculated from reported Ki, fu,mic and alpha

### Formulation: Reyataz capsule

Type: Weibull
#### Parameters

Name                             | Value             | Value Origin            
-------------------------------- | ----------------- | ------------------------
Dissolution time (50% dissolved) | 78.8787658271 min | Parameter Identification
Lag time                         | 0 min             |                         
Dissolution shape                | 1.5566465018      | Parameter Identification
Use as suspension                | Yes               | Other                   

## 3.2 Diagnostics Plots
Below you find the goodness-of-fit visual diagnostic plots for the PBPK model performance of all data used presented in [Section 2.2.2](#222-Clinical-data).

The first plot shows observed versus simulated plasma concentration, the second weighted residuals versus time. 


![001_plotGOFMergedPredictedVsObserved.png](images/003_3_Results_and_Discussion/002_3_2_Diagnostics_Plots/001_plotGOFMergedPredictedVsObserved.png)

![002_plotGOFMergedResidualsOverTime.png](images/003_3_Results_and_Discussion/002_3_2_Diagnostics_Plots/002_plotGOFMergedResidualsOverTime.png)

GMFE = 1.500685 

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

![022_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/022_plotTimeProfile.png)

![023_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/023_plotTimeProfile.png)

![024_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/024_plotTimeProfile.png)

![025_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/025_plotTimeProfile.png)

![026_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/026_plotTimeProfile.png)

![027_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/027_plotTimeProfile.png)

![028_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/028_plotTimeProfile.png)

![029_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/029_plotTimeProfile.png)

![030_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/030_plotTimeProfile.png)

![031_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/031_plotTimeProfile.png)

![032_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/032_plotTimeProfile.png)

![033_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/033_plotTimeProfile.png)

![034_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/034_plotTimeProfile.png)

![035_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/035_plotTimeProfile.png)

![036_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/036_plotTimeProfile.png)

![037_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/037_plotTimeProfile.png)

![038_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/038_plotTimeProfile.png)

![039_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Concentration-Time_Profiles/039_plotTimeProfile.png)

# 4 Conclusion
The  final atazanavir PBPK model applies metabolism by CYP3A4, glomerular filtration and mechanism-based inhibition of CYP3A4. While the latter process has not been evaluated using another victim compound, it should only be regarded preliminary and further work is needed before this model can be applied to predict CYP3A4 DDIs. Overall, the model adequately describes the oral pharmacokinetics of  atazanavir in healthy adults receiving approved atazanavir doses of 300 mg and 400 mg. It is therefore deemed fit for purpose to be applied for the investigation of DDIs involving UGT1A1 inhibition.


# 5 References
**Acosta 2007** Acosta EP, Kendall MA, Gerber JG, Alston-Smith B, Koletar SL, Zolopa AR, et al. Effect of concomitantly administered rifampin on the pharmacokinetics and safety of atazanavir administered twice daily. *Antimicrob Agents Chemother* 2007, 51(9): 3104-3110.

**Agarwala 2003** Agarwala S, Grasela D, Child M, Geraldes M, Geiger M, O’Mara E. Characterization of the steady-state pharmacokinetic (PK) profile of atazanavir (ATV) beyond the 24-hour 
dosing interval. Poster presented at *2nd International AIDS Society Conference on HIV Pathogenesis and Treatment*, Paris, 2003. (http://www.medadvocates.org/resources/conferences/iasconfpath/ias2003/atv%20pk%20past%2024%20hour%20interval.pdf), accessed on 07-30-2019.

**Agarwala 2005a** Agarwala S, Eley T, Child M, Wang Y, Hughes E, Grasela D. Pharmacokinetic effects of coadministration of atazanavir and tenofovir at steady state. Poster presented at *3rd International AIDS Society Conference on HIV Pathogenesis and Treatment*, Rio de Janeiro, 2005a. (http://www.medadvocates.org/resources/conferences/3rd%20_ias/05-156a_agarwala_086.pdf), accessed on 07-30-2019.

**Agarwala 2005b** Agarwala S, Gray K, Eley T, Wang Y, Hughes E, Grasela D. Pharmacokinetic interaction between atazanavir and omeprazole in healthy subjects. Poster presented at *3rd International AIDS Society Conference on HIV Pathogenesis and Treatment*, Rio de Janeiro, 2005b. (http://www.medadvocates.org/resources/conferences/3rd%20_ias/05-156b_agarwala_109.pdf), accessed on 07-30-2019

**Berlin 2015** Berlin M, Ruff A, Kesisoglou F, Xu W, Wang MH, Dressman JB. Advances and challenges in PBPK modeling–analysis of factors contributing to the oral absorption of atazanavir, a poorly soluble weak base. *Eur J Pharm Biopharm* 2015, 93: 267-280.

**drugbank** (https://www.drugbank.ca/drugs/DB01072), accessed on 07-30-2019.

**Fricke 2020** Fricke R. Vericiguat: Investigations on Binding of Atazanavir to Recombinant UGT1A1 and of Mefenamic Acid to Recombinant UGT1A9. 2020. Report-No. PH-41346.

**Hyland 2008** Hyland R, Dickins M, Collins C, Jones H, Jones B. Maraviroc: in vitro assessment of 
drug–drug interaction potential. *Br J Clin Pharmacol* 2008, 66(4): 498-507.

**Jungmann 2019** Jungmann N. Vericiguat: Determination of Ki Values of Atazanavir on 3-Glucuronidation of 17β-Estradiol via UGT1A1 and of Mefenamic Acid on Glucuronidation of Propofol via UGT1A9. Bayer AG Nonclinical study report. 2019 Aug. Report-No. PH-41095.

**Kuepfer 2016** Kuepfer L, Niederalt C, Wendl T, Schlender JF, Willmann S, Lippert J, Block M, Eissing T, Teutonico D. Applied concepts in PBPK modeling: how to build a PBPK/PD model. *CPT Pharmacometrics Syst Pharmacol* 2016, 5(10): 516-531.

**Le Tiec 2005** Le Tiec C, Barrail A, Goujard C, Taburet AM. Clinical pharmacokinetics and summary of 
efficacy and tolerability of atazanavir. *Clin Pharmacokinet.* 2005, 44(10): 1035-1050.

**Martin 2008** Martin DE, Galbraith H, Schettler J, Ellis C, Doto J. Pharmacokinetic properties and tolerability of bevirimat and atazanavir in healthy volunteers: an open-label, parallel-group study. *Clin Ther.* 2008, 30(10): 1794-1805.

**Open Systems Pharmacology Documentation**. (https://docs.open-systems-pharmacology.org/), accessed on 07-30-2019.

**Perloff 2005** Perloff ES, Duan SX, Skolnik PR, Greenblatt DJ, von Moltke LL. Atazanavir: effects on P-glycoprotein transport and CYP3A metabolism in vitro. *Drug Metab Dispos* 2005, 33(6): 764-770.

**PK-Sim Ontogeny Database Version 7.3**. (https://github.com/Open-Systems-Pharmacology/OSPSuite.Documentation/blob/38cf71b384cfc25cfa0ce4d2f3addfd32757e13b/PK-Sim%20Ontogeny%20Database%20Version%207.3.pdf), accessed on 07-30-2019.

**Rodgers 2005** Rodgers T, Leahy D, Rowland M. Physiologically Based Pharmacokinetic Modeling 1: Predicting the Tissue Distribution of Moderate-to-Strong Bases. *J Pharm Sci* 2005, 94: 1259-1275.

**Rodgers 2006** Rodgers T, Rowland M. Physiologically Based Pharmacokinetic Modeling 2: Predicting the Tissue Distribution of Acids, Very Weak Bases, Neutrals and Zwitterions. *J Pharm Sci* 2006, 95: 1238-1257.

**US Food and Drug Administration**. Reyataz (atazanavir) capsules: Clinical Pharmacology and Biopharmaceutics Review, Application number: 21-567, 2002. Available at: https://www.accessdata.fda.gov/drugsatfda_docs/nda/2003/021567_reyataz_toc.cfm, accessed on 07-30-2019.

**Willmann 2007** Willmann S, Höhn K, Edginton A, Sevestre M, Solodenko J, Weiss W, Lippert J, Schmitt W. Development of a physiology-based whole-body population model for assessing the influence of individual variability on the pharmacokinetics of drugs. *J Pharmacokinet Pharmacodyn* 2007, 34(3): 401-431.

**Zhang 2005** Zhang D, Chando TJ, Everett DW, Patten CJ, Dehal SS, Humphreys WG. In vitro inhibition of UDP glucuronosyltransferases by atazanavir and other HIV protease inhibitors and the relationship of this property to in vivo bilirubin glucuronidation. *Drug Metab Dispos* 2005, 33(11): 1729-1739.

**Zhu 2010** Zhu L, Butterton J, Persson A, Stonier M, Comisar W, Panebianco D, et al. Pharmacokinetics and safety of twice-daily atazanavir 300 mg and raltegravir 400 mg in healthy individuals. *Antivir Ther* 2010, 15(8): 1107-1114.

**Zhu 2011** Zhu L, Persson A, Mahnke L, Eley T, Li T, Xu X, et al. Effect of low‐dose omeprazole (20 mg Daily) on the pharmacokinetics of multiple‐dose atazanavir with ritonavir in healthy subjects. *J Clin Pharmacol* 2011, 51(3): 368-377.
