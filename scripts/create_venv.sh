#!/bin/sh

sudo apt install python3-venv
sudo apt install python3-pip

mkdir ~/t_gauge_automation
cd ~/t_gauge_automation || exit 1

python3 -m venv venv

.venv/bin/activate

python3 -m pip install -r requirements.txt
