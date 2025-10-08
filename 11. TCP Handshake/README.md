## TCP Handshake 

In this challenge, you need to send two TCP packets to complete a TCP handshake using scapy. Configure scapy to send the packets to 10.0.50.220 @ 46:b2:69:10:cd:11 using a source port of 45551, a destination port of 24878, a sequence number of 668029990, and using the appropriate flags. Make sure to adjust the sequence and acknowledgement numbers appropriately.


```

                /||\
                ||||
                ||||
                |||| /|\
           /|\  |||| |||
           |||  |||| |||
           |||  |||| |||
           |||  |||| d||
           |||  |||||||/
           ||b._||||~~'
           \||||||||
            `~~~||||
                ||||
                ||||
~~~~~~~~~~~~~~~~||||~~~~~~~~~~~~~~
  \/..__..--  . |||| \/  .  ..
\/         \/ \/    \/
        .  \/              \/    .
. \/             .   \/     .
   __...--..__..__       .     \/
\/  .   .    \/     \/    __..--..
```
# EOF /challenge/README.md

 
===== Welcome to Intercepting Communication! =====
In this series of challenges, you will be working within a virtual network in order to intercept networked traffic.
In this challenge you will manually perform a Transmission Control Protocol handshake.
The initial packet should have `TCP sport=45551, dport=24878, seq=668029990`.
The handshake should occur with the remote host at `10.0.50.220`  @ `46:b2:69:10:cd:11`.
