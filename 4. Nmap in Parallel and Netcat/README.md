## Big Scan 

Use the nmap command to find the remote server with an open 
port. However, this time the subnet that nmap must scan is 
10.0.0.0/16, which is much larger network with 65534 potential nodes. Thus, 
we need to speed up nmap using its parallelism capabilities.

```

         *                  *
             __                *
          ,db'    *     *
         ,d8/       *        *    *
         888
         `db\       *     *
           `o`_                    **
      *               *   *    _      *
            *                 / )
         *    (\__/) *       ( (  *
       ,-.,-.,)    (.,-.,-.,-.) ).,-.,-.
      | @|  ={      }= | @|  / / | @|o |
     _j__j__j_)     `-------/ /__j__j__j_
     ________(               /___________
      |  | @| \              || o|O | @|
      |o |  |,'\       ,   ,'"|  |  |  |  hjw
     vV\|/vV|`-'\  ,---\   | \Vv\hjwVv\//v
                _) )    `. \ /
               (__/       ) )
                         (_/
```

# EOF /challenge/README.md


 
===== Welcome to Intercepting Communication! =====
In this series of challenges, you will be working within a virtual network in order to intercept networked traffic.
In this challenge you will find and connect to a remote host.
The remote host is somewhere on the `10.0.0.0/16` subnetwork, listening on port `46529`.

Note: the IP addr and MAC addr are randomly generated, this excerce is practiced under protected and safe enviorment
