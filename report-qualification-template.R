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

  qualificationRunnerFolder <- normalizePath("QualificationRunner/QualificationRunner", winslash = "/")
  pkSimPortableFolder <- normalizePath("PK-Sim/PK-Sim", winslash = "/")
  pkSimPath <- file.path(pkSimPortableFolder, "PKSim.CLI.exe")
  
  qualificationProject <- modelsData$`Repository name`[modelIndex]
  modelName <- modelsData$`Snapshot name`[modelIndex]
  snapshotFile <- paste0(modelName, ".json")
  workingDirectory <- normalizePath(modelName, mustWork = FALSE, winslash = "/")
  # Clean up because of potential rebase
  unlink(workingDirectory, recursive = TRUE)
  
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
  file.copy(
    list.files("archive", pattern = qualificationProject, full.names = TRUE), 
    getwd(), 
    recursive = TRUE
    )
  warning(list.files())
  file.rename(from = list.files(pattern = qualificationProject), to = modelName)
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
  # Needs to be run from same directory as workflow.R
  setwd(dirname(qualificationPath))
  createQualificationReport(
    qualificationRunnerFolder = qualificationRunnerFolder,
    pkSimPortableFolder = pkSimPortableFolder,
    createWordReport = FALSE,
    versionInfo = versionInfo
  )
  # Include report only in the model folder
  # And clean up qualification
  setwd(workingDirectory)
  reportPaths <- list.files(pattern = "report.md", recursive = TRUE, full.names = TRUE, ignore.case = TRUE)
  copyReport(
    from = tail(reportPaths, 1), 
    to = paste0(modelName, "_evaluation_report.md"), 
    copyWordReport = FALSE
    )
  unlink(dirname(qualificationPath), recursive = TRUE)
  reportPath <- file.path(workingDirectory, paste0(modelName, "_evaluation_report.md"))
  warning(getwd())
  warning(reportPath)
  # Convert markdown to html and then to conversion
  setwd("..")
  knitr::pandoc(reportPath, paste("html", "--embed-resources", "--standalone", "-c \"osp.css\""))
  cmdLine <- paste(
    'chromehtml2pdf',
    paste0('--out="', gsub(pattern = ".md", ".pdf", reportPath), '"'),
    "--displayHeaderFooter true",
    "--format A4", "--marginTop 10mm", "--marginBottom 10mm", "--marginLeft 10mm", "--marginRight 10mm",
    # Header and footer templates are not well converted, leaving default footer so far 
    '--headerTemplate "<span></span>"',
    #'--footerTemplate "<span>Page <span class=\"pageNumber\"></span> / <span class=\"totalPages\"></span></span>"',
    paste0('"', gsub(pattern = ".md", ".html", reportPath), '"')
    )
  warning(cmdLine)
  system(cmdLine)

  # Use PKSim CLI to create project .pksim5
  cmdLine <- paste(
    pkSimPath,
    "snap",
    # Snapshot file <modelName>.json is in working directory
    "-i", workingDirectory,
    "-o", workingDirectory,
    "-p"
    )
  warning(cmdLine)
  system(cmdLine)
  # For next step, remove potential json from working directory
  unlink(file.path(workingDirectory, snapshotFile))
  additionalSnapshots <- ospsuite::toPathArray(modelsData$`Additional projects`[modelIndex])
  for(additionalSnapshot in additionalSnapshots){
    download.file(
      # Use Github raw.githubusercontent.com to download snapshot file
      file.path(
      "https://raw.githubusercontent.com/Open-Systems-Pharmacology", 
      additionalSnapshot
      ), 
      # Keep only the last name of the path (eg <model name>_Pediatrics.json)
      destfile = file.path(workingDirectory, basename(additionalSnapshot))
      )
    warning(cmdLine)
    system(cmdLine)
    unlink(file.path(workingDirectory, basename(additionalSnapshot)))
  }
  return(invisible())
}
