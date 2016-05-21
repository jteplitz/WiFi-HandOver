for DIST in {0..160..5}
do
  ns two_flows.tcl -run_tcp 1 -RTSthresh 2346 -CSthresh 1.55924e-11 -dist $DIST -sendingRate 1000 -sendingRate2 1000 | grep 'Throughput' | sed 's/ /,/g' | sed "s/Throughput/$DIST/g" >> output.txt 
done
