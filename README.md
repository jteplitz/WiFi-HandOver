We highly recommend using EC2 to reproduce our results. Instructions for doing so are as follows:

1. Search for the “ns-2.34-w/NOAH-no-ARP” AMI on the community marketplace
2. Launch a new t2.medium or t2.small instance with this AMI.
3. Login as ‘ubuntu’
4. Clone https://github.com/jteplitz602/WiFi-HandOver
5. Execute “run.sh”

The experiments should take about an hour to run regardless of your instance size.
All graphs should be outputted in the same directory as “.png” files.
