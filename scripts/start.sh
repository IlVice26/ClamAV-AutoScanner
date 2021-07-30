#!/bin/bash

# Virtualenv activation
if [ -z $VIRTUAL_ENV ]
then
    pwd_local=$(pwd)
    source $pwd_local/venv/bin/activate
fi

# Arguments to be used with the program
verbose=""
while getopts v flag
do
    case "${flag}" in
        v) verbose="-v"
    esac
done

# Check if the verbose argument is used
if [[ $verbose != "-v" ]]
then
    # Main program call
    python3 src/main.py

    # Virtualenv deactivation
    deactivate
else
    echo -e "\nVirtual environment activated:" $VIRTUAL_ENV 
    echo -e "Argument: $verbose \n"
 
    # Main program call
    python3 src/main.py $verbose

    # Virtualenv deactivation
    deactivate  
    echo -e "\nVirtual environment deactivated\n" 
fi
