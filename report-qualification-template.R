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
  ospsuite::clearMemory(clearSimulationsCache = TRUE)

  qualificationProject <- modelsData$`Repository name`[modelIndex]
  modelName <- modelsData$`Snapshot name`[modelIndex]
  snapshotFile <- paste0(modelName, ".json")
  workingDirectory <- normalizePath(qualificationProject, mustWork = FALSE, winslash = "/")
  versionInfo <- QualificationVersionInfo$new(
    modelsData$`Released version`[modelIndex],
    paste(head(unlist(strsplit(toolsData$Version[toolsData$Tool %in% "PK-Sim"], "\\.")), 2), collapse = "."),
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
  file.copy(
    list.files("archive", pattern = qualificationProject), 
    workingDirectory, 
    recursive = TRUE
    )
  unlink("archive", recursive = TRUE)
  
  #' @description Use Workflow name to run the qualification
  setwd(workingDirectory)
  qualificationPath <- ifelse(
    modelsData$`Workflow name`[modelIndex] %in% "",
    # If note specified, use default evaluation/workflow.R
    list.files(recursive = TRUE, pattern = "workflow.R", full.names = TRUE, ignore.case = TRUE),
    modelsData$`Workflow name`[modelIndex]
  )
    
  source(qualificationPath)
  createQualificationReport(
    qualificationRunnerFolder = "QualificationRunner/QualificationRunner",
    pkSimPortableFolder = "PK-Sim/PK-Sim",
    createWordReport = FALSE,
    versionInfo = versionInfo
  )
  reportPath <- list.files(recursive = TRUE, pattern = "report.md", full.names = TRUE, ignore.case = TRUE)
  
  # Copy logs to get final run time on reports
  file.copy(
    from = list.files(recursive = TRUE, pattern = "log-info", full.names = TRUE, ignore.case = TRUE),
    to = dirname(reportPath),
    overwrite = TRUE
  )

  # Convert markdown to html and then to conversion
  knitr::pandoc(reportPath, paste("html", "--embed-resources", "--standalone", "-c \"osp.css\""))
  cmdLine <- paste(
    'chromehtml2pdf',
    paste0('--out="', normalizePath(gsub(pattern = ".md", ".pdf", reportPath), mustWork = FALSE), '"'),
    "--displayHeaderFooter true",
    "--format A4", "--marginTop 10mm", "--marginBottom 10mm", "--marginLeft 10mm", "--marginRight 10mm",
    # Header and footer templates are not well converted, leaving default footer so far 
    '--headerTemplate "<span></span>"',
    #'--footerTemplate "<span>Page <span class=\"pageNumber\"></span> / <span class=\"totalPages\"></span></span>"',
    paste0('"', normalizePath(gsub(pattern = ".md", ".html", reportPath)), '"')
    )
  system(cmdLine)

  # Use PKSim CLI to create project named report-configuration-plan.pksim5 by default
  pkSimPath <- normalizePath("PK-Sim/PK-Sim/PKSim.CLI.exe", mustWork = FALSE)
  cmdLine <- paste(
    pkSimPath,
    "snap",
    # Snapshot file <modelName>.json is in working directory
    "-i", workingDirectory,
    "-o", workingDirectory,
    "-p"
    )
  system(cmdLine)
  # For next step, remove potential json from working directory
  unlink(file.path(workingDirectory, snapshotFile))
  additionalSnapshots <- ospsuite::toPathArray(modelsData$`Additional projects`[modelIndex])
  for(additionalSnapshot in additionalSnapshots){
    download.file(
      # Use Github raw.githubusercontent.com to download snapshot file
      file.path(
      "https://raw.githubusercontent.com/Open-Systems-Pharmacology/", 
      additionalSnapshot
      ), 
      # Keep only the last name of the path (eg <model name>_Pediatrics.json)
      destfile = basename(additionalSnapshot)
      )
    system(cmdLine)
    unlink(file.path(workingDirectory, basename(additionalSnapshot)))
  }
  return(invisible())
  
}
