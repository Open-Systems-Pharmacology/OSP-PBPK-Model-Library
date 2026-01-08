# Building and evaluation of a PBPK model for Furosemide in healthy adults

| Version                                         | 1.0-OSP12.1                                                   |
| ----------------------------------------------- | ------------------------------------------------------------ |
| based on *Model Snapshot* and *Evaluation Plan* | https://github.com/Open-Systems-Pharmacology/Furosemide-Model/releases/tag/v1.0 |
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
     * [2.3.1 Absorption ](#model-parameters-and-assumptions-absorption)
     * [2.3.2 Distribution ](#model-parameters-and-assumptions-distribution)
     * [2.3.3 Metabolism and Elimination ](#model-parameters-and-assumptions-metabolism)
     * [2.3.4 Automated Parameter Identification ](#model-parameters-and-assumptions-identification)
 * [3 Results and Discussion](#3)
   * [3.1 Furosemide final input parameters](#31)
   * [3.2 Furosemide Diagnostics Plots](#32)
   * [3.3 Concentration-Time Profiles](#33)
     * [3.3.1 Model Building](#331)
     * [3.3.2 Model Verification](#332)
 * [4 Conclusion](#4)
 * [5 References](#5)

# 1 Introduction<a id="1"></a>

The presented model building and evaluation report evaluates the performance of a PBPK model for furosemide in healthy adults.

The herein presented model was developed and published by Britz et al. [Britz 2020](#5-references) and adjusted later on to PK-Sim V11 by re-optimizing OAT3 and ABCC4 Kcat. 

Furosemide is a loop diuretic, and its primary mechanism of action involves inhibition of tubular re-absorption of sodium and chloride in the kidneys, specifically by blocking the sodium-chloride-potassium transporter system in the thick ascending limb of the loop of Henle ([Ponto and Schoenwald 1990](#5-references)). Furosemide is used to treat edema or high blood pressure.

Furosemide is a poorly soluble and permeable compound and is classified as a BCS IV drug. Transporters play an essential role in
furosemide absorption, distribution and elimination. Furosemide bioavailability is highly variable (37%–83%), and influenced by dosage form and fasted/fed state of the patient. The poor bioavailability has been hypothesized to be due to the poor solubility of the compound, but also site-specific absorption, pre-systemic metabolism and/or other unknown mechanisms ([Ponto and Schoenwald 1990](#5-references)). 
The kidney is the main organ for furosemide metabolism and excretion, 50% to 80% of an intravenously administered dose and 20% to 55% of an orally administered dose are excreted unchanged in urine. The majority of furosemide dose is eliminated unchanged through active secretion mediated primarily by organic anion transporters (i.e., OAT1 and OAT3), and multidrug resistance-associated protein 4 (MRP4, also known as ABCC4), whereas the remaining dose is metabolized by uridine 5'-diphospho-glucuronosyltransferase 1A9 (UGT1A9).

The herein presented PBPK model of furosemide PBPK model has been developed using 42 different clinical studies, including intravenous (single dose) and oral (single- and multiple dose) administration as a solution or an immediate-release tablet. The model has then been evaluated by comparing simulations to observed data of both intravenously and orally administered furosemide covering a dose range of 1 mg to 80 mg. 

The presented model includes the following features:

- metabolism by UGT1A9,
- transport by OAT3,
- transport by ABCC4,
- renal clearance by glomerular filtration,
- oral absorption with dissolution rate assigned to a Weibull function.

# 2 Methods<a id="2"></a>

## 2.1 Modeling strategy<a id="21"></a>

The general concept of building a PBPK model has previously been described by Kuepfer et al. ([Kuepfer 2016](#5-references)). Relevant information on anthropometric (height, weight) and physiological parameters (e.g., blood flows, organ volumes, binding protein concentrations, hematocrit, cardiac output) in adults was gathered from the literature and has been previously published ([Willmann 2007](#5-references)). The information was incorporated into PK-Sim® and was used as default values for the simulations in adults.

The applied activity and variability of plasma proteins and active processes that are integrated into PK-Sim® are described in the publicly available PK-Sim® Ontogeny Database Version 7.3 ([PK-Sim Ontogeny Database Version 7.3](#5-references)) or otherwise referenced for the specific process.

A mean model was built based on clinical data from studies with intravenous and oral administration of furosemide. The studies reported individual or mean plasma concentrations of furosemide, from which 27 studies reported fraction excreted unchanged in urine profiles following intravenous and oral administration. In the intravenous studies, furosemide was administered in doses of 20–80 mg. In the oral studies, furosemide was administered in doses of 1–80 mg. The PBPK models were built based on data from healthy individuals, using the reported sex, ethnicity and mean values for age, weight and height from each study protocol. If no demographic information was reported in the respective clinical study, a default mean individual was used with the following properties: male, European, 30 years of age, 73 kg body weight and 176 cm body height. The relative tissue-specific expressions of the enzyme and transporter predominantly being involved in the metabolism/transport of furosemide (UGT1A9, OAT3, ABCC4) were considered ([Meyer 2012](#5-references)). A Weibull function was fitted to describe the oral dissolution of furosemide.  

The clinical datasets for furosemide PBPK modeling were divided into a training dataset for model building and a test dataset for model evaluation. Both datasets are presented in [Section 2.2](#22-data-used).

A specific set of parameters ([Section 2.3.4.](#model-parameters-and-assumptions-absorption-identification)) was optimized to describe the disposition of furosemide using the Parameter Identification module provided in PK-Sim®. To limit the parameters to be optimized during model building, the minimal number of processes necessary to mechanistically describe the pharmacokinetics and drug-drug interactions (DDIs) of the modeled drugs were implemented into the models. The furosemide OAT1 and OAT3 transport rate constants would be highly correlated in a model parameter optimization since there is no further information found to distinguish these two transporters. To avoid indentifiability issues, renal uptake of furosemide was implemented for the transporter with the slightly higher affinity for the respective substrate (OAT3) to describe a transport that probably is accomplished by both transporters *in vivo*. Structural model selection was mainly guided by visual inspection, mean relative deviation and geometric mean fold error of all predicted AUClast and Cmax values.

The model was verified by simulating further clinical studies reporting pharmacokinetic concentration-time profiles after intravenous and oral administration of furosemide (test datasets).

Details about input data (physicochemical, *in vitro* and clinical) can be found in [Section 2.2](#22-data-used).

Details about the structural model and its parameters can be found in [Section 2.3](#23-model-parameters-and-assumptions).

## 2.2 Data used<a id="22"></a>

### 2.2.1 In vitro and physicochemical data <a id="invitro-and-physico-chemical-data"></a>

A literature search was performed to collect available information on physicochemical properties of furosemide. The obtained information from literature is summarized in the table below, and was used for model building. Final model parameters are stated in [Section 3.1](#31-furosemide-final-input-parameters).

| **Parameter**           | **Unit** | **Value** | Source                               | **Description**                                              |
| :---------------------- | ----------- | --------- | ------------------------------------ | ------------------------------------------------------------ |
| MW                      | g/mol    | 330.74    | [Wishart 2006](#5-references)        | Molecular weight |
| pK<sub>a</sub> (acid)   |          | 3.51      | [Avdeef 2008](#5-references)       | acid dissociation constant |
| pK<sub>b</sub> (base)   |          | 9.87      | [Box 2006](#5-references)       | base dissociation constant |
| Solubility (FaSSIF)     | mg/mL    | 3.20      | [Takács-Novák 2013](#5-references)            | solubility |
| logP                    |          | -0.24     | [Ventura 1996](#5-references), [Avdeef 2003](#5-references) and [Berthod 1999](#5-references) | Partition coefficient between octanol and water |
| fu                      | %        | 2.20      | [Shen 2019](#5-references), [Vree 1995](#5-references), [Andreasen 1977](#5-references), [Smith 1980](#5-references), [Rane 1978](#5-references), [Andreasen 1983](#5-references), [Andreasen 1982](#5-references), [Vree 1994](#5-references) , [Pacifici 1987](#5-references) ,[Andreasen 1974](#5-references)  and [Forrey 1974](#5-references)                         | Fraction unbound in plasma                |                       
| K<sub>m</sub> UGT1A9    | µmol/L   | 72.00     | [Britz 2020](#5-references) | UGT1A9 Michaelis-Menten constant            |
| K<sub>m</sub> OAT3      | µmol/L   | 21.50     | [Ebner 2015](#5-references) | OAT3 Michaelis-Menten constant            |
| K<sub>m</sub> MRP4      | µmol/L   | 27.96     | [Britz 2020](#5-references) | MRP4 Michaelis-Menten constant         |
| Weibull shape           | -        | 0.53      | [McNamara 1987](#5-references) and [Langenbucher 1972](#5-references)  | Dissolution profile shape |
| Weibull time            | min      | 26.77     | [Bindschedler 1997](#5-references), [Martin 1984](#5-references), [FDA 2005](#5-references) and [Shoaf 2007](#5-references)                 | Dissolution time (50% dissolved)                             |

### 2.2.2 Clinical data <a id="clinical-data"></a>

A literature search was performed to collect available clinical data on furosemide in adults. 

The following publications were used for model building (training dataset) and model verification (test dataset):

| **Dose [mg]** | **Dosing** | **PK data** |**Dataset**| **Reference** |
| --------------- | ------------------- | ----------------------- | ----------------- |----------------- |
| 20| iv (bolus), sd |plasma, excretion into urine|training|[Haegeli 2007](#5-references) |
| 20| iv (5 min), sd |plasma|test|[Rosenkranz 1992](#5-references)| 
|22| iv (bolus), sd |plasma|test|[Tilstone 1978](#5-references)| 
| 35.5| iv (bolus), sd |excretion into urine|test|[Alván 1988](#5-references)| 
| 40| iv (bolus), sd |plasma, excretion into urine|test|[Andreasen 1977](#5-references)
| 40| iv (bolus), sd |plasma|test|[González 1982](#5-references)|
| 40| iv (bolus), sd |plasma, excretion into urine|test|[Hammarlund 1984](#5-references)|
| 40| iv (bolus), sd |plasma|test|[Homeida 1977 ](#5-references)|
| 40| iv (bolus), sd |plasma, excretion into urine|training|[Keller 1981](#5-references)|
| 40| iv (bolus), sd |plasma, excretion into urine|test|[Lambert 1983](#5-references)|
| 40| iv (bolus), sd |plasma|training|[Rupp 1974](#5-references)|
| 40| iv (2 min), sd |plasma|test|[Waller 1982](#5-references)|
| 40| iv (3 min), sd |plasma, excretion into urine|test| [Smith 1980a](#5-references)| 
| 40| iv (3 min), sd |excretion into urine|test| [Smith 1980b](#5-references)|  
| 80| iv (bolus), sd |plasma, excretion into urine|training| [Branch 1977](#5-references)|  
| 80| iv (bolus), sd |plasma, excretion into urine|training| [Branch 1977](#5-references)|  
| 80| iv (bolus), sd |plasma|test| [Kelly 1974](#5-references)|
| 80| iv (bolus), sd |plasma|test| [Rane 1978](#5-references)| 
| 80| iv (bolus), sd |plasma, excretion into urine|training| [Verbeeck 1982](#5-references)|
| 80| iv (2 min), sd |excretion into urine|test| [Andreasen 1981](#5-references)| 
| 80| iv (2 min), sd |plasma, excretion into urine|test| [Andreasen 1983](#5-references)|
| 1| po (sol), sd |plasma, excretion into urine|training| [Stopfer 2018](#5-references) |
| 5| po (sol), sd |plasma, excretion into urine|training| [Stopfer 2016](#5-references) |
| 20| po (sol), sd |plasma, excretion into urine|test|[Waller 1985](#5-references) 
| 20| po (tab), sd |plasma, excretion into urine|test|[Haegeli 2007](#5-references)   |
| 20| po (tab), qd |plasma|test|[FDA 2006](#5-references)   |
| 20| po (-), qd |plasma|test|[Vaidyanathan 2008](#5-references)|
| 40| po (sol), sd |plasma|training| [Waller 1982](#5-references)| 
| 40| po (sol), sd |plasma, excretion into urine|training|[Waller 1985](#5-references)|
| 40| po (sol), sd |plasma, excretion into urine|test|[Waller 1988](#5-references)|
| 40| po (sol), sd |plasma, excretion into urine|training|[Wiebe 2020](#5-references)|
| 40| po (tab), sd |plasma|test|[Ballester 2015](#5-references)|
| 40| po (tab), sd |plasma|training|[Bindscheller 1997](#5-references)|
| 40| po (tab), sd |plasma, excretion into urine|test|[Hammarlund 1984](#5-references)|
| 40| po (tab), sd |plasma, excretion into urine|test|[Martin 1984](#5-references)|
| 40| po (tab), sd |plasma, excretion into urine|training|[Rakhit 1987](#5-references)|
| 40| po (tab), sd |plasma, excretion into urine|test|[Rupp 1974](#5-references)|
| 40| po (tab), sd |plasma, excretion into urine|test|[Waller 1982](#5-references)|
| 40| po (tab), qd |plasma|training|[FDA 2005](#5-references)|
| 40| po (tab), sd |plasma|test|[Tilstone 1978](#5-references)|
| 40| po (tab), sd |plasma|test|[Kelly 1974](#5-references)|
| 80| po (sol), sd |plasma, excretion into urine|test|[Waller 1985](#5-references)|
| 80| po (tab), sd |plasma|test|[Kelly 1974](#5-references)|
| 80| po (tab), sd |plasma, excretion into urine|training|[Shoaf 2007](#5-references)|
| 80| po (tab), sd |plasma, excretion into urine|test|[Vree 1995](#5-references)|

## 2.3 Model parameters and assumptions<a id="23"></a>

### 2.3.1 Absorption <a id="model-parameters-and-assumptions-absorption"></a>

The parameter value for  `Specific intestinal permeability` and `Intestinal Paracellular permeability` were optimized based on clinical oral data, see [Section 2.3.4](#model-parameters-and-assumptions-identification). The measured solubility in FaSSIF was used in the model (see [Section 2.2.1](#invitro-and-physico-chemical-data))

The dissolution of tablets was implemented via empirical Weibull dissolution. 

### 2.3.2 Distribution <a id="model-parameters-and-assumptions-distribution"></a>

Furosemide is highly bound to plasma proteins (see [Section 2.2.1](#invitro-and-physico-chemical-data)). A value of fu = 2.2% was used in this PBPK model for `Fraction unbound (plasma, reference value)`. The major binding partner was set to albumin (see [Section 2.2.1](#invitro-and-physico-chemical-data)).

An important parameter influencing the resulting volume of distribution is lipophilicity. The reported experimental logP ranged from -0.24 to 2.56, and a value of -0.24 was used in this model (see [Section 2.2.1](#invitro-and-physico-chemical-data)). 

After testing the available organ-plasma partition coefficient and cell permeability calculation methods built in PK-Sim®, observed clinical data was best described by choosing the partition coefficient calculation by `Schmitt` and cellular permeability calculation by `Charged dependent Schmitt`.

### 2.3.3 Metabolism and Elimination <a id="model-parameters-and-assumptions-metabolism"></a>

One metabolic pathway was implement into the model via Michaelis-Menten kinetics 

* UGT1A9

The UGT1A9 expression profiles are based on high-sensitive real-time RT-PCR ([Nishimura 2006](#5-references)). Metabolic enzyme activity was described as saturable process following Michaelis-Menten kinetics, were the `Km` was taken from literature and the `kcat` was optimized based on clinical data (see [Section 2.3.4](#model-parameters-and-assumptions-identification)).

The following transport proteins are implemented into the model via Michaelis-Menten kinetics 

* OAT3

The OAT3 expression profiles are based on high-sensitive real-time RT-PCR ([Nishimura 2005](#5-references)). Transporter activity was described as saturable process following Michaelis-Menten kinetics, were the `Km` was taken from literature and `kcat` was optimized based on clinical data (see [Section 2.3.4](#model-parameters-and-assumptions-identification)).

* MRP4

The MRP4 expression profiles are based on high-sensitive real-time RT-PCR ([Nishimura 2005](#5-references)). Transporter activity was described as saturable process following Michaelis-Menten kinetics, were the `Km` was taken from literature and `kcat` was optimized based on clinical data (see [Section 2.3.4](#model-parameters-and-assumptions-identification)).

Additionally, passive renal clearance by glomerular filtration was implemented and the `GFR fraction` was set to 1. In addition, fraction of bile that was continuously released was set to 1 (`EHC continuous fraction`)

### 2.3.4 Automated Parameter Identification <a id="model-parameters-and-assumptions-identification"></a>

The following parameters have been estimated in the model:

| Model Parameter                |
| ------------------------------ | 
| `kcat` (UGT1A9)             | 
| `kcat` (OAT3)            |
| `kcat` (MRP4)                    | 
| `Specific intestinal permeability`| 
| `Intestinal permeability (paracellular)`| 
| `Tablet dissolution Weibull Shape`|
| `Tablet dissolution Weibull Time`|

 

# 3 Results and Discussion<a id="3"></a>

The PBPK model for furosemide was developed and verified with clinical pharmacokinetic data.

The model was built and evaluated covering data from studies including in particular

* single intravenous administration and both single and multiple oral administrations (solutions and tablets)
* a dose range of 1 to 80 mg

The model quantifies excretion via urine (by glomerular filtration and active transport mediated by OAT3 and MRP4) and metabolism via UGT1A9.

The next sections show:

1. the final model input parameters for the building blocks: [Section 3.1](#31-furosemide-final-input-parameters).
2. the overall goodness of fit: [Section 3.2](#32-furosemide-diagnostics-plots).
3. simulated vs. observed concentration-time profiles for the clinical studies used for model building and for model verification: [Section 3.3](#33-concentration-time-profiles).

## 3.1 Furosemide final input parameters<a id="31"></a>

The compound parameter values of the final PBPK model are illustrated below.

### Compound: Furosemide

#### Parameters

Name                                             | Value                   | Value Origin                                                                                                                | Alternative               | Default
------------------------------------------------ | ----------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------- | -------
Solubility at reference pH                       | 3201 mg/l               |                                                                                                                             | FaSSiF, Takács-Novák 2013 | True   
Reference pH                                     | 6.5                     |                                                                                                                             | FaSSiF, Takács-Novák 2013 | True   
Lipophilicity                                    | -0.24 Log Units         | Parameter Identification-Parameter Identification-Value updated from 'IV_PO_SOL_MRP4_BI_all_parameters' on 2019-05-06 09:33 | fitted                    | True   
Fraction unbound (plasma, reference value)       | 0.022                   | Publication-In Vivo-Vree 1995                                                                                               | Measurement               | True   
Specific intestinal permeability (transcellular) | 5.0580994501E-07 cm/min | Parameter Identification-Parameter Identification-Value updated from 'IV_PO_LOG_26032020_Ki values new' on 2020-03-26 15:06 | fitted                    | True   
Cl                                               | 1                       |                                                                                                                             |                           |        
Is small molecule                                | Yes                     |                                                                                                                             |                           |        
Molecular weight                                 | 330.74 g/mol            |                                                                                                                             |                           |        
Plasma protein binding partner                   | Albumin                 |                                                                                                                             |                           |        

#### Calculation methods

Name                    | Value                   
----------------------- | ------------------------
Partition coefficients  | Schmitt                 
Cellular permeabilities | Charge dependent Schmitt

#### Processes

##### Metabolizing Enzyme: UGT1A9-Kerdpin 2008

Molecule: UGT1A9

###### Parameters

Name                 | Value                | Value Origin                                                                                                                           
-------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------
Enzyme concentration | 1 µmol/l             |                                                                                                                                        
Vmax                 | 0 µmol/l/min         |                                                                                                                                        
Km                   | 72 µmol/l            | Parameter Identification-Parameter Identification-Value updated from 'IV_PO_LOG_16032020_Km and Ki Literature_LM_2' on 2020-03-17 07:14
kcat                 | 954.3278258031 1/min | Parameter Identification-Parameter Identification-Value updated from 'IV_PO_LOG_26032020_Ki values new' on 2020-03-26 15:06            

##### Transport Protein: OAT3-Ebner 2015

Molecule: OAT3

###### Parameters

Name                      | Value                | Value Origin                                                                                                                         
------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------
Transporter concentration | 1 µmol/l             |                                                                                                                                      
Vmax                      | 0 µmol/l/min         |                                                                                                                                      
Km                        | 21.5 µmol/l          | Publication-In Vitro-https://doi.org/10.1007/s11095-020-02964-z                                                                      
kcat                      | 2896.298211733 1/min | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification transporters Kcat' on 2024-10-16 16:01

##### Systemic Process: Glomerular Filtration-assumed

Species: Human

###### Parameters

Name         | Value | Value Origin
------------ | -----:| ------------:
GFR fraction |     1 |             

##### Transport Protein: ABCC4-Prasad 2020

Molecule: ABCC4

###### Parameters

Name                      | Value                 | Value Origin                                                                                                                         
------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------
Transporter concentration | 1 µmol/l              |                                                                                                                                      
Vmax                      | 0 µmol/l/min          |                                                                                                                                      
Km                        | 27.96 µmol/l          | Publication-In Vitro-https://doi.org/10.1007/s11095-020-02964-z                                                                      
kcat                      | 9418.2278268488 1/min | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification transporters Kcat' on 2024-10-16 16:01

## 3.2 Furosemide Diagnostics Plots<a id="32"></a>

Below you find the goodness-of-fit visual diagnostic plots for the PBPK model performance of all data used presented in [Section 2.2.2](#clinical-data).

The first plot shows observed versus simulated plasma concentration, the second weighted residuals versus time. 

<a id="table-3-1"></a>

**Table 3-1: GMFE for Goodness of fit plot for concentration in plasma.**

|Group                                               |GMFE |
|:---------------------------------------------------|:----|
|Furosemide iv (model building)                      |1.84 |
|Furosemide iv (model verification)                  |1.92 |
|Furosemide oral administration (model building)     |1.71 |
|Furosemide oral administration (model verification) |1.80 |
|All                                                 |1.82 |

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

![](images/006_section_3/009_section_33/010_section_331/2_time_profile_plot_Furosemide_i_v__20_mg__bolus__Haegeli_2007_33_34.png)

**Figure 3-3: Time Profile Analysis**

<br>
<br>

<a id="figure-3-4"></a>

![](images/006_section_3/009_section_33/010_section_331/11_time_profile_plot_Furosemide_i_v__40_mg__bolus__Keller_1981_52_53.png)

**Figure 3-4: Furosemide - i.v. (bolus), 40 mg_Kelly 1981**

<br>
<br>

<a id="figure-3-5"></a>

![](images/006_section_3/009_section_33/010_section_331/15_time_profile_plot_Furosemide_i_v__80_mg__bolus__Branch_1977_21_22.png)

**Figure 3-5: Furosemide - i.v. (bolus), 80 mg_Branch 1977**

<br>
<br>

<a id="figure-3-6"></a>

![](images/006_section_3/009_section_33/010_section_331/18_time_profile_plot_Furosemide_i_v__40_mg__bolus__Rupp_1974_67.png)

**Figure 3-6: Furosemide - i.v. (bolus), 40 mg_Rupp 1974**

<br>
<br>

<a id="figure-3-7"></a>

![](images/006_section_3/009_section_33/010_section_331/19_time_profile_plot_Furosemide_i_v__80_mg__bolus__Verbeeck_1982_90_91.png)

**Figure 3-7: Furosemide - i.v. (bolus), 80 mg_Verbeeck 1982**

<br>
<br>

<a id="figure-3-8"></a>

![](images/006_section_3/009_section_33/010_section_331/22_time_profile_plot_Furosemide_p_o___40_mg__tab__q_d__FDA_2005_48.png)

**Figure 3-8: Furosemide - p.o. (tab), 40 mg q.d._FDA 2005**

<br>
<br>

<a id="figure-3-9"></a>

![](images/006_section_3/009_section_33/010_section_331/23_time_profile_plot_Furosemide_p_o___1__mg__sol__Stopfer_2018_341_342.png)

**Figure 3-9: Furosemide - p.o. (sol), 1 mg_Stopfer 2018**

<br>
<br>

<a id="figure-3-10"></a>

![](images/006_section_3/009_section_33/010_section_331/25_time_profile_plot_Furosemide_p_o___40__mg__sol__Waller_1985_102_103.png)

**Figure 3-10: Furosemide - p.o. (sol), 40 mg_Waller 1985**

<br>
<br>

<a id="figure-3-11"></a>

![](images/006_section_3/009_section_33/010_section_331/27_time_profile_plot_Furosemide_p_o___40_mg__sol__Waller_1982_99.png)

**Figure 3-11: Furosemide - p.o. (sol), 40 mg_Waller 1982**

<br>
<br>

<a id="figure-3-12"></a>

![](images/006_section_3/009_section_33/010_section_331/29_time_profile_plot_Furosemide_p_o___5__mg__sol__Stopfer_2016_167_168.png)

**Figure 3-12: Furosemide - p.o. (sol), 5 mg_Stopfer 2016**

<br>
<br>

<a id="figure-3-13"></a>

![](images/006_section_3/009_section_33/010_section_331/34_time_profile_plot_Furosemide_p_o___40_mg__tab__Bindschedler_1997_19_20.png)

**Figure 3-13: Furosemide - p.o. (tab), 40 mg_Bindschedler 1997**

<br>
<br>

<a id="figure-3-14"></a>

![](images/006_section_3/009_section_33/010_section_331/36_time_profile_plot_Furosemide_p_o___40_mg__tab__Martin_1984___brand_name_tablet_59_60.png)

**Figure 3-14: Furosemide - p.o. (tab), 40 mg_Martin 1984**

<br>
<br>

<a id="figure-3-15"></a>

![](images/006_section_3/009_section_33/010_section_331/37_time_profile_plot_Furosemide_p_o___40_mg__tab__Martin_1984___generic_tablet_61_62.png)

**Figure 3-15: Furosemide - p.o. (tab), 40 mg_Martin 1984**

<br>
<br>

<a id="figure-3-16"></a>

![](images/006_section_3/009_section_33/010_section_331/41_time_profile_plot_Furosemide_p_o___80_mg__tab__Shoaf_2007_74_75.png)

**Figure 3-16: Furosemide - p.o. (tab), 80 mg_Shoaf 2007**

<br>
<br>

<a id="figure-3-17"></a>

![](images/006_section_3/009_section_33/010_section_331/44_time_profile_plot_Furosemide_p_o___40__mg__sol__Wiebe_2020_521_522.png)

**Figure 3-17: Furosemide - p.o. (sol), 40 mg_Wiebe 2020**

<br>
<br>

### 3.3.2 Model Verification<a id="332"></a>

<a id="figure-3-18"></a>

![](images/006_section_3/009_section_33/011_section_332/1_time_profile_plot_Furosemide_i_v__0_5_mgkg__bolus__Alvan_1988_1.png)

**Figure 3-18: Furosemide - i.v. (bolus), 0.5 mgkg_Alván 1988**

<br>
<br>

<a id="figure-3-19"></a>

![](images/006_section_3/009_section_33/011_section_332/3_time_profile_plot_Furosemide_i_v__20_mg__bolus__Rosenkranz_1992_66.png)

**Figure 3-19: Furosemide - i.v. (bolus), 20 mg_Rosenkranz 1992**

<br>
<br>

<a id="figure-3-20"></a>

![](images/006_section_3/009_section_33/011_section_332/4_time_profile_plot_Furosemide_i_v__22_mg__bolus__Tilstone_1978_83.png)

**Figure 3-20: Furosemide - i.v. (bolus), 22 mg_Tilstone 1978**

<br>
<br>

<a id="figure-3-21"></a>

![](images/006_section_3/009_section_33/011_section_332/5_time_profile_plot_Furosemide_i_v__40_mg__2_min__Waller_1982_97.png)

**Figure 3-21: Furosemide - i.v. (2 min), 40 mg_Waller 1982**

<br>
<br>

<a id="figure-3-22"></a>

![](images/006_section_3/009_section_33/011_section_332/6_time_profile_plot_Furosemide_i_v__40_mg__3_min__Smith_1980_78_79.png)

**Figure 3-22: Furosemide - i.v. (3min), 40 mg_Smith 1980a**

<br>
<br>

<a id="figure-3-23"></a>

![](images/006_section_3/009_section_33/011_section_332/7_time_profile_plot_Furosemide_i_v__40_mg__bolus__Andreasen_1977_9_10.png)

**Figure 3-23: Furosemide - i.v. (bolus), 40 mg_Andreasen 1977**

<br>
<br>

<a id="figure-3-24"></a>

![](images/006_section_3/009_section_33/011_section_332/8_time_profile_plot_Furosemide_i_v__40_mg__bolus__Gonzalez_1982_32.png)

**Figure 3-24: Furosemide - i.v. (bolus), 40 mg_González 1982**

<br>
<br>

<a id="figure-3-25"></a>

![](images/006_section_3/009_section_33/011_section_332/9_time_profile_plot_Furosemide_i_v__40_mg__bolus__Hammarlund_1984_39_40.png)

**Figure 3-25: Furosemide - i.v. (bolus), 40 mg_Hammarlund 1984**

<br>
<br>

<a id="figure-3-26"></a>

![](images/006_section_3/009_section_33/011_section_332/10_time_profile_plot_Furosemide_i_v__40_mg__bolus__Homeida_1977_47.png)

**Figure 3-26: Furosemide - i.v. (bolus), 40 mg_Homeida 1977**

<br>
<br>

<a id="figure-3-27"></a>

![](images/006_section_3/009_section_33/011_section_332/12_time_profile_plot_Furosemide_i_v__40_mg__bolus__Lambert_1983_58.png)

**Figure 3-27: Furosemide - i.v. (bolus), 40 mg_Lambert 1983**

<br>
<br>

<a id="figure-3-28"></a>

![](images/006_section_3/009_section_33/011_section_332/13_time_profile_plot_Furosemide_i_v__80_mg__2_min__Andreasen_1981_4.png)

**Figure 3-28: Furosemide - i.v. (bolus), 80 mg_Andreasen 1983**

<br>
<br>

<a id="figure-3-29"></a>

![](images/006_section_3/009_section_33/011_section_332/14_time_profile_plot_Furosemide_i_v__80_mg__2_min__Andreasen_1983_7_8.png)

**Figure 3-29: Furosemide - i.v. (bolus), 80 mg_Andreasen 1983**

<br>
<br>

<a id="figure-3-30"></a>

![](images/006_section_3/009_section_33/011_section_332/16_time_profile_plot_Furosemide_i_v__80_mg__bolus__Kelly_1974_57.png)

**Figure 3-30: Furosemide - i.v. (bolus), 80 mg_Kelly 1974**

<br>
<br>

<a id="figure-3-31"></a>

![](images/006_section_3/009_section_33/011_section_332/17_time_profile_plot_Furosemide_i_v__80_mg__bolus__Rane_1978_65.png)

**Figure 3-31: Furosemide - i.v. (bolus), 80 mg_Rane 1978**

<br>
<br>

<a id="figure-3-32"></a>

![](images/006_section_3/009_section_33/011_section_332/20_time_profile_plot_Furosemide_p_o___20_mg_____q_d__Vaidyanathan_2008_89.png)

**Figure 3-32: Furosemide - p.o. (-), 20 mg_Vaidyanathan 2008**

<br>
<br>

<a id="figure-3-33"></a>

![](images/006_section_3/009_section_33/011_section_332/21_time_profile_plot_Furosemide_p_o___20_mg__tab__q_d__FDA_2006_49.png)

**Figure 3-33: Furosemide - p.o. (tab), 20 mg q.d._FDA 2006**

<br>
<br>

<a id="figure-3-34"></a>

![](images/006_section_3/009_section_33/011_section_332/24_time_profile_plot_Furosemide_p_o___20__mg__sol__Waller_1985_100_101.png)

**Figure 3-34: Furosemide - p.o. (sol), 20 mg_Waller 1985**

<br>
<br>

<a id="figure-3-35"></a>

![](images/006_section_3/009_section_33/011_section_332/26_time_profile_plot_Furosemide_p_o___40__mg__sol__Waller_1988_533_534.png)

**Figure 3-35: Furosemide - p.o. (sol), 40 mg_Waller 1982**

<br>
<br>

<a id="figure-3-36"></a>

![](images/006_section_3/009_section_33/011_section_332/28_time_profile_plot_Furosemide_p_o___44__mg__sol__Tilstone_1978_84.png)

**Figure 3-36: Furosemide - p.o. (sol), 44 mg_Tilstone 1978**

<br>
<br>

<a id="figure-3-37"></a>

![](images/006_section_3/009_section_33/011_section_332/30_time_profile_plot_Furosemide_p_o___80__mg__sol__Kelly_1974_54.png)

**Figure 3-37: Furosemide - p.o. (sol), 80 mg_Kelly 1974**

<br>
<br>

<a id="figure-3-38"></a>

![](images/006_section_3/009_section_33/011_section_332/31_time_profile_plot_Furosemide_p_o___80__mg__sol__Waller_1985_104_105.png)

**Figure 3-38: Furosemide - p.o. (sol), 80 mg_Waller 1985**

<br>
<br>

<a id="figure-3-39"></a>

![](images/006_section_3/009_section_33/011_section_332/32_time_profile_plot_Furosemide_p_o___20_mg__tab__Haegeli_2007_35_36.png)

**Figure 3-39: Furosemide - p.o. (tab), 20 mg_Haegeli 2007**

<br>
<br>

<a id="figure-3-40"></a>

![](images/006_section_3/009_section_33/011_section_332/33_time_profile_plot_Furosemide_p_o___40_mg__tab__Ballester_2015_13_14.png)

**Figure 3-40: Furosemide - p.o. (tab) 40 mg_Ballester 2015**

<br>
<br>

<a id="figure-3-41"></a>

![](images/006_section_3/009_section_33/011_section_332/35_time_profile_plot_Furosemide_p_o___40_mg__tab__Hammarlund_1984_41_42.png)

**Figure 3-41: Furosemide - p.o. (tab), 40 mg_Hammarlund 1984**

<br>
<br>

<a id="figure-3-42"></a>

![](images/006_section_3/009_section_33/011_section_332/38_time_profile_plot_Furosemide_p_o___40_mg__tab__Rakhit_1987_63_64.png)

**Figure 3-42: Furosemide - p.o. (tab), 40 mg_Rahkit 1987**

<br>
<br>

<a id="figure-3-43"></a>

![](images/006_section_3/009_section_33/011_section_332/39_time_profile_plot_Furosemide_p_o___40_mg__tab__Rupp_1974_68.png)

**Figure 3-43: Furosemide - p.o. (tab), 40 mg_Rupp 1974**

<br>
<br>

<a id="figure-3-44"></a>

![](images/006_section_3/009_section_33/011_section_332/40_time_profile_plot_Furosemide_p_o___80_mg__tab__Kelly_1974_56.png)

**Figure 3-44: Furosemide - p.o. (tab), 80 mg_Kelly 1974**

<br>
<br>

<a id="figure-3-45"></a>

![](images/006_section_3/009_section_33/011_section_332/42_time_profile_plot_Furosemide_p_o___40_mg__tab__Waller_1982_98.png)

**Figure 3-45: Furosemide - p.o. (tab), 40 mg_Waller 1982**

<br>
<br>

<a id="figure-3-46"></a>

![](images/006_section_3/009_section_33/011_section_332/43_time_profile_plot_Furosemide_p_o___80_mg__tab__Vree_1995_95_96.png)

**Figure 3-46: Furosemide - p.o. (tab), 80 mg_Vree 1995**

<br>
<br>

# 4 Conclusion<a id="4"></a>

The presented PBPK model adequately describes the intravenous and oral pharmacokinetics of furosemide in adults.

# 5 References<a id="5"></a>

**Alván 1988** Alván G, Beermann B, Hjelte L, et al (1988) Increased nonrenal clearance and increased diuretic efficiency of furosemide in cystic fibrosis. Clin Pharmacol Ther 44:436–441. https://doi.org/10.1038/clpt.1988.177

**Andreasen 1982** Andreasen F, Christensen CK, Jacobsen FK, et al (1982) The individual variation in pharmacokinetics and pharmacodynamics of furosemide in young normal male subjects. European Journal of Clinical Investigation 12:247–255

**Andreasen 1981** Andreasen F, Christensen CK, Jakobsen FK, Mogensen CE (1981) The use of HPLC to elucidate the metabolism and urinary excretion of furosemide and its metabolic products. Acta Pharmacol Toxicol (Copenh) 49:223–229. https://doi.org/10.1111/j.1600-0773.1981.tb00897.x

**Andreasen 1983** Andreasen F, Hansen U, Husted SE, Jansen JA (1983) The pharmacokinetics of frusemide are influenced by age. Br J Clin Pharmacol 16:391–397. https://doi.org/10.1111/j.1365-2125.1983.tb02183.x

**Andreasen 1974** Andreasen F, Jakobsen P (1974) Determination of furosemide in blood plasma and its binding to proteins in normal plasma and in plasma from patients with acute renal failure. Acta Pharmacol Toxicol (Copenh) 35:49–57. https://doi.org/10.1111/j.1600-0773.1974.tb00724.x

**Andreasen 1977** Andreasen F, Mikkelsen E (1977) Distribution, elimination and effect of furosemide in normal subjects and in patients with heart failure. Eur J Clin Pharmacol 12:15–22. https://doi.org/10.1007/BF00561400

**Avdeef 2003** Avdeef A (2003) Absorption and Drug Development: Solubility, Permeability, and Charge State

**Avdeef 2008** Avdeef A, Tsinman O (2008) Miniaturized Rotating Disk Intrinsic Dissolution Rate Measurement: Effects of Buffer Capacity in Comparisons to Traditional Wood’s Apparatus. Pharm Res 25:2613–2627. https://doi.org/10.1007/s11095-008-9679-z

**Ballester 2015** Ballester MR, Roig E, Gich I, et al (2015) Randomized, open-label, blinded-endpoint, crossover, single-dose study to compare the pharmacodynamics of torasemide-PR 10 mg, torasemide-IR 10 mg, and furosemide-IR 40 mg, in patients with chronic heart failure. Drug Des Devel Ther 9:4291–4302. https://doi.org/10.2147/DDDT.S86300

**Berthod 1999** Berthod A, Carda-Broch S, Garcia-Alvarez-Coque MC (1999) Hydrophobicity of Ionizable Compounds. A Theoretical Study and Measurements of Diuretic Octanol−Water Partition Coefficients by Countercurrent Chromatography. Anal Chem 71:879–888. https://doi.org/10.1021/ac9810563

**Bindschedler 1997** Bindschedler M, Degen P, Flesch G, et al (1997) Pharmacokinetic and pharmacodynamic interaction of single oral doses of valsartan and furosemide. Eur J Clin Pharmacol 52:371–378. https://doi.org/10.1007/s002280050303

**Box 2006** Box KJ, Völgyi G, Baka E, et al (2006) Equilibrium versus kinetic measurements of aqueous solubility, and the ability of compounds to supersaturate in solution--a validation study. J Pharm Sci 95:1298–1307. https://doi.org/10.1002/jps.20613

**Branch 1977** Branch RA, Roberts CJ, Homeida M, Levine D (1977) Determinants of response to frusemide in normal subjects. Br J Clin Pharmacol 4:121–127. https://doi.org/10.1111/j.1365-2125.1977.tb00682.x

**Britz 2020** Britz H, Hanke N, Taub ME, et al (2020) Physiologically Based Pharmacokinetic Models of Probenecid and Furosemide to Predict Transporter Mediated Drug-Drug Interactions. Pharm Res 37:250. https://doi.org/10.1007/s11095-020-02964-z

**Ebner2015** Ebner T, Ishiguro N, Taub ME (2015) The Use of Transporter Probe Drug Cocktails for the Assessment of Transporter-Based Drug-Drug Interactions in a Clinical Setting-Proposal of a Four Component Transporter Cocktail. J Pharm Sci 104:3220–3228. https://doi.org/10.1002/jps.24489

**Forrey 1974** Forrey AW, Kimpel B, Blair AD, Cutler RE (1974) Furosemide concentrations in serum and urine, and its binding by serum proteins as measured fluorometrically. Clin Chem 20:152–158

**González 1982** González G, Arancibia A, Rivas MI, et al (1982) Pharmacokinetics of furosemide in patients with hepatic cirrhosis. Eur J Clin Pharmacol 22:315–320. https://doi.org/10.1007/BF00548399

**Haegeli 2007** Haegeli L, Brunner-La Rocca HP, Wenk M, et al (2007) Sublingual administration of furosemide: new application of an old drug. Br J Clin Pharmacol 64:804–809. https://doi.org/10.1111/j.1365-2125.2007.03035.x

**Hammarlund 1984** Hammarlund MM, Paalzow LK, Odlind B (1984) Pharmacokinetics of furosemide in man after intravenous and oral administration. Application of moment analysis. Eur J Clin Pharmacol 26:197–207. https://doi.org/10.1007/BF00630286

**Keller 1981** Keller E, Hoppe-Seyler G, Mumm R, Schollmeyer P (1981) Influence of hepatic cirrhosis and end-stage renal disease on pharmacokinetics and pharmacodynamics of furosemide. Eur J Clin Pharmacol 20:27–33. https://doi.org/10.1007/BF00554663

**Kelly 1974** Kelly MR, Cutler RE, Forrey AW, Kimpel BM (1974) Pharmacokinetics of orally administered furosemide. Clin Pharmacol Ther 15:178–186

**Kuepfer 2016** Kuepfer L, Niederalt C, Wendl T, et al (2016) Applied Concepts in PBPK Modeling: How to Build a PBPK/PD Model. CPT: pharmacometrics & systems pharmacology 5:516–531. https://doi.org/10.1002/psp4.12134

**Lambert 1983** Lambert C, Larochelle P, du Souich P (1983) Effects of phenobarbital and tobacco smoking on furosemide kinetics and dynamics in normal subjects. Clin Pharmacol Ther 34:170–175. https://doi.org/10.1038/clpt.1983.148

**Langenbucher 1972** Langenbucher F (1972) Linearization of dissolution rate curves by the Weibull distribution. J Pharm Pharmacol 24:979–981. https://doi.org/10.1111/j.2042-7158.1972.tb08930.x

**Martin 1984** Martin BK, Uihlein M, Ings RM, et al (1984) Comparative bioavailability of two furosemide formulations in humans. J Pharm Sci 73:437–441. https://doi.org/10.1002/jps.2600730404

**McNamara 1987** McNamara PJ, Foster TS, Digenis GA, et al (1987) Influence of tablet dissolution on furosemide bioavailability: a bioequivalence study. Pharmaceutical research 4:150–153

**Meyer 2012** Meyer M, Schneckener S, Ludewig B, et al (2012) Using expression data for quantification of active processes in physiologically based pharmacokinetic modeling. Drug Metab Dispos 40:892–901. https://doi.org/10.1124/dmd.111.043174

**Nishimura 2005** Nishimura M, Naito S (2005) Tissue-specific mRNA Expression Profiles of Human ATP-binding Cassette and Solute Carrier Transporter Superfamilies. Drug Metabolism and Pharmacokinetics 20:452–477. https://doi.org/10.2133/dmpk.20.452

**Nishimura 2006** Nishimura M, Naito S (2006) Tissue-specific mRNA expression profiles of human phase I metabolizing enzymes except for cytochrome P450 and phase II metabolizing enzymes. Drug Metab Pharmacokinet 21:357–374. https://doi.org/10.2133/dmpk.21.357

**Pacifici 1987** Pacifici GM, Viani A, Schulz HU, Frercks HJ (1987) Plasma protein binding of furosemide in the elderly. Eur J Clin Pharmacol 32:199–202. https://doi.org/10.1007/BF00542196

**PK-Sim Ontogeny Database Version 7.3** PK-Sim Ontogeny Database Version 7.3 (https://github.com/Open-Systems-Pharmacology/OSPSuite.Documentation/blob/38cf71b384cfc25cfa0ce4d2f3addfd32757e13b/PK-Sim%20Ontogeny%20Database%20Version%207.3.pdf)

**Ponto and Schoenwald 1990** Ponto LL, Schoenwald RD (1990) Furosemide (frusemide). A pharmacokinetic/pharmacodynamic review (Part I). Clin Pharmacokinet 18:381–408. https://doi.org/10.2165/00003088-199018050-00004

**Rakhit 1987** Rakhit A, Kochak GM, Tipnis V, Hurley ME (1987) Inhibition of renal clearance of furosemide by pentopril, an angiotensin-converting enzyme inhibitor. Clin Pharmacol Ther 41:580–586. https://doi.org/10.1038/clpt.1987.75

**Rane 1978** Rane A, Villeneuve JP, Stone WJ, et al (1978) Plasma binding and disposition of furosemide in the nephrotic syndrome and in uremia. Clin Pharmacol Ther 24:199–207. https://doi.org/10.1002/cpt1978242199

**Rosenkranz 1992** Rosenkranz B, Lehr KH, Mackert G, Seyberth HW (1992) Metamizole-furosemide interaction study in healthy volunteers. Eur J Clin Pharmacol 42:593–598. https://doi.org/10.1007/BF00265921

**Rupp 1974** Rupp W (1974) Pharmacokinetics and pharmacodynamics of Lasix. Scott Med J 19 Suppl 1:5–13. https://doi.org/10.1177/00369330740190S103

**Schmitt 2008** Schmitt W (2008) General approach for the calculation of tissue to plasma partition coefficients. Toxicol In Vitro 22:457–467. https://doi.org/10.1016/j.tiv.2007.09.010

**Shen 2019** Shen H, Holenarsipur VK, Mariappan TT, et al (2019) Evidence for the Validity of Pyridoxic Acid (PDA) as a Plasma-Based Endogenous Probe for OAT1 and OAT3 Function in Healthy Subjects. J Pharmacol Exp Ther 368:136–145. https://doi.org/10.1124/jpet.118.252643

**Shoaf 2007** Shoaf SE, Bramer SL, Bricmont P, Zimmer CA (2007) Pharmacokinetic and pharmacodynamic interaction between tolvaptan, a non-peptide AVP antagonist, and furosemide or hydrochlorothiazide. J Cardiovasc Pharmacol 50:213–222. https://doi.org/10.1097/FJC.0b013e318074f934

**Smith 1980a** Smith DE, Gee WL, Brater DC, et al (1980a) Preliminary evaluation of furosemide-probenecid interaction in humans. J Pharm Sci 69:571–575. https://doi.org/10.1002/jps.2600690526

**Smith 1980b** Smith DE, Lin ET, Benet LZ (1980b) Absorption and disposition of furosemide in healthy volunteers, measured with a metabolite-specific assay. Drug Metab Dispos 8:337–342

**Söderlind 2010** Söderlind E, Karlsson E, Carlsson A, et al (2010) Simulating fasted human intestinal fluids: understanding the roles of lecithin and bile acids. Mol Pharm 7:1498–1507. https://doi.org/10.1021/mp100144v

**Stopfer 2016** Stopfer P, Giessmann T, Hohl K, et al (2016) Pharmacokinetic Evaluation of a Drug Transporter Cocktail Consisting of Digoxin, Furosemide, Metformin, and Rosuvastatin. Clin Pharmacol Ther 100:259–267. https://doi.org/10.1002/cpt.406

**Stopfer 2018** Stopfer P, Giessmann T, Hohl K, et al (2018) Optimization of a drug transporter probe cocktail: potential screening tool for transporter-mediated drug-drug interactions. Br J Clin Pharmacol 84:1941–1949. https://doi.org/10.1111/bcp.13609

**Takács-Novák 2013**Takács-Novák K, Szőke V, Völgyi G, et al (2013) Biorelevant solubility of poorly soluble drugs: Rivaroxaban, furosemide, papaverine and niflumic acid. Journal of Pharmaceutical and Biomedical Analysis 83:279–285. https://doi.org/10.1016/j.jpba.2013.05.011

**Tilstone 1978** Tilstone WJ, Fine A (1978) Furosemide kinetics in renal failure. Clin Pharmacol Ther 23:644–650. https://doi.org/10.1002/cpt1978236644

**FDA 2005** U.S. FDA (2005) Clinical pharmacology and biopharmaceutics review. NDA: 21-742 - part 3. 

**FDA 2006** U.S. FDA (2006) Clinical pharmacology and biopharmaceutics review. NDA: 21-985 - part 3.

**Vaidyanathan 2008** Vaidyanathan S, Bartlett M, Dieterich HA, et al (2008) Pharmacokinetic interaction of the direct renin inhibitor aliskiren with furosemide and extended-release isosorbide-5-mononitrate in healthy subjects. Cardiovasc Ther 26:238–246. https://doi.org/10.1111/j.1755-5922.2008.00058.x

**Ventura 1996** Ventura R, Segura J (1996) Detection of diuretic agents in doping control. J Chromatogr B Biomed Appl 687:127–144. https://doi.org/10.1016/s0378-4347(96)00279-4

**Verbeeck 1982** Verbeeck RK, Patwardhan RV, Villeneuve JP, et al (1982) Furosemide disposition in cirrhosis. Clin Pharmacol Ther 31:719–725. https://doi.org/10.1038/clpt.1982.101

**Vree 1994** Vree TB, van den Biggelaar-Martea M, Verwey-van Wissen CP (1994) Determination of furosemide with its acyl glucuronide in human plasma and urine by means of direct gradient high-performance liquid chromatographic analysis with fluorescence detection. Preliminary pharmacokinetics and effect of probenecid. J Chromatogr B Biomed Appl 655:53–62. https://doi.org/10.1016/0378-4347(94)00093-x

**Vree 1995** Vree TB, van den Biggelaar-Martea M, Verwey-van Wissen CP (1995) Probenecid inhibits the renal clearance of frusemide and its acyl glucuronide. Br J Clin Pharmacol 39:692–695

**Waller 1988** Waller ES, Crismon ML, Smith RV, et al (1988) Comparative bioavailability of furosemide from solution and 40 mg tablets with different dissolution characteristics following oral administration in normal men. Biopharm Drug Dispos 9:211–218. https://doi.org/10.1002/bod.2510090209

**Waller 1982** Waller ES, Hamilton SF, Massarella JW, et al (1982) Disposition and absolute bioavailability of furosemide in healthy males. J Pharm Sci 71:1105–1108. https://doi.org/10.1002/jps.2600711006

**Waller 1985** Waller ES, Massarella JW, Tomkiw MS, et al (1985) Pharmacokinetics of furosemide after three different single oral doses. Biopharm Drug Dispos 6:109–117. https://doi.org/10.1002/bdd.2510060202

**Wiebe 2020** Wiebe ST, Giessmann T, Hohl K, et al (2020) Validation of a Drug Transporter Probe Cocktail Using the Prototypical Inhibitors Rifampin, Probenecid, Verapamil, and Cimetidine. Clin Pharmacokinet 59:1627–1639. https://doi.org/10.1007/s40262-020-00907-w

**Willmann 2007** Willmann S, Hohn K, Edginton A, et al (2007) Development of a physiology-based whole-body population model for assessing the influence of individual variability on the pharmacokinetics of drugs. Journal of pharmacokinetics and pharmacodynamics 34:401–31. https://doi.org/10.1007/s10928-007-9053-5

**Wishart 2006** Wishart DS, Knox C, Guo AC, et al (2006) DrugBank: a comprehensive resource for in silico drug discovery and exploration. Nucleic Acids Res 34:D668-672. https://doi.org/10.1093/nar/gkj067

