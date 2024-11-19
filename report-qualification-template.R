#' @title report-qualification-template
#' @description
#' Function that evaluates a model and generate its Qualification Report
#' for `Open-Systems-Pharmacology/` sub-repository
#' @param modelIndex Index of model to run
#' @param modelsData data.frame defining input data of models
#' @param toolsData data.frame defining tools used to evaluate models and generate reports
runEvaluationReport <- function(modelIndex, modelsData, toolsData) {
  if (!modelsData$Execute[modelIndex]) {
    return()
  }
  library(ospsuite.reportingengine)

  qualificationProject <- modelsData$`Repository name`[modelIndex]
  snapshotFile <- paste0(modelsData$`Snapshot name`[modelIndex], ".json")
  workingDirectory <- normalizePath(qualificationProject, mustWork = FALSE, winslash = "/")
  qualificationRunnerFolder <- "QualificationRunner/QualificationRunner"
  pkSimPortableFolder <- "PK-Sim/PK-Sim"
  versionInfo <- QualificationVersionInfo$new(
    "1.0",
    toolsData$Version[toolsData$Tool %in% "OSP Suite"],
    toolsData$Version[toolsData$Tool %in% "Qualification Framework"]
  )

  # Load repository content and clean up downloads
  download.file(
    paste0(
      "https://github.com/Open-Systems-Pharmacology/",
      qualificationProject,
      "/archive/refs/tags/v",
      modelsData$`Released version`[modelIndex], ".zip"
    ),
    destfile = "archive.zip"
  )
  unzip("archive.zip", exdir = "archive")
  unlink("archive.zip")
  dir.create(workingDirectory)
  projectFolder <- list.files("archive", pattern = qualificationProject)
  file.copy(file.path("archive", projectFolder, "Evaluation", "Input"), workingDirectory, recursive = TRUE)
  # In this repo, the snapshot is outside the evaluation folder and its path needs to be updated
  file.copy(file.path("archive", projectFolder, snapshotFile), workingDirectory, recursive = TRUE)
  unlink("archive", recursive = TRUE)
  
  #' @description Code hereafter is adapted from `createQualificationReport()` template
  qualificationPlanName <- "evaluation_plan.json"
  qualificationPlanFile <- file.path(workingDirectory, "input", qualificationPlanName)
  jsonContent <- readLines(qualificationPlanFile)
  jsonContent <- gsub(pattern = paste0("../", snapshotFile), replacement = snapshotFile, x = jsonContent)
  writeLines(jsonContent, qualificationPlanFile)

  #' The default outputs of qualification runner should be generated under `<workingDirectory>/re_input`
  reInputFolder <- file.path(workingDirectory, "re_input")
  #' The default outputs or RE should be generated under `<workingDirectory>/re_output`
  reOutputFolder <- file.path(workingDirectory, "re_output")

  #' Configuration Plan created from the Qualification Plan by the Qualification Runner
  configurationPlanName <- "report-configuration-plan"
  configurationPlanFile <- file.path(reInputFolder, paste0(configurationPlanName, ".json"))

  #' Set watermark that will appear in all generated plots
  #' Default is no watermark. `Label` objects from `tlf` package can be used to specify watermark font.
  watermark <- "draft"

  #' If not set, report created will be named `report.md` and located in the workflow folder namely `reOutputFolder`
  #' Here, the report will be copied in the test reports at the end of the workflow
  reportFolder <- qualificationProject
  reportPath <- file.path(reportFolder, "Report.md")

  #' @description Start **Qualification Runner** to generate inputs for the reporting engine
  #' @param logFile If not `null` is passed internally via the `-l` option
  logFile <- NULL
  #' @param logLevel If not `null` is passed internally via the `--logLevel` option
  logLevel <- NULL
  #' @param overwrite If `true`, eventual results from the previous run of the QualiRunner/RE will be removed first
  overwrite <- TRUE

  startQualificationRunner(
    qualificationRunnerFolder = qualificationRunnerFolder,
    qualificationPlanFile = qualificationPlanFile,
    outputFolder = reInputFolder,
    pkSimPortableFolder = pkSimPortableFolder,
    configurationPlanName = configurationPlanName,
    overwrite = overwrite,
    logFile = logFile,
    logLevel = logLevel
  )

  #' @description Run Qualification Workflow to generate inputs for the reporting engine
  titlePageFile <- file.path(reInputFolder, "Intro/titlepage.md")
  addTitlePage <- all(
    !is.null(versionInfo),
    file.exists(titlePageFile)
  )
  if (addTitlePage) {
    adjustTitlePage(titlePageFile, qualificationVersionInfo = versionInfo)
  }

  #' Load `QualificationWorkflow` object from configuration plan
  workflow <- loadQualificationWorkflow(
    workflowFolder = reOutputFolder,
    configurationPlanFile = configurationPlanFile
  )

  #' Set the name of the final report
  workflow$reportFilePath <- reportPath
  #' Do not export word report
  workflow$createWordReport <- FALSE

  #' Set watermark. If set, it will appear in all generated plots
  workflow$setWatermark(watermark)

  #' Run the `QualificationWorklfow`
  workflow$runWorkflow()

  # Copy logs to get final run time on reports
  file.copy(
    from = file.path(reOutputFolder, "log-info.txt"),
    to = reportFolder,
    overwrite = TRUE
  )
}
