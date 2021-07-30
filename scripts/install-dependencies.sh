#!/bin/bash

if [ -z $VIRTUAL_ENV ]
then
    pwd_local=$(pwd)
    source $pwd_local/venv/bin/activate
fi

echo -e "\nVirtual environment activated:" $VIRTUAL_ENV "\n"

echo -n "Installing dependencies.. "
python3 -m pip install --no-index --find-links=packages -r requirements.txt -q
echo "OK"

deactivate
echo -e "\nVirtual environment deactivated\n"