pwd_local=$(pwd)
source $pwd_local/venv/bin/activate

echo -e "\nVirtual environment activated:" $VIRTUAL_ENV "\n" 

python3 src/main.py
deactivate

echo -e "\nVirtual environment deactivated\n" 