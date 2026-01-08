# Building and evaluation of a PBPK model for Metformin in healthy adults

| Version                                         | 1.0-OSP12.1                                                   |
| ----------------------------------------------- | ------------------------------------------------------------ |
| based on *Model Snapshot* and *Evaluation Plan* | https://github.com/Open-Systems-Pharmacology/Metformin-Model/releases/tag/v1.0 |
| OSP Version                                     | 12.1                                                          |
| Qualification Framework Version                 | 3.4                                                          |

This evaluation report and the corresponding PK-Sim project file are filed at:

https://github.com/Open-Systems-Pharmacology/OSP-PBPK-Model-Library/

# Table of Contents

 * [1 Introduction](#1)
 * [2 Methods](#2)
   * [2.1 Modeling strategy](#21)
   * [2.2 Data used](#22)
     * [2.2.1 In vitro and physicochemical data ](#invitro-and-physico-chemical-data)
     * [2.2.2 Clinical data ](#clinical-data)
   * [2.3 Model parameters and assumptions](#23)
     * [2.3.1 Absorption](#model-parameters-and-assumptions-absorption)
     * [2.3.2 Distribution](#model-parameters-and-assumptions-distribution)
     * [2.3.3 Metabolism and Elimination](#model-parameters-and-assumptions-metabolism)
     * [2.3.4 Automated Parameter Identification](#model-parameters-and-assumptions-identification)
 * [3 Results and Discussion](#3)
   * [3.1 Metformin final input parameters](#31)
   * [3.2 Metformin Diagnostics Plots](#32)
   * [3.3 Concentration-Time Profiles](#33)
     * [3.3.1 Model Building](#331)
     * [3.3.2 Model Verification](#332)
 * [4 Conclusion](#4)
 * [5 References](#5)

# 1 Introduction<a id="1"></a>

The presented model building and evaluation report evaluates the performance of a PBPK model for metformin in healthy adults.

The herein presented model was developed and published by Hanke et al. ([Hanke 2020](#5-references)) and adjusted later on to PK-Sim V11 by re-optimizing OCT2.

Metformin is widely used as first-line treatment of type 2 diabetes. It is a highly hydrophilic compound, positively
charged at physiological pH and depends on active transport for its absorption, distribution and
excretion. The absorption of metformin is saturable and reported to be restricted to the upper
intestine ([Vidon 1988](#5-references)). The excretion of metformin is mainly mediated via the sequential action of OCT2 and
MATE in the kidney, with a moderate contribution of renal glomerular filtration (approximately
20 %). Metformin is recommended by the FDA as OCT2/MATE victim drug for the use in clinical
DDI studies and drug labeling ([FDA 2017](#5-references)).

The herein presented PBPK model of metformin PBPK model has been developed and evaluated by comparing simulations to observed data of both intravenously and orally administered metformin covering a dosing range from 0.001 to 2550 mg.

The presented model includes the following features:

- transport by PMAT,
- transport by OCT1,
- transport by OCT2,
- transport by MATE,
- renal clearance by glomerular filtration,
- oral absorption with dissolution rate assigned to a Weibull function.

# 2 Methods<a id="2"></a>

## 2.1 Modeling strategy<a id="21"></a>

The general concept of building a PBPK model has previously been described by Kuepfer et al. ([Kuepfer 2016](#5-references)). Relevant information on anthropometric (height, weight) and physiological parameters (e.g., blood flows, organ volumes, binding protein concentrations, hematocrit, cardiac output) in adults was gathered from the literature and has been previously published ([Willmann 2007](#5-references)). The information was incorporated into PK-Sim® and was used as default values for the simulations in adults.

Transporters and metabolizing enzymes relevant to the pharmacokinetics of the modeled drugs were
implemented in agreement with current literature, utilizing the PK-Sim® expression database ([PK-Sim Ontogeny Database Version 7.3](#5-references)) or otherwise referenced for the specific process.

A model was built based on clinical data from studies with intravenous and oral administration of metformin. The studies reported individual or mean plasma concentrations of metformin,  and some of the studies reported fraction excreted to urine. For the studies reporting intravenous administration, metformin was administered in doses of 0.001 to 1000 mg. For the studies reporting oral administration, metformin was administered in doses of 0.001–2550 mg.

Virtual mean individuals were generated for each study according to the published demographic information, with corresponding age, weight, height, sex, ethnicity, hematocrit and GFR, if available. If no information was provided, a default virtual individual was applied (30 years of age, male, European, mean weight, height, hematocrit and GFR characteristics from the PK-Sim® population database).

The clinical datasets for metformin PBPK modeling were divided into a model building dataset for model building and a test dataset for model evaluation and verification. Both datasets are presented in [Section 2.2](#22-data-used).

A specific set of parameters ([Section 2.3.4.](#model-parameters-and-assumptions-identification)) were optimized to describe the disposition of metformin using the Parameter Identification module provided in PK-Sim®. To limit the parameters to be optimized during model building, the minimal number of processes necessary to mechanistically describe the pharmacokinetics and drug-drug interactions (DDIs) of the modeled drugs were implemented into the models. The saturable absorption is implemented via PMAT and OCT1 in the small intestine. As late absorption of orally administered metformin is neither consistent with the reported plasma concentration time-profiles nor with the incomplete absorption of metformin, the relative expression of PMAT and OCT1 in the large intestinal mucosa was set to zero. Furthermore, no information regarding active transport processes at the basolateral side of the intestinal mucosa could be obtained. Therefore, the passive permeability from the intracellular to the interstitial space of the small intestinal mucosa was optimized.

Details about input data (physicochemical, *in vitro* and clinical) can be found in [Section 2.2](#22-data-used).

Details about the structural model and its parameters can be found in [Section 2.3](#23-model-parameters-and-assumptions).

## 2.2 Data used<a id="22"></a>

### 2.2.1 In vitro and physicochemical data <a id="invitro-and-physico-chemical-data"></a>

A literature search was performed to collect available information on physicochemical properties of metformin. The obtained information from literature is summarized in the table below, and was used for model building. Final model parameters are stated in [Section 3.1](#31-metformin-final-input-parameters).

| **Parameter**           | **Unit** | **Value** | Source                               | **Description**                                              |
| :---------------------- | ----------- | --------- | ------------------------------------ | ------------------------------------------------------------ |
| MW                      | g/mol    |  129.16   | [Wishart 2006](#5-references)         | Molecular weight |
| pK<sub>a</sub> (base)   |          |  2.80      | [Desai 2014](#5-references)         | Base dissociation constant |
| pK<sub>b</sub> (base)   |          | 11.50      | [Desai 2014](#5-references)         | Base dissociation constant |
| Solubility (pH 6.8)     | g/L    |  350.90      | [Desai 2014](#5-references)         | Solubility |
| logP                    |          | -1.43     | [Graham 2011](#5-references)| Partition coefficient between octanol and water |
| fu                      | %        | 100      | [Tucker 1981](#5-references), [Pentikäinen 1979](#5-references), [Sirtori 1978](#5-references)            | Fraction unbound                |                       
| PMAT Hill     |    | 3     | [Zhou 2007](#5-references) | PMAT Hill coefficient, Literature value = 2.64         |
| K<sub>m</sub> OCT1     | µmol/L   | 1180.00     | [Chen 2009](#5-references) | OCT1 Michaelis-Menten constant            |
| K<sub>m</sub> OCT2      | µmol/L   | 810.00     | [Chen 2009](#5-references) | OCT2 Michaelis-Menten constant            |
| K<sub>m</sub> MATE1      | µmol/L   | 283.00    | [Yin 2016](#5-references) |  MATE1 Michaelis-Menten constant         |
| Tablet fasted Weibull shape           | -        |  1.36      | [Block 2008](#5-references) | Dissolution profile shape |
| Tablet fasted Weibull time            | min      |  7.90     | [Block 2008](#5-references)                 | Dissolution time (50% dissolved)                             |

### 2.2.2 Clinical data <a id="clinical-data"></a>

A literature search was performed to collect available clinical data on metformin in adults. 

The following publications were used for model building (training dataset) and model verification (test dataset):

| **Dose [mg]** | **Dosing** | **PK data** |**Dataset**| **Reference** |
| --------------- | ------------------- | ----------------------- | ----------------- |----------------- |
| 0.00145| iv, bolus, sd |plasma, blood and tissue (kidney,liver, intestines and muscle)|training|[Gormsen 2016](#5-references) |
| 250| iv (15 min), sd |plasma, excretion into urine|training|[Tucker 1981](#5-references)| 
| 500| iv (5 min), sd |plasma, excretion into urine|test|[Pentikäinen 1979](#5-references)| 
| 1000| iv (bolus), sd |plasma, excretion into urine|training|[Sirtori 1978](#5-references)| 
| 0.0008556| po, -, fasted, sd |plasma and tissue (kidney, liver, and muscle)|training|[Gormsen 2016](#5-references)
| 10| po, sol, fasted, sd |plasma, excretion into urine|training|[Stopfer 2018](#5-references)|
| 250| po, tab, fed, qd |plasma, excretion into urine|test|[Somogyi 1987](#5-references)|
| 500| po, -, fasted, sd |plasma, excretion into urine|test|[Wang 2008](#5-references)|
| 500| po, sol, fasted, sd |plasma, excretion into urine, and tissue (kidney)|training|[Boehringer 2018](#5-references)|
| 500| po, tablet, fed, sd |plasma|test|[Caillé 1993](#5-references)|
| 500| po, tablet, fed, sd |plasma, excretion into urine|test|[Gusler 2001](#5-references)|
| 500| po, tablet, fasted, sd |plasma|test|[Najib 2002](#5-references)|
| 500| po, tablet, fasted, sd |plasma, excretion into urine|test|[Pentikäinen 1979](#5-references)|
| 500| po, tablet, fasted, sd |plasma, excretion into urine|test|[Sambol 1996b](#5-references)|
| 500| po, tablet, fasted, sd |plasma, excretion into urine|training|[Stopfer 2016](#5-references)|
| 500| po, tablet, fed, sd |plasma, excretion into urine|test|[Tucker 1981](#5-references)|
| 500| po, tablet, fed, bid |plasma, excretion into urine|test|[DiCicco 2014](#5-references)|
| 500 <sup>(a)</sup>| po, tablet, fasted, bid |plasma|test|[Jang 2016](#5-references)|
| 500 <sup>(a)</sup>| po, tablet, fasted, bid |plasma|test|[Kim 2014](#5-references)|
| 500| po, tablet, fasted, bid |plasma|test|[Manitpisitkul 2014](#5-references)|
| 500 <sup>(a)</sup>| po, tablet, fasted, bid |plasma|test|[Oh 2016](#5-references)|
| 750 <sup>(b)</sup>| po, tablet, fasted, bid |plasma|test|[Cho 2011 ](#5-references)|
| 750 <sup>(b)</sup>| po, tablet, fasted, bid |plasma|test|[Cho 2014](#5-references)|
| 750 <sup>(b)</sup>| po, tablet, fasted, bid |plasma|test|[Ding 2014](#5-references)|
| 850| po, sol, fasted, sd |plasma, excretion into urine|training|[Sambol 1996b](#5-references)|
| 850 <sub>(c)<sub>| po, tablet, fasted, bid |plasma|test|[Chen 2009](#5-references)|
| 850| po, tablet, fasted, sd |plasma|test|[Morrissey 2016](#5-references)|
| 850| po, tablet, fed, sd |blood, plasma|test|[Robert 2003 ](#5-references)|
| 850| po, tablet, fasted, sd |blood, plasma, excretion into urine|test|[Sambol 1995](#5-references)|
| 850| po, tablet, fasted, sd |plasma, excretion into urine|test|[Sambol 1996a](#5-references)|
| 850| po, tablet, fed, sd |plasma, excretion into urine|training|[Sambol 1996b](#5-references)|
| 850| po, tablet, fed, sd |plasma, excretion into urine|training|[Sambol 1996b](#5-references)|
| 850<sup>(c)</sup>| po, tablet, fasted, bid |plasma, excretion into urine|test|[Hibma 2016](#5-references)|
| 850| po, tablet, fasted, tid |plasma|test|[Sambol 1996a](#5-references)|
| 1000| po, tablet, fasted, sd |plasma, excretion into urine|test|[Johansson 2014](#5-references)|
| 1000| po, tablet, fasted, qd |plasma|test|[Gan 2016](#5-references)|
| 1500| po, tablet, fed, qd |plasma|test|[Tucker 1981](#5-references)|
| 1700| po, tablet, fasted, sd |plasma, excretion into urine|training|[Sambol 1996a](#5-references)|
| 2550| po, tablet, fasted, sd |plasma, excretion into urine|training|[Sambol 1996a](#5-references)|

<sup>(a)</sup> first dose 750 mg, second dose 500 mg

<sup>(b)</sup> first dose 1000 mg, second dose 750 mg

<sup>(c)</sup> first dose 1000 mg, second dose 850 mg

## 2.3 Model parameters and assumptions<a id="23"></a>

### 2.3.1 Absorption<a id="model-parameters-and-assumptions-absorption"></a>

The parameter value for `Specific intestinal permeability` was optimized based on clinical oral data, see [Section 2.3.4](#model-parameters-and-assumptions-identification). The saturable
absorption is implemented via PMAT and OCT1 in the small intestine. As late absorption of orally administered metformin is neither consistent with the reported plasma concentration time-profiles nor with the incomplete absorption of metformin, the relative expression of PMAT and OCT1 in the large intestinal mucosa was set to zero. Additionally, no information regarding active transport processes at the basolateral side of the intestinal mucosa could be obtained, therefore, the passive  basolateral permeability `(P (intracellular -> interstitial)` was optimized, see [Section 2.3.4](#model-parameters-and-assumptions-identification).

The measured solubility of metformin hydrochloride
in a phosphate buffer at pH 6.8 was used in the model (see [Section 2.2.1](#invitro-and-physico-chemical-data)).

The dissolution of tablets was implemented via empirical Weibull dissolution. 

### 2.3.2 Distribution<a id="model-parameters-and-assumptions-distribution"></a>

Metformin is not bound to plasma proteins (fu = 100 %) (see [Section 2.2.1](#invitro-and-physico-chemical-data)) ([Sirtori 1978](#5-references), [Pentikäinen 1979](#5-references) and [Tucker 1981](#5-references)). A value of 100% was used in this PBPK model for `Fraction unbound (plasma, reference value)`. The major binding partner was set to albumin (see [Section 2.2.1](#invitro-and-physico-chemical-data)).

An important parameter influencing the resulting volume of distribution is lipophilicity. The reported experimental logP of -1.43 was used in this model (see [Section 2.2.1](#in-vitro-and-physicochemical-data)). 

After testing the available organ-plasma partition coefficient and cell permeability calculation methods built in PK-Sim®, observed clinical data was best described by choosing the partition coefficient calculation by `PK-SIM Standard` and cellular permeability calculation by `Charged dependent Schmitt normalized to PK-SIM`.

### 2.3.3 Metabolism and Elimination<a id="model-parameters-and-assumptions-metabolism"></a>

Following its absorption, metformin is not bound to plasma proteins, not metabolized, and not secreted to bile. Metformin is excreted unchanged with the urine by passive glomerular filtration and active renal secretion through the sequential action of organic cation transporter 2 (OCT2) and multidrug and toxin extrusion protein 1 (MATE1).
The transport proteins involved in metformin PK were implemented in the model as described below: 

* PMAT

The PMAT expression profiles are based on high-sensitive real-time RT-PCR ([Nishimura 2005](#5-references)). Metabolic enzyme activity was described as saturable process following Hill kinetics, where the `PMAT Hill` was taken from literature and `Km`and `kcat` where optimized based on clinical data (see [Section 2.3.4](#model-parameters-and-assumptions-identification)).

* OCT1

The OCT1 expression profiles are based on Microarray expression data ([Kolesnikov 2015](#5-references)). Transporter activity was described as saturable process following Michaelis-Menten kinetics, where the `Km` was taken from literature and `kcat` was optimized based on clinical data (see [Section 2.3.4](#model-parameters-and-assumptions-identification)).

* OCT2

The OCT2 expression profiles are based on Expressed Sequece Tags (EST) ([NCBI 2019](#5-references)). Transporter activity was described as saturable process following Michaelis-Menten kinetics, where the `Km` was taken from literature and `kcat` was optimized based on clinical data (see [Section 2.3.4](#model-parameters-and-assumptions-identification)).

* MATE1

The MATE1 expression profiles assumed 100% expression in the Kidney ([Otsuka 2005](#5-references) and [Masuda 2006](#5-references)). Transporter activity was described as saturable process following Michaelis-Menten kinetics, where the `Km` was taken from literature and `kcat` was optimized based on clinical data (see [Section 2.3.4](#model-parameters-and-assumptions-identification)).

Additionally, passive renal clearance by glomerular filtration was implemented and the `GFR fraction` was set to 1. In addition, fraction of bile that was continuously released was set to 1 (`EHC continuous fraction`)

### 2.3.4 Automated Parameter Identification<a id="model-parameters-and-assumptions-identification"></a>

The following parameters have been estimated in the model:

| Model Parameter                |
| ------------------------------ | 
| `Km` (PMAT)             | 
| `kcat` (PMAT)             | 
| `kcat` (OCT1)            |
| `kcat` (OCT2)                    | 
| `kcat` (MATE1)                    | 
| `Specific intestinal permeability`| 
| `Basolateral small intestinal permeability`| 
| `Basolateral large intestinal permeability`| 
| `Tablet dissolution fed Weibull Shape`|
| `Tablet dissolution fed Weibull Time`|

 

# 3 Results and Discussion<a id="3"></a>

The next sections show:

1. the final model input parameters for the building blocks: [Section 3.1](#31-metformin-final-input-parameters).
2. the overall goodness of fit: [Section 3.2](#32-metformin-diagnostics-plots).
3. simulated vs. observed concentration-time profiles for the clinical studies used for model building and for model verification: [Section 3.3](#33-concentration-time-profiles).

## 3.1 Metformin final input parameters<a id="31"></a>

The compound parameter values of the final PBPK model are illustrated below.

### Compound: Metformin

#### Parameters

Name                                             | Value                   | Value Origin                                                                                        | Alternative | Default
------------------------------------------------ | ----------------------- | --------------------------------------------------------------------------------------------------- | ----------- | -------
Solubility at reference pH                       | 350.9 mg/ml             |                                                                                                     | Measurement | True   
Reference pH                                     | 6.8                     |                                                                                                     | Measurement | True   
Lipophilicity                                    | -1.43 Log Units         |                                                                                                     | Measurement | True   
Fraction unbound (plasma, reference value)       | 100 %                   |                                                                                                     | Measurement | True   
Specific intestinal permeability (transcellular) | 8.4891040357E-07 cm/min | Parameter Identification-Parameter Identification-Value updated from '17_final' on 2019-04-09 09:52 | Fit         | True   
Is small molecule                                | Yes                     |                                                                                                     |             |        
Molecular weight                                 | 129.1636 g/mol          |                                                                                                     |             |        
Plasma protein binding partner                   | Albumin                 |                                                                                                     |             |        

#### Calculation methods

Name                    | Value                                        
----------------------- | ---------------------------------------------
Partition coefficients  | PK-Sim Standard                              
Cellular permeabilities | Charge dependent Schmitt normalized to PK-Sim

#### Processes

##### Systemic Process: Glomerular Filtration-GFR

Species: Human

###### Parameters

Name         | Value | Value Origin
------------ | -----:| ------------:
GFR fraction |     1 |             

##### Transport Protein: OCT1-Paper

Molecule: OCT1

###### Parameters

Name                      | Value                    | Value Origin                                     
------------------------- | ------------------------ | -------------------------------------------------
Transporter concentration | 1 µmol/l                 |                                                  
Vmax                      | 641.185138023 µmol/l/min | Parameter Identification-Parameter Identification
Km                        | 1180 µmol/l              |                                                  

##### Transport Protein: OCT2-Paper

Molecule: OCT2

###### Parameters

Name                      | Value               | Value Origin                                     
------------------------- | ------------------- | -------------------------------------------------
Transporter concentration | 1 µmol/l            |                                                  
Vmax                      | 17479.74 µmol/l/min | Parameter Identification-Parameter Identification
Km                        | 810 µmol/l          |                                                  

##### Transport Protein: MATE1-Paper

Molecule: MATE1

###### Parameters

Name                      | Value             | Value Origin                                     
------------------------- | ----------------- | -------------------------------------------------
Transporter concentration | 1 µmol/l          |                                                  
Vmax                      | 165.69 µmol/l/min | Parameter Identification-Parameter Identification
Km                        | 283 µmol/l        | Parameter Identification-Parameter Identification

##### Transport Protein: PMAT-Paper

Molecule: PMAT

###### Parameters

Name                      | Value                    | Value Origin                                                                                       
------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------
Transporter concentration | 1 µmol/l                 |                                                                                                    
Vmax                      | 76.4673688119 µmol/l/min | Parameter Identification-Parameter Identification-Value updated from '17_final' on 2019-04-09 09:51
Km                        | 367.5702930377 µmol/l    | Parameter Identification-Parameter Identification-Value updated from '17_final' on 2019-04-09 09:52
Hill coefficient          | 3                        |                                                                                                    

## 3.2 Metformin Diagnostics Plots<a id="32"></a>

Below you find the goodness-of-fit visual diagnostic plots for the PBPK model performance of all data used presented in [Section 2.2.2](#clinical-data).

The first plot shows observed versus simulated plasma concentration, the second weighted residuals versus time. 

<a id="table-3-1"></a>

**Table 3-1: GMFE for Goodness of fit plot for concentration in plasma.**

|Group                                              |GMFE |
|:--------------------------------------------------|:----|
|Metformin iv (model building)                      |1.24 |
|Metformin iv (model verification)                  |1.23 |
|Metformin oral administration (model building)     |1.37 |
|Metformin oral administration (model verification) |1.43 |
|All                                                |1.39 |

<br>
<br>

<a id="figure-3-1"></a>

![](images/006_section_3/008_section_32/2_gof_plot_predictedVsObserved.png)

**Figure 3-1: Goodness of fit plot for concentration in plasma.**

<br>
<br>

<a id="figure-3-2"></a>

![](images/006_section_3/008_section_32/3_gof_plot_residualsOverTime.png)

**Figure 3-2: Goodness of fit plot for concentration in plasma.**

<br>
<br>

## 3.3 Concentration-Time Profiles<a id="33"></a>

Simulated versus observed concentration-time profiles of all data listed in [Section 2.2.2](#clinical-data) are presented below.

### 3.3.1 Model Building<a id="331"></a>

<a id="figure-3-3"></a>

![](images/006_section_3/009_section_33/010_section_331/1_time_profile_plot_Metformin_iv___0_0014_mg__Gormsen_2016__n_4.png)

**Figure 3-3: Metformin - iv, 0.0014 mg_Gormsen 2016**

<br>
<br>

<a id="figure-3-4"></a>

![](images/006_section_3/009_section_33/010_section_331/2_time_profile_plot_Metformin_iv__250_mg__Tucker_1981__n_4.png)

**Figure 3-4: Metformin - iv, 250 mg_Tucker 1981**

<br>
<br>

<a id="figure-3-5"></a>

![](images/006_section_3/009_section_33/010_section_331/3_time_profile_plot_Metformin_iv_1000_mg__Sirtori_1978__n_5.png)

**Figure 3-5: Metformin - iv, 1000 mg_Sirtori 1978**

<br>
<br>

<a id="figure-3-6"></a>

![](images/006_section_3/009_section_33/010_section_331/4_time_profile_plot_Metformin_po__10_mg__Stopfer_2018__n_24__sol__fast.png)

**Figure 3-6: Metformin - po (sol) 10 mg_Stopfer 2018**

<br>
<br>

<a id="figure-3-7"></a>

![](images/006_section_3/009_section_33/010_section_331/5_time_profile_plot_Metformin_po__500_mg__Boehringer_2018__n_13__sol__fast.png)

**Figure 3-7: Metformin - po (sol) 500 mg_Boehringer 2018**

<br>
<br>

<a id="figure-3-8"></a>

![](images/006_section_3/009_section_33/010_section_331/6_time_profile_plot_Metformin_po___0_0008_mg__Gormsen_2016__n_3__sol__fast.png)

**Figure 3-8: Metformin - po (sol) 0.0008 mg, Gormsen 2016**

<br>
<br>

<a id="figure-3-9"></a>

![](images/006_section_3/009_section_33/010_section_331/7_time_profile_plot_Metformin_po__500_mg__Stopfer_2016__n_20__tab__fast.png)

**Figure 3-9: Metformin - po (tab) 500 mg_Stopfer 2016**

<br>
<br>

<a id="figure-3-10"></a>

![](images/006_section_3/009_section_33/010_section_331/8_time_profile_plot_Metformin_po__850_mg__Sambol_1996b__n_24__sol__fast.png)

**Figure 3-10: Metformin - po (sol) 850 mg_Sambol 1996b**

<br>
<br>

<a id="figure-3-11"></a>

![](images/006_section_3/009_section_33/010_section_331/9_time_profile_plot_Metformin_po__850_mg__Sambol_1996b__n_24__tab__fast.png)

**Figure 3-11: Metformin - po (tab) 850 mg_Sambol 1996b**

<br>
<br>

<a id="figure-3-12"></a>

![](images/006_section_3/009_section_33/010_section_331/10_time_profile_plot_Metformin_po__850_mg__Sambol_1996b__n_24__tab__fed.png)

**Figure 3-12: Metformin - po (tab) 850 mg_Sambol 1996a**

<br>
<br>

<a id="figure-3-13"></a>

![](images/006_section_3/009_section_33/010_section_331/11_time_profile_plot_Metformin_po_1700_mg__Sambol_1996a__n_9__tab__fast.png)

**Figure 3-13: Metformin - po (tab) 0.1700 mg_Sambol 1996a**

<br>
<br>

<a id="figure-3-14"></a>

![](images/006_section_3/009_section_33/010_section_331/12_time_profile_plot_Metformin_po_2550_mg__Sambol_1996a__n_9__tab__fast.png)

**Figure 3-14: Metformin - po (tab) 2550 mg_Sambol 1996a**

<br>
<br>

### 3.3.2 Model Verification<a id="332"></a>

<a id="figure-3-15"></a>

![](images/006_section_3/009_section_33/011_section_332/13_time_profile_plot_Metformin_iv__500_mg__Pentikainen_1979__n_3.png)

**Figure 3-15: Metformin - iv 500 mg_Pentikainen 1979**

<br>
<br>

<a id="figure-3-16"></a>

![](images/006_section_3/009_section_33/011_section_332/14_time_profile_plot_Metformin_po__250_mg__Somogyi_1987__n_7__tab__fed.png)

**Figure 3-16: Metformin - po (tab) 250 mg_Somogyi 1987**

<br>
<br>

<a id="figure-3-17"></a>

![](images/006_section_3/009_section_33/011_section_332/15_time_profile_plot_Metformin_po__500_mg__Wang_2008__n_6__tab__fast.png)

**Figure 3-17: Metformin - po (tablet) 500 mg_Wang 2008**

<br>
<br>

<a id="figure-3-18"></a>

![](images/006_section_3/009_section_33/011_section_332/16_time_profile_plot_Metformin_po__500_mg__Caille_1993__n_24__tab__fed.png)

**Figure 3-18: Metformin - po (tab) 500 mg_Caille 1993**

<br>
<br>

<a id="figure-3-19"></a>

![](images/006_section_3/009_section_33/011_section_332/17_time_profile_plot_Metformin_po__500_mg__Gusler_2001__n_14__tab__fed.png)

**Figure 3-19: Metformin - po (tab) 500 mg_Gusler 2001**

<br>
<br>

<a id="figure-3-20"></a>

![](images/006_section_3/009_section_33/011_section_332/18_time_profile_plot_Metformin_po__500_mg__Najib_2002__n_24__tab__fast.png)

**Figure 3-20: Metformin - po (tab) 500 mg_Najib 2002**

<br>
<br>

<a id="figure-3-21"></a>

![](images/006_section_3/009_section_33/011_section_332/19_time_profile_plot_Metformin_po__500_mg__Pentikainen_1979__n_5__tab__fast.png)

**Figure 3-21: Metformin - po (tab) 500 mg_Pentikainen 1979**

<br>
<br>

<a id="figure-3-22"></a>

![](images/006_section_3/009_section_33/011_section_332/20_time_profile_plot_Metformin_po__500_mg__Sambol_1996b__n_24__tab__fast.png)

**Figure 3-22: Metformin - po (tab) 500 mg_Sambol 1996b**

<br>
<br>

<a id="figure-3-23"></a>

![](images/006_section_3/009_section_33/011_section_332/21_time_profile_plot_Metformin_po__500_mg__Tucker_1981__n_4__tab__fed.png)

**Figure 3-23: Metformin - po (tab) 500 mg_Tucker 1981**

<br>
<br>

<a id="figure-3-24"></a>

![](images/006_section_3/009_section_33/011_section_332/22_time_profile_plot_Metformin_po__500_mg__DiCicco_2000__n_16__tab__fed.png)

**Figure 3-24: Metformin - po (tab) 500 mg_DiCicco 2000**

<br>
<br>

<a id="figure-3-25"></a>

![](images/006_section_3/009_section_33/011_section_332/23_time_profile_plot_Metformin_po__500_mg__Jang_2016__n_20__tab__fast.png)

**Figure 3-25: Metformin - po (tab) 500 mg_Jan 2016**

<br>
<br>

<a id="figure-3-26"></a>

![](images/006_section_3/009_section_33/011_section_332/24_time_profile_plot_Metformin_po__500_mg__Kim_2014__n_23__tab__fast.png)

**Figure 3-26: Metformin - po (tab) 500 mg_Kim 2014**

<br>
<br>

<a id="figure-3-27"></a>

![](images/006_section_3/009_section_33/011_section_332/25_time_profile_plot_Metformin_po__500_mg__Manitpisitkul_2014__n_18__tab__fast.png)

**Figure 3-27: Metformin - po (tab) 500 mg_Manitpisitkul 2014**

<br>
<br>

<a id="figure-3-28"></a>

![](images/006_section_3/009_section_33/011_section_332/26_time_profile_plot_Metformin_po__500_mg__Oh_2016__n_20__tab__fast.png)

**Figure 3-28: Metformin - po (tab) 500 mg_Oh 2016**

<br>
<br>

<a id="figure-3-29"></a>

![](images/006_section_3/009_section_33/011_section_332/27_time_profile_plot_Metformin_po__750_mg__Cho_2011__n_16__tab__fast.png)

**Figure 3-29: Metformin - po (tab) 750 mg_Cho 2011**

<br>
<br>

<a id="figure-3-30"></a>

![](images/006_section_3/009_section_33/011_section_332/28_time_profile_plot_Metformin_po__750_mg__Cho_2014__n_12__tab__fast.png)

**Figure 3-30: Metformin - po (tab) 750 mg_Cho 2014**

<br>
<br>

<a id="figure-3-31"></a>

![](images/006_section_3/009_section_33/011_section_332/29_time_profile_plot_Metformin_po__750_mg__Ding_2014__n_20__tab__fast.png)

**Figure 3-31: Metformin - po (tab) 750 mg tid_Ding 2014**

<br>
<br>

<a id="figure-3-32"></a>

![](images/006_section_3/009_section_33/011_section_332/30_time_profile_plot_Metformin_po__850_mg__Chen_2009__n_14__tab__fast.png)

**Figure 3-32: Metformin - po (tab) 850 mg_Chen 2009**

<br>
<br>

<a id="figure-3-33"></a>

![](images/006_section_3/009_section_33/011_section_332/31_time_profile_plot_Metformin_po__850_mg__Robert_2003__WholeBlood__n_6__tab__fed.png)

**Figure 3-33: Metformin - po (tab) 850 mg_Robert 2003**

<br>
<br>

<a id="figure-3-34"></a>

![](images/006_section_3/009_section_33/011_section_332/32_time_profile_plot_Metformin_po__850_mg__Sambol_1995__WholeBlood__n_6__tab__fast.png)

**Figure 3-34: Metformin - po (tab) 850 mg_Sambol 1995**

<br>
<br>

<a id="figure-3-35"></a>

![](images/006_section_3/009_section_33/011_section_332/33_time_profile_plot_Metformin_po__850_mg__Sambol_1996a__n_9__tab__fast.png)

**Figure 3-35: Metformin - po (tab) 850 mg_Sambol 1996a**

<br>
<br>

<a id="figure-3-36"></a>

![](images/006_section_3/009_section_33/011_section_332/34_time_profile_plot_Metformin_po__850_mg__Hibma_2016__n_12__tab__fast.png)

**Figure 3-36: Metformin - po (tab) 850 mg_Hibma 2016**

<br>
<br>

<a id="figure-3-37"></a>

![](images/006_section_3/009_section_33/011_section_332/35_time_profile_plot_Metformin_po__850_mg_tid__Sambol_1996a__n_9__tab__fast.png)

**Figure 3-37: Metformin - po (tab) 850 mg tid_Sambol 1996a**

<br>
<br>

<a id="figure-3-38"></a>

![](images/006_section_3/009_section_33/011_section_332/36_time_profile_plot_Metformin_po_1000_mg__Johansson_2014__n_14__tab__fast.png)

**Figure 3-38: Metformin - po (tab) 1000 mg_Johansson 2014**

<br>
<br>

<a id="figure-3-39"></a>

![](images/006_section_3/009_section_33/011_section_332/37_time_profile_plot_Metformin_po_1000_mg__Gan_2016__n_27__tab__fast.png)

**Figure 3-39: Metformin - po (tab) 1000 mg_Gan 2016**

<br>
<br>

<a id="figure-3-40"></a>

![](images/006_section_3/009_section_33/011_section_332/38_time_profile_plot_Metformin_po_1500_mg__Tucker_1981__n_4__tab__fed.png)

**Figure 3-40: Metformin - po (tab) 1500 mg_Tucker 1981**

<br>
<br>

<a id="figure-3-41"></a>

![](images/006_section_3/009_section_33/011_section_332/39_time_profile_plot_Metformin_po__850_mg__Morrissey_2016__n_12__tab__fast.png)

**Figure 3-41: Metformin - po (tab) 850 mg_Morrissey 2016**

<br>
<br>

# 4 Conclusion<a id="4"></a>

The presented PBPK model adequately describes the intravenous and oral pharmacokinetics of metformin in adults.

# 5 References<a id="5"></a>

**Block  2008** Block LC, Schemling LO, Couto AG, et al (2008) Pharmaceutical equivalence of metformin tablets with various binders. Revista de Ciências Farmacêuticas Básica e Aplicada 29(1):29–35

**Boehringer Ingelheim 2018** Boehringer Ingelheim Pharma GmbH & Co KG (2018) The effect of potent inhibitors of drug transporters (verapamil, rifampin, cimetidine, probenecid) on pharmacokinetics of a transporter probe drug cocktail consisting of digoxin, furosemide, metformin and rosuvastatin. BI Trial No. 0352-2100. EudraCT 2017-001549-29

**Caillé 1993** Caillé G, Lacasse Y, Raymond M, et al (1993) Bioavailability of metformin in tablet form using a new high pressure liquid chromatography assay method. Biopharm Drug Dispos 14:257–263. https://doi.org/10.1002/bdd.2510140308

**Chen 2009** Chen Y, Li S, Brown C, et al (2009) Effect of genetic variation in the organic cation transporter 2 on the renal elimination of metformin. Pharmacogenet Genomics 19:497–504. https://doi.org/10.1097/fpc.0b013e32832cc7e9

**Cho 2011** Cho SK, Yoon JS, Lee MG, et al (2011) Rifampin enhances the glucose-lowering effect of metformin and increases OCT1 mRNA levels in healthy participants. Clin Pharmacol Ther 89:416–421. https://doi.org/10.1038/clpt.2010.266

**Cho 2014** Cho SK, Kim CO, Park ES, Chung J-Y (2014) Verapamil decreases the glucose-lowering effect of metformin in healthy volunteers. Br J Clin Pharmacol 78:1426–1432. https://doi.org/10.1111/bcp.12476

**Desai 2014** Desai D, Wong B, Huang Y, et al (2014) Surfactant-Mediated Dissolution of Metformin Hydrochloride Tablets: Wetting Effects Versus Ion Pairs Diffusivity. Journal of Pharmaceutical Sciences 103:920–926. https://doi.org/10.1002/jps.23852

**Di Cicco 2000** Di Cicco RA, Allen A, Carr A, et al (2000) Rosiglitazone Does Not Alter the Pharmacokinetics of Metformin. The Journal of Clinical Pharmacology 40:1280–1285. https://doi.org/10.1177/009127000004001113

**Ding 2014** Ding Y, Jia Y, Song Y, et al (2014) The effect of lansoprazole, an OCT inhibitor, on metformin pharmacokinetics in healthy subjects. Eur J Clin Pharmacol 70:141–146. https://doi.org/10.1007/s00228-013-1604-7

**FDA 2017** US Food and Drug Administration (2017) Drug development and drug interactions: Table
of substrates, inhibitors and inducers. https://www.fda.gov/drugs/drug-interactions/labeling/drug-development-and-drug-interactions-table-substrates-inhibitors-and-inducers

**Gan 2016** Gan L, Jiang X, Mendonza A, et al (2016) Pharmacokinetic drug-drug interaction assessment of LCZ696 (an angiotensin receptor neprilysin inhibitor) with omeprazole, metformin or levonorgestrel-ethinyl estradiol in healthy subjects. Clin Pharmacol Drug Dev 5:27–39. https://doi.org/10.1002/cpdd.181

**Gormsen 2016** Gormsen LC, Sundelin EI, Jensen JB, et al (2016) In Vivo Imaging of Human 11C-Metformin in Peripheral Organs: Dosimetry, Biodistribution, and Kinetic Analyses. J Nucl Med 57:1920–1926. https://doi.org/10.2967/jnumed.116.177774

**Graham 2011** Graham GG, Punt J, Arora M, et al (2011) Clinical pharmacokinetics of metformin. Clin Pharmacokinet 50:81–98. https://doi.org/10.2165/11534750-000000000-00000

**Gusler 2001** Gusler G, Gorsline J, Levy G, et al (2001) Pharmacokinetics of metformin gastric-retentive tablets in healthy volunteers. J Clin Pharmacol 41:655–661. https://doi.org/10.1177/00912700122010546

**Hanke 2020** Hanke N, Türk D, Selzer D, et al (2020) A Comprehensive Whole-Body Physiologically Based Pharmacokinetic Drug-Drug-Gene Interaction Model of Metformin and Cimetidine in Healthy Adults and Renally Impaired Individuals. Clin Pharmacokinet. 59:1419-1431. doi: 10.1007/s40262-020-00896-w. 

**Hibma 2016** Hibma JE, Zur AA, Castro RA, et al (2016) The Effect of Famotidine, a MATE1-Selective Inhibitor, on the Pharmacokinetics and Pharmacodynamics of Metformin. Clin Pharmacokinet 55:711–721. https://doi.org/10.1007/s40262-015-0346-3

**Jang 2016** Jang K, Chung H, Yoon J-S, et al (2016) Pharmacokinetics, Safety, and Tolerability of Metformin in Healthy Elderly Subjects. J Clin Pharmacol 56:1104–1110. https://doi.org/10.1002/jcph.699

**Johansson 2014** Johansson S, Read J, Oliver S, et al (2014) Pharmacokinetic evaluations of the co-administrations of vandetanib and metformin, digoxin, midazolam, omeprazole or ranitidine. Clin Pharmacokinet 53:837–847. https://doi.org/10.1007/s40262-014-0161-2

**Kim 2014** Kim A, Chung I, Yoon SH, et al (2014) Effects of proton pump inhibitors on metformin pharmacokinetics and pharmacodynamics. Drug Metab Dispos 42:1174–1179. https://doi.org/10.1124/dmd.113.055616

**Kolesnikov 2015**Kolesnikov N, Hastings E, Keays M, et al (2015) ArrayExpress update—simplifying data submissions. Nucleic Acids Research 43:D1113–D1116. https://doi.org/10.1093/nar/gku1057

**Manitpisitkul 2014** Manitpisitkul P, Curtin CR, Shalayda K, et al (2014) Pharmacokinetic interactions between topiramate and pioglitazone and metformin. Epilepsy Res 108:1519–1532. https://doi.org/10.1016/j.eplepsyres.2014.08.013

**Masuda 2006** Masuda S, Terada T, Yonezawa A, et al (2006) Identification and functional characterization of a new human kidney-specific H+/organic cation antiporter, kidney-specific multidrug and toxin extrusion 2. J Am Soc Nephrol 17:2127–2135. https://doi.org/10.1681/asn.2006030205

**Meyer 2012** Meyer M, Schneckener S, Ludewig B, et al (2012) Using expression data for quantification of active processes in physiologically based pharmacokinetic modeling. Drug Metab Dispos 40:892–901. https://doi.org/10.1124/dmd.111.043174

**Morrissey 2016** Morrissey KM, Stocker SL, Chen EC, et al (2016) The Effect of Nizatidine, a MATE2K Selective Inhibitor, on the Pharmacokinetics and Pharmacodynamics of Metformin in Healthy Volunteers. Clin Pharmacokinet 55:495–506. https://doi.org/10.1007/s40262-015-0332-9

**NCHS 1997** National Center for Health Statistics (NCHS) (1997) Third National Health and Nutrition Examination
Survey (NHANES III). Tech. rep., Hyattsville, MD 20782

**Najib 2002** Najib N, Idkaidek N, Beshtawi M, et al (2002) Bioequivalence evaluation of two brands of metformin 500 mg tablets (Dialon & Glucophage)--in healthy human volunteers. Biopharm Drug Dispos 23:301–306. https://doi.org/10.1002/bdd.326

**NCBI 2019** National Center for Biotechnology Information (NCBI) (2019) Expressed Sequence Tags (EST) from UniGene

**Nishimura 2005** Nishimura M, Naito S (2005) Tissue-specific mRNA Expression Profiles of Human ATP-binding Cassette and Solute Carrier Transporter Superfamilies. Drug Metabolism and Pharmacokinetics 20:452–477. https://doi.org/10.2133/dmpk.20.452

**Nishimura 2006** Nishimura M, Naito S (2006) Tissue-specific mRNA expression profiles of human phase I metabolizing enzymes except for cytochrome P450 and phase II metabolizing enzymes. Drug Metab Pharmacokinet 21:357–374. https://doi.org/10.2133/dmpk.21.357

**Oh 2016** Oh J, Chung H, Park S-I, et al (2016) Inhibition of the multidrug and toxin extrusion (MATE) transporter by pyrimethamine increases the plasma concentration of metformin but does not increase antihyperglycaemic activity in humans. Diabetes Obes Metab 18:104–108. https://doi.org/10.1111/dom.12577

**Otsuka 2005** Otsuka M, Matsumoto T, Morimoto R, et al (2005) A human transporter protein that mediates the final excretion step for toxic organic cations. Proc Natl Acad Sci U S A 102:17923–17928. https://doi.org/10.1073/pnas.0506483102

**Pentikäinen 1979** Pentikäinen PJ, Neuvonen PJ, Penttilä A (1979a) Pharmacokinetics of metformin after intravenous and oral administration to man. Eur J Clin Pharmacol 16:195–202. https://doi.org/10.1007/BF00562061

**PK-Sim Ontogeny Database Version 7.3** PK-Sim Ontogeny Database Version 7.3 (https://github.com/Open-Systems-Pharmacology/OSPSuite.Documentation/blob/38cf71b384cfc25cfa0ce4d2f3addfd32757e13b/PK-Sim%20Ontogeny%20Database%20Version%207.3.pdf)

**Robert 2003** Robert F, Fendri S, Hary L, et al (2003) Kinetics of plasma and erythrocyte metformin after acute administration in healthy subjects. Diabetes Metab 29:279–283. https://doi.org/10.1016/s1262-3636(07)70037-x

**Sambol 1996** Sambol NC, Brookes LG, Chiang J, et al (1996) Food intake and dosage level, but not tablet vs solution dosage form, affect the absorption of metformin HC1 in man. British Journal of Clinical Pharmacology 42:510–512. https://doi.org/10.1111/j.1365-2125.1996.tb00017.x

**Sambol 1995** Sambol NC, Chiang J, Lin ET, et al (1995) Kidney function and age are both predictors of pharmacokinetics of metformin. J Clin Pharmacol 35:1094–1102. https://doi.org/10.1002/j.1552-4604.1995.tb04033.x

**Sirtori 1978** Sirtori CR, Franceschini G, Galli-Kienle M, et al (1978a) Disposition of metformin (N,N-dimethylbiguanide) in man. Clinical Pharmacology & Therapeutics 24:683–693. https://doi.org/10.1002/cpt1978246683

**Somogyi 1987** Somogyi A, Stockley C, Keal J, et al (1987) Reduction of metformin renal tubular secretion by cimetidine in man. British Journal of Clinical Pharmacology 23:545–551. https://doi.org/10.1111/j.1365-2125.1987.tb03090.x

**Stopfer 2016** Stopfer P, Giessmann T, Hohl K, et al (2016) Pharmacokinetic Evaluation of a Drug Transporter Cocktail Consisting of Digoxin, Furosemide, Metformin, and Rosuvastatin. Clin Pharmacol Ther 100:259–267. https://doi.org/10.1002/cpt.406

**Stopfer 2018** Stopfer P, Giessmann T, Hohl K, et al (2018) Effects of Metformin and Furosemide on Rosuvastatin Pharmacokinetics in Healthy Volunteers: Implications for Their Use as Probe Drugs in a Transporter Cocktail. Eur J Drug Metab Pharmacokinet 43:69–80. https://doi.org/10.1007/s13318-017-0427-9

**Tucker 1981** Tucker GT, Casey C, Phillips PJ, et al (1981a) Metformin kinetics in healthy subjects and in patients with diabetes mellitus. Br J Clin Pharmacol 12:235–246. https://doi.org/10.1111/j.1365-2125.1981.tb01206.x

**Valentin 2002** Valentin J (2002) Basic anatomical and physiological data for use in radiological protection:
reference values: ICRP Publication 89. Annals of the ICRP 32:1–277

**Vidon 1988** Vidon N, Chaussade S, Noel M, Franchisseur C, Huchet B, Bernier JJ (1988) Metformin in the
digestive tract. Diabetes Research and Clinical Practice 4:223–229

**Wang 2008** Wang Z-J, Yin OQP, Tomlinson B, Chow MSS (2008) OCT2 polymorphisms and in-vivo renal functional consequence: studies with metformin and cimetidine. Pharmacogenet Genomics 18:637–645. https://doi.org/10.1097/FPC.0b013e328302cd41

**Willmann 2007** Willmann S, Hohn K, Edginton A, et al (2007) Development of a physiology-based whole-body population model for assessing the influence of individual variability on the pharmacokinetics of drugs. Journal of pharmacokinetics and pharmacodynamics 34:401–31. https://doi.org/10.1007/s10928-007-9053-5

**Wishart 2006** Wishart DS, Knox C, Guo AC, et al (2006) DrugBank: a comprehensive resource for in silico drug discovery and exploration. Nucleic Acids Res 34:D668-672. https://doi.org/10.1093/nar/gkj067

**Yin 2016** Yin J, Duan H, Wang J (2016) Impact of Substrate-Dependent Inhibition on Renal Organic Cation Transporters hOCT2 and hMATE1/2-K-Mediated Drug Transport and Intracellular Accumulation. J Pharmacol Exp Ther 359:401–410. https://doi.org/10.1124/jpet.116.236158

**Zhou 2007** Zhou M, Xia L, Wang J (2007) Metformin Transport by a Newly Cloned Proton-Stimulated Organic Cation Transporter (Plasma Membrane Monoamine Transporter) Expressed in Human Intestine. Drug Metab Dispos 35:1956–1962 https://doi: 10.1124/dmd.107.015495.

**Zhou 2009** Zhou SF, Zhou ZW, Yang LP, Cai JP (2009) Substrates, inducers, inhibitors and structure-activity relationships of human cytochrome P450 2C9 and implications in drug development. Current Medicinal Chemistry 16:3480–3675. https://doi.org/10.2174/092986709789057635

