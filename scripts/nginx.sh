#!/usr/bin/bash

PROJECT_MAIN_DIR_NAME="Manhwa"

sudo rm -f /etc/nginx/sites-enabled/default

sudo cp "/home/ubuntu/ngnix/$PROJECT_MAIN_DIR_NAME" "/etc/nginx/sites-available/$PROJECT_MAIN_DIR_NAME"
sudo ln -s /etc/nginx/sites-available/$PROJECT_MAIN_DIR_NAME /etc/nginx/sites-enabled/

#sudo unlink /etc/nginx/sites-enabled/default
sudo gpasswd -a www-data ubuntu