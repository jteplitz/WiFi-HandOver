import subprocess
CSTHRESH="1.76149e-10"
import sys

SKIP=10

for x in xrange(150):
	if x % SKIP == 0:
		for y in xrange(130):
			if y % SKIP == 0:
				x0 = y / 1.73
				x1 = 150 - x0
				if x >= x0 and x <= x1:
					subprocess.call(["./udp_three_flows.sh", str(x), str(y), sys.argv[1]])
					
