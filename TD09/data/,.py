import numpy as np
import numpy.random as rd

k = 1
hasard = rd.randint(1, k+2)
while hasard < k+1:
    k = k + 1
    hasard = rd.randint(1, k+2)

print('U a pris la valeur', k)
