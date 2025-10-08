## TCP Flow

The communication is already occurring in the background. 

You have once again infiltrated the system and the host you are currently 
logged into is on the same network as 2 other hosts that are communicating. 
You want to intercept their network communications on this flat network. 
However, in this case, the traffic is slower and spread out over multiple 
tcp packets. To bring the packets back together you will need to use Wireshark's
tcp flow analysis.

The target network is 3.13.37.0/24
- If you need to limit the search look for traffic on **port 1337** (destination port)
- You will want to find the 2 remote hosts ip address and then filter in wireshark

```
                    _,    _   _    ,_
               .o888P     Y8o8Y     Y888o.
              d88888      88888      88888b
             d888888b_  _d88888b_  _d888888b
             8888888888888888888888888888888
             8888888888888888888888888888888
             YJGS8P"Y888P"Y888P"Y888P"Y8888P
              Y888   '8'   Y8P   '8'   888Y
               '8o          V          o8'
                 `                     `

```

# EOF /challenge/README.md


Note: the IP addr and MAC addr are randomly generated, this excerce is practiced under protected and safe enviorment
