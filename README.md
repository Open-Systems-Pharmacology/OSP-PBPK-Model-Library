# OSP-PBPK-Model-Library

Library of released PBPK substance models and evaluation reports

## How to create evaluation reports

- Create a new branch from the `create-reports` branch (for instance, `my-reports`)
  - Define the appropriate OSP environment and tools by updating `tools.csv`
  - Define the models and projects by updating `models.csv`
  - Go to the Github Action: [Automated Evaluation Reports and Projects](https://github.com/Open-Systems-Pharmacology/OSP-PBPK-Model-Library/actions/workflows/create-reports.yaml)
    - Click on the button __Run workflow__ 
      - Select your branch (for instance, `my-reports`)
      - Click on the green button __Run workflow__ 
  
## What to do when reports are created

When the evaluation reports are created, a pull request is triggered toward the `develop` branch.
The pull request will allow users to review the updates in the reports and adopt the new version.

