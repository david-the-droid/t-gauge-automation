#!/bin/sh

sudo apt install python3-venv
sudo apt install python3-pip

mkdir ~/t_gauge_automation && cd ~/t_gauge_automation

python3 -m venv venv

source .venv/bin/activate

python3 -m pip install -r requirements.txt
