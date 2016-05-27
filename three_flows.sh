#!/bin/bash

CSTHRESH=1.76149e-10

ns three_flows.tcl -run_tcp 1 -RTSthresh 3000 -CSthresh $CSTHRESH -x_dist $1 -y_dist $2 -sendingRate 1.7Mbps -sendingRate2 1.7Mbps -udp_node 1 -numRetries 7 | grep 'Throughput' | sed 's/ /,/g' | sed "s/Throughput/$1,$2/g" >> tcp-three-$CSTHRESH.csv
