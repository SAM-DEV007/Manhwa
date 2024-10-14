#!/bin/bash
set -e

GIT_REPO_URL="https://github.com/SAM-DEV007/Manhwa.git"

PROJECT_MAIN_DIR_NAME="Manhwa"

git clone "$GIT_REPO_URL" "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

cd "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

# Hidden environment variables

chmod +x scripts/*.sh

./scripts/instance_os_dependencies.sh
./scripts/python_dependencies.sh
./scripts/gunicorn.sh
./scripts/start_app.sh