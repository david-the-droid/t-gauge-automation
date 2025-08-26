#!/bin/sh

python3 -m venv venv

echo "Contents are: $(ls -l)"

.venv/bin/activate

python3 -m pip install -r requirements.txt
