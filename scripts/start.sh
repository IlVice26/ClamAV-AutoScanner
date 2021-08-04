#!/bin/bash

# Virtualenv activation
if [ -z $VIRTUAL_ENV ]
then
    pwd_local=$(pwd)
    source $pwd_local/venv/bin/activate
fi

# Arguments to be used with the program
verbose=""
while getopts "vr" flag
do
    case "${flag}" in
        v) verbose="-v";;
        r) rewrite="-r"
    esac
done

# Check if the verbose argument is used
if [[ $verbose != "-v" ]]
then

    if [[ $rewrite != "-r" ]]
    then
        # Main program call
        python3 -B src/main.py -r
    else
        python3 -B src/main.py
    fi

    # Virtualenv deactivation
    deactivate
else
    echo -e "\nVirtual environment activated:" $VIRTUAL_ENV 
    echo -e "Arguments: $verbose $rewrite\n"
 
    # Main program call
    if [[ $rewrite != "-r" ]]
    then
        python3 -B src/main.py $verbose 
    else
        python3 -B src/main.py $verbose $rewrite
    fi

    # Virtualenv deactivation
    deactivate  
    echo -e "\nVirtual environment deactivated\n" 
fi
