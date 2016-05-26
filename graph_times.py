from __future__ import division
import matplotlib

matplotlib.use('Agg')

from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid, legend
from numpy import linspace, loadtxt, ones, convolve
import numpy as numpy
import sys

def movingaverage(interval, window_size):
    window= numpy.ones(int(window_size))/float(window_size)
    return numpy.convolve(interval, window, 'same')


csv = numpy.genfromtxt (sys.argv[1], delimiter=",")
csv2 = numpy.genfromtxt (sys.argv[2], delimiter=",")
csv3 = numpy.genfromtxt (sys.argv[3], delimiter=",")
csv4 = numpy.genfromtxt (sys.argv[4], delimiter=",")

distance = []
throughput = []
distance2 = []
throughput2 = []

throughput3 = []
distance3 =  []
throughput4 = []
distance4 = []

old_val = None
for val in csv:
    if old_val is None:
        old_val = val[2]
    else:
        throughput.append(val[2] + old_val)
        distance.append(val[0])
        old_val = None

old_val = None
for val in csv2:
    if old_val is None:
        old_val = val[2]
    else:
        throughput2.append(val[2] + old_val)
        distance2.append(val[0])
        old_val = None

old_val = None
for val in csv3:
    if old_val is None:
        old_val = val[2]
    else:
        throughput3.append(val[2])
        distance3.append(val[0])
        old_val = None

old_val = None
for val in csv4:
    if old_val is None:
        old_val = val[2]
    else:
        throughput4.append(val[2])
        distance4.append(val[0])
        old_val = None
#iat = csv[:,1]
#rtt = csv[:,2]
#iat = movingaverage(iat, 200)
#rtt = movingaverage(rtt, 200)
#plot(time, iat)
#plot(time, rtt)
plot(distance, throughput, label = 'TCP 1+2');
plot(distance2, throughput2, '-k', label = 'UDP 1+2');
plot(distance3, throughput3, label = 'UDP 1');
plot(distance4, throughput4, label = 'UDP 2');
legend(loc='lower right')
#send = movingaverage(csv[:,2], 50)
#plot(time, send);
#csv = numpy.genfromtxt ('iat.underuse.csv', delimiter=",")
#iat = movingaverage(csv[:,1] * -1, 50)
#time = csv[:,0] / 1000
#plot(time, iat);
#csv = numpy.genfromtxt ('out.2.csv', delimiter=",")
#iat = movingaverage(csv[:,1] * -1, 50)
#time = csv[:,0] / 1000
#plot(time, iat);
#ylim(-0.75, .75)
xlabel('Distance (meters)')
ylabel('Throughput (bps)')
matplotlib.pyplot.savefig("hidden-terminal.png")
