CSTHRESH=1.76149e-10
rm tcp-$CSTHRESH.csv
rm udp-$CSTHRESH.csv
rm udp1-$CSTHRESH.csv
rm udp2-$CSTHRESH.csv
for TRIAL in {0..9}
do
rm tcp-loss-$TRIAL.csv
done
rm twoflows-shadow.*

for DIST in {0..160..5}
do
  ns two_flows.tcl -run_tcp 0 -RTSthresh 3000 -CSthresh $CSTHRESH -dist $DIST -sendingRate 1.7Mbps -sendingRate2 1.7Mbps -udp_node 1 -numRetries 7 | grep 'Throughput' | sed 's/ /,/g' | sed "s/Throughput/$DIST/g" >> udp-$CSTHRESH.csv
  ns two_flows.tcl -run_tcp 1 -RTSthresh 3000 -CSthresh $CSTHRESH -dist $DIST -sendingRate 1.7Mbps -sendingRate2 1.7Mbps -udp_node 1 -numRetries 7 | grep 'Throughput' | sed 's/ /,/g' | sed "s/Throughput/$DIST/g" >> tcp-$CSTHRESH.csv
  ns two_flows.tcl -run_tcp 2 -RTSthresh 3000 -CSthresh $CSTHRESH -dist $DIST -sendingRate 1.7Mbps -sendingRate2 1.7Mbps -udp_node 1 -numRetries 7 | grep 'Throughput' | sed 's/ /,/g' | sed "s/Throughput/$DIST/g" >> udp1-$CSTHRESH.csv
  ns two_flows.tcl -run_tcp 2 -RTSthresh 3000 -CSthresh $CSTHRESH -dist $DIST -sendingRate 1.7Mbps -sendingRate2 1.7Mbps -udp_node 3 -numRetries 7 | grep 'Throughput' | sed 's/ /,/g' | sed "s/Throughput/$DIST/g" >> udp2-$CSTHRESH.csv
done
python graph_times.py tcp-$CSTHRESH.csv udp-$CSTHRESH.csv udp1-$CSTHRESH.csv udp2-$CSTHRESH.csv
for TRIAL in {0..9}
do
for NUMRETRIES in {0..19}
do
  TEXT="$(ns two_flows.tcl -run_tcp 1 -RTSthresh 3000 -CSthresh $CSTHRESH -dist 68 -sendingRate 1.7Mbps -sendingRate2 1.7Mbps -udp_node 1 -numRetries $NUMRETRIES | grep 'Throughput' | sed 's/ /,/g' | sed 's/Throughput//g')"
  arrTEXT=(${TEXT//,/ })
  THROUGHPUT0=${arrTEXT[1]}
  THROUGHPUT2=${arrTEXT[3]}
  FLOW_0_LOSS="$(grep -c 'd -t .* -Ni 1 .* tcp' twoflows-shadow.tr)"
  FLOW_0_SENT="$(grep -c 's -t .* -Hs 0 -Hd 1 .* tcp' twoflows-shadow.tr)"
  FLOW_2_LOSS="$(grep -c 'd -t .* -Ni 3 .* tcp' twoflows-shadow.tr)"
  FLOW_2_SENT="$(grep -c 's -t .* -Hs 2 -Hd 3 .* tcp' twoflows-shadow.tr)"
  echo 0, $NUMRETRIES, $FLOW_0_LOSS, $FLOW_0_SENT, $THROUGHPUT0 >> tcp-loss-$TRIAL.csv
  echo 2, $NUMRETRIES, $FLOW_2_LOSS, $FLOW_2_SENT, $THROUGHPUT2 >> tcp-loss-$TRIAL.csv
  rm twoflows-shadow.tr
done
done
python graph_loss.py
