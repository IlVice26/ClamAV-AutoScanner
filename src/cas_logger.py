"""
ClamAV AutoScanner Logger - ClamAV AutoScanner

Author: Elia Vicentini <eliavicentini26@gmail.com>
"""

import os
import time
import logging
import datetime


timestamp_logs = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H-%M-%S') 
timestamp_file = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')


def print_timestamp(rewrite=False):
    """
    Print the timestamp at the beginning of the program 
    and set the logging library.

    By default, when the program starts, it does not rewrite
    the log file of the same day, but you can set
    the rewriting of the file using the -r flag at program startup
    """

    # Check if the logs folder is present
    if not os.path.exists('logs'):
        os.mkdir('logs')

    # Depending on the argument rewrites or appends the initial timestamp 
    if rewrite:
        file = open('logs/cas_log_{}.log'.format(timestamp_file), 'w')
        file.write('-'*20 + timestamp_logs + '-'*20 + '\n')
        file.close()
    else:
        file = open('logs/cas_log_{}.log'.format(timestamp_file), 'a')
        file.write('-'*20 + timestamp_logs + '-'*20 + '\n')
        file.close()

    logging.basicConfig(
        level=logging.INFO,
        filename='logs/cas_log_{}.log'.format(timestamp_file),
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def log(message="", screen_verbose=False, level="INFO"):
    """
    Logs all the information that the program executes

    By default the verbose occurs only on file, but 
    depending on the argument that is used at program 
    startup (in this case '-v') screen_verbose can be 
    set to True

    Levels can be of three types:
    - INFO: For basic information about the program
    - WARNING: For information that requires the user's attention
    - ERROR: For program error information.
    """

    if level == "INFO":
        logging.info(message.replace("\n", ""))

    if level == "WARNING":
        logging.warning(message.replace("\n", ""))

    if level == "ERROR":
        logging.error(message.replace("\n", ""))

    print(level + ": " + message) if screen_verbose else ""
