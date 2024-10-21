#!/usr/bin/bash

PROJECT_MAIN_DIR_NAME="Manhwa"

sudo cp "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/gunicorn/gunicorn.socket" "/etc/systemd/system/gunicorn.socket"
sudo cp "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/gunicorn/gunicorn.service" "/etc/systemd/system/gunicorn.service"

sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket