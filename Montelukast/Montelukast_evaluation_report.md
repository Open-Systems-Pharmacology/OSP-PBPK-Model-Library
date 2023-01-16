# Building and evaluation of a PBPK model for montelukast in adults





| Version                                         | 1.2-OSP11.1                                                   |
| ----------------------------------------------- | ------------------------------------------------------------ |
| based on *Model Snapshot* and *Evaluation Plan* | https://github.com/Open-Systems-Pharmacology/Montelukast-Model/releases/tag/v1.2 |
| OSP Version                                     | 11.1                                                          |
| Qualification Framework Version                 | 2.3                                                          |





This evaluation report and the corresponding PK-Sim project file are filed at:

https://github.com/Open-Systems-Pharmacology/OSP-PBPK-Model-Library/

# Table of Contents
  * [1 Introduction](#1-introduction)
  * [2 Methods](#2-methods)
    * [2.1 Modeling strategy](#21-modeling-strategy)
    * [2.2 Data used](#22-data-used)
    * [2.3 Model parameters and assumptions](#23-model-parameters-and-assumptions)
  * [3 Results and Discussion](#3-results-and-discussion)
    * [3.1 Montelukast final input parameters](#31-montelukast-final-input-parameters)
    * [3.2 Montelukast Diagnostics Plots](#32-montelukast-diagnostics-plots)
    * [3.3 Montelukast Concentration-Time profiles](#33-montelukast-concentration-time-profiles)
  * [4 Conclusion](#4-conclusion)
  * [5 References](#5-references)
# 1 Introduction
The presented model building and evaluation report evaluates the performance of a physiology-based  pharmacokinetic (PBPK) model for montelukast in adults.

Montelukast is a selective and orally active leukotriene receptor antagonist that inhibits the cysteinyl leukotriene (CysLT) receptor 1, used in the maintenance treatment of asthma. Montelukast is mainly metabolized by CYP2C8 (72%) ([Marzolini 2017](#5-references)).  Montelukast is a strongly lipophilic drug. The final lipophilicity was estimated to be lower than the reported values, as with lipophilicity values above 3-4 log units the drug already reached maximal permeability levels. The final montelukast model applies metabolism by CYP2C8, and to a minor extend involved clearance by the enzymes CYP3A4/5 (16% ), CYP2C9 (12%) and glomerular filtration ([Marzolini 2017, Filppula 2011, Zhou 2017](#5-references)) and adequately described the pharmacokinetics of montelukast in adults.

The montelukast model is a whole-body PBPK model, allowing for dynamic translation between individuals. The montelukast report demonstrates the level of confidence in the montelukast PBPK model built with the OSP suite with regard to reliable predictions of montelukast pharmacokinetics (PK) in adults during model-informed drug development.

# 2 Methods


## 2.1 Modeling strategy
The general concept of building a PBPK model has previously been described by Kuepfer et al. ([Kuepfer 2016](#5-references)). Relevant information on anthropometric (height, weight) and physiological parameters (e.g. blood flows, organ volumes, binding protein concentrations, hematocrit, cardiac output) in adults was gathered from the literature and has been previously published ([Schlender 2016](#5-references)). The information was incorporated into PK-Sim® and was used as default values for the simulations in adults.

The  applied activity and variability of plasma proteins and active processes that are integrated into PK-Sim® are described in the publicly available PK-Sim® Ontogeny Database Version 7.3 ([PK-Sim Ontogeny Database Version 7.3](#5-references)) or otherwise referenced for the specific process.

First, a base mean model was built using data from the single dose escalation study to find an appropriate structure describing the PK of montelukast. The mean PK model was developed using a typical European individual. Unknown parameters were identified using the Parameter Identification module provided in PK-Sim®. Structural model selection was mainly guided by visual inspection of the resulting description of data and biological plausibility.

Once the appropriate structural model was identified, additional parameters for different formulations were identified, if available. 

A final PBPK model was established and simulations were compared to the reported data to evaluate model appropriateness and to assess model verification, by means of diagnostics plots and predicted versus observed concentration-time profiles, of which the results support an adequate prediction of the PK in adults.

During model building, uncertainties in data quality, as well as study differences may cause not being able to adequately describe the PK of all reported clinical studies. 


## 2.2 Data used
### 2.2.1 In vitro / physicochemical data

A literature search was performed to collect available information on physicochemical properties of montelukast. The obtained information from literature is summarized in the table below and is used for model building.

| **Parameter**   | **Unit**    | **Value (reference)** | **Description**                                  |
| :-------------- | ----------- | ----------------------------------- | ------------------------------------------------ |
| MW              | g/mol       | 586.2 ([Marzolini 2017](#5-references)) | Molecular weight                                 |
| pKa             |             | 4.4 ([Marzolini 2017](#5-references)) | Acid dissociation constant                   |
| Solubility (pH) | mg/mL       | 8.2E-06 (7) ([Drugbank](#5-references)) | Solubility                                       |
| logP            |             | 7.90 ([Marzolini 2017](#5-references)) | Partition coefficient between octanol and water  |
| fu              |             | 0.0018 ([Marzolini 2017](#5-references)) | Fraction unbound                                 |
| fe**   |          | <0.002 ([Marzolini 2017](#5-references)) | fraction of dose excreted unchanged in urine |
| CYP3A4-CLint | µl/min/pmol | 1.8 ([Marzolini 2017](#5-references)) | Cytochrome-P450 3A4 mediated intrinsic clearance |
| CYP3A5-CLint | µl/min/pmol | 1.8 ([Marzolini 2017](#5-references)) | Cytochrome-P450 3A5 mediated intrinsic clearance |
| CYP2C8-CLint | µl/min/pmol | 3.6 ([Marzolini 2017](#5-references)) | Cytochrome-P450 2C8 mediated intrinsic clearance |
| CYP2C9-CLint | µl/min/pmol | 0.48 ([Marzolini 2017](#5-references)) | Cytochrome-P450 2C9 mediated intrinsic clearance |

** fe was matched by modeling unchanged renal excretion in PK-Sim as glomerular filtration (GF)

### 2.2.2 Clinical data

A literature search was performed to collect available clinical data on montelukast PK in adults. 

The following publications were found in adults for model building and evaluation:

| Publication                       | Study description                                            |
| :-------------------------------- | :----------------------------------------------------------- |
| [Cheng 1996](#5-references) | Pharmacokinetics, bioavailability, and safety of montelukast sodium (MK-0476) in healthy males and females |
| [Fey 2014](#5-references) | Bioequivalence of two formulations of montelukast sodium 4 mg oral granules in healthy adults |
| [Knorr 2000](#5-references) | Montelukast adult (10-mg film-coated tablet) and pediatric (5-mg chewable tablet) dose selections |
| [Zhao 1997](#5-references) | Pharmacokinetics and bioavailability of montelukast sodium (MK-0476) in healthy young and elderly volunteers |



## 2.3 Model parameters and assumptions
### 2.3.1 Absorption

Montelukast is a selective and orally active leukotriene receptor antagonist. For oral administration the following parameters play, amongst others, a role with regard to the absorption kinetics of a compound, which can be estimated with PBPK: solubility, lipophilicity and intestinal permeability. Montelukast is a strongly lipophilic drug. The final lipophilicity was estimated to be lower than the reported values, as with lipophilicity values above 3-4 log units the drug already reached maximal permeability levels.

### 2.3.2 Distribution

It has been determined that the protein binding of montelukast to plasma proteins exceeds 99% ([FDA drug label](#5-references)).  The fraction unbound (fu) of montelukast is built-in as 0.0018 as also reported by Marzolini et al. ([Marzolini 2017](#5-references)).

After testing the available organ-plasma partition coefficient and cell permeability calculation methods built-in in PK-Sim, observed clinical data was best described by choosing the partition coefficient calculation method by Rodgers and Rowland, and PK-Sim standard cell permeability calculation method. Specific organ permeability normalized to surface area was automatically calculated by PK-Sim.

### 2.3.3 Metabolism and Elimination

Montelukast is mainly metabolized by CYP2C8 (72%) ([Marzolini 2017](#5-references)).  The final montelukast model applies metabolism by CYP2C8, and to a minor involved clearance by the enzymes CYP3A4/5 (16%), CYP2C9 (12%) and glomerular filtration ([Marzolini 2017, Filppula 2011, Zhou 2017](#5-references)) and adequately described the pharmacokinetics of montelukast in adults.

# 3 Results and Discussion
The PBPK model for montelukast was developed with clinical pharmacokinetic data covering intravenous as well as oral administration with a dose range of 2-10mg including single dose and multiple dose clinical data, for different types of tablet formulations.

During the model fitting, the following parameters were estimated (all other parameters were fixed to reported values):

* Lipophilicity
* Specific intestinal permeability (transcellular)
* Formulation kinetics : Weibull function parameters (Dissolution shape and Dissolution time) for
  * Singular tablet
  * Sandoz tablet
  * Film-coated tablet
  * Chewable tablet

The fit resulted in an adequate description of the clinical data. Overall the model results show that the PBPK model of montelukast adequately described the data for intravenous administration for single dose. The estimated clearance values as a fraction of the reported clearance using only intravenous data resulted in a value close to 1, which allowed to fix the clearance parameters to the reported values. This was done to prevent the otherwise high correlation with the estimated absorption related parameters (dissolution kinetics for the different tablet formulations, lipophilicity and intestinal permeability during model building). 


## 3.1 Montelukast final input parameters
The compound parameter values of the final montelukast PBPK model are illustrated below.




### Formulation: Chewable tablet

Type: Weibull

#### Parameters

Name                             | Value             | Value Origin                                                                                                          
-------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------
Dissolution time (50% dissolved) | 70.3249031902 min | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 15' on 2019-03-21 11:13
Lag time                         | 0 min             |                                                                                                                       
Dissolution shape                | 1.2919957494      | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 15' on 2019-03-21 11:13
Use as suspension                | Yes               |                                                                                                                       



### Formulation: Filmcoated tablet

Type: Weibull

#### Parameters

Name                             | Value              | Value Origin                                                                                                          
-------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------
Dissolution time (50% dissolved) | 130.7856594083 min | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 15' on 2019-03-21 11:13
Lag time                         | 0 min              |                                                                                                                       
Dissolution shape                | 1.309742335        | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 15' on 2019-03-21 11:13
Use as suspension                | Yes                |                                                                                                                       



### Compound: Montelukast

#### Parameters

Name                                             | Value                  | Value Origin                                      | Alternative               | Default
------------------------------------------------ | ---------------------- | ------------------------------------------------- | ------------------------- | -------
Solubility at reference pH                       | 8.2E-06 mg/ml          | Internet-source: Drugbank (ALOGPS)                | Water Solubility (ALOGPS) | True   
Reference pH                                     | 7                      | Internet-source: Drugbank (ALOGPS)                | Water Solubility (ALOGPS) | True   
Lipophilicity                                    | 3.3153408097 Log Units | Parameter Identification-Parameter Identification | Fit                       | True   
Fraction unbound (plasma, reference value)       | 0.0018                 | Publication-Marzolini 2017                        | Marzolini 2017            | True   
Specific intestinal permeability (transcellular) | 0.0819181318 cm/min    | Parameter Identification-Parameter Identification | Fit                       | True   
Cl                                               | 1                      | Publication-Marzolini 2017                        |                           |        
Is small molecule                                | Yes                    |                                                   |                           |        
Molecular weight                                 | 586.2 g/mol            | Publication-Marzolini 2017                        |                           |        
Plasma protein binding partner                   | Albumin                |                                                   |                           |        


#### Calculation methods

Name                    | Value              
----------------------- | -------------------
Partition coefficients  | Rodgers and Rowland
Cellular permeabilities | PK-Sim Standard    


#### Processes

##### Metabolizing Enzyme: CYP2C8-Marzolini 2017

Molecule: CYP2C8

###### Parameters

Name                           | Value                       | Value Origin              
------------------------------ | --------------------------- | --------------------------
In vitro CL/recombinant enzyme | 3.6 µl/min/pmol rec. enzyme | Publication-Marzolini 2017


##### Metabolizing Enzyme: CYP3A4-Marzolini 2017

Molecule: CYP3A4

###### Parameters

Name                           | Value                       | Value Origin              
------------------------------ | --------------------------- | --------------------------
In vitro CL/recombinant enzyme | 1.8 µl/min/pmol rec. enzyme | Publication-Marzolini 2017


##### Metabolizing Enzyme: CYP2C9-Marzolini 2017

Molecule: CYP2C9

###### Parameters

Name                           | Value                        | Value Origin              
------------------------------ | ---------------------------- | --------------------------
In vitro CL/recombinant enzyme | 0.48 µl/min/pmol rec. enzyme | Publication-Marzolini 2017


##### Metabolizing Enzyme: CYP3A5-Filppula 2011

Molecule: CYP3A5

###### Parameters

Name                           | Value                        | Value Origin              
------------------------------ | ---------------------------- | --------------------------
In vitro CL/recombinant enzyme | 0.16 µl/min/pmol rec. enzyme | Publication-Marzolini 2017


##### Systemic Process: Glomerular Filtration-Marzolini 2017

Species: Human

###### Parameters

Name         | Value | Value Origin              
------------ | -----:| --------------------------
GFR fraction |     1 | Publication-Marzolini 2017



### Formulation: Sandoz Oral granules

Type: Weibull

#### Parameters

Name                             | Value             | Value Origin                                                                                                          
-------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------
Dissolution time (50% dissolved) | 96.1730639663 min | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 15' on 2019-03-21 11:13
Lag time                         | 0 min             |                                                                                                                       
Dissolution shape                | 1.9271553023      | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 15' on 2019-03-21 11:13
Use as suspension                | Yes               |                                                                                                                       



### Formulation: Singulair mini Oral granules

Type: Weibull

#### Parameters

Name                             | Value              | Value Origin                                                                                                          
-------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------
Dissolution time (50% dissolved) | 133.9238802749 min | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 15' on 2019-03-21 11:13
Lag time                         | 0 min              |                                                                                                                       
Dissolution shape                | 1.6357552071       | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 15' on 2019-03-21 11:13
Use as suspension                | Yes                |                                                                                                                       



## 3.2 Montelukast Diagnostics Plots
Below you find the goodness-of-fit visual diagnostic plots for montelukast PBPK model performance (Individually simulated versus observed plasma concentration and weighted residuals versus time, including the geometric mean fold error (GMFE)) of all data used for model building.

![001_plotGOFMergedPredictedVsObserved.png](images/003_3_Results_and_Discussion/002_3_2_Montelukast_Diagnostics_Plots/001_plotGOFMergedPredictedVsObserved.png)

![002_plotGOFMergedResidualsOverTime.png](images/003_3_Results_and_Discussion/002_3_2_Montelukast_Diagnostics_Plots/002_plotGOFMergedResidualsOverTime.png)

GMFE = 1.310087 

## 3.3 Montelukast Concentration-Time profiles
Simulated versus observed plasma concentration-time profiles of all data are listed below.


![001_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/001_plotTimeProfile.png)

![002_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/002_plotTimeProfile.png)

![003_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/003_plotTimeProfile.png)

![004_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/004_plotTimeProfile.png)

![005_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/005_plotTimeProfile.png)

![006_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/006_plotTimeProfile.png)

![007_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/007_plotTimeProfile.png)

![008_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/008_plotTimeProfile.png)

![009_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/009_plotTimeProfile.png)

![010_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/010_plotTimeProfile.png)

![011_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/011_plotTimeProfile.png)

![012_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/012_plotTimeProfile.png)

![013_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/013_plotTimeProfile.png)

![014_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/014_plotTimeProfile.png)

![015_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/015_plotTimeProfile.png)

![016_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/016_plotTimeProfile.png)

![017_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/017_plotTimeProfile.png)

![018_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/018_plotTimeProfile.png)

![019_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/019_plotTimeProfile.png)

![020_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/020_plotTimeProfile.png)

![021_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/021_plotTimeProfile.png)

![022_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/022_plotTimeProfile.png)

![023_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/023_plotTimeProfile.png)

![024_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3_Montelukast_Concentration-Time_profiles/024_plotTimeProfile.png)

# 4 Conclusion
The final montelukast PBPK model applies elimination mainly by CYP2C8 and adequately describes the pharmacokinetics of montelukast in adults receiving intravenous and oral SD and MD of montelukast ranging from 2-10mg, for different types of tablet formulations. 

This model could be applied for the investigation of drug-drug interactions (DDI), and translation to special populations such as pediatrics with regard to CYP2C8 based elimination.


# 5 References
**Cheng 1996** Cheng H, Leff JA, Amin R, Gertz BJ, De Smet M, Noonan N, Rogers JD, Malbecq W, Meisner D, Somers G. Pharmacokinetics, bioavailability, and safety of montelukast sodium (MK-0476) in healthy males and females. Pharm Res. 1996 Mar;13(3):445-8.

**Drugbank.ca** (https://www.drugbank.ca/drugs/DB00471 )

**FDA drug label** (https://www.merck.com/product/usa/pi_circulars/s/singulair/singulair_pi.pdf)

**Fey 2014** Fey C, Thyroff-Friesinger U, Jones S. Bioequivalence of two formulations of montelukast sodium 4 mg oral granules in healthy adults. Clin Transl Allergy. 2014 Sep 18;4:29. doi: 10.1186/2045-7022-4-29. eCollection 2014.

**Filppula 2011** Filppula AM, Laitila J, Neuvonen PJ, Backman JT. Reevaluation of the microsomal metabolism of montelukast: major contribution by CYP2C8 at clinically relevant concentrations. Drug Metab Dispos. 2011 May;39(5):904-11. doi: 10.1124/dmd.110.037689. Epub 2011 Feb 2.

**Knorr 2000** Knorr B, Holland S, Rogers JD, Nguyen HH, Reiss TF. Montelukast adult (10-mg film-coated tablet) and pediatric (5-mg chewable tablet) dose selections. J Allergy Clin Immunol. 2000 Sep;106(3 Suppl):S171-8

**Kuepfer 2016** Kuepfer L, Niederalt C, Wendl T, Schlender JF, Willmann S, Lippert J, Block M, Eissing T, Teutonico D. Applied Concepts in PBPK Modeling: How to Build a PBPK/PD Model.CPT Pharmacometrics Syst Pharmacol. 2016 Oct;5(10):516-531. doi: 10.1002/psp4.12134. Epub 2016 Oct 19.

**Marzolini 2017** Marzolini C, Rajoli R, Battegay M, Elzi L, Back D, Siccardi M. Efavirenz Involving Simultaneous Inducing and Inhibitory Effects on Cytochromes. Clin Pharmacokinet. 2017 Apr;56(4):409-420. doi: 10.1007/s40262-016-0447-7.

**PK-Sim Ontogeny Database Version 7.3** (https://github.com/Open-Systems-Pharmacology/OSPSuite.Documentation/blob/38cf71b384cfc25cfa0ce4d2f3addfd32757e13b/PK-Sim%20Ontogeny%20Database%20Version%207.3.pdf)

**Schlender 2016** Schlender JF, Meyer M, Thelen K, Krauss M, Willmann S, Eissing T, Jaehde U. Development of a Whole-Body Physiologically Based Pharmacokinetic Approach to Assess the Pharmacokinetics of Drugs in Elderly Individuals. Clin Pharmacokinet. 2016 Dec;55(12):1573-1589.

**Zhao 1997** Zhao JJ, Rogers JD, Holland SD, Larson P, Amin RD, Haesen R, Freeman A, Seiberling M, Merz M, Cheng H. Pharmacokinetics and bioavailability of montelukast sodium (MK-0476) in healthy young and elderly volunteers.Biopharm Drug Dispos. 1997 Dec;18(9):769-77

**Zhou 2017**  Zhou W, Johnson TN, Bui KH, Cheung SYA, Li J, Xu H, Al-Huniti N, Zhou D. Predictive Performance of Physiologically Based Pharmacokinetic (PBPK) Modeling of Drugs Extensively Metabolized by Major Cytochrome P450s in Children. Clin Pharmacol Ther. 2018 Jul;104(1):188-200. doi: 10.1002/cpt.905. Epub 2017 Nov 20.
