#!/bin/bash

BASEPATH="${1:-/}"
python3 src/main.py "$BASEPATH"
cd docs && python3 -m http.server 8888
cd ..
