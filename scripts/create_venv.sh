#!/bin/bash

python3 -m venv .venv

echo "Contents are: $(ls -l)"

source .venv/bin/activate

python3 -m pip install -r requirements.txt
