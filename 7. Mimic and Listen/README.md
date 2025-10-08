## Mimic and Listen 


We have infiltrated the target network and now we want to intercept traffic being sent from 10.0.44.4 to 10.0.167.181 on port 47619. What if we configured our network interface to mimic the target ip address of 10.0.167.181 and listened for requests on 47619.

```

                                    _
                                 ,:'/   _..._
                                // ( `""-.._.'
                                \| /    6\___
                                |     6      4
                                |            /
                                \_       .--'
                                (_'---'`)
                                / `'---`()
                              ,'        |
              ,            .'`          |
              )\       _.-'             ;
             / |    .'`   _            /
           /` /   .'       '.        , |
          /  /   /           \   ;   | |
          |  \  |            |  .|   | |
           \  `"|           /.-' |   | |
            '-..-\       _.;.._  |   |.;-.
                  \    <`.._  )) |  .;-. ))
                  (__.  `  ))-'  \_    ))'
                      `'--"`       `"""`
```


# EOF /challenge/README.md

 
===== Welcome to Intercepting Communication! =====
In this series of challenges, you will be working within a virtual network in order to intercept networked traffic.
In this challenge you will hijack traffic from a remote host by configuring your network interface.
The remote host at `10.0.44.4` is communicating with the remote host at `10.0.167.181` on port `47619`.

Note: the IP addr and MAC addr are randomly generated, this excerce is practiced under protected and safe enviorment
