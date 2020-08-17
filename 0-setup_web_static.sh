#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "simple content, to test your Nginx configuration" | sudo tee /data/web_static/releases/test/index.html
ln -sf  /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
content="location /hbnb_static/ {\nalias /data/web_static/current;\n}"
echo "$content" | sudo tee -a /etc/nginx/sites-enabled/default
sudo service nginx restart
