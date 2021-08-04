#!/bin/bash

# Virtualenv activation
if [ -z $VIRTUAL_ENV ]
then
    pwd_local=$(pwd)
    source $pwd_local/venv/bin/activate
fi

# Arguments to be used with the program
verbose=""
while getopts "vrd" flag
do
    case "${flag}" in
        v) verbose="-v";;
        r) rewrite="-r";;
        d) development="-d"
    esac
done

# Check if the verbose argument is used
if [[ $verbose != "-v" ]]
then

    # Main program call
    python3 -B src/main.py $verbose $rewrite $development

    deactivate
else
    echo -e "\nVirtual environment activated:" $VIRTUAL_ENV 
    echo -e "Arguments: $verbose $rewrite $development\n"
 
    # Main program call
    python3 -B src/main.py $verbose $rewrite $development

    # Virtualenv deactivation
    deactivate  
    echo -e "\nVirtual environment deactivated\n" 
fi
