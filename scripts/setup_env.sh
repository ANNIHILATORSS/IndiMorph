#!/bin/bash
set -e
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
# Install TFLite for Jetson/RPi if needed
if [[ $(uname -m) == "aarch64" ]]; then
  pip install tflite-runtime
fi
# Unity plugins (placeholder)
echo "Install Unity plugins manually in unity_project/ if needed."
echo "Environment setup complete." 