@echo off

bitsadmin /transfer mydownloadjob /download /priority FOREGROUND %1 %2
