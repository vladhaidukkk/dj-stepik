default: fmt fix

# Project management commands
start-project name dir:
    -@mkdir {{dir}} &> /dev/null
    uv run django-admin startproject {{name}} {{dir}}

project_dir := "project"

manage command *params:
    cd ./{{project_dir}} && uv run manage.py {{command}} {{params}}

start-app name:
    @just manage startapp {{name}}

# Startup commands
shell:
    @just manage shell_plus --ipython --print-sql

serve port="8000":
    @just manage runserver {{port}}

# Migrations management commands
make-migrations app="":
    @just manage makemigrations {{app}}

show-sql app name="":
    @just manage sqlmigrate {{app}} {{name}}

migrate app="" name="":
    @just manage migrate {{app}} {{name}}

# Code quality commands
fmt:
    uv run ruff format
    uv run djlint ./{{project_dir}} --reformat --quiet

check-fmt:
    uv run ruff format --check
    uv run djlint ./{{project_dir}} --check

lint:
    uv run ruff check
    uv run djlint ./{{project_dir}} --lint

fix:
    uv run ruff check --fix
