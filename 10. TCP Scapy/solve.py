#!/usr/bin/env python3 

import requests
from pwn import *

from scapy.all import *
# add python script

eth = Ether(src=get_if_hwaddr("eth0"), dst="ff:ff:ff:ff:ff:ff")

ip = IP(dst="10.0.33.56")

tcp =TCP(sport=5992, dport=32561, seq=217425892, ack=1786146862, flags="APRSF")

payload = Raw(b"Hello")
packet= eth / ip / tcp / payload
sendp(packet, iface="eth0", verbose=True)

