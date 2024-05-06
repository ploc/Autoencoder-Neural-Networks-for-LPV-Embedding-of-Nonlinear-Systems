# Autoencoder-Neural-Networks-for-LPV-Embedding-of-Nonlinear-Systems

# Files

Jupyter notebooks:
- LPVmodel.ipynb
- comparison.ipynb

Python:
- simulation_functions.py: inverted pendulum model
- sim.py: one runwith the provided state feedback controller, from a specific initial point.
- TrainData.py: run the model with the provided state feedback
  controller with saturation, save the trajectories (state and output)
  for a set of initial angular positions and velocitys.

# Create data

```shell
python TrainData.py
```

Produces Udata.npy, XPdata.npy and Xdata.npy


```shell
python sim.py
```

Produces Xfig and Ufig.npy as well as plots

# Run jupyter notebooks

```shell
jupyter notebook
```
