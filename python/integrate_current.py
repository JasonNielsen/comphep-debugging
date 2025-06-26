import numpy as np
import computational_functions as cp

# This code calculates the magnetic field for all points
# in the plane of a current loop.

# I = current (Amps)
# R = radius of loop (m)
# r = test location

I = 15.3
R = 120.
r = 84.

# Integration parameters
A = 0.
B = np.pi/2.
N = 1000
h = (B - A)/(N - 1)

suma = 0.0
for i in range(1, N + 1):
    t = A + (i - 1)*h
    suma  = suma + cp.wTrap(i, N, h) * cp.f(t, I, R, r)
    
print('Final sum = ', suma, 'amperes/meter')
