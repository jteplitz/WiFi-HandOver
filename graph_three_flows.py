from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid, legend, figure, gca, cm, savefig
from numpy import linspace, loadtxt, ones, convolve
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
import numpy as np
import sys

mptcp = np.genfromtxt (sys.argv[1], delimiter=",")
x = []
y = []
throughput = []

curr = 0
this_throughput = 0
for val in mptcp:
    this_throughput += val[3]
    if curr % 3 == 0:
        x.append(val[0])
        y.append(val[1])
        throughput.append(this_throughput)
        this_throughput = 0
    curr = curr + 1

#tri = mtri.Triangulation(vals)
fig = figure(figsize=(16, 12), dpi=80)
ax = fig.add_subplot(1, 1, 1, projection='3d')
#ax.plot_trisurf(x, y, throughput, triangles=tri.triangles)
ax.plot_trisurf(x, y, throughput, cmap=cm.Spectral)
axes = gca()
axes.set_xlim([0, 150])
axes.set_ylim([0, 130])

if "udp" in sys.argv[1]:
    fig.suptitle("UDP Throughput with Three Routers")
else:
    fig.suptitle("MPTCP Throughput with Three Routers")

ax.set_xlabel("Distance along x axis (m)")
ax.set_ylabel("Distance along y axis (m)")
ax.set_zlabel("Throughput (bits / s)")

figname = sys.argv[1].replace(".csv", "")
ax.view_init(22, -130)
savefig(figname + "-flows-side.png")
ax.view_init(97, -90)
savefig(figname + "-flows-top.png")
ax.view_init(-122, -38)
savefig(figname + "-flows-bottom.png")

#Un-comment the below line to get an interactive plot
#show()
