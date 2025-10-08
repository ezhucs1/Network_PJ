# ARP Scapy 

In this challenge, you need to convince 10.0.245.218 that you are 10.0.42.11 by creating an ARP packet using scapy. Configure scapy to send the appropriate ARP packet to 10.0.245.218 @ b4:68:19:be:f9:78 using your host's mac address (consider using get_if_hwaddr) and the ip address 10.0.42.11.

```

                                  |>>>                            
                                  |                               
                    |>>>      _  _|_  _         |>>>              
                    |        |;| |;| |;|        |
                _  _|_  _    \\.    .  /    _  _|_  _
               |;|_|;|_|;|    \\:. ,  /    |;|_|;|_|;|
               \\..      /    ||;   . |    \\.    .  /
                \\.  ,  /     ||:  .  |     \\:  .  /
                 ||:   |_   _ ||_ . _ | _   _||:   |
                 ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |
                 ||:   ||.    .     .      . ||:  .|
                 ||: . || .     . .   .  ,   ||:   |       \,/
                 ||:   ||:  ,  _______   .   ||: , |            /`\
                 ||:   || .   /+++++++\    . ||:   |
                 ||:   ||.    |+++++++| .    ||: . |
              __ ||: . ||: ,  |+++++++|.  . _||_   |
     ____--`~    '--~~__|.    |+++++__|----~    ~`---,              ___
-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~~

```

# EOF /challenge/README.md 
===== Welcome to Intercepting Communication! =====
In this series of challenges, you will be working within a virtual network in order to intercept networked traffic.
In this challenge you will manually send an Address Resolution Protocol packet.
The packet should have `ARP op=is-at` and correctly inform the remote host of where the sender can be found.
The packet should be sent to the remote host at `10.0.245.218`  @ `b4:68:19:be:f9:78`.
