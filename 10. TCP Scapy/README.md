## TCP Scapy 

In this challenge, you will create and send a TCP packet using scapy. Configure scapy to send the packet to 10.0.182.250 using a source port of 40188, a destination port of 38884, a sequence number of 2102660698, an acknowledgement number of 888364452, and using the flags APRSF


```

    ~ _>/O O\<_ ~~ ~~ ~  ~ ~
  ~~ ( o     o )  ~~~~ ~~~ ~~~~~
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    _/         \_
   (__/(     )\__)      ?
      _/     \_          <
     (__/   \__)
```
# EOF /challenge/README.md

 
===== Welcome to Intercepting Communication! =====
In this series of challenges, you will be working within a virtual network in order to intercept networked traffic.
In this challenge you will manually send a Transmission Control Protocol packet.
The packet should have `TCP sport=40188, dport=38884, seq=2102660698, ack=888364452, flags=APRSF`.
The packet should be sent to the remote host at `10.0.182.250`.
