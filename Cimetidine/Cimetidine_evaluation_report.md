# Building and evaluation of a PBPK model for cimetidine in healthy adults

| Version                                         | 2.0-OSP12.1                                                   |
| ----------------------------------------------- | ------------------------------------------------------------ |
| based on *Model Snapshot* and *Evaluation Plan* | https://github.com/Open-Systems-Pharmacology/Cimetidine-Model/releases/tag/v2.0 |
| OSP Version                                     | 12.1                                                          |
| Qualification Framework Version                 | 3.4                                                          |

This evaluation report and the corresponding PK-Sim project file are stored at:

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
     * [3.3.2 Model Validation](#model-validation)
 * [4 Conclusion](#conclusion)
 * [5 References](#main-references)

# 1 Introduction<a id="introduction"></a>

Cimetidine is a histamine H2 receptor antagonist that inhibits stomach acid production. It is mainly used as an antacid for the treatment of gastric and duodenal ulcers, Zollinger-Ellison syndrome and esophageal reflux.

The herein presented model was developed and published by Hanke et al. ([Hanke 2020](#5-references)) and adjusted later on to PK-Sim V10 by refitting CYP3A4 K<sub>i</sub> and MATE1 K<sub>i</sub>.

Cimetidine is mainly excreted unchanged via the kidneys (40–80% of the dose) with a high renal clearance of 400 ml/min. Metabolism is reported to account for 25– 40% of of the total elimination of cimetidine, with less than 2% of the dose excreted unchanged with the bile. Cimetidine inhibits several transporters and CYP enzymes and it is recommended by the FDA as strong inhibitor of OCT2/MATE and as weak inhibitor of CYP3A4 and CYP2D6 for the use in clinical DDI studies and drug labeling.

The cimetidine model was established using 27 clinical studies, covering a dosing range from 100 to 800 mg. The final model applies active uptake of cimetidine into the liver by OCT1,
uptake into the kidney by OAT3 and secretion from the kidney into the urine by MATE1, as well
as an unspecific hepatic clearance and passive renal glomerular filtration.

The herein presented model building and evaluation report evaluates the performance of the PBPK model for cimetidine in (healthy) adults. 

# 2 Methods<a id="methods"></a>

## 2.1 Modeling Strategy<a id="modeling-strategy"></a>

The general concept of building a PBPK model has previously been described by e.g. Kuepfer et al. ([Kuepfer 2016](#5-references)). The relevant anthropometric (height, weight) and physiological information (e.g. blood flows, organ volumes, binding protein concentrations, hematocrit, cardiac output) in adults was gathered from the literature and has been previously published ([Willmann 2007](#5-references)). This information was incorporated into PK-Sim® and was used as default values for the simulations in adults. Variability of plasma proteins and CYP enzymes are integrated into PK-Sim® and described in the publicly available PK-Sim® Ontogeny Database Version 7.3 ([PK-Sim Ontogeny Database Version 7.3](#5-references)) or otherwise referenced for the specific process. 

The final model applies active uptake of cimetidine into the liver by OCT1, uptake into the kidney by OAT3 and secretion from the kidney into the urine by MATE1, as well
as an unspecific hepatic clearance and passive renal glomerular filtration. The transporters were integrated into the PBPK model using the ([PK-Sim Ontogeny Database Version 7.3](#5-references)) and is described in detail in [Hanke 2020](#5-references). For PK-Sim V10, CYP3A4 K<sub>i</sub> and MATE1 K<sub>i</sub> were adjusted to improve the performance in CYP3A4 and MATE1 interaction scenarios. For further details, see [Section 2.3](#23-model-parameters-and-assumptions).

First, a base PBPK model was built using clinical data including single and multiple dose studies with intravenous and oral applications of cimetidine to find an appropriate structure to describe the pharmacokinetics in plasma. This PBPK model was developed using a typical European individual adjusted to the demography of the respective study population.

Oral administration of cimetidine in the fasted state frequently produces two plasma concentrations peaks. These double peaks are probably caused by the phasic gastrointestinal motility that controls gastric emptying in the fasted state. To describe the very different shapes of the observed mean cimetidine plasma profiles, split dose administration protocols for all studies of cimetidine administered orally in the fasted state were optimized in a NONMEM analysis (see [Hanke 2020](#5-references)). The resulting split dose administration protocols were then implemented and used for the PBPK modeling of the respective cimetidine studies.

Unknown parameters (see below) were identified using the Parameter Identification module provided in PK-Sim®. Structural model selection was mainly guided by visual inspection of the resulting description of data and biological plausibility.

Details about input data (physicochemical, *in vitro* and clinical) can be found in  [Section 2.2](#22-data).

Details about the structural model and its parameters can be found in [Section 2.3](#23-model-parameters-and-assumptions).

## 2.2 Data<a id="data"></a>

### 2.2.1 In vitro / physico-chemical Data

A literature search was performed to collect available information on physiochemical properties of cimetidine. The obtained information from literature is summarized in the table below. 

| **Parameter**   | **Unit** | **Value**       | Source                                                       | **Description**                                 |
| :-------------- | -------- | --------------- | ------------------------------------------------------------ | ----------------------------------------------- |
| MW              | g/mol    | 252.34    | [Wishart 2006](#5-references) | Molecular weight                                |
| pK<sub>a</sub>1 | 6.93  | (base)          | [Avdeef 2001](#5-references)                       | Acid dissociation constant                      |
| pK<sub>a</sub>2 | 13.38  | (acid)          | [Wishart 2006](#5-references)                    | Acid dissociation constant                      |
| Solubility (pH) | mg/L     | 24.00 (6.8) | [Avdeef 2001](#5-references) | Water solubility                               |
| logP            |          | 0.48 | [Avdeef 2001](#5-references) | Partition coefficient between octanol and water |
| f<sub>u</sub> |   %      | 78.00 | [Taylor 1978](#5-references) | Fraction unbound in plasma                      |
| B/P ratio              |         | 0.98 | [Somogyi 1983](#5-references) | Blood to plasma ratio        |
| OCT1 K<sub>m</sub> | μmol/l | 2600 | [Umehara 2007](#5-references) | Michaelis-Menten constant |
| OAT3 K<sub>m</sub> | µmol/l | 149     | [Tahara 2005](#5-references) | Michaelis-Menten constant |
| MATE1 K<sub>m</sub> | µmol/l | 8.0 | [Ohta 2005](#5-references) | Michaelis-Menten constant |
| OCT1 K<sub>i</sub> | µmol/l | 104     | [Ito 2012](#5-references) | Inhibition constant for competitive inhibition |
| OCT2 K<sub>i</sub> | µmol/l | 124 | [Ito 2012](#5-references) | Inhibition constant for competitive inhibition |
| MATE1 K<sub>i</sub> (refitted in PK-Sim V10) | µmol/l | 3.8 (0.65) | [Ito 2012](#5-references) | Inhibition constant for competitive inhibition |
| CYP3A4 K<sub>i</sub> (refitted in PK-Sim V10) | µmol/l | 268 (30.51266) | [Wrighton 1994](#5-references) | Inhibition constant for competitive inhibition |

### 2.2.2 Clinical Data

A literature search was performed to collect available clinical data on efavirenz in healthy adults.

#### 2.2.2.1 Model Building

The following studies were used for model building:

| Publication                       | Arm / Treatment / Information used for model building        |
| :-------------------------------- | :----------------------------------------------------------- |
| [Bodemar 1981](#5-references)     | Peptic ulcer patients receiving a single intravenous dose of 200 mg and oral doses of 200, 400 and 800 mg |
| [Morgan 1983](#5-references)      | Peptic ulcer patients receiving a single intravenous dose of 200 mg (5 min infusion) |
| [Bodemar 1979](#5-references)     | Healthy subjects receiving single oral doses of 200 and 400mg (tablet) |
| [Walkenstein 1978](#5-references) | Healthy subjects receiving a single oral dose of 300mg (solution) |
| [D'Angio 1986](#5-references)     | Healthy subjects receiving a single oral dose of 300mg (tablet) |

#### 2.2.2.2 Model verification

The following studies were used for model verification:

| Publication                       | Arm / Treatment / Information used for model verification    |
| :-------------------------------- | :----------------------------------------------------------- |
| [Grahnen 1979](#5-references)     | Healthy subjects receiving a single intravenous dose of 100 mg and a single oral dose of 400 mg (tablet) |
| [Larsson 1982](#5-references)     | Peptic ulcer patients receiving a single intravenous dose of 200 mg |
| [Mihaly  1984](#5-references)     | Peptic ulcer patients receiving a single intravenous and a single oral dose of 200 mg |
| [Morgan 1983](#5-references)      | Peptic ulcer patients receiving a single intravenous dose of 200 mg (30 min infusion) |
| [Lebert 1981](#5-references)      | Healthy subjects receiving a single intravenous dose of 300 mg (2 min infusion) |
| [Walkenstein 1978](#5-references) | Healthy subjects receiving a single intravenous dose of 300 mg (2 min infusion) and a single oral dose of 300 mg (tablet) |
| [Kanto 1981](#5-references)       | Healthy subjects receiving a single oral dose of 200 mg      |
| [Burland 1975](#5-references)     | Healthy subjects receiving single oral doses of 200 mg solution and capsule |
| [Bodemar 1979](#5-references)     | Peptic ulcer patients receiving a single oral dose of 200 mg (tablet) |
| [Bodemar 1981](#5-references)     | Peptic ulcer patients receiving single oral doses of 800 mg and multiple oral doses of 200 and 400 mg |
| [Barbhaiya 1995](#5-references)   | Healthy subjects receiving multiple oral doses of 300 mg (tablet) |
| [Somogyi 1981](#5-references)     | Healthy subjects receiving a single oral dose of 400 mg (tablet) |
| [Tiseo 1998](#5-references)       | Healthy subjects receiving multiple oral doses of 800 mg (tablet) |

#### 2.2.2.3 Model update due to PK-Sim V10 conversion

As a consequence of updating the cimetidine PBPK model to PK-Sim version 10, the CYP3A4 K<sub>i</sub> value needed to be readjusted. For this purpose, AUC ratios of the following clinical DDI studies were used to inform K<sub>i</sub> in an additional parameter identification:

| Publication                      | Interaction of cimetidine with:                              |
| :------------------------------------- | :------------------------------|
| [Kienlen 1993](#5-references)    | Alfentanil |
| [Abernethy 1983](#5-references)  | Alprazolam and triazolam |
| [Elliott 1984](#5-references)    | Midazolam |
| [Fee 1987](#5-references)        | Midazolam |
| [Greenblatt 1986](#5-references) | Intravenous and oral midazolam |
| [Martinez 1999](#5-references)   | Midazolam |
| [Salonen 1986](#5-references)    | Midazolam |
| [Pourbaix 1985](#5-references)   | Triazolam. NOTE: The interaction of cimetidine with alprazolam of this publication was not used for parameterization due to very long simulation duration! |
| [Cox 1986](#5-references)        | Triazolam |
| [Friedman 1988](#5-references)   | Triazolam |

Similarly, MATE1 K<sub>i</sub> value was adjusted to reproduce the observed inhibition effect on metformin PK (https://github.com/Open-Systems-Pharmacology/Cimetidine-Metformin-DDI).

## 2.3 Model Parameters and Assumptions<a id="model-parameters-and-assumptions"></a>

### 2.3.1 Absorption

Absorption observed in clinical studies can be fully explained by passive absorption.

### 2.3.2 Distribution

Cimetidine is reported to be actively taken up into the liver by OCT1 ([Umehara 2007](#5-references)), into the kidney by OAT3 ([Tahara 2005](#5-references)) and secreted from the kidney into the urine by MATE1 ([Ohta 2010](#5-references)).

After testing the available organ-plasma partition coefficient and cell permeability calculation methods built in PK-Sim, observed clinical data was best described by choosing the partition coefficient calculation method by `Rodgers and Rowland` and cellular permeability calculation by `PK-Sim Standard`. 

A `Lipophilicity` of 1.66 was back-calculated from the blood-to-plasma ratio of 0.98 ([Somogyi 1983](#5-references), [Hanke 2020](#5-references)).

### 2.3.3 Metabolism, Elimination and Inhibition

Cimetidine is mainly excreted unchanged via the kidneys. Additionally, 25 to 40 % is hepatically metabolized via an unknown pathway. 

Cimetidine inhibits several enzymes such as CYP3A4 and CYP2D6 as well as transporters such as OCT2, OCT2 and MATE.

### 2.3.4 Automated Parameter Identification

The parameter identification tool in PK-Sim has been used to estimate selected model parameters by adjusting to PK data of the clinical studies that were used in the model building process (see [Section 2.2](#22-data)). 

Specific intestinal permeability, unspecific hepatic clearance (CLhep) and Kcat values for OCT1, OAT3 and MATE1 were reestimated in PK-Sim Version 10, and, therefore, do not correspond to the original values published by [Hanke 2020](#5-references). The result of the final parameter identification is shown in the table below:

| Model Parameter            | Optimized Value | Unit |
| -------------------------- | --------------- | ---- |
| Specific intestinal permeability| 5.26E-06 | cm/min |
| CLhep| 0.12| 1/min |
| kcat OCT1| 14098.32 | 1/min |
| kcat OAT3| 2522831.10 | 1/min |
| kcat MATE1| 159.47 | 1/min |

As a result of updating the cimetidine PBPK model to PK-Sim V10, the interaction parameter CYP3A4 K<sub>i</sub> was fitted in a second step to improve the performance in CYP3A4 interactions. In detail, CYP3A4 K<sub>i</sub> was adjusted such that the error of the simulated AUC ratios of cimetidine with several CYP3A4 substrates vs. corresponding observed AUC ratios of the clinical studies (see [Section 2.2.2.3](#2223-model-update-due-to-pk-sim-v10-conversion)) was minimized.

| Model Parameter            | Optimized Value | Unit |
| -------------------------- | --------------- | ---- |
| CYP3A4 K<sub>i</sub>| 30.51266 | µmol/l |

# 3 Results and Discussion<a id="results-and-discussion"></a>

The PBPK model for cimetidine was developed and evaluated using publicly available clinical pharmacokinetic data from studies listed in [Section 2.2.2](#222-clinical-data).

The next sections show:

1. the final model parameters for the building blocks: [Section 3.1](#31-final-input-parameters).
2. the overall goodness of fit: [Section 3.2](#32-diagnostics-plots).
3. simulated vs. observed concentration-time profiles for the clinical studies used for model building and for model verification: [Section 3.3](#33-concentration-time-profiles).

## 3.1 Final input parameters<a id="final-input-parameters"></a>

The compound parameter values of the final PBPK model are illustrated below.

### Compound: Cimetidine

#### Parameters

Name                                             | Value                   | Value Origin                                                                                                        | Alternative | Default
------------------------------------------------ | ----------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------- | -------
Solubility at reference pH                       | 24 mg/ml                | Publication-Avdeef 2001                                                                                             | Measurement | True   
Reference pH                                     | 6.8                     | Publication-Avdeef 2001                                                                                             | Measurement | True   
Lipophilicity                                    | 1.655 Log Units         | Parameter Identification                                                                                            | Measurement | True   
Fraction unbound (plasma, reference value)       | 0.78                    | Publication-Taylor 1978                                                                                             | Measurement | True   
Specific intestinal permeability (transcellular) | 5.2554004942E-06 cm/min | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification' on 2021-09-13 17:00 | Fit         | True   
Is small molecule                                | Yes                     |                                                                                                                     |             |        
Molecular weight                                 | 252.34 g/mol            | Database-Drugbank                                                                                                   |             |        
Plasma protein binding partner                   | Unknown                 |                                                                                                                     |             |        

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
----------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------
Fraction unbound (experiment) | 0.78               |                                                                                                                    
Lipophilicity (experiment)    | 1.655 Log Units    |                                                                                                                    
Plasma clearance              | 0 ml/min/kg        |                                                                                                                    
Specific clearance            | 0.1209722937 1/min | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification' on 2021-09-13 17:00

##### Transport Protein: MATE1-Paper

Molecule: MATE1

###### Parameters

Name                      | Value                | Value Origin                                                                                                       
------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------
Transporter concentration | 1 µmol/l             |                                                                                                                    
Vmax                      | 0 µmol/l/min         |                                                                                                                    
Km                        | 8 µmol/l             | Parameter Identification                                                                                           
kcat                      | 159.4749627996 1/min | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification' on 2021-09-13 17:00

##### Transport Protein: OAT3-Paper

Molecule: OAT3

###### Parameters

Name                      | Value              | Value Origin                                                                                                       
------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------
Transporter concentration | 1 µmol/l           |                                                                                                                    
Vmax                      | 0 µmol/l/min       |                                                                                                                    
Km                        | 149 µmol/l         | Publication-Tahara 2005                                                                                            
kcat                      | 2522831.1016 1/min | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification' on 2021-09-13 17:00

##### Transport Protein: OCT1-Paper

Molecule: OCT1

###### Parameters

Name                      | Value                  | Value Origin                                                                                                       
------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------
Transporter concentration | 1 µmol/l               |                                                                                                                    
Vmax                      | 0 µmol/l/min           |                                                                                                                    
Km                        | 2600 µmol/l            | Publication-Umehara 2007                                                                                           
kcat                      | 14098.3224931732 1/min | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification' on 2021-09-13 17:00

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

Name | Value       | Value Origin                                                                                                           
---- | ----------- | -----------------------------------------------------------------------------------------------------------------------
Ki   | 0.65 µmol/l | Parameter Identification-Parameter Identification-https://github.com/Open-Systems-Pharmacology/Cimetidine-Metformin-DDI

##### Inhibition: CYP3A4-Wrighton 1994

Molecule: CYP3A4

###### Parameters

Name | Value           | Value Origin                                                                                                                
---- | --------------- | ----------------------------------------------------------------------------------------------------------------------------
Ki   | 30.51266 µmol/l | Parameter Identification-Parameter Identification-Value adjusted in parameter identification outside of PK-Sim on 2023-11-14

### Formulation: Tablet

Type: Weibull

#### Parameters

Name                             | Value | Value Origin
-------------------------------- | ----- | ------------:
Dissolution time (50% dissolved) | 1 min |             
Lag time                         | 0 h   |             
Dissolution shape                | 10    |             
Use as suspension                | Yes   |             

## 3.2 Diagnostics Plots<a id="diagnostics-plots"></a>

Below you find the goodness-of-fit visual diagnostic plots for the PBPK model performance of all data used presented in [Section 2.2.2](#222-clinical-data).

The first plot shows simulated versus observed plasma concentration, the second weighted residuals versus time. 

<a id="table-3-1"></a>

**Table 3-1: GMFE for Goodness of fit plot for concentration in plasma**

|Group                        |GMFE |
|:----------------------------|:----|
|iv administration            |1.36 |
|multiple oral administration |1.50 |
|single oral administration   |1.51 |
|All                          |1.47 |

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

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/4_time_profile_plot_Cimetidine_iv_200_mg__5_min__Morgan_1983__n_6.png)

**Figure 3-3: iv 200 mg (5 min),Morgan 1983, n=6**

<br>
<br>

<a id="figure-3-4"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/8_time_profile_plot_Cimetidine_iv_200_mg__Bodemar_1981__n_10.png)

**Figure 3-4: iv 200 mg, Bodemar 1981, n=10**

<br>
<br>

<a id="figure-3-5"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/9_time_profile_plot_Cimetidine_iv_200_mg__Bodemar_1981__n_10.png)

**Figure 3-5: iv 200 mg, Bodemar 1981, n=10, urine**

<br>
<br>

<a id="figure-3-6"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/15_time_profile_plot_Cimetidine_po_200_mg__Bodemar_1981__n_10.png)

**Figure 3-6: po 200 mg, Bodemar 1981, n=10**

<br>
<br>

<a id="figure-3-7"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/16_time_profile_plot_Cimetidine_po_200_mg__Bodemar_1981__n_10.png)

**Figure 3-7: po 200 mg, Bodemar 1981, n=10, urine**

<br>
<br>

<a id="figure-3-8"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/22_time_profile_plot_Cimetidine_po_300_mg__sol___Walkenstein_1978__n_24.png)

**Figure 3-8: po 300 mg (sol), Walkenstein 1978, n=24**

<br>
<br>

<a id="figure-3-9"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/23_time_profile_plot_Cimetidine_po_300_mg__sol___Walkenstein_1978__n_24.png)

**Figure 3-9: po 300 mg (sol), Walkenstein 1978, n=24, urine**

<br>
<br>

<a id="figure-3-10"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/24_time_profile_plot_Cimetidine_po_300_mg__tab___D_Angio_1986__n_6.png)

**Figure 3-10: po 300 mg (tab), D'Angio 1986, n=6**

<br>
<br>

<a id="figure-3-11"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/31_time_profile_plot_Cimetidine_po_400_mg__Bodemar_1981__n_9.png)

**Figure 3-11: po 400 mg, Bodemar 1981, n=9**

<br>
<br>

<a id="figure-3-12"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/32_time_profile_plot_Cimetidine_po_400_mg__Bodemar_1981__n_9.png)

**Figure 3-12: po 400 mg, Bodemar 1981, n=9, urine**

<br>
<br>

<a id="figure-3-13"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/34_time_profile_plot_Cimetidine_po_800_mg__Bodemar_1981__n_9.png)

**Figure 3-13: po 800 mg, Bodemar 1981, n=9**

<br>
<br>

<a id="figure-3-14"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/35_time_profile_plot_Cimetidine_po_800_mg__Bodemar_1981__n_9.png)

**Figure 3-14: po 800 mg, Bodemar 1981, n=9, urine**

<br>
<br>

### 3.3.2 Model Validation<a id="model-validation"></a>

<a id="figure-3-15"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/1_time_profile_plot_Cimetidine_iv_100_mg__5_min___Grahnen_1979__n_3.png)

**Figure 3-15: iv 100 mg (5 min), Grahnen 1979, n=3**

<br>
<br>

<a id="figure-3-16"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/2_time_profile_plot_Cimetidine_iv_100_mg__5_min___Grahnen_1979__n_3.png)

**Figure 3-16: iv 100 mg (5 min), Grahnen 1979, n=3, urine**

<br>
<br>

<a id="figure-3-17"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/3_time_profile_plot_Cimetidine_iv_200_mg__30_min__Morgan_1983__n_4.png)

**Figure 3-17: iv 200 mg (30 min),Morgan 1983, n=4**

<br>
<br>

<a id="figure-3-18"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/5_time_profile_plot_Cimetidine_iv_200_mg__Larsson_1982__n_9.png)

**Figure 3-18: iv 200 mg, Larsson 1982, n=9**

<br>
<br>

<a id="figure-3-19"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/6_time_profile_plot_Cimetidine_iv_200_mg__Larsson_1982__n_9.png)

**Figure 3-19: iv 200 mg, Larsson 1982, n=9, urine**

<br>
<br>

<a id="figure-3-20"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/7_time_profile_plot_Cimetidine_iv_200_mg__Mihaly_1984__n_6.png)

**Figure 3-20: iv 200 mg, Mihaly 1984, n=6**

<br>
<br>

<a id="figure-3-21"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/10_time_profile_plot_Cimetidine_iv_300_mg__2_min___Lebert_1981__n_1.png)

**Figure 3-21: iv 300 mg (2 min), Lebert 1981, n=1**

<br>
<br>

<a id="figure-3-22"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/11_time_profile_plot_Cimetidine_iv_300_mg__2_min___Walkenstein_1978__n_12.png)

**Figure 3-22: iv 300 mg (2 min), Walkenstein 1978, n=12**

<br>
<br>

<a id="figure-3-23"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/12_time_profile_plot_Cimetidine_iv_300_mg__2_min___Walkenstein_1978__n_12.png)

**Figure 3-23: iv 300 mg (2 min), Walkenstein 1978, n=12**

<br>
<br>

<a id="figure-3-24"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/13_time_profile_plot_Cimetidine_po_200_mg__tab___Bodemar_1979__fasted_.png)

**Figure 3-24: po 200 mg (tab), Bodemar 1979 (fasted)**

<br>
<br>

<a id="figure-3-25"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/14_time_profile_plot_Cimetidine_po_200_mg__tab___Bodemar_1979__fed_.png)

**Figure 3-25: po 200 mg (tab), Bodemar 1979 (fed)**

<br>
<br>

<a id="figure-3-26"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/17_time_profile_plot_Cimetidine_po_200_mg__Burland_1975__caps.png)

**Figure 3-26: po 200 mg, Burland 1975, caps**

<br>
<br>

<a id="figure-3-27"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/18_time_profile_plot_Cimetidine_po_200_mg__Burland_1975__sol.png)

**Figure 3-27: po 200 mg, Burland 1975, sol**

<br>
<br>

<a id="figure-3-28"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/19_time_profile_plot_Cimetidine_po_200_mg__Kanto_1981__n_8.png)

**Figure 3-28: po 200 mg, Kanto 1981, n=8**

<br>
<br>

<a id="figure-3-29"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/20_time_profile_plot_Cimetidine_po_200_mg__Mihaly_1984__n_8.png)

**Figure 3-29: po 200 mg, Mihaly 1984, n=8**

<br>
<br>

<a id="figure-3-30"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/21_time_profile_plot_Cimetidine_po_200_400_mg_QID__Bodemar_1981__fasted_.png)

**Figure 3-30: po 200/400 mg QID, Bodemar 1981 (fasted)**

<br>
<br>

<a id="figure-3-31"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/25_time_profile_plot_Cimetidine_po_300_mg__tabl___Walkenstein_1978__n_12.png)

**Figure 3-31: po 300 mg (tabl), Walkenstein 1978, n=12**

<br>
<br>

<a id="figure-3-32"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/26_time_profile_plot_Cimetidine_po_300_mg_QID__sol___Barbhaiya_1995__n_18.png)

**Figure 3-32: po 300 mg QID (sol), Barbhaiya 1995, n=18**

<br>
<br>

<a id="figure-3-33"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/27_time_profile_plot_Cimetidine_po_400_mg__tab___Bodemar_1979__n_10.png)

**Figure 3-33: po 400 mg (tab), Bodemar 1979, n=10**

<br>
<br>

<a id="figure-3-34"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/28_time_profile_plot_Cimetidine_po_400_mg__tab___Somogyi_1981__n_8.png)

**Figure 3-34: po 400 mg (tab), Somogyi 1981, n=8**

<br>
<br>

<a id="figure-3-35"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/29_time_profile_plot_Cimetidine_po_400_mg__tab__Grahnen_1979__n_3.png)

**Figure 3-35: po 400 mg (tab),Grahnen 1979, n=3**

<br>
<br>

<a id="figure-3-36"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/30_time_profile_plot_Cimetidine_po_400_mg__tab__Grahnen_1979__n_3.png)

**Figure 3-36: po 400 mg (tab),Grahnen 1979, n=3, urine**

<br>
<br>

<a id="figure-3-37"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-validation/33_time_profile_plot_Cimetidine_po_800_mg__tab__qd__Tiseo_1998__n_18.png)

**Figure 3-37: po 800 mg (tab) qd, Tiseo 1998, n=18**

<br>
<br>

# 4 Conclusion<a id="conclusion"></a>

The herein presented PBPK model adequately describes the pharmacokinetics of cimetidine after intravenous and oral administration of single and multiple doses to healthy adults and peptic ulcer patients covering a broad dosing range from 100 to 800 mg. The established cimetidine PBPK model is verified for the use as a mild inhibitor of CYP3A4 drug in drug-drug interaction simulations.

# 5 References<a id="main-references"></a>

**Abernethy 1983**  Abernethy DR,  Greenblatt DJ, Divoll M, Moschitto LJ, Harmatz JS, Shader RI.  Interaction of cimetidine with the triazolobenzodiazepines alprazolam  and triazolam. Psychopharmacology (Berl). 1983;80(3):275-8. doi:  10.1007/BF00436169.

**Avdeef 2001** Avdeef A, Berger CM. pH-metric solubility. 3. Dissolution titration  template method for solubility determination. Eur J Pharm Sci. 2001  Dec;14(4):281-91. doi: 10.1016/s0928-0987(01)00190-7. PMID: 11684402.

**Barbhaiya 1995** Barbhaiya RH, Shukla UA, Greene DS. Lack of interaction between  nefazodone and cimetidine: a steady state pharmacokinetic study in  humans. Br J Clin Pharmacol. 1995 Aug;40(2):161-5. doi:  10.1111/j.1365-2125.1995.tb05771.x. PMID: 8562300; PMCID: PMC1365177.

**Bodemar 1979** Bodemar G,  Norlander B, Fransson L, Walan A. The absorption of cimetidine before  and during maintenance treatment with cimetidine and the influence of a  meal on the absorption of cimetidine--studies in patients with peptic  ulcer disease. Br J Clin Pharmacol. 1979 Jan;7(1):23-31. doi:  10.1111/j.1365-2125.1979.tb00892.x. PMID: 760739; PMCID: PMC1429608.

**Bodemar 1981** Bodemar G, Norlander B, Walan A. Pharmacokinetics of cimetidine after  single doses and during continuous treatment. Clin Pharmacokinet. 1981  Jul-Aug;6(4):306-15. doi: 10.2165/00003088-198106040-00005. PMID:  7249489.

**Burland 1975** Burland WL, Duncan WA, Hesselbo T, Mills JG, Sharpe PC, Haggie SJ,  Wyllie JH. Pharmacological evaluation of cimetidine, a new histamine  H2-receptor antagonist, in healthy man. Br J Clin Pharmacol. 1975  Dec;2(6):481-6. doi: 10.1111/j.1365-2125.1975.tb00564.x. PMID: 9952;  PMCID: PMC1402643.

**Cox 1986** Cox SR, Kroboth PD, Anderson PH, Smith RB. Mechanism for the interaction between triazolam  and cimetidine. Biopharm Drug Dispos. 1986 Nov-Dec;7(6):567-75.

**D'Angio 1986** D'Angio R, Mayersohn M, Conrad KA, Bliss M. Cimetidine absorption in  humans during sucralfate coadministration. Br J Clin Pharmacol. 1986  May;21(5):515-20. doi: 10.1111/j.1365-2125.1986.tb02834.x. PMID:  3755052; PMCID: PMC1401033.

**Elliott 1984** Elliott P, Dundee  JW, Elwood RJ, Collier PS. The influence of H2 receptor antagonists on  the plasma concentrations of midazolam and temazepam. Eur J  Anaesthesiol. 1984 Sep;1(3):245-51.

**Fee 1987** Fee JP, Collier PS, Howard PJ, Dundee JW. Cimetidine and ranitidine increase midazolam  bioavailability. Clin Pharmacol Ther. 1987 Jan;41(1):80-4. doi:  10.1038/clpt.1987.13. PMID: 3802710.

**Friedman 1988** Friedman H,  Greenblatt DJ, Burstein ES, Scavone JM, Harmatz JS, Shader RI. Triazolam kinetics: interaction with cimetidine, propranolol, and the  combination. J Clin Pharmacol. 1988 Mar;28(3):228-33.

**Grahnen 1979** Grahnén A, von Bahr C, Lindström B, Rosén A. Bioavailability and  pharmacokinetics of cimetidine. Eur J Clin Pharmacol. 1979  Nov;16(5):335-40. doi: 10.1007/BF00605632. PMID: 520401.

**Greenblatt 1986** Greenblatt DJ, Locniskar A, Scavone JM, Blyden GT, Ochs HR, Harmatz JS,  Shader RI. Absence of interaction of cimetidine and ranitidine with  intravenous and oral midazolam. Anesth Analg. 1986 Feb;65(2):176-80.  PMID: 2935051.

**Hanke 2020** Hanke N, Türk D, Selzer D, Ishiguro N, Ebner  T, Wiebe S, Müller F, Stopfer P, Nock V, Lehr T. A Comprehensive  Whole-Body Physiologically Based Pharmacokinetic Drug-Drug-Gene  Interaction Model of Metformin and Cimetidine in Healthy Adults and  Renally Impaired Individuals. Clin Pharmacokinet. 2020  Nov;59(11):1419-1431. doi: 10.1007/s40262-020-00896-w. PMID: 32449077;  PMCID: PMC7658088.

**Ito 2012** Ito S, Kusuhara H,  Yokochi M, Toyoshima J, Inoue K, Yuasa H, Sugiyama Y. Competitive  inhibition of the luminal efflux by multidrug and toxin extrusions, but  not basolateral uptake by organic cation transporter 2, is the likely  mechanism underlying the pharmacokinetic drug-drug interactions caused  by cimetidine in the kidney. J Pharmacol Exp Ther. 2012  Feb;340(2):393-403. doi: 10.1124/jpet.111.184986. Epub 2011 Nov 9. PMID: 22072731.

**Kanto 1981** Kanto J, Allonen H, Jalonen H, Mäntylä R. The effect of metoclopramide  and propantheline on the gastrointestinal absorption of cimetidine. Br J Clin Pharmacol. 1981 Jun;11(6):629-31. doi:  10.1111/j.1365-2125.1981.tb01184.x. PMID: 7272182; PMCID: PMC1402204.

**Kuepfer 2016** Kuepfer L, Niederalt C, Wendl T, Schlender JF, Willmann S, Lippert J, Block M, Eissing T, Teutonico D. Applied Concepts in PBPK Modeling: How to Build a PBPK/PD Model.CPT Pharmacometrics Syst Pharmacol. 2016 Oct;5(10):516-531.

**Kienlen 1993** Kienlen, J., Levron, JC., Aubas, S. *et al.* Pharmacokinetics of Alfentanil in Patients Treated with Either Cimetidine or Ranitidine.  Drug Invest **6,** 257–262 (1993).

**Larsson 1982** Larsson R, Erlanson P, Bodemar G, Walan A, Bertler A, Fransson L,  Norlander B. The pharmacokinetics of cimetidine and its sulphoxide  metabolite in patients with normal and impaired renal function. Br J  Clin Pharmacol. 1982 Feb;13(2):163-70. doi:  10.1111/j.1365-2125.1982.tb01351.x. PMID: 7059413; PMCID: PMC1402003.

**Lebert 1981** Lebert PA, Mahon  WA, MacLeod SM, Soldin SJ, Fenje P, Vandenberghe HM. Ranitidine kinetics and dynamics. II. Intravenous dose studies and comparison with  cimetidine. Clin Pharmacol Ther. 1981 Oct;30(4):545-50. doi:  10.1038/clpt.1981.201. PMID: 6269789.

**Martinez  1999** Martínez C, Albet  C, Agúndez JA, Herrero E, Carrillo JA, Márquez M, Benítez J, Ortiz JA.  Comparative in vitro and in vivo inhibition of cytochrome P450 CYP1A2,  CYP2D6, and CYP3A by H2-receptor antagonists. Clin Pharmacol Ther. 1999  Apr;65(4):369-76. doi: 10.1016/S0009-9236(99)70129-3. PMID: 10223772.

**Meyer 2012** Meyer M, Schneckener S, Ludewig B, Kuepfer L, Lippert J. Using expression data for quantification of active processes in physiologically based pharmacokinetic modeling. Drug Metab Dispos. 2012 May;40(5):892-901.

**Mihaly  1984** Mihaly GW, Jones DB, Anderson JA, Smallwood RA, Louis WJ.  Pharmacokinetic studies of cimetidine and ranitidine before and after  treatment in peptic ulcer patients. Br J Clin Pharmacol. 1984  Jan;17(1):109-11. doi: 10.1111/j.1365-2125.1984.tb05010.x. PMID:  6318788; PMCID: PMC1463299.

**Morgan 1983** Morgan DJ, Uccellini DA, Raymond K, Mihaly GW, Jones DB, Smallwood RA.  The influence of duration of intravenous infusion of an acute dose on  plasma concentrations of cimetidine. Eur J Clin Pharmacol.  1983;25(1):29-34. doi: 10.1007/BF00544010. PMID: 6617722.

**Nishimura 2013** Nishimura M, Yaguti H, Yoshitsugu H, Naito S, Satoh T. Tissue distribution of mRNA expression of human cytochrome P450 isoforms assessed by high-sensitivity real-time reverse transcription PCR. Yakugaku Zasshi. 2003 May;123(5):369-75.

**Ohta 2005** Ohta KY, Inoue K, Yasujima T, Ishimaru M, Yuasa H. Functional  characteristics of two human MATE transporters: kinetics of cimetidine  transport and profiles of inhibition by various compounds. J Pharm Pharm Sci. 2009;12(3):388-96. doi: 10.18433/j3r59x. PMID: 20067714.

**PK-Sim Ontogeny Database Version 7.3** (https://github.com/Open-Systems-Pharmacology/OSPSuite.Documentation/blob/38cf71b384cfc25cfa0ce4d2f3addfd32757e13b/PK-Sim%20Ontogeny%20Database%20Version%207.3.pdf)

**Pourbaix 1985** Pourbaix S, Desager JP, Hulhoven R, Smith RB, Harvengt C. Pharmacokinetic consequences of  long term coadministration of cimetidine and triazolobenzodiazepines,  alprazolam and triazolam, in healthy subjects. Int J Clin Pharmacol Ther Toxicol. 1985 Aug;23(8):447-51.

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

