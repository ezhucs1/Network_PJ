#!/usr/bin/env python3 

import requests
from pwn import *

from scapy.all import *
# add python script

eth = Ether(src=get_if_hwaddr("eth0"), dst="a0:f2:a2:b2:1e:61")

ip = IP(dst="10.0.33.160", proto=0xFF)

packet = eth/ip

sendp(packet, iface="eth0", verbose=True)
