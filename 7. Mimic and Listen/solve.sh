#!/usr/bin/env bash

# enter commands

# 10.0.255.210 is sending to 10.0.185.24:31551
# impersonate 10.0.185.24
# configure my interface with that IP address and listen on port 31551 to see traffic

ip addr add 10.0.185.24/24 dev eth0

nc -l 31551
# or
# nc -l 10.0.185.24 31551
