#!/bin/sh
python3 -m venv virtual_env
source virtual_env/bin/activate
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "env is active!"
else
    echo "env is not active!"
fi
pip install -r requirements.txt
