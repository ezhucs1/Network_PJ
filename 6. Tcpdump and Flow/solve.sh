#!/usr/bin/env bash

# enter commands

# Key concept:
# Using Wireshark
# enter "tcp.port == 1337"

# will see two address communicate via the spesfic port
# as in, 3.13.37.2 <-> 3.13.37.4

# select any packet in that conversation and select Follow -> TCP Stream

# the idea: Wireshark will reassemble all the payload across packets into one continuous conversation.

# That’s where to see the “intercepted communication” (likely a secret, a flag, or a message).
