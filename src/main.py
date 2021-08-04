"""
Main - ClamAV AutoScanner

Author: Elia Vicentini <eliavicentini26@gmail.com>
"""

import os
import sys
import json
import pyudev
import requests
import argparse


__VERSION__ = "alpha 0.1"


def enumerate_devices():
    """
    Returns a list of devices connected to the PC
    """

    return set([item for item in pyudev.Context().list_devices(subsystem='block', DEVTYPE='partition')])


def check_usb_device():
    """
    Check if the device is a USB stick
    """

    for device in enumerate_devices():
        if device.get('ID_BUS') == 'usb':
            print(device.get('DEVNAME') + " | " + device.get('ID_FS_TYPE'))


def download_config_file():
    """
    Download from the project's Github repository the updated 
    program configuration file
    """

    req = requests.get('https://raw.githubusercontent.com/IlVice26/ClamAV-AutoScanner/dev/src/config/config.json')

    if req.ok:
        open('src/config/config.json', 'wb').write(req.content)
    else:
        print("The requested file 'config.json' could not be downloaded") if args.verbose else ""


def check_os():
    """
    Checks which operating system the program runs on
    """

    if not sys.platform in program_config['OS']['OS_SUPPORTED']:
        print("\nYour operating system is not officially supported by " + 
            "ClamAV-AutoScanner. Please keep yourself updated about possible updates.")
        sys.exit(-1)

    print("\nOS Check Passed")


def load_config():
    """
    Load the program configuration file
    """

    config_file = 'src/config/config.json'  # config.json path

    download_config_file()  # Download the latest version of the config file

    if os.path.exists(config_file):
        print("Found a local 'config.json' file. It will be used until " + 
            "the program is restarted. \nThe file 'config.json' has been loaded correctly")
        return json.load(open(config_file, 'r'))
    else:
        print("Error loading config.json file") if args.verbose else ""


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="ClamAV - AutoScanner")
    parser.add_argument("-v", "--verbose", 
                        action="store_true", 
                        help="View logs on screen")

    args = parser.parse_args()

    print("Program version: " + __VERSION__ + "\n") if args.verbose else ""
    
    # Initial operations
    program_config = load_config()    
    check_os()
