#!/usr/bin/env bash
# This script sets up the web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Hello From Holberton!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
serve_content="location /hbnb_static {\n alias /data/web_static/current/;\n}\n"
sudo sed -i "52i\ $serve_content" /etc/nginx/sites-available/default
sudo service nginx restart
