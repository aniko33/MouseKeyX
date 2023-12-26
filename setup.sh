#!/bin/sh

echo Installing pystray
pip install pystray --break-system-package

echo Adding mousekeyx.desktop into .config/autostart
cp resource/mousekeyx.desktop ~/.config/autostart

echo Copy folder into /opt
sudo cp -r . /opt/mousekeyx

echo Adding command: mousekeyx
sudo cp resource/mousekeyx /usr/bin
sudo chmod +x /usr/bin/mousekeyx

echo Running...
nohup python /opt/mousekeyx/main.py > /dev/null 2>&1&