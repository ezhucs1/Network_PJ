#!/usr/bin/env python3 

import requests
from pwn import *

from scapy.all import *

# add python script

# Define the target
target_ip = "10.0.120.174"
target_mac = "d9:fa:fa:3a:69:91"
src_port = 3732
dst_port = 34996
seq_num = 2811895413

# Get your own IP and MAC
iface = "eth0"  # change to your interface name
src_ip = get_if_addr(iface)
src_mac = get_if_hwaddr(iface)

# SYN packet
syn = Ether(src=src_mac, dst=target_mac) / IP(src=src_ip, dst=target_ip) / TCP(sport=src_port, dport=dst_port, seq=seq_num, flags="S")

# Send SYN and receive SYN-ACK
syn_ack = srp1(syn, timeout=2, iface=iface)

# If we got a response
if syn_ack:
    # Create ACK with ack number = syn_ack.seq + 1
    ack = Ether(src=src_mac, dst=target_mac) / IP(src=src_ip, dst=target_ip) / TCP(sport=src_port, dport=dst_port, seq=seq_num+1, ack=syn_ack.seq+1, flags="A")
    sendp(ack, iface=iface)
else:
    print("No SYN-ACK received")


# concept:

# SYN: "Knock knock."

# SYN-ACK: "Who's there?" (The door is now open)

# ACK: "It's me, Alice." (You step inside)
