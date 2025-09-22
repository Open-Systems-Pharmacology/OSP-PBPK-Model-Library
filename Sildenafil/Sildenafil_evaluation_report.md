# Building and evaluation of a PBPK model for Sildenafil in healthy adults

| Version                                         | 2.0-OSP12.1                                                   |
| ----------------------------------------------- | ------------------------------------------------------------ |
| based on *Model Snapshot* and *Evaluation Plan* | https://github.com/Open-Systems-Pharmacology/Sildenafil-Model/releases/tag/v2.0 |
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

Sildenafil is a cGMP-specific phosphodiesterase 5 inhibitor, indicated for erectile dysfunction and pulmonary arterial hypertension. It is mostly metabolized by CYP3A4 making it a sensitive probe and victim drug for the investigation of CYP3A4 activity *in vivo*. Other CYPs are involved in sildenafil metabolism: CYP2C9 and CYP2C19. It is a BCS class II compound. Sildenafil shows substantial first pass metabolism resulting in a bioavailability of 40%. 

The model has been developed and evaluated by comparing observed data to simulations of a large number of clinical studies covering a dose range of 20 mg to 100 mg after intravenous and oral administrations. Furthermore, it has been evaluated within a CYP3A4 DDI modeling network as a victim drug. 

Model features include:

- metabolism by CYP3A4
- metabolism by CYP2C9
- metabolism by CYP2C19
- a decrease in the permeability between the intracellular and interstitial space (model parameters `P (intracellular->interstitial)` and `P (interstitial->intracellular)`) in intestinal mucosa to optimize quantitatively the extent of gut wall metabolism

# 2 Methods<a id="methods"></a>

## 2.1 Modeling Strategy<a id="modeling-strategy"></a>

The general concept of building a PBPK model has previously been described by Kuepfer et al. ([Kuepfer 2016](#5-references)). Relevant information on anthropometric (height, weight) and physiological parameters (e.g. blood flows, organ volumes, binding protein concentrations, hematocrit, cardiac output) in adults was gathered from the literature and has been previously published ([Willmann 2007](#5-references)). The information was incorporated into PK-Sim® and was used as default values for the simulations in adults.

The applied activity and variability of plasma proteins and active processes that are integrated into PK-Sim® are described in the publicly available PK-Sim® Ontogeny Database Version 7.3 ([PK-Sim Ontogeny Database Version 7.3](#5-references)) or otherwise referenced for the specific process.

First, a mean model was built using clinical data from single dose studies with intravenous and oral administration of sildenafil by Muirhead et al. 2002 ([Muirhead 2002a](#5-references)), Nichols et al. 2002 ([Nichols 2002](#5-references)), the FDA 2009 ([FDA 2009](#5-references)), and Walker et al. 1999 ([Walker 1999](#5-references)). The mean PBPK model was developed using a typical male European individual. The relative tissue-specific expressions of enzymes predominantly being involved in the metabolism of sildenafil (CYP3A4) were considered ([Meyer 2012](#5-references)).

A specific selected set of parameters (see below) was optimized using the Parameter Identification module provided in PK-Sim®. Structural model selection was mainly guided by visual inspection of the resulting description of data and biological plausibility.

Once the appropriate structural model was identified, a Weibull function was fitted using R 4.2.1 based on in vitro data ([Sawatdee 2019](#5-references)), and the resulting dissolution kinetic parameters were implemented in the model.

The model was then evaluated by simulating further clinical studies reporting pharmacokinetic concentration-time profiles of sildenafil.

Details about input data (physicochemical, *in vitro* and clinical) can be found in [Section 2.2](#22-data).

Details about the structural model and its parameters can be found in [Section 2.3](#23-model-parameters-and-assumptions).

## 2.2 Data<a id="data"></a>

### 2.2.1 In vitro and physicochemical data

A literature search was performed to collect available information on physicochemical properties of sildenafil. The obtained information from literature is summarized in the table below, and is used for model building.

| **Parameter**                         | **Unit**                   | **Value**        | Source                            | **Description**                                              |
| :------------------------------------ | -------------------------- | ---------------- | --------------------------------- | ------------------------------------------------------------ |
| MW                                    | g/mol                      | 474.576          | [DrugBank DB00203](#5-references) | Molecular weight                                             |
| pK<sub>a1</sub>                       |                            | 5.97             | [Salerno 2021](#5-references)     | Acid dissociation constant of conjugate acid; compound type: basic |
| pK<sub>a1</sub>                       |                            | 6.78             | [Gobry 2000](#5-references)       | Acid dissociation constant of conjugate acid; compound type: ampholyte |
| pK<sub>a2</sub>                       |                            | 9.12             | [Gobry 2000](#5-references)       | Acid dissociation constant of conjugate acid; compound type: ampholyte |
| Solubility (pH)                       | mg/mL                      | 0.025<br />(7.1) | [Takano 2016](#5-references)      | Aqueous Solubility                                           |
|                                       |                            | 3.5              | [Salerno 2021](#5-references)     | Aqueous Solubility                                           |
|                                       |                            | 3.5              | [DrugBank DB00203](#5-references) | Aqueous Solubility                                           |
|                                       |                            | 4.1              | [Jung 2011](#5-references)        | Aqueous Solubility                                           |
|                                       |                            | 3.965<br />(3)   | [Wang 2008](#5-references)        | Aqueous Solubility                                           |
|                                       |                            | 7.077<br />(4)   | [Wang 2008](#5-references)        | Aqueous Solubility                                           |
|                                       |                            | 2.068<br />(5)   | [Wang 2008](#5-references)        | Aqueous Solubility                                           |
|                                       |                            | 0.114<br />(6)   | [Wang 2008](#5-references)        | Aqueous Solubility                                           |
|                                       |                            | 0.025<br />(7)   | [Wang 2008](#5-references)        | Aqueous Solubility                                           |
|                                       |                            | 0.027<br />(8)   | [Wang 2008](#5-references)        | Aqueous Solubility                                           |
|                                       |                            | 0.04<br />(9)    | [Wang 2008](#5-references)        | Aqueous Solubility                                           |
|                                       |                            | 0.103<br />(10)  | [Wang 2008](#5-references)        | Aqueous Solubility                                           |
|                                       |                            | 0.322<br />(11)  | [Wang 2008](#5-references)        | Aqueous Solubility                                           |
| logP                                  |                            | 3.18             | [Gobry 2000](#5-references)       | Partition coefficient between octanol and water              |
|                                       |                            | 2.70             | [Takano 2016](#5-references)      | Partition coefficient between octanol and water              |
|                                       |                            | 2.70             | [Walker 1999](#5-references)      | Partition coefficient between octanol and water              |
|                                       |                            | 2.24             | [Wang 2008](#5-references)        | Partition coefficient between octanol and water              |
|                                       |                            | 1.59             | [Wang 2008](#5-references)        | Partition coefficient between octanol and water              |
|                                       |                            | 1.8              | [DrugBank DB00203](#5-references) | Partition coefficient between octanol and water              |
|                                       |                            | 1.87             | [DrugBank DB00203](#5-references) | Partition coefficient between octanol and water              |
| fu                                    | %                          | 4                | [Walker 1999](#5-references)      | Fraction unbound in plasma (α1-acid glycoprotein)            |
|                                       | %                          | 4.3              | [Muirhead 2002b](#5-references)    | Fraction unbound in plasma (α1-acid glycoprotein)            |
|                                       | %                          | 2.7              | [Muirhead 2002b](#5-references)    | Fraction unbound in plasma (α1-acid glycoprotein)            |
|                                       | %                          | 3.46             | [Muirhead 2002b](#5-references)    | Fraction unbound in plasma (α1-acid glycoprotein)            |
| V<sub>max</sub>, K<sub>m</sub> CYP3A4 | pmol/min/pmol P450,<br />µmol/L | 78.6<br />4.34   | [Takano 2016](#5-references)      | Recombinant CYP3A4 Michaelis-Menten kinetics                 |
| V<sub>max</sub>, K<sub>m</sub> CYP3A4 | relative units,<br />µmol/L| 1.9<br />23.10   | [Warrington 2000](#5-references)  | Recombinant CYP3A4 Michaelis-Menten kinetics                 |   
| V<sub>max</sub>, K<sub>m</sub> CYP2C9 | relative units,<br />µmol/L| 0.2<br />9.60    | [Warrington 2000](#5-references)  | Recombinant CYP3A4 Michaelis-Menten kinetics                 |
| V<sub>max</sub>, K<sub>m</sub> CYP2C19| relative units,<br />µmol/L| 0.02<br />23.10  | [Warrington 2000](#5-references)  | Recombinant CYP3A4 Michaelis-Menten kinetics                 |              

### 2.2.2 Clinical data

A literature search was performed to collect available clinical data on sildenafil in adults. 

The following publications were found in adults for model building:

| Publication                            | Arm / Treatment / Information used for model building                                                                                                |
| :------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Muirhead 2002a](#5-references)         | Plasma PK profiles in healthy subjects with single dose administrations of a sildenafil 25 mg intravenous infusion                                   |
| [Nichols 2002](#5-references)          | Plasma PK profiles in healthy subjects with single dose administrations of a sildenafil:<br />- 50 mg intravenous infusion <br />- 100mg oral tablet |
| [FDA 2009](#5-references) | Plasma PK profiles in healthy subjects with single dose administrations of a sildenafil:<br />- 20 mg intravenous infusion <br />- 40 mg intravenous infusion <br />- 80 mg intravenous infusion|
| [Walker 1999](#5-references)           | Plasma PK profiles in healthy subjects with single dose administrations of a sildenafil 50 mg oral solution                                          |
| [Spence 2008](#5-references)           | Plasma PK profiles in healthy subjects with single dose administrations of a sildenafil 20 mg tablet                                                 |
| [Lee 2021](#5-references)              | Plasma PK profiles in healthy subjects with single dose administrations of a sildenafil:<br />- 25 mg tablet (in the absence of itraconazole)<br />- 25 mg tablet (in the absence of clarithromycin)|
| [Abdelkawy 2016](#5-references)        | Plasma PK profiles in healthy subjects with single dose administrations of a sildenafil 50 mg tablet                                                 |
| [Gillen 2017](#5-references)           | Plasma PK profiles in healthy subjects with single dose administrations of a sildenafil 50 mg tablet (Panel 1)                                       |
| [Jetter 2002](#5-references)           | Plasma PK profiles in healthy subjects with single dose administrations of a sildenafil 50 mg tablet                                                 |
| [Murtadha 2021](#5-references)         | Plasma PK profiles in healthy subjects with single dose administrations of a sildenafil 50 mg tablet (non-smoker group)                              |
| [Wilner 2002](#5-references)           | Plasma PK profiles in healthy subjects with single dose administrations of a sildenafil 50 mg tablet (study I)                                       |

The following dosing scenarios were simulated and compared to respective data for model verification:

| Scenario                                                     | Data reference                       |
| ------------------------------------------------------------ | ------------------------------------ |
| po SD 50mg                                                   | [Al-Ghazawi 2010](#5-references)     |
|                                                              | [Hedaya 2006](#5-references)         |
|                                                              | [Wilner 2002](#5-references)         |
|                                                              | [Gillen 2017](#5-references)         |
| po SD 100mg                                                  | [Muirhead 2000](#5-references)       |
| po MD 20/80 mg                                               | [Burgess 2008](#5-references)        |
| po MD 20 mg                                                  | [Gotzkowsky 2013](#5-references)     |

 

## 2.3 Model Parameters and Assumptions<a id="model-parameters-and-assumptions"></a>

### 2.3.1 Absorption

The model parameter `Specific intestinal permeability` was optimized to best match clinical data (see  [Section 2.3.4](#234-automated-parameter-identification)). A formulation without limitation to absorption was assumed for the oral solution, therefore its solubility was set to 100 mg/L. A default solubility of 3.5 mg/L was taken from the model of [Salerno 2021](#5-references) and used for tablets (see [Section 2.2.1](#221-in-vitro-and-physicochemical-data))

The dissolution of tablets was implemented via a Weibull dissolution tablet. The Weibull function was fitted using R 4.2.1 based on in vitro data ([Sawatdee 2019](#5-references)), and the resulting dissolution kinetic parameters were fixed in the model.

### 2.3.2 Distribution

Sildenafil is highly bound to α1-acid glycoprotein in plasma (see [Section 2.2.1](#221-in-vitro-and-physicochemical-data)). A value of 4% was used in this PBPK model for `Fraction unbound (plasma, reference value)`. 

An important parameter influencing the resulting volume of distribution is lipophilicity. The reported experimental logP values are in the range of 3 (see [Section 2.2.1](#221-in-vitro-and-physicochemical-data)) which served as a starting value. Finally, the model parameters `Lipophilicity` was optimized to match best clinical data (see also [Section 2.3.4](#234-automated-parameter-identification)).

After testing the available organ-plasma partition coefficient and cell permeability calculation methods built in PK-Sim, observed clinical data was best described by choosing the partition coefficient calculation by `Rodgers and Rowland` and cellular permeability calculation by `PK-Sim Standard`.

### 2.3.3 Metabolism and Elimination

Three metabolic pathways were implement into the model via Michaelis-Menten kinetics 

* CYP3A4
* CYP3A9
* CYP3A19

Relative kcat were calculated with the following inputs:

| Input                                       | Unit                             | CYP3A4      | CYP2C9      | CYP2C19     | Reference                         |    
| ------------------------------------------- | -------------------------------- | ----------- | ----------- | ----------- | --------------------------------- |
| Contributions in vitro (scaled)*            | µL/min/mg microsomal protein     | 0.79        | 0.20        | 0.01        | [Warrington 2000](#5-references)  | 
| CYP amount                                  | pmol CYP/mg microsomal protein   | 108         | 96          | 19          | [Rodrigues 1999](#5-references)   |
| Michaelis Menten constant (Km)              | µmol/L                           | 23.1        | 9.6         | 23.1        | [Warrington 2000](#5-references)  |
*The contribution in vitro has initially no unit. It was scaled multiplying it by 1 µL/min/mg microsomal protein. This is a joint scaling factor over the three CYPs to keep their relative hepatic contributions fixed. It was later optimized as part of kcat. 

The scaled contributions in vitro were converted to specific clearance per enzyme dividing by the respective CYP amount per milligram microsomal protein. Then these relative specific clearances per enzyme were multiplied by the Km value to obtain kcat values which were then in a next step optimized with a joint factor in the parameter identification to best match clinical data (see [Section 2.3.4](#234-automated-parameter-identification))

| Calculated parameters                       | Unit                             | CYP3A4      | CYP2C9      | CYP2C19     |    
| ------------------------------------------- | -------------------------------- | ----------- | ----------- | ----------- | 
| CLspec/Enzyme                               | L/µmol/min                       | 0.007324074 | 0.002083333 | 0.000436842 | 
| kcat                                        | 1/min                            | 0.17        | 0.02        | 0.01        | 

The CYP3A4 expression profiles is based on high-sensitive real-time RT-PCR ([Nishimura 2003](#5-references)). Absolute tissue-specific expressions were obtained by considering the respective absolute concentration in the liver. The PK-Sim database provides a default value for CYP3A4 (compare [Rodrigues 1999](#5-references) and assume 40 mg protein per gram liver). 

The first model simulations showed that gut wall metabolism was underrepresented in the PBPK model. In order to increase gut wall metabolism, the “mucosa permeability on basolateral side” (jointly the model parameters in the mucosa: ``P (interstitial->intracellular)`` and ``P (intracellular->interstitial)``) was estimated. A decrease in this permeability may lead to higher gut wall concentrations and, in turn, to a higher gut wall elimination. This parameter was preferred over other parameters such as relative CYP3A4 expression or fraction unbound (fu) in the gut wall as it is technically not limited to a maximum value of 100%.

### 2.3.4 Automated Parameter Identification

This is the result of the final parameter identification for the base model:

| Model Parameter                                              | Optimized Value                                              | Unit      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | --------- |
| `Lipophilicity`                                              | 2.84                                                         | Log Units |
| `Fraction unbound`                                           | 0.04 (FIXED)                                                 |           |
| `Specific intestinal permeability`                           | 1.21E-3                                                      | cm/min    |
| Basolateral mucosa permeability<br />(``P (interstitial->intracellular)``, ``P (intracellular->interstitial)``) | 6.07E-4   | cm/min    |
| `kcat` (CYP3A4)                                              | 27.21                                                        | 1/min     |
| `kcat` (CYP2C9)                                              | 3.22                                                         | 1/min     |
| `kcat` (CYP2C19)                                             | 1.62                                                         | 1/min     |
| `Dissolution time`                                           | 4.16 (FIXED)                                                 | min       |
| `Dissolution shape`                                          | 1.37 (FIXED)                                                 |           |

# 3 Results and Discussion<a id="results-and-discussion"></a>

The PBPK model for sildenafil was developed and verified with clinical pharmacokinetic data.

The model was built and evaluated covering data from studies including in particular

* intravenous (infusions) and oral administrations (solutions and tablets).
* a dose range of 20 to 100 mg.

The model quantifies metabolism via CYP3A4, CYP2C9 and CYP2C19.

The next sections show:

1. the final model input parameters for the building blocks: [Section 3.1](#31-final-input-parameters).
2. the overall goodness of fit: [Section 3.2](#32-diagnostics-plots).
3. simulated vs. observed concentration-time profiles for the clinical studies used for model building and for model verification: [Section 3.3](#33-concentration-time-profiles).

## 3.1 Final input parameters<a id="final-input-parameters"></a>

The compound parameter values of the final PBPK model are illustrated below.

### Compound: Sildenafil

#### Parameters

Name                                             | Value                  | Value Origin                                                                                                                   | Alternative   | Default
------------------------------------------------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------- | -------
Solubility at reference pH                       | 3.5 mg/l               | Publication-Salerno 2021                                                                                                       | Measurement   | True   
Reference pH                                     | 7                      | Publication-Salerno 2021                                                                                                       | Measurement   | True   
Solubility at reference pH                       | 100 mg/l               | Other-Assumption                                                                                                               | Oral solution | False  
Reference pH                                     | 7                      | Other-Assumption                                                                                                               | Oral solution | False  
Lipophilicity                                    | 2.8413676507 Log Units | Parameter Identification-Parameter Identification-Value updated from 'PI_All_DissoKineticFit_P calculated' on 2023-03-24 17:29 | Measurement   | True   
Fraction unbound (plasma, reference value)       | 0.04                   | Parameter Identification-Parameter Identification-Value updated from 'PI_All_DissoKineticFit_P calculated' on 2023-03-24 17:29 | Measurement   | True   
Permeability                                     | 0.0758702742 cm/min    | Parameter Identification-Parameter Identification-Value updated from 'PI_All_DissoKineticFit' on 2022-08-12 15:40              | Optimized     | False  
Specific intestinal permeability (transcellular) | 0.0012071993309 cm/min | Parameter Identification-Parameter Identification-Value updated from 'PI_All_DissoKineticFit_P calculated' on 2023-03-24 17:29 | Optimized     | True   
Is small molecule                                | Yes                    |                                                                                                                                |               |        
Molecular weight                                 | 474.58 g/mol           | Internet-DrugBank DB00203                                                                                                      |               |        
Plasma protein binding partner                   | α1-acid glycoprotein   |                                                                                                                                |               |        

#### Calculation methods

Name                    | Value              
----------------------- | -------------------
Partition coefficients  | Rodgers and Rowland
Cellular permeabilities | PK-Sim Standard    

#### Processes

##### Metabolizing Enzyme: CYP2C19-Warrington

Molecule: CYP2C19

###### Parameters

Name                             | Value                                | Value Origin                                                                                                                  
-------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------
In vitro Vmax/recombinant enzyme | 0.01009105 pmol/min/pmol rec. enzyme | Publication-Warrington 2000                                                                                                   
Km                               | 23.1 µmol/l                          | Publication-Warrington 2000                                                                                                   
kcat                             | 1.6232116026 1/min                   | Parameter Identification-Parameter Identification-Value updated from 'PI_All_DissoKineticFit_P calculated' on 2023-03-24 17:29

##### Metabolizing Enzyme: CYP2C9-Warrington

Molecule: CYP2C9

###### Parameters

Name                             | Value                          | Value Origin                                                                                                                  
-------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------
In vitro Vmax/recombinant enzyme | 0.02 pmol/min/pmol rec. enzyme | Publication-Warrington 2000                                                                                                   
Km                               | 9.6 µmol/l                     | Publication-Warrington 2000                                                                                                   
kcat                             | 3.2171312254 1/min             | Parameter Identification-Parameter Identification-Value updated from 'PI_All_DissoKineticFit_P calculated' on 2023-03-24 17:29

##### Metabolizing Enzyme: CYP3A4-Warrington

Molecule: CYP3A4

###### Parameters

Name                             | Value                                | Value Origin                                                                                                                  
-------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------
In vitro Vmax/recombinant enzyme | 0.16918611 pmol/min/pmol rec. enzyme | Publication-Warrington 2000                                                                                                   
Km                               | 23.1 µmol/l                          | Publication-Warrington 2000                                                                                                   
kcat                             | 27.2146958692 1/min                  | Parameter Identification-Parameter Identification-Value updated from 'PI_All_DissoKineticFit_P calculated' on 2023-03-24 17:29

### Formulation: Sildenafil Tablet

Type: Weibull

#### Parameters

Name                             | Value        | Value Origin                                                                                                                  
-------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------
Dissolution time (50% dissolved) | 4.164698 min | Parameter Identification-Parameter Identification-Value updated from 'PI_All_DissoKineticFit_P calculated' on 2023-03-24 17:29
Lag time                         | 0 min        |                                                                                                                               
Dissolution shape                | 1.37405      | Parameter Identification-Parameter Identification-Value updated from 'PI_All_DissoKineticFit_P calculated' on 2023-03-24 17:29
Use as suspension                | Yes          |                                                                                                                               

## 3.2 Diagnostics Plots<a id="diagnostics-plots"></a>

Below you find the goodness-of-fit visual diagnostic plots for the PBPK model performance of all data used presented in [Section 2.2.2](#222-clinical-data).

The first plot shows observed versus simulated plasma concentration, the second weighted residuals versus time. 

<a id="table-3-1"></a>

**Table 3-1: GMFE for Sildenafil concentration in plasma**

|Group                                            |GMFE |
|:------------------------------------------------|:----|
|Intravenous administration (model building)      |1.64 |
|Oral administration, solution (model building)   |1.37 |
|Oral administration, tablet (model building)     |1.44 |
|Oral administration, tablet (model verification) |1.82 |
|All                                              |1.62 |

<br>
<br>

<a id="figure-3-1"></a>

![](images/006_section_results-and-discussion/008_section_diagnostics-plots/2_gof_plot_predictedVsObserved.png)

**Figure 3-1: Sildenafil concentration in plasma**

<br>
<br>

<a id="figure-3-2"></a>

![](images/006_section_results-and-discussion/008_section_diagnostics-plots/3_gof_plot_residualsOverTime.png)

**Figure 3-2: Sildenafil concentration in plasma**

<br>
<br>

## 3.3 Concentration-Time Profiles<a id="ct-profiles"></a>

Simulated versus observed concentration-time profiles of all data listed in [Section 2.2.2](#222-clinical-data) are presented below.

### 3.3.1 Model Building<a id="model-building"></a>

<a id="figure-3-3"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/1_time_profile_plot_Sildenafil_IV_20mg.png)

**Figure 3-3: Time Profile Analysis**

<br>
<br>

<a id="figure-3-4"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/2_time_profile_plot_Sildenafil_IV_25mg.png)

**Figure 3-4: Time Profile Analysis**

<br>
<br>

<a id="figure-3-5"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/3_time_profile_plot_Sildenafil_IV_40mg.png)

**Figure 3-5: Time Profile Analysis**

<br>
<br>

<a id="figure-3-6"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/4_time_profile_plot_Sildenafil_IV_50mg.png)

**Figure 3-6: Time Profile Analysis**

<br>
<br>

<a id="figure-3-7"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/5_time_profile_plot_Sildenafil_IV_80mg.png)

**Figure 3-7: Time Profile Analysis**

<br>
<br>

<a id="figure-3-8"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/6_time_profile_plot_Sildenafil_Oral_solution.png)

**Figure 3-8: Time Profile Analysis**

<br>
<br>

<a id="figure-3-9"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/9_time_profile_plot_Sildenafil_Tablet_SD_100mg_fasted.png)

**Figure 3-9: Time Profile Analysis**

<br>
<br>

<a id="figure-3-10"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/11_time_profile_plot_Sildenafil_Tablet_SD_20mg_fasted.png)

**Figure 3-10: Time Profile Analysis**

<br>
<br>

<a id="figure-3-11"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/12_time_profile_plot_Sildenafil_Tablet_SD_25mg_fasted.png)

**Figure 3-11: Time Profile Analysis**

<br>
<br>

<a id="figure-3-12"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/13_time_profile_plot_Sildenafil_Tablet_SD_50mg_fasted.png)

**Figure 3-12: Time Profile Analysis**

<br>
<br>

### 3.3.2 Model Verification<a id="model-verification"></a>

<a id="figure-3-13"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/7_time_profile_plot_Sildenafil_Tablet_MD_20_80mg_fasted_Test.png)

**Figure 3-13: Time Profile Analysis**

<br>
<br>

<a id="figure-3-14"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/8_time_profile_plot_Sildenafil_Tablet_MD_20mg_fasted_Test.png)

**Figure 3-14: Time Profile Analysis**

<br>
<br>

<a id="figure-3-15"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/10_time_profile_plot_Sildenafil_Tablet_SD_100mg_fasted_Test.png)

**Figure 3-15: Time Profile Analysis**

<br>
<br>

<a id="figure-3-16"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/14_time_profile_plot_Sildenafil_Tablet_SD_50mg_fasted_Test.png)

**Figure 3-16: Time Profile Analysis**

<br>
<br>

# 4 Conclusion<a id="conclusion"></a>

The herein presented PBPK model adequately describes the pharmacokinetics of sildenafil in adults.

In particular, it applies quantitative metabolism by CYP3A4, CYP2C9 and CYP2C19. Thus, the model is fit for purpose to be applied for the investigation of drug-drug interactions with regard to its CYP3A4 metabolism.

# 5 References<a id="main-references"></a>

**Abdelkawy 2016** Abdelkawy KSDonia AM, Turner RB, Elbarbry F. Effects of Lemon and Seville Orange Juices on the Pharmacokinetic Properties of Sildenafil in Healthy Subjects. Drugs R D. 2016;16(3):271-8.

**Al-Ghazawi 2010** Al-Ghazawi MATutunji MS, AbuRuz SM. The effects of pummelo juice on pharmacokinetics of sildenafil in healthy adult male Jordanian volunteers. Eur J Clin Pharmacol. 2010;66(2):159-63.

**Burgess 2008** Burgess GHoogkamer H, Collings L, Dingemanse J. Mutual pharmacokinetic interactions between steady-state bosentan and sildenafil. Eur J Clin Pharmacol. 2008;64(1):43-50.

**DrugBank DB00203** https://go.drugbank.com/drugs/DB00203

**FDA 2009** Food and Drug Administration, Clinical Pharmacology and biopharmaceutics review of Revatio. 2009; https://www.accessdata.fda.gov/drugsatfda_docs/nda/2009/022473s000_ClinPharmR.pdf

**Gillen 2017** Gillen M, Yang C, Wilson D, Valdez S, Lee C, Kerr B, et al. Evaluation of Pharmacokinetic Interactions Between Lesinurad, a New Selective Urate Reabsorption Inhibitor, and CYP Enzyme Substrates Sildenafil, Amlodipine, Tolbutamide, and Repaglinide. Clin Pharmacol Drug Dev. 2017;6(4):363-76.

**Gobry 2000** Gobry V, Bouchard G, Carrupt PA, Testa B, Girault HH. Physicochemical characterization of sildenafil: ionization, lipophilicity behavior, and ionic‐partition diagram studied by two‐phase titration and electrochemistry. Helvetica Chimica Acta. 2000;83(7):1465-74.

**Gotzkowsky 2013** Gotzkowsky SK, Kumar P, Mottola D, Laliberte K. Lack of a pharmacokinetic interaction between treprostinil diolamine and sildenafil in healthy adult volunteers. J Cardiovasc Pharmacol. 2013;61(5):444-51.

**Hedaya 2006** Hedaya MA, El-Afify DR, El-Maghraby GM. The effect of ciprofloxacin and clarithromycin on sildenafil oral bioavailability in human volunteers. Biopharm Drug Dispos. 2006;27(2):103-10.

**Jetter 2002** Jetter A, Kinzig-Schippers M, Walchner-Bonjean M, Hering U, Bulitta J, Schreiner P, et al. Effects of grapefruit juice on the pharmacokinetics of sildenafil. Clin Pharmacol Ther. 2002;71(1):21-9.

**Jung 2011** Jung SY, Seo YG, Kim GK, Woo JS, Yong CS, Choi HG. Comparison of the solubility and pharmacokinetics of sildenafil salts. Arch Pharm Res. 2011;34(3):451-4.

**Kuepfer 2016** Kuepfer L, Niederalt C, Wendl T, Schlender JF, Willmann S, Lippert J, et al. Applied Concepts in PBPK Modeling: How to Build a PBPK/PD Model. CPT Pharmacometrics Syst Pharmacol. 2016;5(10):516-31.

**Lee 2021** Lee S, Kim AH, Yoon S, Lee J, Lee Y, Ji SC, et al. The utility of CYP3A activity endogenous markers for evaluating drug-drug interaction between sildenafil and CYP3A inhibitors in healthy subjects. Drug Metab Pharmacokinet. 2021;36:100368.

**Meyer 2012** Meyer M, Schneckener S, Ludewig B, Kuepfer L, Lippert J. Using expression data for quantification of active processes in physiologically based pharmacokinetic modeling. Drug Metab Dispos. 2012;40(5):892-901.

**Muirhead 2000** Muirhead GJ, Wulff MB, Fielding A, Kleinermans D, Buss N. Pharmacokinetic interactions between sildenafil and saquinavir/ritonavir. Br J Clin Pharmacol. 2000;50(2):99-107.

**Muirhead 2002a** Muirhead GJ, Rance DJ, Walker DK, Wastall P. Comparative human pharmacokinetics and metabolism of single-dose oral and intravenous sildenafil. Br J Clin Pharmacol. 2002;53 Suppl 1(Suppl 1):13s-20s.

**Muirhead 2002b** Muirhead GJ, Wilner K, Colburn W, Haug-Pihale G, Rouviex B. The effects of age and renal and hepatic impairment on the pharmacokinetics of sildenafil. Br J Clin Pharmacol. 2002;53 Suppl 1(Suppl 1):21s-30s.

**Murtadha 2021** Murtadha M, Raslan MA, Fahmy SF, Sabri NA. Changes in the Pharmacokinetics and Pharmacodynamics of Sildenafil in Cigarette and Cannabis Smokers. Pharmaceutics. 2021;13(6).

**Nichols 2002** Nichols DJ, Muirhead GJ, Harness JA. Pharmacokinetics of sildenafil after single oral doses in healthy male subjects: absolute bioavailability, food effects and dose proportionality. Br J Clin Pharmacol. 2002;53 Suppl 1(Suppl 1):5s-12s.

**Nishimura 2003** Nishimura M, Yaguti H, Yoshitsugu H, Naito S, Satoh T. Tissue distribution of mRNA expression of human cytochrome P450 isoforms assessed by high-sensitivity real-time reverse transcription PCR. Yakugaku Zasshi. 2003;123(5):369-75.

**PK-Sim Ontogeny Database Version 7.3**  https://github.com/Open-Systems-Pharmacology/OSPSuite.Documentation/blob/38cf71b384cfc25cfa0ce4d2f3addfd32757e13b/PK-Sim%20Ontogeny%20Database%20Version%207.3.pdf

**Rodrigues 2003** Rodrigues E, Vilarem MJ, Ribeiro V, Maurel P, Lechner MC. Two CCAAT/enhancer binding protein sites in the cytochrome P4503A1 locus. Potential role in the glucocorticoid response. Eur J Biochem. 2003;270(3):556-64.

**Salerno 2021** Salerno SN, Edginton A, Gerhart JG, Laughon MM, Ambalavanan N, Sokol GM, et al. Physiologically-Based Pharmacokinetic Modeling Characterizes the CYP3A-Mediated Drug-Drug Interaction Between Fluconazole and Sildenafil in Infants. Clin Pharmacol Ther. 2021;109(1):253-62.

**Sawatdee 2019** Sawatdee S, Atipairin A, Sae Yoon A, Srichana T, Changsan N. Enhanced dissolution of sildenafil citrate as dry foam tablets. Pharm Dev Technol. 2019;24(1):1-11.

**Spence 2008** Spence R, Mandagere A, Dufton C, Venitz J. Pharmacokinetics and safety of ambrisentan in combination with sildenafil in healthy volunteers. J Clin Pharmacol. 2008;48(12):1451-9.

**Takano 2016** Takano J, Maeda K, Bolger MB, Sugiyama Y. The Prediction of the Relative Importance of CYP3A/P-glycoprotein to the Nonlinear Intestinal Absorption of Drugs by Advanced Compartmental Absorption and Transit Model. Drug Metab Dispos. 2016;44(11):1808-18.

**Walker 1999** Walker DK, Ackland MJ, James GC, Muirhead GJ, Rance DJ, Wastall P, et al. Pharmacokinetics and metabolism of sildenafil in mouse, rat, rabbit, dog and man. Xenobiotica. 1999;29(3):297-310.

**Wang 2008** Wang Y, Chow MS, Zuo Z. Mechanistic analysis of pH-dependent solubility and trans-membrane permeability of amphoteric compounds: application to sildenafil. Int J Pharm. 2008;352(1-2):217-24.

**Warrington 2000** Warrington JS, Shader RI, von Moltke LL, Greenblatt DJ. In vitro biotransformation of sildenafil (Viagra): identification of human cytochromes and potential drug interactions. Drug Metab Dispos. 2000;28(4):392-7.

**Willmann 2007** Willmann S, Höhn K, Edginton A, Sevestre M, Solodenko J, Weiss W, et al. Development of a physiology-based whole-body population model for assessing the influence of individual variability on the pharmacokinetics of drugs. J Pharmacokinet Pharmacodyn. 2007;34(3):401-31.

**Wilner 2002** Wilner K, Laboy L, LeBel M. The effects of cimetidine and antacid on the pharmacokinetic profile of sildenafil citrate in healthy male volunteers. Br J Clin Pharmacol. 2002;53 Suppl 1(Suppl 1):31s-6s.

