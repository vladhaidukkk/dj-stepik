start-project name dir:
    -@mkdir {{dir}} &> /dev/null
    uv run django-admin startproject {{name}} {{dir}}

project_dir := "project"

manage command *params:
    cd ./{{project_dir}} && uv run manage.py {{command}} {{params}}

start-app name:
    @just manage startapp {{name}}
