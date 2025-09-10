#!/bin/bash

python3 -m venv .venv

# shellcheck disable=SC1091
source .venv/bin/activate

python3 -m pip install -r requirements.txt
