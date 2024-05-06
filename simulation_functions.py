import numpy as np

def model(x, u):
    '''This function provides the dynamical model of the inverted penfulum on a cart'''

    x1, x2, x3, x4 = x

     # parameters for invrted pendulum
    T = 0.05
    g = 9.8
    m = 0.22
    M = 1.3282
    f0 = 22.915
    f1 = 0.007056
    l = 0.304
    J = 0.004963

    # nonlinear state space represenation of the inverted pendulum
    V = (M + m) * (J + m * (l ** 2)) - (m ** 2) * (l ** 2) * (np.cos(x1) ** 2)

    x1_p = x1 + T * x2
    x2_p = T * (-f1 * ( M + m) * x2 - (m ** 2) * (l ** 2) * (x2 ** 2) *
          np.sin(x1) *    np.cos(x1) + f0 * m * l * x4 * np.cos(x1) + (M + m) * m
          * g * l *   np.sin(x1) - m * l * np.cos(x1) * u) / V + x2
    x3_p = x3 + T * x4
    x4_p = T * (f1 * m * l * x2 * np.cos(x1) + (J + m * (l ** 2)) * m * l *
          (x2 ** 2) * np.sin(x1) - f0 * (J + m * (l ** 2)) * x4 - (m ** 2) * g *
          (l ** 2) *  np.sin(x1) * np.cos(x1) + (J + m * (l ** 2)) * u) / V + x4

    # State vector at instant k+1 when the input and state vector at k are given
    x = [x1_p, x2_p, x3_p, x4_p]

    # return the state vector value at k+1
    return x


def controller(x, K, limit):
    ''' This functions provided the state feedback controller for the inverted
        pendulum on a cart'''

    u = - (K[0] * x[0] + K[1] * x[1] + K[2] * x[2] + K[3] * x[3])

    # Apply the saturation on the control input
    if (u>limit):
        u = limit
    elif u< -limit:
        u = -limit
    else:
        u = u

    return [u]


def oneTraj(x, K, limit, Final=2000):
    '''This function simulate the inverted pendulum for an initial
        state vector'''

    x_dat = list()
    u_dat = list()

    for i in range(1, Final):
        u = controller(x, K, limit)
        x_dat.append(x)
        u_dat.append(u)
        x = model(x, u[0])

    return x_dat, u_dat
