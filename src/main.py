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
import subprocess

import cas_logger


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
            cas_logger.log(device.get('DEVNAME')
                  + " | "
                  + device.get('ID_FS_TYPE'), args.verbose, "INFO")


def download_config_file():
    """
    Download from the project's Github repository the updated 
    program configuration file
    """

    req = requests.get(
        'https://raw.githubusercontent.com/IlVice26/ClamAV-AutoScanner/dev/src/config/config.json')

    if req.ok:
        open('src/config/config.json', 'wb').write(req.content)
        cas_logger.log("The requested file 'config.json' has been successfully downloaded", args.verbose, "INFO")
    else:
        cas_logger.log("The requested file 'config.json' could not be downloaded", args.verbose, "WARNING")


def load_config(development=False):
    """
    Load the program configuration file
    """

    config_file = 'src/config/config.json'  # config.json path

    if not development:
        download_config_file()  # Download the latest version of the config file

    if os.path.exists(config_file):
        cas_logger.log("The file 'config.json' has been loaded correctly", args.verbose, "INFO")
        return json.load(open(config_file, 'r'))
    else:
        cas_logger.log("Error loading config.json file", args.verbose, "ERROR") 


def check_os():
    """
    Checks which operating system the program runs on
    """

    if not sys.platform in program_config['OS']['OS_SUPPORTED']:
        cas_logger.log("Your operating system is not officially supported by " 
                    + "ClamAV-AutoScanner. Please keep yourself updated about possible updates.", 
                    args.verbose, "ERROR")
        sys.exit(-1)

    cas_logger.log("OS check passed", args.verbose, "INFO")


def check_clamav():
    """
    Check if ClamAV is installed correctly
    """

    cmd_to_check = ['freshclam', 'clamscan']

    for cmd in cmd_to_check:
        output = subprocess.Popen(['whereis', cmd], stdout=subprocess.PIPE)
        
        if not len(str(output.stdout.read()).split(" ")) > 1:
            cas_logger.log("The program {} was not found. Try reinstalling ClamAV.". format(cmd),
            args.verbose,
            "ERROR")
            sys.exit(-1)
        else:
            cas_logger.log("{} installed".format(cmd),
            False,
            "INFO")
    
    cas_logger.log("ClamAV executable check passed\n", args.verbose, "INFO")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="ClamAV - AutoScanner")
    parser.add_argument("-v", "--verbose",
                        action="store_true",
                        help="View logs on screen")
    parser.add_argument("-r", "--rewrite",
                        action="store_true",
                        help="Rewrite today log file")
    parser.add_argument("-d", "--development",
                        action="store_true",
                        help="Start the program in the development environment")

    args = parser.parse_args()

    cas_logger.print_timestamp(args.rewrite)

    cas_logger.log("Program version: " + __VERSION__, args.verbose, "INFO")

    # Initial operations
    program_config = load_config(args.development)
    check_os()
    check_clamav()

    #check_usb_device()
