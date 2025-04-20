#!/bin/bash

# Allow running as: ./run.sh rabbits
export PYTHONPATH="$(dirname "$0")/src:$PYTHONPATH"

python3 src/main.py "$@"
