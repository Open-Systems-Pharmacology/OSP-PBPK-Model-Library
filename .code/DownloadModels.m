function DownloadModels
    modelNames = GetModelNames;
    
    for i=1:length(modelNames)
        modelName = modelNames{i};
        try
            disp(sprintf('===================== Downloading "%s" ===================== \n', modelName));
            DownloadReleasedModel(modelName);
        catch
            disp(sprintf('ERROR downloading model %s\n', modelName));
        end
    end
end

function DownloadReleasedModel(modelName)

    % e.g. Alfentanil-Model-2.2 ==> https://github.com/Open-Systems-Pharmacology/Alfentanil-Model/archive/refs/tags/v2.2.zip
    url = ['https://github.com/Open-Systems-Pharmacology/' strrep(modelName, '-Model-', '-Model/archive/refs/tags/v') '.zip'];
    target = [pwd filesep modelName '.zip'];
    %websave([modelName '.zip'], url); %fails due to some certificate problems
    
    if exist(modelName, 'dir')
        [status, message] = rmdir(modelName, 's');
        if status~=1 
            error('Cannot remove directory "%s": %s\n', modelName, message); 
        end
    end
    
    if exist(target, 'file')
        delete(target);
    end
    
    for attempt = 1:10
        [status, message] = system([pwd filesep 'DownloadFile.bat "' url '" "' target '"']);
        if status==0 
            break;
        end
    end
    
    if status~=0 
        error('Download of "%s" failed: %s\n', url, message); 
    end
    
    unzip(target);
end