function runModelEvaluationReports
    tic
    
    modelNames = GetModelNames;
    failedModels = {};
    
    UpdateTitlePages(modelNames);
    
    for i=1:length(modelNames)
        modelName = modelNames{i};
        
        [success, errorMsg] = createModelReport(modelName);
        if success == 0
            failedModels{end+1} = sprintf('%s: %s', modelName, errorMsg); %#ok<AGROW>
        end
    end

    fprintf('===================== FINISHED ===================== \n\n');

    if isempty(failedModels)
        disp('ALL MODEL EVALUATION REPORTS CREATED SUCCESSFULLY');
    else
        disp('SOME MODELS FAILED:');
        disp(failedModels');
    end
        
    toc
end

function UpdateTitlePages(modelNames)
    env = QualificationEnvironment;
    
    for i=1:length(modelNames)
        modelVersion = getModelVersion(modelNames{i});
        UpdateTitlePage([pwd filesep 'Input' filesep 'Content' filesep 'titlepage.md'], modelVersion, env.OSPVersion, env.QualificationFrameworkVersion);
    end
end

function [success, errorMsg] = createModelReport(modelName)
    errorMsg = '';
    
	basisDir = fileparts(which('runModelEvaluationReports'));
    addpath(basisDir);
    
    env = QualificationEnvironment;
    addpath(genpath(env.ReportingEnginePath));

    OSPVersion = env.OSPVersion;
    qualificationFrameworkVersion = env.QualificationFrameworkVersion;
	
	try
        fprintf('===================== Creating model report for "%s" ===================== \n\n', modelName);
		cd([basisDir filesep modelName filesep 'Evaluation']);
                
        [success, message] = copyfile([basisDir filesep 'Workflow.m'], [pwd filesep 'Workflow.m'], 'f');
        if success ~= 1
            error('Could no copy Workflow.m: %s\n', message);
        end
        
		Workflow
        
        renameReport([pwd filesep 'report' filesep 'markdown_for_github'], modelName);
        renameReport([pwd filesep 'report' filesep 'markdown_for_pdf'], modelName);
        
        success = 1;
    catch ME
        success = 0;
        errorMsg = sprintf('ERROR creating report for %s: %s\n', modelName, ME.message);
		disp(errorMsg);
	end
	
	cd(basisDir);
end

function UpdateTitlePage(titlePageFile, modelVersion, OSPVersion, qualificationFrameworkVersion)
    text = fileread(titlePageFile);
    
    text = strrep(text, 'x.x', modelVersion);
    text = strrep(text, 'y.y', OSPVersion);
    text = strrep(text, 'z.z', qualificationFrameworkVersion);
    
    [fid, message] = fopen(titlePageFile,'wt');
    if fid == -1
        error('Cannot update %s: %s\n', titlePageFile, message);
    end
    
    fprintf(fid, text);
    fclose(fid);
end
    
function renameReport(reportFolder, modelName)
    system(['RENAME "' reportFolder filesep 'report.md" "' getModelNameWithoutVersion(modelName) '_evaluation_report.md"']);
%    movefile([reportFolder filesep 'report.md'], [reportFolder filesep getModelNameWithoutVersion(modelName) '_evaluation_report.md']);
%    %movefile corrupts it!
end

function modelVersion = getModelVersion(modelName)
    %modelName looks like 'Alfentanil-Model-2.2'
    modelVersion = modelName(strfind(modelName, '-Model-')+7:end);
end

function modelNameWithoutVersion = getModelNameWithoutVersion(modelName)
    modelNameWithoutVersion = modelName(1:strfind(modelName, '-Model-')-1);
end
