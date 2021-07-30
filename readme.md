# ClamAV - AutoScanner

The aim of this project is to address the problem that USB sticks can create when used by other people outside the company, who, by connecting them to their personal PC, can infect the USB stick and consequently the company's computers, servers, etc.. 

## How does the project work?

Basically, the project takes the logs of the **dmesg** program and checks every second whether a USB stick has been inserted into a USB port on the PC that will be used.

When it detects a stick, the program will take from the dmesg logs some technical information about the stick and the partition names of the stick to be checked with ClamAV.

Next, the program will check the file system type of each partition and mount it correctly.

Finally, it will run two main ClamAV commands:

    freshclam
    clamscan -r /mnt/[partition name]

The first is used to update the virus definition database, while the second is used to start the virus scan on the USB stick.

## Technical Informations

The programme will be developed with the **Python 3.9.2** programming language and run on the **Fedora Workstation 34** operating system. The program should also run on other Linux operating systems. Over time, a list of fully supported operating systems will be compiled.

| Operating System | Support |
| ---------------- | :-----: |
| Fedora 34        |    ✅    |

## License

This software is licensed under the MIT License. See LICENSE file for more information.

## Author

Elia Vicentini <eliavicentini26@gmail.com>

