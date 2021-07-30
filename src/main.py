"""
Main - ClamAV AutoScanner

Author: Elia Vicentini <eliavicentini26@gmail.com>
"""

import sys
import argparse


__VERSION__ = "alpha 0.1"


def check_os():
    """
    Checks which operating system the program runs on
    """

    supported_platforms = [
        "linux",
        "darwin"  # TODO Test the program also on macOS
    ]

    if not sys.platform in supported_platforms:
        return False

    return True


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="ClamAV - AutoScanner")
    parser.add_argument("-v", "--verbose", 
                        action="store_true", 
                        help="View logs on screen")

    args = parser.parse_args()

    if check_os():
        print("OS Check OK") if args.verbose else None