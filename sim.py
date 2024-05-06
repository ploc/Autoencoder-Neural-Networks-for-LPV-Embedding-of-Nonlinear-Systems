import numpy as np
import matplotlib.pyplot as plt
from simulation_functions import controller, model, oneTraj

# Define the initial state, the state feedback controller, and the limit for the
# saturation on the input signal
x = [np.pi/6, 5, 0, 0]
#K = [-138.3892,  -26.9881,  -11.8016, -51.7673]
K = [-109.3936,  -21.1989,   -8.0214,  -43.1398]
limit = 105

x_dat = list()
u_dat = list()

# Perform simulation for given initial state
x_dat, u_dat = oneTraj(x, K, limit, Final=150)

# plot the obtained results for different state variables and input signal
fig, axs = plt.subplots(4,1, figsize=(8,20))
axs[0].plot(np.array(x_dat)[:,0])
axs[1].plot(np.array(x_dat)[:,1])
axs[2].plot(np.array(x_dat)[:,2])
axs[3].plot(np.array(x_dat)[:,3])

plt.figure()
plt.plot(u_dat)
plt.show()

# Save data for one trajectory for producing the related figure in the paper
np.save('Xfig', x_dat)
np.save('Ufig', u_dat)
