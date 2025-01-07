#' @title install_tools.R
#' @description
#' This script installs the necessary tools for Automated Evaluation Reports and Projects
#' @param tools.csv csv file describing the versions of software tools used to generate the reports
#' @author [Open Systems Pharmacology](https://github.com/Open-Systems-Pharmacology)

#' @description Install CRAN R packages
install.packages(c("dplyr", "purrr", "covr", "readr", "tidyr", "webshot", "spelling", "readxl", "data.table", "gridtext", "ggtext", "tidyselect", "testthat", "rmarkdown", "rsvg", "svglite", "cowplot"), repos = "http://cran.us.r-project.org", type = "win.binary")

toolsData <- read.csv("tools.csv", stringsAsFactors = FALSE, colClasses = "character")
print(toolsData)

#' @title installTool
#' @description
#' Install tool by tool name and version
#' TODO: this may be changed later on because newer versions of OSPSuite may rely on `{remotes}` package directly
#' @param toolName Identifier of the tool to install
#' @param toolsData data.frame mapping tool identifier and version
installTool <- function(toolName, toolsData = toolsData) {
  toolVersion <- toolsData$Version[toolsData$Tool %in% toolName]
  if (is.na(toolVersion)) {
    return()
  }
  toolPath <- switch(toolName,
    "ospsuite-R" = paste0(
      "https://github.com/Open-Systems-Pharmacology/OSPSuite-R/releases/download/v",
      toolVersion, "/ospsuite_", toolVersion, ".zip"
    ),
    "TLF" = paste0(
      "https://github.com/Open-Systems-Pharmacology/TLF-Library/releases/download/v",
      toolVersion, "/tlf_", toolVersion, ".zip"
    ),
    "RUtils" = paste0(
      "https://github.com/Open-Systems-Pharmacology/OSPSuite.RUtils/releases/download/v",
      toolVersion, "/ospsuite.utils_", toolVersion, ".zip"
    ),
    "rClr" = paste0(
      "https://github.com/Open-Systems-Pharmacology/rClr/releases/download/v",
      toolVersion, "/rClr_", toolVersion, ".zip"
    ),
    "rSharp" = paste0(
      "https://github.com/Open-Systems-Pharmacology/rSharp/releases/download/v",
      toolVersion, "/rSharp-v", toolVersion, "-Windows-r_4.4.0.zip"
    ),
    # Link not consistent across versions
    "Qualification Runner" = paste0(
      "https://github.com/Open-Systems-Pharmacology/QualificationRunner/releases/download/v",
      toolVersion, "/qualificationrunner-portable-setup", 
      switch(toolVersion, "10.0.59" = "", "11.0" = "_11.0.138", "11.1" = "_11.1.130"), ".zip"
    ),
    "Reporting Engine" = paste0(
      "https://github.com/Open-Systems-Pharmacology/OSPSuite.ReportingEngine/releases/download/v",
      toolVersion, "/ospsuite.reportingengine_", toolVersion, ".zip"
    ),
    "PK-Sim" = paste0(
      "https://github.com/Open-Systems-Pharmacology/PK-Sim/releases/download/v",
      toolVersion, "/pk-sim-portable-setup.zip"
    )
  )
  archiveName <- switch(toolName,
    "ospsuite-R" = "ospsuite",
    "TLF" = "tlf",
    "RUtils" = "ospsuite.utils",
    "rClr" = "rClr",
    "rSharp" = "rsharp",
    "Reporting Engine" = "ospsuite.reportingengine",
    "Qualification Runner" = "qualificationrunner",
    "PK-Sim" = "pk-sim"
  )
  toolArchive <- paste0(archiveName, ".zip")
  # If archive is an R package
  if (toolName %in% c("ospsuite-R", "TLF", "RUtils", "rClr", "rSharp", "Reporting Engine")) {
    download.file(toolPath, destfile = toolArchive, mode = "wb")
    if (toolName %in% "rSharp") {
      unzip(toolArchive)
      unlink(toolArchive)
      toolArchive <- list.files(pattern = "rSharp.*\\.zip")
    }
    install.packages(toolArchive, repos = NULL, type = "binary")
    unlink(toolArchive)
    print(paste(toolName, "version", toolVersion, "installed"))
    return()
  }
  download.file(toolPath, destfile = toolArchive)
  exdir <- switch(toolName,
    "Qualification Runner" = "QualificationRunner",
    "PK-Sim" = "PK-Sim"
  )
  unzip(toolArchive, exdir = exdir)
  unlink(toolArchive)
  file.rename(
    from = list.files(exdir, full.names = TRUE),
    to = file.path(exdir, exdir)
  )
  print(paste(toolName, "version", toolVersion, "installed"))
  return()
}

toInstall <- c(
  # R Packages
  "RUtils", "rClr", "rSharp", "TLF", "ospsuite-R", "Reporting Engine", 
  # Qualification Framework
  "Qualification Runner", "PK-Sim"
  )
for(toolName in toInstall){
  installTool(toolName, toolsData)
}
