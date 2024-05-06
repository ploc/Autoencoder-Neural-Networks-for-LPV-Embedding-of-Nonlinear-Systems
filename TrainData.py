import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from simulation_functions import *

# Define state feedback controller, and the saturation limit
K = [-109.3936,  -21.1989,   -8.0214,  -43.1398]
limit = 105

# Duration of the simulation  ( Final * 0.005)
Final = 200

# initalization to gather x(k), x(k+1), u(k)
x_dat = list()
xp_dat = list()
u_dat = list()

# Perform the simulation by griding the state variable x1 and x2 which are
#(angular position and velocity)
for teta in tqdm(np.linspace(-np.pi/6, +np.pi/6, num=100)):
    for vel in np.linspace(-5, 5, num=100):
        x0 = [teta, vel, 0, 0]
        x_traj, u_traj = oneTraj(x0, K, limit, Final)
        x_dat.append(x_traj[:-1])
        xp_dat.append(x_traj[1:])
        u_dat.append(u_traj[:-1])


# Construct the X, Xp, and U datasets
X = np.concatenate(x_dat, axis=0)
XP = np.concatenate(xp_dat, axis=0)
U = np.concatenate(u_dat, axis=0)

# Print the shape of the obtained data
print(f'Shape of X is {X.shape}.')
print(f'Shape of XP is {XP.shape}.')
print(f'Shape of U is {U.shape}.')

# Save the X, Xp and U datasets for future use
np.save('Xdata', X)
np.save('XPdata', XP)
np.save('Udata', U)
