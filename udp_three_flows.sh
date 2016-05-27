#!/bin/bash

CSTHRESH=1.76149e-10

ns three_flows.tcl -run_tcp 0 -RTSthresh 3000 -CSthresh $CSTHRESH -x_dist $1 -y_dist $2 -sendingRate 3Mbps -sendingRate2 3Mbps -udp_node 1 -numRetries 7 | grep 'Throughput' | sed 's/ /,/g' | sed "s/Throughput/$1,$2/g" >> $3
