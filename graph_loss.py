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

NUM_TRIES = 20
NUM_RETR = 15
perc1 = []
perc2 = []
retr = []
for i in range(NUM_RETR):
    perc1.append(0)
    perc2.append(0)
    retr.append(i)

#retr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
for j in range(NUM_TRIES):
    csv = numpy.genfromtxt ('tcp-loss-' + str(j) + '.csv', delimiter=",")
    i = 0
    while i < len(csv):
        firstLine = csv[i]
        secondLine = csv[i + 1]
        if firstLine[4] >= secondLine[4]:
            perc1[int(i / 2)] += firstLine[2] / firstLine[3]
            perc2[int(i / 2)] += secondLine[2] / secondLine[3]
        elif secondLine[4] > firstLine[4]:
            perc1[int(i / 2)] += secondLine[2] / secondLine[3]
            perc2[int(i / 2)] += firstLine[2] / firstLine[3]
        i += 2
for a in range(len(perc1)):
    perc1[a] /= NUM_TRIES
    perc2[a] /= NUM_TRIES
# retr = []
# perc = []
# retr2 = []
# perc2 = []

# old_val = None
# zeroFlow = True
# oldPair = []
# for val in csv:
#     if len(oldPair) == 0:
#         oldPair.append(val[1])
#         oldPair.append(val[2] / val[3])
#         oldPair.append(val[4])
#     else:
#         if val[4] > oldPair[2]:
#             perc.append(val[2] / val[3])
#             perc2.append(oldPair[1])
#         else:
#             perc.append(oldPair[1])
#             perc2.append(val[2] / val[3])
#         oldPair = []
#         retr.append(val[1])
#         retr2.append(val[1])

#iat = csv[:,1]
#rtt = csv[:,2]
#iat = movingaverage(iat, 200)
#rtt = movingaverage(rtt, 200)
#plot(time, iat)
#plot(time, rtt)

plot(retr, perc1, label = 'Subflow 1');
plot(retr, perc2, label = 'Subflow 2');
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

xlabel('Number of Retransmissions')
ylabel('Packets Dropped (%)')
matplotlib.pyplot.savefig('mptcp-loss.png')
