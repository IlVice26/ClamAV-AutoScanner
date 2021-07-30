pwd_local=$(pwd)

if [ -z $VIRTUAL_ENV ]
then 
    source $pwd_local/venv/bin/activate
fi

echo -e "\nVirtual environment activated:" $VIRTUAL_ENV "\n"

echo -n "Saving pip modules.. "
python3 -m pip freeze > requirements.txt -q
echo "OK"

echo -n "Downloading pip modules.. "
python3 -m pip download -r requirements.txt -d packages -q
echo "OK"

deactivate

echo -e "\nVirtual environment deactivated\n"