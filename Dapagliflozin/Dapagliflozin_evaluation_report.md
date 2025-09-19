# Building and Evaluation of a PBPK Model for Dapagliflozin in Adults

| Version                                         | 2.0-OSP12.1                                                   |
| ----------------------------------------------- | ------------------------------------------------------------ |
| based on *Model Snapshot* and *Evaluation Plan* | https://github.com/Open-Systems-Pharmacology/Dapagliflozin-Model/releases/tag/v2.0 |
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
     * [3.3.3 Overview](#ct-profiles-overview)
 * [4 Conclusion](#conclusion)
 * [5 References](#main-references)

# 1 Introduction<a id="introduction"></a>

Dapagliflozin is an active, highly selective sodium-glucose transport protein 2 (SGLT2) inhibitor that improves glycemic control in patients with type 2 diabetes mellitus by reducing renal glucose reabsorption leading to urinary glucose excretion (glucuresis). It is administered orally.

Dapagliflozin is predominantly metabolized by uridine diphosphate-glucuronosyltransferase 1A9 (UGT1A9) in the liver and kidneys to the major metabolite dapagliflozin 3-O-glucuronide and can be considered a sensitive substrate for characterization of UGT1A9 activity. In a clinical drug interaction study, co-administration of mefenamic acid with dapagliflozin resulted in a dapagliflozin AUC ratio of 1.51 and C<sub>max</sub> ratio of 1.13 ([Kasichayanula 2013a](#5-references)).

Using published clinical data, the objective is to establish a whole-body PBPK model for dapagliflozin with a quantitative representation of its UGT1A9 metabolism.

The herein presented model building and evaluation report evaluates the performance of the PBPK model for dapagliflozin in (healthy) adults.

# 2 Methods<a id="methods"></a>

## 2.1 Modeling Strategy<a id="modeling-strategy"></a>

The general concept of building a PBPK model has previously been described by Kuepfer *et al.* ([Kuepfer 2016](#5-references)). Relevant information on anthropometric (height, weight) and physiological parameters (e.g. blood flows, organ volumes, binding protein concentrations, hematocrit, cardiac output) in adults was gathered from the literature and has been previously published ([PK-Sim Ontogeny Database Version 7.3](#5-references)). The information was incorporated into PK-Sim® and was used as default values for the simulations in adults.

The  applied activity and variability of plasma proteins and active processes that are integrated into PK-Sim® are described in the publicly available PK-Sim® Ontogeny Database Version 7.3 ([Schlender 2016](#5-references)) or otherwise referenced for the specific process.

First, a base mean model was built using clinical Phase I data including selected single dose studies with intravenous and oral applications (capsule) of dapagliflozin to find an appropriate structure to describe the pharmacokinetics in plasma. The mean PBPK model was developed using a typical European individual. The relative tissue-specific expressions of enzymes predominantly being involved in the metabolism of dapagliflozin (UGT1A9 and UGT2B7) were considered based on high-sensitive real-time RT-PCR ([Nishimura 2013](#5-references)). Absolute tissue-specific expressions were obtained by considering the respective absolute concentration in the liver as reported by Ohtsuki *et al.* ([Ohtsuki  2012](#5-references)).

Unknown parameters (see below) were identified using the Parameter Identification module provided in PK-Sim®. Structural model selection was mainly guided by visual inspection of the resulting description of data and biological plausibility.

Once the appropriate structural model was identified, additional parameters for tablet formulations were identified. 

The model was then verified by simulating:

- multiple dose studies
- a food effect study

Details about input data (physicochemical, *in vitro* and clinical) can be found in [Section 2.2](#22-data).

Details about the structural model and its parameters can be found in [Section 2.3](#23-model-parameters-and-assumptions).

## 2.2 Data<a id="data"></a>

### 2.2.1 In vitro / physicochemical Data

A literature search was performed to collect available information on physicochemical properties of dapagliflozin. The obtained information from literature is summarized in the table below. 

| **Parameter**   | **Unit** | **Value** | Source                                           | **Description**                                 |
| :-------------- | -------- | --------- | ------------------------------------------------ | ----------------------------------------------- |
| MW              | g/mol    | 408.873   | [DrugBank DB06292](#5-references)                | Molecular weight                                |
| pK<sub>a</sub>  |          | 12.57     | [DrugBank DB06292](#5-references)                | Acid dissociation constant                      |
| Solubility (pH) | mg/mL    | 0.173 (7) | [DrugBank DB06292](#5-references)                | Aqueous Solubility                              |
| logP            |          | 2.7       | [DrugBank DB06292](#5-references) (experimental) | Partition coefficient between octanol and water |
| f<sub>u</sub>   | %        | 9         | [Obermeier 2009](#5-references)                  | Fraction unbound in plasma                      |
| B/P ratio       |          | 0.88      | [Obermeier 2009](#5-references)                  | Blood to plasma ratio                           |

### 2.2.2 Clinical Data

A literature search was performed to collect available clinical data on dapagliflozin in healthy adults.

#### 2.2.2.1 Model Building

The following studies were used for model building (training data):

| Publication                                                  | Arm / Treatment / Information used for model building        |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [Boulton 2013](#5-references)                                | 14C-dapagliflozin intravenous and<br />Dapagliflozin oral administration |
| [DeFronzo 2013](#5-references)                               | Healthy subjects with a single oral dose of 10 mg            |
| [Imamura 2013](#5-references)                                | Control phase with a single oral dose of 10 mg               |
| [Kasichayanula 2008](#5-references)                          | Mass balance information                                     |
| [Kasichayanula 2011a](#5-references)                         | Fasted, single oral dose of 10 mg                            |
| [Kasichayanula 2011b](#5-references)                         | Control phases of study 1, 2 and 3<br />(single oral doses of 20 mg or 50 mg) |
| [Kasichayanula 2011c](#5-references)                         | Healthy subjects with a single oral dose of 10 mg            |
| [Kasichayanula 2012](#5-references)                          | Control phase with a single oral dose of 20 mg               |
| [Kasichayanula 2013a](#5-references)                         | Control phases of study 1 and 2<br />(single oral doses of 10 mg) |
| [Kasichayanula 2013b](#5-references)                         | Healthy subjects with normal kidney function<br />with a single oral dose of 50 mg |
| [Komoroski 2009](#5-references) and<br />[FDA Clinical Pharmacology Review for NDA 202293](#5-references) | SAD (single ascending dose) 2.5 to 500 mg (fasted)<br />MAD (multiple ascending dose) 2.5 to 100 mg (**day 1 data only**) |
| [Vakkalagadda 2016](#5-references)                           | Dapagliflozin only (single oral dose 10 mg)                  |

Kasichayanula *et al.* ([Kasichayanula 2008](#5-references)) investigated the mass balance of dapagliflozin in healthy subjects after a single oral dose of 50 mg. The following table gives an overview of the results:

| Output                     | reported | normalized** |
| -------------------------- | -------- | ------------ |
| Total recovery after 312 h | 96.15%   |              |
| Urine                      | 75.16%   |              |
| - unchanged                | 1.20%    | 1.23%        |
| - as metabolites           | 72.00%   | 73.93%       |
| Feces                      | 20.99%   |              |
| - unchanged                | 15.40%   | 18.90%       |
| - as metabolites           | 1.70%    | 2.09%        |

** to sum up to total excretion of urine and feces, respectively.

The metabolic pattern was determined as shown in the following table.

| Output                              | reported | normalized** | add fraction excretion to feces of unchanged dapagliflozin to  glucuronides*** |
| ----------------------------------- | -------- | ------------ | ------------------------------------------------------------ |
| Dapagliflozin-3-O-glucuronide       | 60.70%   | 61.44%       | 78.80%                                                       |
| Dapagliflozin-2-O-glucuronide       | 5.40%    | 5.47%        | 7.01%                                                        |
| Dapagliflozin oxidative metabolites | 9.00%    | 9.11%        | 9.11%                                                        |
| **SUM**                             |          | **76.01%**   | **94.92%**                                                   |

** to sum up to the values of metabolic quantifications from the table above (73.93% + 2.09%)

*** The fraction excretion to feces of unchanged dapagliflozin of 18.90% (see above) was added and distributed proportionally to dapagliflozin-3-O-glucuronide and dapagliflozin-2-O-glucuronide under the assumption that the measured fraction of unchanged dapagliflozin resulted from originally glucuronidated metabolites that underwent biliary excretion and subsequent degradation to dapagliflozin by bacterial glucuronidases in feces.

The following table shows the final mass balance data used for model building under the assumption of that unchanged dapagliflozin molecules in feces were originally glucuronides. Please refer to [Section 2.3](#23-model-parameters-and-assumptions) for rationale.

| Observer                                                     | Value      |
| ------------------------------------------------------------ | ---------- |
| Fraction excreted  to urine of unchanged dapagliflozin       | 1.23%      |
| Fraction metabolized UGT1A9 (to dapagliflozin-3-O-glucuronide) | 78.80%     |
| Fraction metabolized UGT2B7 (to dapagliflozin-2-O-glucuronide) | 7.01%      |
| Fraction metabolized to oxidative  metabolites               | 9.11%      |
| **SUM**                                                      | **96.15%** |

#### 2.2.2.2 Model Verification

The following studies were used for model verification:

| Publication                                                  | Arm / Treatment / Information used for model verification    |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [Chang 2015](#5-references)                                  | Study 1 Treatment A (single oral dose of 5 mg as IC (individual component) tablet) and<br /> Study 2 Treatment A (single oral dose of 10 mg as IC tablet) |
| [Komoroski 2009](#5-references) and<br />[FDA Clinical Pharmacology Review for NDA 202293](#5-references) | MAD (multiple ascending dose) 2.5 to 100 mg (day 7 and 14)   |
| [Komoroski 2009](#5-references)                              | Single oral dose 250 mg (fed)                                |

## 2.3 Model Parameters and Assumptions<a id="model-parameters-and-assumptions"></a>

### 2.3.1 Absorption

Studies including oral applications of dapagliflozin used for model building applied either a capsule or immediate release tablets. They all demonstrated rapid and extensive absorption. The availability of dense data during absorption, data covering a broad range of doses (from 2.5 up to 500 mg), and intravenous pharmacokinetic data ([Boulton 2013](#5-references)) allowed the identification of the *in vivo* intestinal permeability and an effective *in vivo* solubility in this PBPK model (see also [Section 2.3.4](#234-automated-parameter-identification)).

During model building, two different "data scenarios" regarding mass balance information were tested:

**Scenario 1**: The measured fraction excreted to feces as unchanged drug of approx. 19% resulted from incomplete absorption (assuming f<sub>a</sub>  ~ 0.81).

**Scenario 2**:  The measured fraction excretion to feces of unchanged dapagliflozin resulted from originally glucuronidated metabolites that underwent biliary excretion and subsequent degradation to dapagliflozin by bacterial glucuronidases in feces (assuming f<sub>a</sub> ~ 1). The cleavage of hepatobiliary secreted glucuronides to the aglycone (e.g. parent drug) by beta-glucuronidases in the colon was reported previously ([Blaut 2013](#5-references), [Molly 1993](#5-references), [Possemiers 2004](#5-references), [Sakamoto 2002](#5-references)). 

Scenario 1 did not allow to find a good description of the pharmacokinetic data. Thus, scenario 2 was used during further model building. Note that this increased the fraction metabolized via UGT1A9 and UGT2B7.

The dissolution of the tablets from Chang *et al.* ([Chang 2015](#5-references)) - referenced as individual component (IC) tablets - were implemented via an empirical Weibull dissolution tablet. The respective parameters were identified via manual sensitivity analysis.

### 2.3.2 Distribution

Dapagliflozin is moderately protein bound (91 %) in plasma ([Kasichayanula 2014](#5-references)). This value was used in this PBPK model. It was assumed that the major binding partner is albumin.

An important parameter influencing the resulting volume of distribution is lipophilicty. The reported experimental logP value of 2.7 ([DrugBank DB06292](#5-references)) served as a starting value. Finally, the model parameters `Lipophilicity` and `logP (veg.oil/water)` were optimized to match best clinical data (see also [Section 2.3.4](#234-automated-parameter-identification)).

After testing the available organ-plasma partition coefficient and cell permeability calculation methods built in PK-Sim, observed clinical data was best described by choosing the partition coefficient calculation by `Rodgers and Rowland` and cellular permeability calculation by `PK-Sim Standard`. The specific organ permeability was also optimized to match best clinical data (see also [Section 2.3.4](#234-automated-parameter-identification)).

The reported blood to plasma ratio of 0.88 ([Obermeier 2009](#5-references)) was fixed in the model.

### 2.3.3 Metabolism and Elimination

As previously described in [Section 2.2.2](#222-clinical-data),  mass balance data ([Kasichayanula 2008](#5-references), [Obermeier 2009](#5-references), [Kasichayanula 2014](#5-references)) indicated that UGT1A9 is predominatly responsible for the metabolism of dapagliflozin to dapagliflozin-3-O-glucuronide. A minor fraction is metabolized via UGT2B7 to dapagliflozin-2-O-glucuronide and via oxidative cytochrome-P450 enzymes.

In summary, three metabolic first order routes were implement into the model:

* UGT1A9-specific clearance
* UGT2B7-specific clearance
* an unspecific hepatic oxidative clearance ("Hepatic-CYP")
  (The hypothetical lumped Hepatic-CYP enzyme was assumed to be expressed only in the liver with a reference concentration of 1 µmol/L.)

Additionally, a renal clearance (assumed to be mainly driven by glomerular filtration) was implemented.

This clearance and excretion pathways were quantified during parameter optimization to best match clinical data (see also [Section 2.2.2](#222-clinical-data), [Section 2.3.1](#231-absorption), and [Section 2.3.4](#234-automated-parameter-identification)).

### 2.3.4 Automated Parameter Identification

This is the result of the final parameter identification.

| Model Parameter                    | Optimized Value | Unit       |
| ---------------------------------- | --------------- | ---------- |
| `Lipophilicity`                    | 2.672           | Log Units  |
| `logP (veg.oil/water)`             | 2.083           | Log Units  |
| `Permeability`                     | 3.75E-04        | cm/min     |
| `Specific intestinal permeability` | 3.97E-05        | cm/min     |
| `Solubility at reference pH`       | 0.221           | mg/ml      |
| `CLspec/[Enzyme]` (UGT1A9)         | 0.399           | l/µmol/min |
| `CLspec/[Enzyme]` (UGT2B7)         | 6.60E-03        | l/µmol/min |
| `CLspec/[Enzyme]` (Hepatic-CYP)    | 0.143           | l/µmol/min |
| `GFR fraction`                     | 0.79            |            |
| `Blood/Plasma concentration ratio` | 0.88 FIXED      |            |

# 3 Results and Discussion<a id="results-and-discussion"></a>

The PBPK model for dapagliflozin was developed and verified with clinical pharmacokinetic data.

The model was evaluated covering data from studies including in particular

* intravenous and oral administrations.
* single and multiple doses.
* a dose range of 2.5 to 500 mg.
* fasted and fed state administrations.

The model quantifies metabolism via UGT1A9 and UGT2B7.

The next sections show:

1. the final model parameters for the building blocks: [Section 3.1](#31-final-input-parameters).
2. the overall goodness of fit: [Section 3.2](#32-diagnostics-plots).
3. simulated vs. observed concentration-time profiles for the clinical studies used for model building and for model verification: [Section 3.3](#33-concentration-time-profiles).

## 3.1 Final input parameters<a id="final-input-parameters"></a>

The compound parameter values of the final PBPK model are illustrated below.

### Compound: Dapagliflozin

#### Parameters

Name                                             | Value                   | Value Origin                                                                                               | Alternative      | Default
------------------------------------------------ | ----------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------- | -------
Solubility at reference pH                       | 0.2210041453 mg/ml      | Parameter Identification-Parameter Identification-Value updated from 'PI full  (perm)' on 2019-08-23 15:34 | Water solubility | True   
Reference pH                                     | 7                       | Database-DrugBank DB06292                                                                                  | Water solubility | True   
Lipophilicity                                    | 2.6719093089 Log Units  | Parameter Identification-Parameter Identification-Value updated from 'PI full  (perm)' on 2019-08-23 15:34 | Optimized        | True   
Fraction unbound (plasma, reference value)       | 0.09                    | Publication-Kasichayanula et al. 2014                                                                      | Human            | True   
Permeability                                     | 0.00037527645658 cm/min | Parameter Identification-Parameter Identification-Value updated from 'PI full  (perm)' on 2019-08-23 15:34 | Optimized        | True   
Specific intestinal permeability (transcellular) | 3.9684694792E-05 cm/min | Parameter Identification-Parameter Identification-Value updated from 'PI full  (perm)' on 2019-08-23 15:34 | Optimized        | True   
Cl                                               | 1                       |                                                                                                            |                  |        
Is small molecule                                | Yes                     |                                                                                                            |                  |        
Molecular weight                                 | 408.873 g/mol           |                                                                                                            |                  |        
Plasma protein binding partner                   | Albumin                 |                                                                                                            |                  |        

#### Calculation methods

Name                    | Value              
----------------------- | -------------------
Partition coefficients  | Rodgers and Rowland
Cellular permeabilities | PK-Sim Standard    

#### Processes

##### Metabolizing Enzyme: UGT1A9-Optimized

Molecule: UGT1A9

Metabolite: Dapagliflozin-3-O-glucuronide

###### Parameters

Name                 | Value                  | Value Origin                                                                                              
-------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------
Enzyme concentration | 1 µmol/l               |                                                                                                           
Specific clearance   | 0 1/min                |                                                                                                           
CLspec/[Enzyme]      | 0.399443557 l/µmol/min | Parameter Identification-Parameter Identification-Value updated from 'PI full  (perm)' on 2019-08-23 15:34

##### Metabolizing Enzyme: UGT2B7-Optimized

Molecule: UGT2B7

Metabolite: Dapagliflozin-2-O-glucuronide

###### Parameters

Name                 | Value                      | Value Origin                                                                                              
-------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------
Enzyme concentration | 1 µmol/l                   |                                                                                                           
Specific clearance   | 0 1/min                    |                                                                                                           
CLspec/[Enzyme]      | 0.0066043366201 l/µmol/min | Parameter Identification-Parameter Identification-Value updated from 'PI full  (perm)' on 2019-08-23 15:34

##### Systemic Process: Glomerular Filtration-assumed

Species: Human

###### Parameters

Name         |        Value | Value Origin                                                                                              
------------ | ------------:| ----------------------------------------------------------------------------------------------------------
GFR fraction | 0.7899801465 | Parameter Identification-Parameter Identification-Value updated from 'PI full  (perm)' on 2019-08-23 15:34

##### Metabolizing Enzyme: Hepatic-CYP-Optimized

Molecule: Hepatic-CYP

###### Parameters

Name                 | Value                   | Value Origin                                                                                              
-------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------
Enzyme concentration | 1 µmol/l                |                                                                                                           
Specific clearance   | 0 1/min                 |                                                                                                           
CLspec/[Enzyme]      | 0.1432967727 l/µmol/min | Parameter Identification-Parameter Identification-Value updated from 'PI full  (perm)' on 2019-08-23 15:34

### Formulation: IC tablet (Chang 2015)

Type: Weibull

#### Parameters

Name                             | Value  | Value Origin
-------------------------------- | ------ | ------------:
Dissolution time (50% dissolved) | 30 min |             
Lag time                         | 0 min  |             
Dissolution shape                | 0.6    |             
Use as suspension                | Yes    |             

### Formulation: Dissolved

Type: Dissolved

## 3.2 Diagnostics Plots<a id="diagnostics-plots"></a>

Below you find the goodness-of-fit visual diagnostic plots for the PBPK model performance of all data used presented in [Section 2.2.2](#222-clinical-data).

The first plot shows simulated versus observed plasma concentrations, the second weighted residuals versus time. 

<a id="table-3-1"></a>

**Table 3-1: GMFE for Goodness of fit plot for concentration in plasma**

|Group                         |GMFE |
|:-----------------------------|:----|
|IV (model building)           |1.38 |
|PO MD                         |1.22 |
|PO SD fasted (model building) |1.20 |
|PO SD fed                     |1.43 |
|PO SD IC tablets (Chang 2015) |1.27 |
|All                           |1.22 |

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

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/1_time_profile_plot_Dapagliflozin_IV_0_08_mg__perm_.png)

**Figure 3-3: IV 0.08 mg (perm)**

<br>
<br>

<a id="figure-3-4"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/2_time_profile_plot_Dapagliflozin_PO_SD_2_5_mg__perm_.png)

**Figure 3-4: PO SD 2.5 mg (perm)**

<br>
<br>

<a id="figure-3-5"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/3_time_profile_plot_Dapagliflozin_PO_SD_2_5_mg__perm_.png)

**Figure 3-5: PO SD 2.5 mg (perm)**

<br>
<br>

<a id="figure-3-6"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/4_time_profile_plot_Dapagliflozin_PO_SD_2_5_mg__perm_.png)

**Figure 3-6: PO SD 2.5 mg (perm) (urinary excretion)**

<br>
<br>

<a id="figure-3-7"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/5_time_profile_plot_Dapagliflozin_PO_SD_5_mg__perm_.png)

**Figure 3-7: PO SD 5 mg (perm)**

<br>
<br>

<a id="figure-3-8"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/6_time_profile_plot_Dapagliflozin_PO_SD_5_mg__perm_.png)

**Figure 3-8: PO SD 5 mg (perm)**

<br>
<br>

<a id="figure-3-9"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/7_time_profile_plot_Dapagliflozin_PO_SD_5_mg__perm_.png)

**Figure 3-9: PO SD 5 mg (perm) (urinary excretion)**

<br>
<br>

<a id="figure-3-10"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/8_time_profile_plot_Dapagliflozin_PO_SD_10_mg__perm_.png)

**Figure 3-10: PO SD 10 mg (perm)**

<br>
<br>

<a id="figure-3-11"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/9_time_profile_plot_Dapagliflozin_PO_SD_10_mg__perm_.png)

**Figure 3-11: PO SD 10 mg (perm)**

<br>
<br>

<a id="figure-3-12"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/10_time_profile_plot_Dapagliflozin_PO_SD_10_mg__perm_.png)

**Figure 3-12: PO SD 10 mg (perm) (urinary excretion)**

<br>
<br>

<a id="figure-3-13"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/11_time_profile_plot_Dapagliflozin_PO_SD_20_mg__perm_.png)

**Figure 3-13: PO SD 20 mg (perm)**

<br>
<br>

<a id="figure-3-14"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/12_time_profile_plot_Dapagliflozin_PO_SD_20_mg__perm_.png)

**Figure 3-14: PO SD 20 mg (perm)**

<br>
<br>

<a id="figure-3-15"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/13_time_profile_plot_Dapagliflozin_PO_SD_20_mg__perm_.png)

**Figure 3-15: PO SD 2.5 mg (perm) (urinary excretion)**

<br>
<br>

<a id="figure-3-16"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/14_time_profile_plot_Dapagliflozin_PO_SD_50_mg__perm_.png)

**Figure 3-16: PO SD 50 mg (perm)**

<br>
<br>

<a id="figure-3-17"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/15_time_profile_plot_Dapagliflozin_PO_SD_50_mg__perm_.png)

**Figure 3-17: PO SD 50 mg (perm)**

<br>
<br>

<a id="figure-3-18"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/16_time_profile_plot_Dapagliflozin_PO_SD_50_mg__perm_.png)

**Figure 3-18: PO SD 50 mg (perm) (fraction excreted/metabolized)**

<br>
<br>

<a id="figure-3-19"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/17_time_profile_plot_Dapagliflozin_PO_SD_100_mg__perm_.png)

**Figure 3-19: PO SD 100 mg (perm)**

<br>
<br>

<a id="figure-3-20"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/18_time_profile_plot_Dapagliflozin_PO_SD_100_mg__perm_.png)

**Figure 3-20: PO SD 100 mg (perm)**

<br>
<br>

<a id="figure-3-21"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/19_time_profile_plot_Dapagliflozin_PO_SD_100_mg__perm_.png)

**Figure 3-21: PO SD 100 mg (perm) (urinary excretion)**

<br>
<br>

<a id="figure-3-22"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/20_time_profile_plot_Dapagliflozin_PO_SD_250_mg__perm_.png)

**Figure 3-22: PO SD 250 mg (perm)**

<br>
<br>

<a id="figure-3-23"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/21_time_profile_plot_Dapagliflozin_PO_SD_250_mg__perm_.png)

**Figure 3-23: PO SD 250 mg (perm)**

<br>
<br>

<a id="figure-3-24"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/22_time_profile_plot_Dapagliflozin_PO_SD_250_mg__perm_.png)

**Figure 3-24: PO SD 250 mg (perm) (urinary excretion)**

<br>
<br>

<a id="figure-3-25"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/23_time_profile_plot_Dapagliflozin_PO_SD_500_mg__perm_.png)

**Figure 3-25: PO SD 500 mg (perm)**

<br>
<br>

<a id="figure-3-26"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/24_time_profile_plot_Dapagliflozin_PO_SD_500_mg__perm_.png)

**Figure 3-26: PO SD 500 mg (perm)**

<br>
<br>

<a id="figure-3-27"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/010_section_model-building/25_time_profile_plot_Dapagliflozin_PO_SD_500_mg__perm_.png)

**Figure 3-27: PO SD 500 mg (perm) (urinary excretion)**

<br>
<br>

### 3.3.2 Model Verification<a id="model-verification"></a>

<a id="figure-3-28"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/26_time_profile_plot_Dapagliflozin_PO_SD_5_mg_IC_tablet__Chang_2015___perm_.png)

**Figure 3-28: PO SD 5 mg IR tablet (perm)**

<br>
<br>

<a id="figure-3-29"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/27_time_profile_plot_Dapagliflozin_PO_SD_5_mg_IC_tablet__Chang_2015___perm_.png)

**Figure 3-29: PO SD 5 mg IR tablet (perm)**

<br>
<br>

<a id="figure-3-30"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/28_time_profile_plot_Dapagliflozin_PO_SD_10_mg_IC_tablet__Chang_2015___perm_.png)

**Figure 3-30: PO SD 10 mg IR tablet (perm)**

<br>
<br>

<a id="figure-3-31"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/29_time_profile_plot_Dapagliflozin_PO_SD_10_mg_IC_tablet__Chang_2015___perm_.png)

**Figure 3-31: PO SD 10 mg IR tablet (perm)**

<br>
<br>

<a id="figure-3-32"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/30_time_profile_plot_Dapagliflozin_PO_SD_250_mg_fed__perm_.png)

**Figure 3-32: PO SD 250 mg fed (perm) (log)**

<br>
<br>

<a id="figure-3-33"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/31_time_profile_plot_Dapagliflozin_PO_SD_250_mg_fed__perm_.png)

**Figure 3-33: PO SD 250 mg fed (perm)**

<br>
<br>

<a id="figure-3-34"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/32_time_profile_plot_Dapagliflozin_PO_MD_2_5_mg__perm_.png)

**Figure 3-34: PO MD 2.5 mg (perm)**

<br>
<br>

<a id="figure-3-35"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/33_time_profile_plot_Dapagliflozin_PO_MD_2_5_mg__perm_.png)

**Figure 3-35: PO MD 2.5 mg (perm)**

<br>
<br>

<a id="figure-3-36"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/34_time_profile_plot_Dapagliflozin_PO_MD_10_mg__perm_.png)

**Figure 3-36: PO MD 10 mg (perm)**

<br>
<br>

<a id="figure-3-37"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/35_time_profile_plot_Dapagliflozin_PO_MD_10_mg__perm_.png)

**Figure 3-37: PO MD 10 mg (perm)**

<br>
<br>

<a id="figure-3-38"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/36_time_profile_plot_Dapagliflozin_PO_MD_20_mg__perm_.png)

**Figure 3-38: PO MD 20 mg (perm)**

<br>
<br>

<a id="figure-3-39"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/37_time_profile_plot_Dapagliflozin_PO_MD_20_mg__perm_.png)

**Figure 3-39: PO MD 20 mg (perm)**

<br>
<br>

<a id="figure-3-40"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/38_time_profile_plot_Dapagliflozin_PO_MD_50_mg__perm_.png)

**Figure 3-40: PO MD 20 mg (perm)**

<br>
<br>

<a id="figure-3-41"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/39_time_profile_plot_Dapagliflozin_PO_MD_50_mg__perm_.png)

**Figure 3-41: PO MD 50 mg (perm)**

<br>
<br>

<a id="figure-3-42"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/40_time_profile_plot_Dapagliflozin_PO_MD_100_mg__perm_.png)

**Figure 3-42: PO MD 100 mg (perm)**

<br>
<br>

<a id="figure-3-43"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/011_section_model-verification/41_time_profile_plot_Dapagliflozin_PO_MD_100_mg__perm_.png)

**Figure 3-43: PO MD 100 mg (perm)**

<br>
<br>

### 3.3.3 Overview<a id="ct-profiles-overview"></a>

Overview of the multiple ascending dose study stratified by dose and day ([Komoroski 2009](#5-references), [FDA Clinical Pharmacology Review for NDA 202293](#5-references)).

<a id="figure-3-44"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/012_section_ct-profiles-overview/comparison_time_profile_Multiple_Dose_Escalation_Study__day_1__1.png)

**Figure 3-44: Multiple Dose Escalation Study (day 1)**

<br>
<br>

<a id="figure-3-45"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/012_section_ct-profiles-overview/comparison_time_profile_Multiple_Dose_Escalation_Study__day_7__2.png)

**Figure 3-45: Multiple Dose Escalation Study (day 7)**

<br>
<br>

<a id="figure-3-46"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/012_section_ct-profiles-overview/comparison_time_profile_Multiple_Dose_Escalation_Study__day_14__3.png)

**Figure 3-46: Multiple Dose Escalation Study (day 14)**

<br>
<br>

# 4 Conclusion<a id="conclusion"></a>

The herein presented PBPK model adequately describes the pharmacokinetics of dapagliflozin in adults.

In particular, it applies quantitative metabolism by UGT1A9 and UGT2B7. Thus, the model is fit for purpose to be applied for the investigation of drug-drug interactions with regard to its UGT metabolism.

# 5 References<a id="main-references"></a>

**Blaut 2013** Blaut, M., Ecology and physiology of the intestinal tract. Curr Top Microbiol Immunol, 2013. 358: p. 247-72.

**Boulton 2013** Boulton DW, Kasichayanula S, Keung CF, Arnold ME, Christopher LJ, Xu XS, Lacreta F. Simultaneous oral therapeutic and intravenous 14C-microdoses to determine the absolute oral bioavailability of saxagliptin and dapagliflozin. Br J Clin Pharmacol. 2013 Mar;75(3):763-8. doi: 10.1111/j.1365-2125.2012.04391.x.	

**Chang 2015** Chang M, Liu X, Cui D, Liang D, LaCreta F, Griffen SC, Lubin S, Quamina-Edghill D, Boulton DW. Bioequivalence, Food Effect, and Steady-State Assessment of Dapagliflozin/Metformin Extended-release Fixed-dose Combination Tablets Relative to Single-component Dapagliflozin and Metformin Extended-release Tablets in Healthy Subjects. Clin Ther. 2015 Jul 1;37(7):1517-28. doi: 10.1016/j.clinthera.2015.05.004.

**DeFronzo 2013** DeFronzo RA, Hompesch M, Kasichayanula S, Liu X, Hong Y, Pfister M, Morrow LA, Leslie BR, Boulton DW, Ching A, LaCreta FP, Griffen SC. Characterization of renal glucose reabsorption in response to dapagliflozin in healthy subjects and subjects with type 2 diabetes. Diabetes Care. 2013 Oct;36(10):3169-76. doi: 10.2337/dc13-0387.	

**DrugBank DB06292** (https://www.drugbank.ca/drugs/DB06292)	

**FDA Clinical Pharmacology Review for NDA 202293** (https://www.accessdata.fda.gov/drugsatfda_docs/nda/2014/202293Orig1s000ClinPharmR.pdf)	

**Imamura 2013** Imamura A, Kusunoki M, Ueda S, Hayashi N, Imai Y. Impact of voglibose on the pharmacokinetics of dapagliflozin in Japanese patients with type 2 diabetes. Diabetes Ther. 2013 Jun;4(1):41-9. doi: 10.1007/s13300-012-0016-5.	

**Kasichayanula 2008** Kasichayanula S, Yao M, Vachharajani M, et al. Disposition and Mass Balance of [14C]-dapagliflozin after single oral dose in healthy male volunteers. AAPS J. 2008;10(S2).	

**Kasichayanula 2011a** Kasichayanula S, Liu X, Zhang W, Pfister M, Reele SB, Aubry AF, LaCreta FP, Boulton DW. Effect of a high-fat meal on the pharmacokinetics of dapagliflozin, a selective SGLT2 inhibitor, in healthy subjects. Diabetes Obes Metab. 2011 Aug;13(8):770-3. doi: 10.1111/j.1463-1326.2011.01397.x.	

**Kasichayanula 2011b** Kasichayanula S, Liu X, Shyu WC, Zhang W, Pfister M, Griffen SC, Li T, LaCreta FP, Boulton DW. Lack of pharmacokinetic interaction between dapagliflozin, a novel sodium-glucose transporter 2 inhibitor, and metformin, pioglitazone, glimepiride or sitagliptin in healthy subjects. Diabetes Obes Metab. 2011 Jan;13(1):47-54. doi: 10.1111/j.1463-1326.2010.01314.x.	

**Kasichayanula 2011c** Kasichayanula S, Liu X, Zhang W, Pfister M, LaCreta FP, Boulton DW. Influence of hepatic impairment on the pharmacokinetics and safety profile of dapagliflozin: an open-label, parallel-group, single-dose study. Clin Ther. 2011 Nov;33(11):1798-808. doi: 10.1016/j.clinthera.2011.09.011.

**Kasichayanula 2012** Kasichayanula S, Chang M, Liu X, Shyu WC, Griffen SC, LaCreta FP, Boulton DW. Lack of pharmacokinetic interactions between dapagliflozin and simvastatin, valsartan, warfarin, or digoxin. Adv Ther. 2012 Feb;29(2):163-77. doi: 10.1007/s12325-011-0098-x.	

**Kasichayanula 2013a** Kasichayanula S, Liu X, Griffen SC, Lacreta FP, Boulton DW. Effects of rifampin and mefenamic acid on the pharmacokinetics and pharmacodynamics of dapagliflozin. Diabetes Obes Metab. 2013 Mar;15(3):280-3. doi: 10.1111/dom.12024.	

**Kasichayanula 2013b** Kasichayanula S, Liu X, Pe Benito M, Yao M, Pfister M, LaCreta FP, Humphreys WG, Boulton DW. The influence of kidney function on dapagliflozin exposure, metabolism and pharmacodynamics in healthy subjects and in patients with type 2 diabetes mellitus. Br J Clin Pharmacol. 2013 Sep;76(3):432-44. doi: 10.1111/bcp.12056.	

**Kasichayanula 2014** Kasichayanula S, Liu X, Lacreta F, Griffen SC, Boulton DW. Clinical pharmacokinetics and pharmacodynamics of dapagliflozin, a selective inhibitor of sodium-glucose co-transporter type 2. Clin Pharmacokinet. 2014 Jan;53(1):17-27. doi: 10.1007/s40262-013-0104-3.

**Komoroski 2009** Komoroski B, Vachharajani N, Boulton D, Kornhauser D, Geraldes M, Li L, Pfister M. Dapagliflozin, a novel SGLT2 inhibitor, induces dose-dependent glucosuria in healthy subjects. Clin Pharmacol Ther. 2009 May;85(5):520-6. doi: 10.1038/clpt.2008.251.	

**Kuepfer 2016** Kuepfer L, Niederalt C, Wendl T, Schlender JF, Willmann S, Lippert J, Block M, Eissing T, Teutonico D. Applied Concepts in PBPK Modeling: How to Build a PBPK/PD Model.CPT Pharmacometrics Syst Pharmacol. 2016 Oct;5(10):516-531. doi: 10.1002/psp4.12134. Epub 2016 Oct 19. 	

**Molly 1993**	Molly, K., M. Vande Woestyne, and W. Verstraete, Development of a 5-step multi-chamber reactor as a simulation of the human intestinal microbial ecosystem. Appl Microbiol Biotechnol, 1993. 39(2): p. 254-8.

**Nishimura 2013** Nishimura M, Yaguti H, Yoshitsugu H, Naito S, Satoh T. Tissue distribution of mRNA expression of human cytochrome P450 isoforms assessed by high-sensitivity real-time reverse transcription PCR. Yakugaku Zasshi. 2003 May;123(5):369-75.	

**Obermeier 2009** Obermeier M, Yao M, Khanna A, Koplowitz B, Zhu M, Li W, Komoroski B, Kasichayanula S, Discenza L, Washburn W, Meng W, Ellsworth BA, Whaley JM, Humphreys WG. In vitro characterization and pharmacokinetics of dapagliflozin (BMS-512148), a potent sodium-glucose cotransporter type II inhibitor, in animals and humans. Drug Metab Dispos. 2010 Mar;38(3):405-14. doi: 10.1124/dmd.109.029165.	

**Ohtsuki 2012** Ohtsuki S, Schaefer O, Kawakami H, Inoue T, Liehner S, Saito A, Ishiguro N, Kishimoto W, Ludwig-Schwellinger E, Ebner T, Terasaki T. Simultaneous absolute protein quantification of transporters, cytochromes P450, and UDP-glucuronosyltransferases as a novel approach for the characterization of individual human liver: comparison with mRNA levels and activities. Drug Metab Dispos. 2012 Jan;40(1):83-92. doi: 10.1124/dmd.111.042259.	

**PK-Sim Ontogeny Database Version 7.3** (https://github.com/Open-Systems-Pharmacology/OSPSuite.Documentation/blob/38cf71b384cfc25cfa0ce4d2f3addfd32757e13b/PK-Sim%20Ontogeny%20Database%20Version%207.3.pdf)	

**Possemiers 2004**	Possemiers, S., et al., PCR-DGGE-based quantification of stability of the microbial community in a simulator of the human intestinal microbial ecosystem. FEMS Microbiol Ecol, 2004. 49(3): p. 495-507.

**Sakamoto 2002**	Sakamoto, H., et al., Excretion of bisphenol A-glucuronide into the small intestine and deconjugation in the cecum of the rat. Biochim Biophys Acta, 2002. 1573(2): p. 171-6.

**Schlender 2016** Schlender JF, Meyer M, Thelen K, Krauss M, Willmann S, Eissing T, Jaehde U. Development of a Whole-Body Physiologically Based Pharmacokinetic Approach to Assess the Pharmacokinetics of Drugs in Elderly Individuals. Clin Pharmacokinet. 2016 Dec;55(12):1573-1589. 

**Vakkalagadda 2016** Vakkalagadda B, Lubin S, Reynolds L, Liang D, Marion AS, LaCreta F, Boulton DW. Lack of a Pharmacokinetic Interaction Between Saxagliptin and Dapagliflozin in Healthy Subjects: A Randomized Crossover Study. Clin Ther. 2016 Aug;38(8):1890-9. doi: 10.1016/j.clinthera.2016.07.005.	

