import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

# Load the original drag shit...
crs = open('DragLift_org.fce','r')
D = np.loadtxt(crs)

# Load the tempss drag shit...
crt = open('DragLift_tempss.fce','r')
E = np.loadtxt(crt)

# Make range
R = np.zeros(6)
vals = np.zeros(6)
for i in range(0,6):
        R[i] = D[i][0]

# Plot original data
plt.title('NACA65 - Drag Forces Original Vs TemPSS')
plt.ylabel('Force (N)')
plt.xlabel('Timesteps')
plt.plot(R,D[:,1], "r", lw="2", label="Pressure - Orig.")
plt.plot(R,D[:,2], "g", lw="2", label="Viscous - Orig.")
plt.plot(R,D[:,3], "b", lw="2", label="Total - Orig.")
plt.plot(R,E[:,1], "k-.", lw="2", label="Pressure - TemPSS.")
plt.plot(R,E[:,2], "k--", lw="2", label="Viscous - TemPSS.")
plt.plot(R,E[:,3], "k:", lw="3", label="Total - TemPSS.")
plt.legend(bbox_to_anchor=(1, .66), loc=1, borderaxespad=0.)

plt.savefig('./drag')
