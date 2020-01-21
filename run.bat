@echo off
if "%~1" == "" (
    docker run -it -p 5000:5000 max-skeleton-dev:latest  
) else (
    docker run -it  -p 5000:5000 max-skeleton-dev:latest /bin/bash
)
