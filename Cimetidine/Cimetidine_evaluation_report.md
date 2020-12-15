# Building and evaluation of a PBPK model for cimetidine in healthy adults





| Version                                         | 1.0-OSP9.1                                                   |
| ----------------------------------------------- | ------------------------------------------------------------ |
| based on *Model Snapshot* and *Evaluation Plan* | https://github.com/Open-Systems-Pharmacology/Cimetidine-Model/releases/tag/v1.0 |
| OSP Version                                     | 9.1                                                          |
| Qualification Framework Version                 | 2.2                                                          |



This evaluation report and the corresponding PK-Sim project file are stored at:

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
    * [3.3: Concentration-Time Profiles](#33-concentration-time-profiles)
      * [3.3.1 Model Building](#331-model-building)
      * [3.3.2 Model Validation](#332-model-validation)
  * [4 Conclusion](#4-conclusion)
  * [5 References](#5-references)
# 1 Introduction
Cimetidine is a histamine H2 receptor antagonist that inhibits stomach acid production. It is mainly used as an antacid for the treatment of gastric and duodenal ulcers, Zollinger-Ellison syndrome and esophageal reflux.

The herein presented model was developed and published by Hanke et al. ([Hanke 2020](#5-References)).

Cimetidine is mainly excreted unchanged via the kidneys (40–80% of the dose) with a high renal clearance of 400 ml/min. Metabolism is reported to account for 25– 40% of of the total elimination of cimetidine, with less than 2% of the dose excreted unchanged with the bile. Cimetidine inhibits several transporters and CYP enzymes and it is recommended by the FDA as strong inhibitor of OCT2/MATE and as weak inhibitor of CYP3A4 and CYP2D6 for the use in clinical DDI studies and drug labeling.

The cimetidine model was established using 27 clinical studies, covering a dosing range from 100 to 800 mg. The final model applies active uptake of cimetidine into the liver by OCT1,
uptake into the kidney by OAT3 and secretion from the kidney into the urine by MATE1, as well
as an unspecific hepatic clearance and passive renal glomerular filtration.  

The herein presented model building and evaluation report evaluates the performance of the PBPK model for cimetidine in (healthy) adults. 



# 2 Methods


## 2.1 Modeling Strategy
The general concept of building a PBPK model has previously been described by e.g. Kuepfer et al. ([Kuepfer 2016](#5-References)). The relevant anthropometric (height, weight) and physiological information (e.g. blood flows, organ volumes, binding protein concentrations, hematocrit, cardiac output) in adults was gathered from the literature and has been previously published ([Willmann 2007](#5-References)). This information was incorporated into PK-Sim® and was used as default values for the simulations in adults.

Variability of plasma proteins and CYP enzymes are integrated into PK-Sim® and described in the publicly available PK-Sim® Ontogeny Database Version 7.3 ([PK-Sim Ontogeny Database Version 7.3](#5-References)) or otherwise referenced for the specific process. The final model applies active uptake of cimetidine into the liver by OCT1, uptake into the kidney by OAT3 and secretion from the kidney into the urine by MATE1, as well
as an unspecific hepatic clearance and passive renal glomerular filtration. The transporters were integrated into the PBPK model using the ([PK-Sim Ontogeny Database Version 7.3](#5-References)) and is described in detail in [Hanke 2020](#5-References).

First, a base PBPK model was built using clinical data including single and multiple dose studies with intravenous and oral applications of cimetidine to find an appropriate structure to describe the pharmacokinetics in plasma. This PBPK model was developed using a typical European individual adjusted to the demography of the respective study population. 

Oral administration of cimetidine in the fasted state frequently produces two plasma concentrations peaks. These double peaks are probably caused by the phasic gastrointestinal motility that controls gastric emptying in the fasted state. To describe the very different shapes of the observed mean cimetidine plasma profiles, split dose administration protocols for all studies of cimetidine administered orally in the fasted state were optimized in a NONMEM analysis (see [Hanke 2020](#5-References)). The resulting split dose administration protocols were then implemented and used for the PBPK modeling of the respective cimetidine studies.

Unknown parameters (see below) were identified using the Parameter Identification module provided in PK-Sim®. Structural model selection was mainly guided by visual inspection of the resulting description of data and biological plausibility.

Details about input data (physicochemical, *in vitro* and clinical) can be found in  [Section 2.2](#22-Data).

Details about the structural model and its parameters can be found in [Section 2.3](#23-Model-Parameters-and-Assumptions).

## 2.2 Data
### 2.2.1 In vitro / physico-chemical Data

A literature search was performed to collect available information on physiochemical properties of cimetidine. The obtained information from literature is summarized in the table below. 

| **Parameter**   | **Unit** | **Value**       | Source                                                       | **Description**                                 |
| :-------------- | -------- | --------------- | ------------------------------------------------------------ | ----------------------------------------------- |
| MW              | g/mol    | 252.34    | [Wishart 2006](#5-References) | Molecular weight                                |
| pK<sub>a</sub>1 | 6.93  | (base)          | [Avdeef 2001](#5-References)                       | Acid dissociation constant                      |
| pK<sub>a</sub>2 | 13.38  | (acid)          | [Wishart 2006](#5-References)                    | Acid dissociation constant                      |
| Solubility (pH) | mg/L     | 24.00 (6.8) | [Avdeef 2001](#5-References) | Water solubility                               |
| logP            |          | 0.48 | [Avdeef 2001](#5-References) | Partition coefficient between octanol and water |
| f<sub>u</sub> |   %      | 78.00 | [Taylor 1978](#5-References) | Fraction unbound in plasma                      |
| B/P ratio              |         | 0.98 | [Somogyi 1983](#5-References) | Blood to plasma ratio        |
| OCT1 K<sub>m</sub> | μmol/l | 2600 | [Umehara 2007](#5-References) | Michaelis-Menten constant |
| OAT3 K<sub>m</sub> | µmol/l | 149     | [Tahara 2005](#5-References) | Michaelis-Menten constant |
| MATE1 K<sub>m</sub> | µmol/l | 8.0 | [Ohta 2005](#5-References) | Michaelis-Menten constant |
| OCT1 K<sub>i</sub> | µmol/l | 104     | [Ito 2012](#5-References) | Inhibition constant for competitive inhibition |
| OCT2 K<sub>i</sub> | µmol/l | 124 | [Ito 2012](#5-References) | Inhibition constant for competitive inhibition |
| MATE1 K<sub>i</sub> | µmol/l | 3.8     | [Ito 2012](#5-References) | Inhibition constant for competitive inhibition |
| CYP3A4 K<sub>i</sub> | µmol/l | 268     | [Wrighton 1994](#5-References) | Inhibition constant for competitive inhibition |


### 2.2.2 Clinical Data

A literature search was performed to collect available clinical data on efavirenz in healthy adults.

#### 2.2.2.1 Model Building

The following studies were used for model building:

| Publication                       | Arm / Treatment / Information used for model building        |
| :-------------------------------- | :----------------------------------------------------------- |
| [Bodemar 1981](#5-References)     | Peptic ulcer patients receiving a single intravenous dose of 200 mg and oral doses of 200, 400 and 800 mg |
| [Morgan 1983](#5-References)      | Peptic ulcer patients receiving a single intravenous dose of 200 mg (5 min infusion) |
| [Bodemar 1979](#5-References)     | Healthy subjects receiving single oral doses of 200 and 400mg (tablet) |
| [Walkenstein 1978](#5-References) | Healthy subjects receiving a single oral dose of 300mg (solution) |
| [D'Angio 1986](#5-References)     | Healthy subjects receiving a single oral dose of 300mg (tablet) |



#### 2.2.2.2 Model verification

The following studies were used for model verification:

| Publication                       | Arm / Treatment / Information used for model verification    |
| :-------------------------------- | :----------------------------------------------------------- |
| [Grahnen 1979](#5-References)     | Healthy subjects receiving a single intravenous dose of 100 mg and a single oral dose of 400 mg (tablet) |
| [Larsson 1982](#5-References)     | Peptic ulcer patients receiving a single intravenous dose of 200 mg |
| [Mihaly  1984](#5-References)     | Peptic ulcer patients receiving a single intravenous and a single oral dose of 200 mg |
| [Morgan 1983](#5-References)      | Peptic ulcer patients receiving a single intravenous dose of 200 mg (30 min infusion) |
| [Lebert 1981](#5-References)      | Healthy subjects receiving a single intravenous dose of 300 mg (2 min infusion) |
| [Walkenstein 1978](#5-References) | Healthy subjects receiving a single intravenous dose of 300 mg (2 min infusion) and a single oral dose of 300 mg (tablet) |
| [Kanto 1981](#5-References)       | Healthy subjects receiving a single oral dose of 200 mg      |
| [Burland 1975](#5-References)     | Healthy subjects receiving single oral doses of 200 mg solution and capsule |
| [Bodemar 1979](#5-References)     | Peptic ulcer patients receiving a single oral dose of 200 mg (tablet) |
| [Bodemar 1981](#5-References)     | Peptic ulcer patients receiving single oral doses of 800 mg and multiple oral doses of 200 and 400 mg |
| [Barbhaiya 1995](#5-References)   | Healthy subjects receiving multiple oral doses of 300 mg (tablet) |
| [Somogyi 1981](#5-References)     | Healthy subjects receiving a single oral dose of 400 mg (tablet) |
| [Tiseo 1998](#5-References)       | Healthy subjects receiving multiple oral doses of 800 mg (tablet) |

## 2.3 Model Parameters and Assumptions
### 2.3.1 Absorption

Absorption observed in clinical studies can be fully explained by passive absorption.

### 2.3.2 Distribution

Cimetidine is reported to be actively taken up into the liver by OCT1 ([Umehara 2007](#5-References)), into the kidney by OAT3 ([Tahara 2005](#5-References)) and secreted from the kidney into the urine by MATE1 ([Ohta 2010](#5-References)).

After testing the available organ-plasma partition coefficient and cell permeability calculation methods built in PK-Sim, observed clinical data was best described by choosing the partition coefficient calculation method by `Rodgers and Rowland` and cellular permeability calculation by `PK-Sim Standard`. 

A `Lipophilicity` of 1.66 was back-calculated from the blood-to-plasma ratio of 0.98 ([Somogyi 1983](#5-References), [Hanke 2020](#5-References)).



### 2.3.3 Metabolism, Elimination and Inhibition

Cimetidine is mainly excreted unchanged via the kidneys. Additionally, 25 to 40 % is hepatically metabolized via an unknown pathway. 

Cimetidine inhibits several enzymes such as CYP3A4 and CYP2D6 as well as transporters such as OCT2, OCT2 and MATE.

### 2.3.4 Automated Parameter Identification

The parameter identification tool in PK-Sim has been used to estimate selected model parameters by adjusting to PK data of the clinical studies that were used in the model building process (see [Section 2.2](#22-Data)). 

The result of the final parameter identification is shown in the table below:

| Model Parameter            | Optimized Value | Unit |
| -------------------------- | --------------- | ---- |
| Specific intestinal permeability | 8.72E-7 | cm/min |
| CLhep | 0.16 | 1/min |
| kcat OCT1 | 8.66E+4 | 1/min |
| kcat OAT3 | 5.75E+07 | 1/min |
| kcat MATE1 | 32.37 | 1/min |


# 3 Results and Discussion
The PBPK model for efavirenz was developed and evaluated using publicly available clinical pharmacokinetic data from studies listed in [Section 2.2.2](#222-Clinical-Data).

The next sections show:

1. the final model parameters for the building blocks: [Section 3.1](#31-Final-Input-Parameters).
2. the overall goodness of fit: [Section 3.2](#32-Diagnostics-Plots).
3. simulated vs. observed concentration-time profiles for the clinical studies used for model building and for model verification: [Section 3.3](#33-Concentration-Time-Profiles).


## 3.1 Final input parameters
The compound parameter values of the final PBPK model are illustrated below.




### Compound: Cimetidine

#### Parameters

Name                                             | Value                   | Value Origin             | Alternative | Default
------------------------------------------------ | ----------------------- | ------------------------ | ----------- | -------
Solubility at reference pH                       | 24 mg/ml                | Publication-Avdeef 2001  | Measurement | True   
Reference pH                                     | 6.8                     | Publication-Avdeef 2001  | Measurement | True   
Lipophilicity                                    | 1.655 Log Units         | Parameter Identification | Measurement | True   
Fraction unbound (plasma, reference value)       | 0.78                    | Publication-Taylor 1978  | Measurement | True   
Specific intestinal permeability (transcellular) | 8.7196061807E-07 cm/min | Parameter Identification | Fit         | True   
Is small molecule                                | Yes                     |                          |             |        
Molecular weight                                 | 252.34 g/mol            | Database-Drugbank        |             |        
Plasma protein binding partner                   | Unknown                 |                          |             |        
#### Calculation methods

Name                    | Value              
----------------------- | -------------------
Partition coefficients  | Rodgers and Rowland
Cellular permeabilities | PK-Sim Standard    
#### Processes

##### Systemic Process: Total Hepatic Clearance-Somogyi 1983

Species: Human
###### Parameters

Name                          | Value              | Value Origin            
----------------------------- | ------------------ | ------------------------
Fraction unbound (experiment) | 0.78               |                         
Lipophilicity (experiment)    | 1.655 Log Units    |                         
Plasma clearance              | 0 ml/min/kg        |                         
Specific clearance            | 0.1600808777 1/min | Parameter Identification
##### Transport Protein: MATE1-Paper

Molecule: MATE1
###### Parameters

Name                      | Value              | Value Origin            
------------------------- | ------------------ | ------------------------
Transporter concentration | 1 µmol/l           |                         
Vmax                      | 0 µmol/l/min       |                         
Km                        | 8 µmol/l           | Parameter Identification
kcat                      | 32.371673382 1/min | Parameter Identification
##### Transport Protein: OAT3-Paper

Molecule: OAT3
###### Parameters

Name                      | Value             | Value Origin            
------------------------- | ----------------- | ------------------------
Transporter concentration | 1 µmol/l          |                         
Vmax                      | 0 µmol/l/min      |                         
Km                        | 149 µmol/l        | Publication-Tahara 2005 
kcat                      | 57506485.67 1/min | Parameter Identification
##### Transport Protein: OCT1-Paper

Molecule: OCT1
###### Parameters

Name                      | Value                  | Value Origin            
------------------------- | ---------------------- | ------------------------
Transporter concentration | 1 µmol/l               |                         
Vmax                      | 0 µmol/l/min           |                         
Km                        | 2600 µmol/l            | Publication-Umehara 2007
kcat                      | 86599.4219923521 1/min | Parameter Identification
##### Systemic Process: Glomerular Filtration-GFR

Species: Human
###### Parameters

Name         | Value | Value Origin
------------ | -----:| ------------:
GFR fraction |     1 |             
##### Inhibition: OCT1-Ito 2012

Molecule: OCT1
###### Parameters

Name | Value      | Value Origin        
---- | ---------- | --------------------
Ki   | 104 µmol/l | Publication-Ito 2012
##### Inhibition: OCT2-Ito 2012

Molecule: OCT2
###### Parameters

Name | Value      | Value Origin        
---- | ---------- | --------------------
Ki   | 124 µmol/l | Publication-Ito 2012
##### Inhibition: MATE1-Ito 2012

Molecule: MATE1
###### Parameters

Name | Value      | Value Origin         
---- | ---------- | ---------------------
Ki   | 3.8 µmol/l | Other-NBI measurement
##### Inhibition: CYP3A4-Wrighton 1994

Molecule: CYP3A4
###### Parameters

Name | Value      | Value Origin
---- | ---------- | ------------:
Ki   | 268 µmol/l |             

### Formulation: Tablet

Type: Weibull
#### Parameters

Name                             | Value | Value Origin
-------------------------------- | ----- | ------------:
Dissolution time (50% dissolved) | 1 min |             
Lag time                         | 0 h   |             
Dissolution shape                | 10    |             
Use as suspension                | Yes   |             

## 3.2 Diagnostics Plots
Below you find the goodness-of-fit visual diagnostic plots for the PBPK model performance of all data used presented in [Section 2.2.2](#222-Clinical-Data).

The first plot shows simulated versus observed plasma concentration, the second weighted residuals versus time. 


![001_plotGOFMergedPredictedVsObserved.png](images/003_3_Results_and_Discussion/002_3_2_Diagnostics_Plots/001_plotGOFMergedPredictedVsObserved.png)

![002_plotGOFMergedResidualsOverTime.png](images/003_3_Results_and_Discussion/002_3_2_Diagnostics_Plots/002_plotGOFMergedResidualsOverTime.png)

GMFE = 1.530217 

## 3.3: Concentration-Time Profiles
Simulated versus observed concentration-time profiles of all data listed in [Section 2.2.2](#222-Clinical-Data) are presented below.


### 3.3.1 Model Building





![001_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/001_3_3_1_Model_Building/001_plotTimeProfile.png)

![002_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/001_3_3_1_Model_Building/002_plotTimeProfile.png)

![003_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/001_3_3_1_Model_Building/003_plotTimeProfile.png)

![004_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/001_3_3_1_Model_Building/004_plotTimeProfile.png)

![005_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/001_3_3_1_Model_Building/005_plotTimeProfile.png)

![006_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/001_3_3_1_Model_Building/006_plotTimeProfile.png)

![007_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/001_3_3_1_Model_Building/007_plotTimeProfile.png)

![008_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/001_3_3_1_Model_Building/008_plotTimeProfile.png)

![009_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/001_3_3_1_Model_Building/009_plotTimeProfile.png)

![010_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/001_3_3_1_Model_Building/010_plotTimeProfile.png)

![011_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/001_3_3_1_Model_Building/011_plotTimeProfile.png)

![012_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/001_3_3_1_Model_Building/012_plotTimeProfile.png)

### 3.3.2 Model Validation



![001_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/001_plotTimeProfile.png)

![002_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/002_plotTimeProfile.png)

![003_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/003_plotTimeProfile.png)

![004_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/004_plotTimeProfile.png)

![005_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/005_plotTimeProfile.png)

![006_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/006_plotTimeProfile.png)

![007_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/007_plotTimeProfile.png)

![008_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/008_plotTimeProfile.png)

![009_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/009_plotTimeProfile.png)

![010_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/010_plotTimeProfile.png)

![011_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/011_plotTimeProfile.png)

![012_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/012_plotTimeProfile.png)

![013_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/013_plotTimeProfile.png)

![014_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/014_plotTimeProfile.png)

![015_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/015_plotTimeProfile.png)

![016_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/016_plotTimeProfile.png)

![017_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/017_plotTimeProfile.png)

![018_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/018_plotTimeProfile.png)

![019_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/019_plotTimeProfile.png)

![020_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/020_plotTimeProfile.png)

![021_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/021_plotTimeProfile.png)

![022_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/022_plotTimeProfile.png)

![023_plotTimeProfile.png](images/003_3_Results_and_Discussion/003_3_3__Concentration-Time_Profiles/002_3_3_2_Model_Validation/023_plotTimeProfile.png)

# 4 Conclusion
The herein presented PBPK model adequately describes the pharmacokinetics of cimetidine after intravenous and oral administration of single and multiple doses to healthy adults and peptic ulcer patients covering a broad dosing range from 100 to 800 mg. The established cimetidine PBPK model is verified for the use as a mild inhibitor of CYP3A4 drug in drug-drug interaction simulations.

# 5 References
**Avdeef 2001** Avdeef A, Berger CM. pH-metric solubility. 3. Dissolution titration  template method for solubility determination. Eur J Pharm Sci. 2001  Dec;14(4):281-91. doi: 10.1016/s0928-0987(01)00190-7. PMID: 11684402.

**Barbhaiya 1995** Barbhaiya RH, Shukla UA, Greene DS. Lack of interaction between  nefazodone and cimetidine: a steady state pharmacokinetic study in  humans. Br J Clin Pharmacol. 1995 Aug;40(2):161-5. doi:  10.1111/j.1365-2125.1995.tb05771.x. PMID: 8562300; PMCID: PMC1365177.

**Bodemar 1979** Bodemar G,  Norlander B, Fransson L, Walan A. The absorption of cimetidine before  and during maintenance treatment with cimetidine and the influence of a  meal on the absorption of cimetidine--studies in patients with peptic  ulcer disease. Br J Clin Pharmacol. 1979 Jan;7(1):23-31. doi:  10.1111/j.1365-2125.1979.tb00892.x. PMID: 760739; PMCID: PMC1429608.

**Bodemar 1981** Bodemar G, Norlander B, Walan A. Pharmacokinetics of cimetidine after  single doses and during continuous treatment. Clin Pharmacokinet. 1981  Jul-Aug;6(4):306-15. doi: 10.2165/00003088-198106040-00005. PMID:  7249489.

**Burland 1975** Burland WL, Duncan WA, Hesselbo T, Mills JG, Sharpe PC, Haggie SJ,  Wyllie JH. Pharmacological evaluation of cimetidine, a new histamine  H2-receptor antagonist, in healthy man. Br J Clin Pharmacol. 1975  Dec;2(6):481-6. doi: 10.1111/j.1365-2125.1975.tb00564.x. PMID: 9952;  PMCID: PMC1402643.

**D'Angio 1986** D'Angio R, Mayersohn M, Conrad KA, Bliss M. Cimetidine absorption in  humans during sucralfate coadministration. Br J Clin Pharmacol. 1986  May;21(5):515-20. doi: 10.1111/j.1365-2125.1986.tb02834.x. PMID:  3755052; PMCID: PMC1401033.

**Fee 1987** Fee JP, Collier PS, Howard PJ, Dundee JW. Cimetidine and ranitidine increase midazolam  bioavailability. Clin Pharmacol Ther. 1987 Jan;41(1):80-4. doi:  10.1038/clpt.1987.13. PMID: 3802710.

**Grahnen 1979** Grahnén A, von Bahr C, Lindström B, Rosén A. Bioavailability and  pharmacokinetics of cimetidine. Eur J Clin Pharmacol. 1979  Nov;16(5):335-40. doi: 10.1007/BF00605632. PMID: 520401.

**Greenblatt 1986** Greenblatt DJ, Locniskar A, Scavone JM, Blyden GT, Ochs HR, Harmatz JS,  Shader RI. Absence of interaction of cimetidine and ranitidine with  intravenous and oral midazolam. Anesth Analg. 1986 Feb;65(2):176-80.  PMID: 2935051.

**Ito 2012** Ito S, Kusuhara H,  Yokochi M, Toyoshima J, Inoue K, Yuasa H, Sugiyama Y. Competitive  inhibition of the luminal efflux by multidrug and toxin extrusions, but  not basolateral uptake by organic cation transporter 2, is the likely  mechanism underlying the pharmacokinetic drug-drug interactions caused  by cimetidine in the kidney. J Pharmacol Exp Ther. 2012  Feb;340(2):393-403. doi: 10.1124/jpet.111.184986. Epub 2011 Nov 9. PMID: 22072731.

**Kanto 1981** Kanto J, Allonen H, Jalonen H, Mäntylä R. The effect of metoclopramide  and propantheline on the gastrointestinal absorption of cimetidine. Br J Clin Pharmacol. 1981 Jun;11(6):629-31. doi:  10.1111/j.1365-2125.1981.tb01184.x. PMID: 7272182; PMCID: PMC1402204.

**Kuepfer 2016** Kuepfer L, Niederalt C, Wendl T, Schlender JF, Willmann S, Lippert J, Block M, Eissing T, Teutonico D. Applied Concepts in PBPK Modeling: How to Build a PBPK/PD Model.CPT Pharmacometrics Syst Pharmacol. 2016 Oct;5(10):516-531.

**Larsson 1982** Larsson R, Erlanson P, Bodemar G, Walan A, Bertler A, Fransson L,  Norlander B. The pharmacokinetics of cimetidine and its sulphoxide  metabolite in patients with normal and impaired renal function. Br J  Clin Pharmacol. 1982 Feb;13(2):163-70. doi:  10.1111/j.1365-2125.1982.tb01351.x. PMID: 7059413; PMCID: PMC1402003.

**Lebert 1981** Lebert PA, Mahon  WA, MacLeod SM, Soldin SJ, Fenje P, Vandenberghe HM. Ranitidine kinetics and dynamics. II. Intravenous dose studies and comparison with  cimetidine. Clin Pharmacol Ther. 1981 Oct;30(4):545-50. doi:  10.1038/clpt.1981.201. PMID: 6269789.

**Martinez  1999** Martínez C, Albet  C, Agúndez JA, Herrero E, Carrillo JA, Márquez M, Benítez J, Ortiz JA.  Comparative in vitro and in vivo inhibition of cytochrome P450 CYP1A2,  CYP2D6, and CYP3A by H2-receptor antagonists. Clin Pharmacol Ther. 1999  Apr;65(4):369-76. doi: 10.1016/S0009-9236(99)70129-3. PMID: 10223772.

**Meyer 2012** Meyer M, Schneckener S, Ludewig B, Kuepfer L, Lippert J. Using expression data for quantification of active processes in physiologically based pharmacokinetic modeling. Drug Metab Dispos. 2012 May;40(5):892-901.

**Mihaly  1984** Mihaly GW, Jones DB, Anderson JA, Smallwood RA, Louis WJ.  Pharmacokinetic studies of cimetidine and ranitidine before and after  treatment in peptic ulcer patients. Br J Clin Pharmacol. 1984  Jan;17(1):109-11. doi: 10.1111/j.1365-2125.1984.tb05010.x. PMID:  6318788; PMCID: PMC1463299.

**Morgan 1983** Morgan DJ, Uccellini DA, Raymond K, Mihaly GW, Jones DB, Smallwood RA.  The influence of duration of intravenous infusion of an acute dose on  plasma concentrations of cimetidine. Eur J Clin Pharmacol.  1983;25(1):29-34. doi: 10.1007/BF00544010. PMID: 6617722.

**Nishimura 2013** Nishimura M, Yaguti H, Yoshitsugu H, Naito S, Satoh T. Tissue distribution of mRNA expression of human cytochrome P450 isoforms assessed by high-sensitivity real-time reverse transcription PCR. Yakugaku Zasshi. 2003 May;123(5):369-75.

**Ohta 2005** Ohta KY, Inoue K, Yasujima T, Ishimaru M, Yuasa H. Functional  characteristics of two human MATE transporters: kinetics of cimetidine  transport and profiles of inhibition by various compounds. J Pharm Pharm Sci. 2009;12(3):388-96. doi: 10.18433/j3r59x. PMID: 20067714.

**PK-Sim Ontogeny Database Version 7.3** (https://github.com/Open-Systems-Pharmacology/OSPSuite.Documentation/blob/38cf71b384cfc25cfa0ce4d2f3addfd32757e13b/PK-Sim%20Ontogeny%20Database%20Version%207.3.pdf)

**Salonen 1986** Salonen M, Aantaa  E, Aaltonen L, Kanto J. Importance of the interaction of midazolam and  cimetidine. Acta Pharmacol Toxicol (Copenh). 1986 Feb;58(2):91-5. doi:  10.1111/j.1600-0773.1986.tb00076.x. PMID: 2939688.

**Smith  1984** Smith MS, Benyunes  MC, Bjornsson TD, Shand DG, Pritchett EL. Influence of cimetidine on  verapamil kinetics and dynamics. Clin Pharmacol Ther. 1984  Oct;36(4):551-4. doi: 10.1038/clpt.1984.218. PMID: 6478741.

**Somogyi 1981** Somogyi A, Thielscher S, Gugler R. Influence of phenobarbital treatment  on cimetidine kinetics. Eur J Clin Pharmacol. 1981;19(5):343-7. doi:  10.1007/BF00544584. PMID: 7238562.

**Somogyi 1983** Somogyi A, Gugler R. Clinical pharmacokinetics of cimetidine. Clin  Pharmacokinet. 1983 Nov-Dec;8(6):463-95. doi:  10.2165/00003088-198308060-00001. PMID: 6418428.

**Tahara 2005** Tahara H, Kusuhara H, Endou H, Koepsell H, Imaoka T, Fuse E, Sugiyama Y. A species difference in the transport activities of H2 receptor  antagonists by rat and human renal organic anion and cation  transporters. J Pharmacol Exp Ther. 2005 Oct;315(1):337-45. doi:  10.1124/jpet.105.088104. Epub 2005 Jul 8. PMID: 16006492.

**Taylor 1978** Taylor DC, Cresswell PR, Bartlett DC. The metabolism and elimination of  cimetidine, a histamine H2-receptor antagonist, in the rat, dog, and  man. Drug Metab Dispos. 1978 Jan-Feb;6(1):21-30. PMID: 23270.

**Tiseo 1998** Tiseo PJ, Perdomo CA, Friedhoff LT. Concurrent administration of  donepezil HCl and cimetidine: assessment of pharmacokinetic changes  following single and multiple doses. Br J Clin Pharmacol. 1998 Nov;46  Suppl 1(Suppl 1):25-9. doi: 10.1046/j.1365-2125.1998.0460s1025.x. PMID:  9839762; PMCID: PMC1873814.

**Umehara 2007** Umehara KI, Iwatsubo T, Noguchi K, Kamimura H. Functional involvement of organic cation transporter1 (OCT1/Oct1) in the hepatic uptake of  organic cations in humans and rats. Xenobiotica. 2007 Aug;37(8):818-31.  doi: 10.1080/00498250701546012. PMID: 17701831.

**Walkenstein 1978** Walkenstein SS, Dubb JW, Randolph WC, Westlake WJ, Stote RM, Intoccia  AP. Bioavailability of cimetidine in man. Gastroenterology. 1978  Feb;74(2 Pt 2):360-5. PMID: 620910.

**Willmann 2007** Willmann S, Höhn K, Edginton A, Sevestre M, Solodenko J, Weiss W, Lippert J, Schmitt W. Development of a physiology-based whole-body population model for assessing the influence of individual variability on the pharmacokinetics of drugs. J Pharmacokinet Pharmacodyn. 2007, 34(3): 401-431.

**Wishart 2006** Wishart DS, Knox C, Guo AC, Shrivastava S, Hassanali M, Stothard P,  Chang Z, Woolsey J. DrugBank: a comprehensive resource for in silico  drug discovery and exploration. Nucleic Acids Res. 2006 Jan  1;34(Database issue):D668-72. doi: 10.1093/nar/gkj067. PMID: 16381955;  PMCID: PMC1347430.

**Wrighton 1994** Wrighton SA, Ring  BJ. Inhibition of human CYP3A catalyzed 1'-hydroxy midazolam formation  by ketoconazole, nifedipine, erythromycin, cimetidine, and nizatidine.  Pharm Res. 1994 Jun;11(6):921-4. doi: 10.1023/a:1018906614320. PMID:  7937537.


