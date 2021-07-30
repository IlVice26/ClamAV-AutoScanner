#!/bin/bash

# Virtualenv activation
if [ -z $VIRTUAL_ENV ]
then
    pwd_local=$(pwd)
    source $pwd_local/venv/bin/activate
fi

echo -e "\nVirtual environment activated:" $VIRTUAL_ENV "\n"

echo -n "Saving python modules list.. "
python3 -m pip freeze > requirements.txt -q
echo "OK"

echo -n "Downloading and saving python modules.. "
python3 -m pip download -r requirements.txt -d packages -q
echo "OK"

# Virtualenv deactivation
deactivate
echo -e "\nVirtual environment deactivated\n"