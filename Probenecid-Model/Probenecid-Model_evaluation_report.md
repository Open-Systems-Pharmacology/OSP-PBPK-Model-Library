# Building and evaluation of a PBPK model for Probenecid in healthy adults

| Version                                         | 1.0-OSP12.1                                                   |
| ----------------------------------------------- | ------------------------------------------------------------ |
| based on *Model Snapshot* and *Evaluation Plan* | https://github.com/Open-Systems-Pharmacology/Probenecid-Model/releases/tag/v1.0 |
| OSP Version                                     | 12.1                                                          |
| Qualification Framework Version                 | 3.4                                                          |

This evaluation report and the corresponding PK-Sim project file are filed at:

https://github.com/Open-Systems-Pharmacology/OSP-PBPK-Model-Library/

# Table of Contents

 * [1 Introduction](#1)
 * [2 Methods](#2)
   * [2.1 Modeling strategy](#21)
   * [2.2 Data used](#22)
   * [2.3 Model parameters and assumptions](#23)
 * [3 Results and Discussion](#3)
   * [3.1 Probenecid final input parameters](#31)
   * [3.2 Probenecid Diagnostics Plots](#32)
   * [3.3 Concentration-Time Profiles](#33)
     * [3.3.1 Model Building](#331)
     * [3.3.2 Model Verification](#332)
 * [4 Conclusion](#4)
 * [5 References](#5)

# 1 Introduction<a id="1"></a>

Probenecid is a uricosuric agent for the treatment of gout and hyperuricemia and is also used to increase plasma concentrations of antibiotics. It is metaboliszed by UGT1A9, transported by OAT3 and renally excreted by glomerular filtration and subject of tubular reabsorbtion (GFR <1). About 72% to 86% of an oral dose of probenecid is excreted in urine and of this fraction only 0.3-5% are excreted unchanged. Probenecid is an inhibitor of OAT1, OAT3, UGT1A9, MRP4 (ABCC4) and OATP1B1 and can therefore serve as a perpetrator for these transporters in DDI studies. 

The herein presented PBPK model of probenecid has been developed using published pharmacokinetic clinical data by Dayton 1963 ([Dayton 1963](#5-references)), Emanuelsson 1987 ([Emanuelsson 1987](#5-references)), Vree 1992 ([Vree 1992](#5-references)), Selen 1982 ([Selen 1982](#5-references)), Wiebe 2020 ([Wiebe 2020](#5-references)) and Landersdorfer 2009 ([Landersdorfer 2009](#5-references)). 
The model has then been evaluated by comparing observed data to simulations of both intravenously and orally administered probenecid covering a dose range of 500 mg to 2000 mg. Both single dose and multiple dose administration are represented in the development and evaluation data sets. 

The presented model includes the following features:

- metabolism by UGT1A9,
- transport by OAT3,
- inhibition of OAT3, MRP4 (ABCC4) and OATP1B1,
- renal clearance by glomerular filtration and tubular reabsorption modelled by GFR <1,
- oral absorption with dissolution rate assigned to the Weibull function.

# 2 Methods<a id="2"></a>

## 2.1 Modeling strategy<a id="21"></a>

The general concept of building a PBPK model has previously been described by Kuepfer et al. ([Kuepfer 2016](#5-references)). Relevant information on anthropometric (height, weight) and physiological parameters (e.g. blood flows, organ volumes, binding protein concentrations, hematocrit, cardiac output) in adults was gathered from the literature and has been previously published ([Willmann 2007](#5-references)). The information was incorporated into PK-Sim® and was used as default values for the simulations in adults.

The applied activity and variability of plasma proteins and active processes that are integrated into PK-Sim® are described in the publicly available PK-Sim® Ontogeny Database Version 7.3 ([PK-Sim Ontogeny Database Version 7.3](#5-references)) or otherwise referenced for the specific process.

A mean model was built based on clinical data from studies with intravenous and oral administration of probenecid by Dayton 1963 ([Dayton 1963](#5-references)), Emanuelsson 1987 ([Emanuelsson 1987](#5-references)), Vree 1992 ([Vree 1992](#5-references)), Selen 1982 ([Selen 1982](#5-references)), Wiebe 2020 ([Wiebe 2020](#5-references)) and Landersdorfer 2009 [Landersdorfer 2009](#5-references). The studies reported individual (Dayton 1963 ([Dayton 1963](#5-references))) or mean (Emanuelsson 1987 ([Emanuelsson 1987](#5-references)), Vree 1992 ([Vree 1992](#5-references)), Selen 1982 ([Selen 1982](#5-references)), Wiebe 2020 ([Wiebe 2020](#5-references)) and Landersdorfer 2009 ([Landersdorfer 2009](#5-references))) plasma concentrations of probenecid. The studies by Vree 1992 also reported individual urine fraction of unchanged probenecid. The mean PBPK model was developed using a mean individual based on the demographic data for each study and if no demographic data were provided the following values were used; male, European, 30 years of age, 73 kg body weight and 176 cm body height. The relative tissue-specific expressions of the enzyme and transporter predominantly being involved in the metabolism/transport of probenecid (UGT1A9 and OAT3) were considered ([Meyer 2012](#5-references)). A Weibull function was fitted to describe the oral dissolution of probenecid. For the studies conducted by Vree, the tablet was broken in half and a shorter time to maximum concentration was observed and therefore a different Weibull function was fitted for these data. 

A specific set of parameters (see below) was optimized to describe the disposition of probenecid using the Parameter Identification module provided in PK-Sim®. Structural model selection was mainly guided by visual inspection and total error of the resulting description of data, 95% confidence interval of the identified parameter values and biological plausibility.

The model was then verified by simulating further clinical studies reporting pharmacokinetic concentration-time profiles after intravenous and oral administration of probenecid.

Details about input data (physicochemical, *in vitro* and clinical) can be found in [Section 2.2](#22-data-used).

Details about the structural model and its parameters can be found in [Section 2.3](#23-model-parameters-and-assumptions).

## 2.2 Data used<a id="22"></a>

### 2.2.1 In vitro and physicochemical data

A literature search was performed to collect available information on physicochemical properties of probenecid. The obtained information from literature is summarized in the table below, and is used for model building. Final model parameters are stated in [Section 3.1](#31-probenecid-final-input-parameters).

| **Parameter**           | **Unit** | **Value** | Source                               | **Description**                                              |
| :---------------------- | -------- | --------- | ------------------------------------ | ------------------------------------------------------------ |
| MW                      | g/mol    | 285.36    | [Wishart 2006](#5-references)        | Molecular weight                                             |
| pK<sub>a</sub> (acid)   |          | 3.01      | [Avdeef 2001](#5-references)         | acid dissociation constant of conjugate acid                 |
|                         |          | 3.7       | [Avdeef 2003](#5-references)         | acid dissociation constant of conjugate acid                 |
| Solubility (HIF)        | mg/mL    | 0.74      | [Söderlind 2010](#5-references)      | Aqueous Solubility in human intestinal fluid                 |
| logP                    |          | -0.52     | [Dayton 1963](#5-references)         | Partition coefficient between octanol and water              |
|                         |          |-0.23      | [Avdeef 2001](#5-references)         | Partition coefficient between octanol and water              |
|                         |          | 0.13      | [Avdeef 2003](#5-references)         | Partition coefficient between octanol and water              |
|                         |          | 3.21      | [Hansch 1995](#5-references)         | Partition coefficient between octanol and water              |
|                         |          | 3.7       | [Hansch 1995](#5-references)         | Partition coefficient between octanol and water              |
| fu                      | %        | 6.2       | [Vree 1992](#5-references)           | Fraction unbound in plasma                                   |
|                         | %        | 7.56      | [Vree 1993](#5-references)           | Fraction unbound in plasma                                   |
|                         | %        | 11.7      | [Shen 2019](#5-references)           | Fraction unbound in plasma                                   |
| K<sub>m</sub> UGT1A9    | µmol/L   | 198.3     | [Ito 2014](#5-references)            | UGT1A9 Michaelis-Menten constant                             |
| Ki UGT1A9               | µmol/L   | 242       | Measured                             | Inhibition of UGT1A9                                         |
| Ki OAT3                 | µmol/L   | 5.41      | [Tsuruya 2016](#5-references)        | Inhibition of OAT3                                           |
| Ki OATP1B1              | µmol/L   | 39.8      | [Izumi 2016](#5-references)          | Inhibition of OATP1B1                                        |
| Ki OATP1B1              | µmol/L   | 17.89      | In vivo Ki estimated based on CP-I data| Inhibition of OATP1B1                                     |
| Ki MRP4 (ABCC4)         | µmol/L   |    87.40   |     Probenecid-Furosemid-DDI*            |    Inhibition of MRP4                 |
*To describe the competitive inhibition of MRP4 by probenecid, the corresponding inhibition constant was optimized during the furosemide PBPK model parameter identification, using the clinical data of one of the probenecid-furosemide interaction studies ([Probenecid-Furosemid-DDI Repository](https://github.com/Open-Systems-Pharmacology/Probenecid-Furosemide-DDI)).

### 2.2.2 Clinical data

A literature search was performed to collect available clinical data on probenecid in adults. 

The following publications were found in adults for model building:

| Publication                   | Arm / Treatment / Information used for model building        |
| :---------------------------- | :----------------------------------------------------------- |
| [Dayton 1963](#5-references)  | Individual plasma PK profiles in healthy subjects after single intravenous administration of 464.20 and 1860 mg probenecid |
| [Emanuelsson 1987](#5-references) | Plasma PK profiles in healthy subjects after single intravenous infusion (15 min) of 500 mg probenecid and single oral administration of 2000 mg probenecid|
| [Vree 1992](#5-references)    | Plasma PK profiles and urine data in healthy subjects after single oral administration of 250 and 1500 mg probenecid |
| [Selen 1992](#5-references)   | Plasma PK profiles in healthy subjects after single oral administration of 500, 1000 and 2000mg probenecid |
| [Wiebe 2020](#5-references)   | Plasma PK profiles in healthy subjects after multiple oral administration of 1000 mg probenecid |
| [Landersdorfer 2009](#5-references)    | Plasma PK profiles in healthy subjects after multiple oral administration of 250, 500 and 1000 mg probenecid |

The following table shows the data from the excretion studies ([Vree 1992](#5-references)) used for model building:

| Observer                                                     | Value |
| ------------------------------------------------------------ | ----- |
| Fraction excreted  to urine of unchanged probenecid after oral administration 1000 mg | 2%   |
| Fraction excreted  to urine of unchanged probenecid after oral administration 1500 mg | 5%   |
| Fraction excreted  to urine of unchanged probenecid after oral administration 500 mg | 0.3%  |
| Fraction excreted  to urine of unchanged probenecid after oral administration 250 mg | 1.1%  |

The following dosing scenarios were simulated and compared to respective data for model verification:

| Scenario                                                     | Data reference                       |
| ------------------------------------------------------------ | ------------------------------------ |
| iv bolus 464.2 mg                         | [Dayton 1963](#5-references) |
| iv bolus 1860 mg                          | [Dayton 1963](#5-references) |
| po 500 mg                                 | [Emanuelsson 1987](#5-references) and [Vree 1992](#5-references) |
| po 1000 mg                                | [Emanuelsson 1987](#5-references), [Shen 2019](#5-references), [Vree 1992](#5-references), [Vree 1993](#5-references)|
| po 2000 mg                                | [Dayton 1963](#5-references)|
| po 1000 mg bid for 1 day                  | [Smith 1980](#5-references) |
| po 500 mg at 0, 1000 mg at 8 h and 500 mg at 14.5, 20.5 and 26.5 h| [Landersdorfer 2010](#5-references) |

## 2.3 Model parameters and assumptions<a id="23"></a>

### 2.3.1 Absorption

The parameter value for  `Specific intestinal permeability`  was optimized based on clinical oral data, see results of optimization in [Section 2.3.4](#234-automated-parameter-identification). The measured solubility in human intestinal fluid (HIF) was used in the model (see [Section 2.2.1](#221-in-vitro-and-physicochemical-data))

The dissolution of tablets was implemented via empirical Weibull dissolution. A different Weibull function was used for the studies by Vree ([Vree 1992](#5-references)), as the tablets were broken in half and an shorter time to reach maximum concentration was observed, see results of optimization in [Section 2.3.4](#234-automated-parameter-identification).

### 2.3.2 Distribution

Probenecid is highly bound to plasma proteins (approx. 88 %) (see [Section 2.2.1](#221-in-vitro-and-physicochemical-data)). A value of 12% was used in this PBPK model for `Fraction unbound (plasma, reference value)`. The major binding partner was set to albumin (see [Section 2.2.1](#221-in-vitro-and-physicochemical-data)).

An important parameter influencing the resulting volume of distribution is lipophilicity. The reported experimental logP values are in the range of -0.52 to 3.7 (see [Section 2.2.1](#221-in-vitro-and-physicochemical-data)) which served as a starting value. Finally, the model parameter `Lipophilicity` was optimized to match clinical data (see also [Section 2.3.4](#234-automated-parameter-identification)).

After testing the available organ-plasma partition coefficient and cell permeability calculation methods built in PK-Sim, observed clinical data was best described by choosing the partition coefficient calculation by `PK-Sim Standard` and cellular permeability calculation by `Charge dependent Schmitt normalized to PK-Sim`.

### 2.3.3 Metabolism and Elimination

One metabolic pathway was implement into the model via Michaelis-Menten kinetics 

* UGT1A9

The UGT1A9 expression profiles is based on high-sensitive real-time RT-PCR ([Nishimura 2003](#5-references)). Metabolic enzyme activity was described as saturable process following Michaelis-Menten kinetics, were the `Km` was taken from literature measured in liver microsomes and the `kcat` was optimized based on clinical data (see [Section 2.3.4](#234-automated-parameter-identification)).

And one transport protein was implemented into the model via Michaelis-Menten kinetics 

* OAT3

The OAT3 expression profiles is based on high-sensitive real-time RT-PCR ([Nishimura 2003](#5-references)). Transporter activity was described as saturable process following Michaelis-Menten kinetics, were both `Km` and `kcat` was optimized based on clinical data (see [Section 2.3.4](#234-automated-parameter-identification)).

Additionally, renal clearance assumed to be mainly driven by glomerular filtration and tubular reabsorption modelled as GFR <1 was implemented. The `GFR fraction` was identified to best describe the observed fraction of unchanged probenecid that was renally excreted (see [Section 2.3.4](#234-automated-parameter-identification)).

### 2.3.4 Automated Parameter Identification

These are the parameters estimated in the final parameter identification:

| Model Parameter                | 
| ------------------------------ | 
| `Lipophilicity`                | 
| `GFR fraction`                 |
| `kcat` (UGT1A9)                | 
| `km` (OAT3)                    |
| `kcat` (OAT3)                  | 
| `Specific intestinal permeability`|
| `Dissolution time (50% dissolved)`| 
| `Dissolution shape`               | 
| `Dissolution time (50% dissolved)` (Broken tablet)|
| `Dissolution shape` (broken tablet) | 

 

# 3 Results and Discussion<a id="3"></a>

The PBPK model for probenecid was developed and verified with clinical pharmacokinetic data.

The model was built and evaluated covering data from studies including in particular

* single intravenous administration and both single and multiple oral administrations (tablets).
* a dose range of 250 to 2000 mg.

The model quantifies excretion via urine (glomerular filtration and reabsorption assigned to reduced GFR), metabolism via UGT1A9 and transport by OAT3.

The next sections show:

1. the final model input parameters for the building blocks: [Section 3.1](#31-probenecid-final-input-parameters).
2. the overall goodness of fit: [Section 3.2](#32-probenecid-diagnostics-plots).
3. simulated vs. observed concentration-time profiles for the clinical studies used for model building and for model verification: [Section 3.3](#33-concentration-time-profiles).

## 3.1 Probenecid final input parameters<a id="31"></a>

The compound parameter values of the final PBPK model are illustrated below.

### Compound: Probenecid

#### Parameters

Name                                             | Value                  | Value Origin                                                                                                                                        | Alternative         | Default
------------------------------------------------ | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | -------
Solubility at reference pH                       | 738 mg/l               | Publication-In Vitro-Söderlind 2010, HIF                                                                                                            | Söderlind 2010, HIF | True   
Reference pH                                     | 7                      | Publication-In Vitro-Söderlind 2010, HIF                                                                                                            | Söderlind 2010, HIF | True   
Lipophilicity                                    | 1.3396899029 Log Units | Parameter Identification-Parameter Identification-Value updated from 'IV_PO_TAB_GFRfraction_without Land 2010_250919_LM_FINAL2' on 2019-12-18 15:32 | Avdeef 2003         | True   
Fraction unbound (plasma, reference value)       | 0.117                  | Publication-In Vitro-Vree 1992                                                                                                                      | Vree 1992           | True   
Specific intestinal permeability (transcellular) | 0.0003971252633 cm/min | Parameter Identification-Parameter Identification-Value updated from 'IV_PO_TAB_GFRfraction_without Land 2010_250919_LM_FINAL2' on 2019-12-18 15:32 | fitted              | True   
Is small molecule                                | Yes                    |                                                                                                                                                     |                     |        
Molecular weight                                 | 285.359 g/mol          |                                                                                                                                                     |                     |        
Plasma protein binding partner                   | Albumin                |                                                                                                                                                     |                     |        

#### Calculation methods

Name                    | Value                                        
----------------------- | ---------------------------------------------
Partition coefficients  | PK-Sim Standard                              
Cellular permeabilities | Charge dependent Schmitt normalized to PK-Sim

#### Processes

##### Systemic Process: Glomerular Filtration-GFR

Species: Human

###### Parameters

Name         |        Value | Value Origin                                                                                                                                       
------------ | ------------:| ---------------------------------------------------------------------------------------------------------------------------------------------------
GFR fraction | 0.0298169506 | Parameter Identification-Parameter Identification-Value updated from 'IV_PO_TAB_GFRfraction_without Land 2010_250919_LM_FINAL2' on 2019-12-18 15:32

##### Inhibition: OAT3-Tsuruya 2016

Molecule: OAT3

###### Parameters

Name | Value       | Value Origin                     
---- | ----------- | ---------------------------------
Ki   | 5.41 µmol/l | Publication-In Vitro-Tsuruya 2016

##### Metabolizing Enzyme: UGT1A9-Ito 2014

Molecule: UGT1A9

###### Parameters

Name                               | Value                       | Value Origin                                                                                                                                       
---------------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------
In vitro Vmax for liver microsomes | 59 pmol/min/mg mic. protein | Publication-In Vitro-Ito 2014                                                                                                                      
Km                                 | 198.3 µmol/l                | Publication-In Vitro-Ito 2014                                                                                                                      
kcat                               | 74.9179385436 1/min         | Parameter Identification-Parameter Identification-Value updated from 'IV_PO_TAB_GFRfraction_without Land 2010_250919_LM_FINAL2' on 2019-12-18 15:32

##### Transport Protein: OAT3-assumed

Molecule: OAT3

###### Parameters

Name                      | Value                | Value Origin                                                                                                                                       
------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------
Transporter concentration | 1 µmol/l             |                                                                                                                                                    
Vmax                      | 0 µmol/l/min         |                                                                                                                                                    
Km                        | 12.1775959667 µmol/l | Parameter Identification-Parameter Identification-Value updated from 'IV_PO_TAB_GFRfraction_without Land 2010_250919_LM_FINAL2' on 2019-12-18 15:32
kcat                      | 1118.97811 1/min     | Other-Manual Fit-obtained by optimited Kcat value in V9 * 0.569. 0.569 is the ratio of OAT3 amount in V9/V11 with script transporterFactorsOAT3    

##### Inhibition: OATP1B1-Izumi 2016

Molecule: OATP1B1

###### Parameters

Name | Value       | Value Origin                   
---- | ----------- | -------------------------------
Ki   | 39.8 µmol/l | Publication-In Vitro-Izumi 2016

##### Inhibition: OATP1B1-In vivo Ki based on CP-I

Molecule: OATP1B1

###### Parameters

Name | Value        | Value Origin                                                                 
---- | ------------ | -----------------------------------------------------------------------------
Ki   | 17.89 µmol/l | Parameter Identification-Parameter Identification-based on CP-I plasma levels

##### Inhibition: UGT1A9-Wang 2020

Molecule: UGT1A9

###### Parameters

Name | Value      | Value Origin                  
---- | ---------- | ------------------------------
Ki   | 242 µmol/l | Publication-In Vitro-Wang 2020

##### Inhibition: ABCC4-Fitted

Molecule: ABCC4

###### Parameters

Name | Value               | Value Origin                                   
---- | ------------------- | -----------------------------------------------
Ki   | 87.396448408 µmol/l | Publication-Parameter Identification-Wiebe 2020

## 3.2 Probenecid Diagnostics Plots<a id="32"></a>

Below you find the goodness-of-fit visual diagnostic plots for the PBPK model performance of all data used presented in [Section 2.2.2](#222-clinical-data).

The first plot shows observed versus simulated plasma concentration, the second weighted residuals versus time. 

<a id="table-3-1"></a>

**Table 3-1: GMFE for Goodness of fit plot for concentration in plasma.**

|Group                                               |GMFE |
|:---------------------------------------------------|:----|
|Probenecid iv (model building)                      |1.27 |
|Probenecid oral administration (model building)     |1.30 |
|Probenecid oral administration (model verification) |1.38 |
|All                                                 |1.33 |

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

Simulated versus observed concentration-time profiles of all data listed in [Section 2.2.2](#222-clinical-data) are presented below.

### 3.3.1 Model Building<a id="331"></a>

<a id="figure-3-3"></a>

![](images/006_section_3/009_section_33/010_section_331/1_time_profile_plot_Probenecid_Dayton_1963___Subject_A_1860mg_i_v__s_d__1.png)

**Figure 3-3: Dayton 1963 - 1860 mg IV Subject A**

<br>
<br>

<a id="figure-3-4"></a>

![](images/006_section_3/009_section_33/010_section_331/2_time_profile_plot_Probenecid_Dayton_1963___Subject_B_1860mg_i_v__s_d__3.png)

**Figure 3-4: Dayton 1963 - 1860 mg IV Subject B**

<br>
<br>

<a id="figure-3-5"></a>

![](images/006_section_3/009_section_33/010_section_331/3_time_profile_plot_Probenecid_Dayton_1963___Subject_C_1860mg_i_v__s_d__5.png)

**Figure 3-5: Dayton 1963 - 1860 mg IV Subject C**

<br>
<br>

<a id="figure-3-6"></a>

![](images/006_section_3/009_section_33/010_section_331/4_time_profile_plot_Probenecid_Dayton_1963___Subject_D_1860mg_i_v__s_d__7.png)

**Figure 3-6: Dayton 1963 - 1860 mg IV Subject D**

<br>
<br>

<a id="figure-3-7"></a>

![](images/006_section_3/009_section_33/010_section_331/5_time_profile_plot_Probenecid_Dayton_1963___Subject_C_464_2mg_i_v__s_d__6.png)

**Figure 3-7: Dayton 1963 - 464.2 mg IV Subject C**

<br>
<br>

<a id="figure-3-8"></a>

![](images/006_section_3/009_section_33/010_section_331/7_time_profile_plot_Probenecid_Dayton_1963___Subject_E_1860mg_i_v__s_d__9.png)

**Figure 3-8: Dayton 1963 - 1860 mg IV Subject E**

<br>
<br>

<a id="figure-3-9"></a>

![](images/006_section_3/009_section_33/010_section_331/8_time_profile_plot_Probenecid_Dayton_1963___Subject_E_464_2mg_i_v__s_d__10.png)

**Figure 3-9: Dayton 1963 - 464.2 mg IV Subject E**

<br>
<br>

<a id="figure-3-10"></a>

![](images/006_section_3/009_section_33/010_section_331/9_time_profile_plot_Probenecid_Emanuelsson_1987_500mg_i_v__s_d__14.png)

**Figure 3-10: Emanuelsson 1987 - 500 mg iv**

<br>
<br>

<a id="figure-3-11"></a>

![](images/006_section_3/009_section_33/010_section_331/10_time_profile_plot_Probenecid_Landersdorfer_2009_500mg_p_o__b_i_d__21.png)

**Figure 3-11: Landersdorfer 2009 - 500 mg BID**

<br>
<br>

<a id="figure-3-12"></a>

![](images/006_section_3/009_section_33/010_section_331/13_time_profile_plot_Probenecid_Wiebe_2020_1000mg_p_o__b_i_d__6005.png)

**Figure 3-12: Wiebe 2020 - 1000 mg BID**

<br>
<br>

<a id="figure-3-13"></a>

![](images/006_section_3/009_section_33/010_section_331/17_time_profile_plot_Probenecid_Emanuelsson_1987_2000mg_p_o__s_d__13.png)

**Figure 3-13: Emanuelsson 1987 - 2000 mg po**

<br>
<br>

<a id="figure-3-14"></a>

![](images/006_section_3/009_section_33/010_section_331/19_time_profile_plot_Probenecid_Selen_1982_1000mg_p_o__s_d__29.png)

**Figure 3-14: Selen 1982 - 1000 mg po**

<br>
<br>

<a id="figure-3-15"></a>

![](images/006_section_3/009_section_33/010_section_331/20_time_profile_plot_Probenecid_Selen_1982_2000mg_p_o__s_d__30.png)

**Figure 3-15: Selen 1982 - 2000 mg po**

<br>
<br>

<a id="figure-3-16"></a>

![](images/006_section_3/009_section_33/010_section_331/21_time_profile_plot_Probenecid_Selen_1982_500mg_p_o__s_d__28.png)

**Figure 3-16: Selen 1982 - 500 mg po**

<br>
<br>

<a id="figure-3-17"></a>

![](images/006_section_3/009_section_33/010_section_331/22_time_profile_plot_Probenecid_Shen_2019_1000mg_p_o__s_d__5003.png)

**Figure 3-17: Shen 2019 - 1000 mg po**

<br>
<br>

<a id="figure-3-18"></a>

![](images/006_section_3/009_section_33/010_section_331/24_time_profile_plot_Probenecid_Vree_1992_1500mg_p_o__s_d__38_39.png)

**Figure 3-18: Vree 1992 - 1500 mg po**

<br>
<br>

<a id="figure-3-19"></a>

![](images/006_section_3/009_section_33/010_section_331/25_time_profile_plot_Probenecid_Vree_1992_250mg_p_o__s_d__32_33.png)

**Figure 3-19: Vree 1992 - 250 mg po**

<br>
<br>

### 3.3.2 Model Verification<a id="332"></a>

<a id="figure-3-20"></a>

![](images/006_section_3/009_section_33/011_section_332/6_time_profile_plot_Probenecid_Dayton_1963___Subject_D_464_2mg_i_v__s_d__8.png)

**Figure 3-20: Dayton 1963 - 464.2 mg IV Subject D - Probenecid - IV - 464.2 mg - Plasma - indiv.**

<br>
<br>

<a id="figure-3-21"></a>

![](images/006_section_3/009_section_33/011_section_332/11_time_profile_plot_Probenecid_Landersdorfer_2010_3000mg_p_o__m_d__50.png)

**Figure 3-21: Landersdorfer 2010 - 500-1000-500x3 mg**

<br>
<br>

<a id="figure-3-22"></a>

![](images/006_section_3/009_section_33/011_section_332/12_time_profile_plot_Probenecid_Smith_1980_1000mg_p_o__b_i_d__6002.png)

**Figure 3-22: Smith 1980a - 1000 mg BID**

<br>
<br>

<a id="figure-3-23"></a>

![](images/006_section_3/009_section_33/011_section_332/14_time_profile_plot_Probenecid_Dayton_1963___Subject_A_2000mg_p_o__s_d__2.png)

**Figure 3-23: Dayton 1963 - 2000 mg PO Subject A**

<br>
<br>

<a id="figure-3-24"></a>

![](images/006_section_3/009_section_33/011_section_332/15_time_profile_plot_Probenecid_Dayton_1963___Subject_B_2000mg_p_o__s_d__4.png)

**Figure 3-24: Dayton 1963 - 2000 mg PO Subject B**

<br>
<br>

<a id="figure-3-25"></a>

![](images/006_section_3/009_section_33/011_section_332/16_time_profile_plot_Probenecid_Emanuelsson_1987_1000mg_p_o__s_d__12.png)

**Figure 3-25: Emanuelsson 1987 - 1000 mg po**

<br>
<br>

<a id="figure-3-26"></a>

![](images/006_section_3/009_section_33/011_section_332/18_time_profile_plot_Probenecid_Emanuelsson_1987_500mg_p_o__s_d__11.png)

**Figure 3-26: Emanuelsson 1987 - 500 mg po**

<br>
<br>

<a id="figure-3-27"></a>

![](images/006_section_3/009_section_33/011_section_332/23_time_profile_plot_Probenecid_Vree_1992_1000mg_p_o__s_d__36_37.png)

**Figure 3-27: Vree 1992 - 1000 mg po**

<br>
<br>

<a id="figure-3-28"></a>

![](images/006_section_3/009_section_33/011_section_332/26_time_profile_plot_Probenecid_Vree_1992_500mg_p_o__s_d__34_35.png)

**Figure 3-28: Vree 1992 - 500 mg po**

<br>
<br>

<a id="figure-3-29"></a>

![](images/006_section_3/009_section_33/011_section_332/27_time_profile_plot_Probenecid_Vree_1993_1000mg_p_o__s_d__44_45.png)

**Figure 3-29: Vree 1993 - 1000 mg po**

<br>
<br>

# 4 Conclusion<a id="4"></a>

The presented PBPK model adequately describes the intravenous and oral pharmacokinetics of probenecid in adults.

# 5 References<a id="5"></a>

**Avdeef 2001** A. Avdeef. (2001). Physicochemical profiling (solubility, permeability and charge state). *Current Topics in Medicinal Chemistry*, *1*(4), 277-351.

**Avdeef 2003** A. Avdeef. (2003). Absorption and drug development - Solubility, permeability, and charge state.

**Dayton 1963** P.G. Dayton, T.F. Yu, W. Chen, L. Berger, L.A. West, and A.B. Gutman.  (1963). The physiological disposition of probenecid, including renal clearance, in man, studied by an improved method for its estimation in biological material. *The Journal of pharmacology and experimental therapeutics*, *140*, 278-286. 

**Emanuelsson 1987** B.M. Emanuelsson, B. Beermann, and L.K. Paalzow. (1987). w. Non-linear elimination and protein binding
of probenecid. *European Journal of Clinical Pharmacology*. *32*(4), 395-401.

**Hansch 1995** C. Hansch, A. Leo, and D. Hoekman (1995). Exploring QSAR: hydrophobic, electronic, steric constants.

**Ito 2014**  Y. Ito, T. Fukami, T. Yokoi, and M. Nakajima (2014).  An orphan esterase ABHD10 modulates probenecid acyl glucuronidation in human liver. *Drug Metabolism and Disposition*, *42*(12), 2109-2116.

**Izumi 2016** S. Izumi, Y. Nozaki, T. Komori, O. Takenaka, K. Maeda, H. Kusuhara, and Y. Sugiyama (2016). Investigation of fluorescein derivatives as substrates of organic anion transporting polypeptide (OATP) 1B1 to develop sensitive fluorescence-based OATP1B1 inhibition assays. *Molecular Pharmaceutics*, *13*(2), 438-448.

**Kuepfer 2016** Kuepfer L, Niederalt C, Wendl T, Schlender JF, Willmann S, Lippert J, Block M, Eissing T, Teutonico D. (2016). Applied Concepts in PBPK Modeling: How to Build a PBPK/PD Model. *CPT Pharmacometrics Syst Pharmacol*. Oct;5(10), 516-531.

**Landersdorfer 2009** C.B. Landersdorfer, C.M.J. Kirkpatrick, M. Kinzig, J.B. Bulitta, U. Holzgrabe, G.L. Drusano, and F. Sorgel. (2009). Competitive inhibition of renal tubular secretion of f gemifloxacin by probenecid. *Antimicrobial Agents and Chemotherapy*, *53*(9), 3902-3907.

**Landersdorfer 2010** C.B. Landersdorfer, C.M.J. Kirkpatrick, M. Kinzig, J.B. Bulitta, U. Holzgrabe, U. Jaehde, A. Reiter, K.G. NaberM. Rodamer and F. Sorgel. (2010). Competitive inhibition of renal tubular secretion of ciprofloxacin and metabolite by probenecid. *British journal of clinical pharmacology*, *69*(2), 167-78.

**Meyer 2012** Meyer M, Schneckener S, Ludewig B, Kuepfer L, Lippert J. (2012). Using expression data for quantification of active processes in physiologically based pharmacokinetic modeling. *Drug Metab Dispos*. May;40(5), 892-901.

**Nishimura 2003** Nishimura M, Yaguti H, Yoshitsugu H, Naito S, Satoh T. (2003). Tissue distribution of mRNA expression of human cytochrome P450 isoforms assessed by high-sensitivity real-time reverse transcription PCR. *Yakugaku Zasshi.* May;123(5), 369-75.

**Shen 2019** H. Shen, V.K. Holenarsipur, T.T. Mariappan, D.M. Drexler, J.L. Cantone, P. Rajanna, S. Singh Gautam, Y. Zhang, J. Gan, P.A. Shipkova, P. Marathe, and W.G. Humphreys. (2019). Evidence for the validity of pyridoxic acid (PDA) as a plasma-based endogenous probe for OAT1 and OAT3 function in healthy subjects. *Journal of Pharmacology and Experimental Therapeutics*, *368*(1), 136-145.

**Selen 1982** A. Selen, G.L. Amidon, and P.G. Wellingx. (1982). Pharmacokinetics of probenecid following oral doses to human volunteers. *Journal of Pharmaceutical Sciences*, *71*(11), 1238-1242.

**Smith 1980** D.E. Smith, W.L. Gee, D.C. Brater, E.T. Lin, and L.Z. Benet (1980). Preliminary evaluation of furosemide–probenecid interaction in humans. *Journal of Pharmaceutical Sciences*, *69*(5):571–75.

**Söderlind 2010** E. Söderlind, E. Karlsson, A. Carlsson, R. Kong, A. Lenz, S. Lindborg, and J.J. Sheng (2010). Simulating fasted human intestinal fluids: understanding the roles of lecithin and bile acids. *Molecular pharmaceutics*, *7*(5), 1498-1507.

**Tsuruya 2016** Y. Tsuruya, K. Kato, Y. Sano, Y. Imamura, K. Maeda, Y. Kumagai, Y. Sugiyama, and H. Kusuhara (2016). Investigation of endogenous compounds applicable to drug-drug interaction studies involving the renal organic anion transporters, OAT1 and OAT3, in humans, *Drug Metabolism and Disposition*, *44*(12), 1825-1933.

**Vree 1992** T.B. Vree, E.W. Van Ewijk-Beneken Kolmer, E.W. Wuis, and Y.A. Hekster.  (1992). Capacity-limited renal glucuronidation of probenecid by humans. A pilot Vmax-finding study. *Pharmaceutisch weekblad. Scientific edition*, *14*(5), 325-331.

**Vree 1993** T.B. Vree, E.W. Van Ewijk-Beneken Kolmer, E.W. Wuis, Y.A. Hekster, and M.M. Broekman (1993). Interindividual variation in the capacity-limited renal glucuronidation of probenecid by humans. *Pharmacy world & science : PWS*, *15*(5), 197-202.

**Wiebe 2020** S.T. Wiebe, T. Giessmann, K. Hohl, S. Schmidt-Gerets, E. Hauel, A. Jambrecina, K. Bader, N. Ishiguro, M.E. Taub, A. Sharma, T. Ebner, G. Mikus, M.F. Fromm, F. Müller, and P. Stopfer (2020). Validation of a drug transporter probe cocktail using the prototypical inhibitors rifampin, probenecid, verapamil, and cimetidine. *Clinical Pharmacokinetics*.

**Willmann 2007** Willmann S, Höhn K, Edginton A, Sevestre M, Solodenko J, Weiss W, Lippert J, Schmitt W. (2007). Development of a physiology-based whole-body population model for assessing the influence of individual variability on the pharmacokinetics of drugs. *J Pharmacokinet Pharmacodyn.* 34(3), 401-431.

**Wishart 2006** D.S. Wishart, C. Knox, A.C. Guo, S. Shrivastava, M. Hassanali, P. Stothard, Z. Chang, and J. Woolsey (2006). DrugBank: a comprehensive resource for in silico drug discovery and exploration. *Nucleic acids research*, *34*, D668-72.

