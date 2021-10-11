# Run all / selected model evaluation reports in Matlab 2017b

## Prerequisites
* OSP Suite 10 is installed
* All components of the [Qualification Framework 2.3](https://github.com/Open-Systems-Pharmacology/QualificationPlan/releases/tag/v2.3) are installed

## Step 1: preparation
* Fill model names and versions in `GetModelNames.m`
* Fill your environment properties in `QualificationEnvironment.m`

## Step 2: download model snapshots and evaluation plans

Execute `DownloadModels.m`. This will download and unzip released versions of the model repositories given by `GetModelNames.m`

E.g. *Alfentanil-Model-2.2* will download the release 2.2 of Alfentanil-Model from <br>https://github.com/Open-Systems-Pharmacology/Alfentanil-Model/releases/tag/v2.2

## Step 3: Create evaluation reports

Execute `runModelEvaluationReports.m`. 

This will automatically update the title page and create all selected model evaluation reports in Markdown format.