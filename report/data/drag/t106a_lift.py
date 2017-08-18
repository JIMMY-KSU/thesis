import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

# Load the original drag shit...
crs = open('Aero_orig.fce','r')
D = np.loadtxt(crs)

# Load the tempss drag shit...
crt = open('Aero_tempss.fce','r')
E = np.loadtxt(crt)

# Make range
R = np.zeros(3)
vals = np.zeros(3)
for i in range(0,3):
        R[i] = D[i][0]

# Plot original data
plt.title('T106a - Lift Forces Original Vs TemPSS')
plt.ylabel('Streamwise Velocity')
plt.xlabel('Timesteps')
plt.plot(R,D[:,4], "r", lw="2", label="Pressure - Orig.")
plt.plot(R,D[:,5], "g", lw="2", label="Viscous - Orig.")
plt.plot(R,D[:,6], "b", lw="2", label="Total - Orig.")
plt.plot(R,E[:,4], "k-.", lw="2", label="Pressure - TemPSS.")
plt.plot(R,E[:,5], "k--", lw="2", label="Viscous - TemPSS.")
plt.plot(R,E[:,6], "k:", lw="3", label="Total - TemPSS.")
plt.legend(bbox_to_anchor=(1, .66), loc=1, borderaxespad=0.)

plt.savefig('./lift_t106a')