import numpy as np

# Integrand over the current loop
def f(theta, I, R, r):
    norm = (4*I*R)/(R**2-r**2)
    radical = 1. - (r/R)**2 * pow(np.sin(theta),2)
    return norm * np.sqrt(radical)

# Implementation of trapezoidal integration
def wTrap(i, N, h):
    if ( (i == 1) or (i == N) ):
        wTotal = h/2.0
    else:
        wTotal = h
    return wTotal
