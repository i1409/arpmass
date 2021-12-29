# arpmass
This tool was made over a GNU/Linux Distro (Debian)
Make sure to be able to run over your bash the comands arp and arpsoof, this is just a simple arp spoofing tool designed to run over GNU/Linux and a network with CIDR /24

> If not have on your distro the comments previously mentionet install with: user@host# apt install net-tools dsniff

In order to run the tool just download and run over your python3 directly on your system or into a virtual env running python3 (recommended)

- user@host$pip3 install -r reqs.txt

> If you want to use a virtual env install with: user@host# apt-get install virtualenv

> If error reported on gnureadline install the following package by run: "apt-get install libncurses5-dev" and try again

# usage
- ./arpmass.py

It will prompt a line asking for the network interface to use, another line for the network, and one last for the ip address of the gateway or host to spoof the MAC address

then it will check on the ARP table the known host ip and mac addresses for run the spoofing over them



