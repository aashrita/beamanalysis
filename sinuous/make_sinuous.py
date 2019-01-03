import numpy as np
import matplotlib.pyplot as pl
import math

N = 1000
alpha = 45 * math.pi/180
delta = 22.5 * math.pi/180
tau = 1.3
R0 = 100 #mm

rmin = R0 + 1
rmax = R0 * (tau ** N) - 1
rstep = (rmax - rmin)/N
print(rmin, rmax, rstep)

rlist = []
phi_max = []
phi_min = []

cntr = 0
for r in np.linspace(rmin, rmax, num = N, dtype = float):
	phi_max.append(alpha * math.sin(math.pi * math.log(r/R0)/math.log(tau)) + delta)
	phi_min.append(alpha * math.sin(math.pi * math.log(r/R0)/math.log(tau)) - delta)
	rlist.append(r)
	cntr = cntr + 1

#phi_max = np.sort(phi_max)

pl.polar(phi_max, rlist, phi_min, rlist)
#pl.yscale('log')
#pl.xscale('log')
pl.grid()
#pl.xlabel(r'r')
#pl.ylabel(r'tau_inspiral')
pl.title(r'sinuous')
pl.show()