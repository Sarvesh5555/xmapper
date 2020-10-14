#!/usr/bin/env python

import scapy.all as scapy

print("------------------------------------------------------------")
print("| ██╗  ██╗ ███╗   ███╗  █████╗  ██████╗  ███████╗ ██████╗  |")
print("| ╚██╗██╔╝ ████╗ ████║ ██╔══██╗ ██╔══██╗ ██╔════╝ ██╔══██╗ |")
print("|  ╚███╔╝  ██╔████╔██║ ███████║ ██████╔╝ █████╗   ██████╔╝ |")
print("|  ██╔██╗  ██║╚██╔╝██║ ██╔══██║ ██╔═══╝  ██╔══╝   ██╔══██╗ |")
print("| ██╔╝ ██╗ ██║ ╚═╝ ██║ ██║  ██║ ██║      ███████╗ ██║  ██║ |")
print("| ╚═╝  ╚═╝ ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝      ╚══════╝ ╚═╝  ╚═╝ |")
print("------------------------------------------------------------")
print("                  Created BY \n\t\t\t  SARVESH              ")
print("------------------------------------------------------------")
print("            Enter Target IP or IP Range                     ")
ip = input("[+] Target= ")


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print("IP ADDRESS\t\t\tMAC ADDRESS\n----------------------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t\t" + element[1].hwsrc)


scan(ip)
