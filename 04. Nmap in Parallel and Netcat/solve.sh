#!/usr/bin/env bash

# enter commands

# nmap -Pn -T5 -p 14755 10.0.0.0/16 --min-parallelism 100 --max-parallelism 256

# alternative command
#nmap -Pn -T5 -p 14755 10.0.0.0/16 --min-rate 5000 --max-rtt-timeout 100ms
#nmap -Pn -T5 -p 14755 10.0.0.0/16

# step 1
nmap -Pn -T5 -p 14755 10.0.0.0/16 -n --min-rate 5000

# step 2
# nc <ip addr> <port>




