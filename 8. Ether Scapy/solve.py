#!/usr/bin/env python3 

import requests
from pwn import *
# add python script
from scapy.all import *

eth = Ether(src=get_if_hwaddr("eth0"), dst="94:9d:26:1b:4e:f4", type = 0xFFFF)

ip = IP(dst="10.0.235.63")

packet = eth / ip
sendp(packet, iface="eth0", verbose=True)
