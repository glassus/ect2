import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd
from math import exp, sqrt

plt.clf()


def tirage():
    return rd.randint(0,11)

def moyenne_tirages(n):
    s = 0
    for _ in range(n):
        s += tirage()
    return s / n

x = np.array([moyenne_tirages(10) for n in range(10**4)])
plt.hist(x, np.linspace(0, 10, 100), density=False)


x = np.array([rd.normal(5,3.67) for n in range(10**4)])
plt.hist(x, np.linspace(0, 10, 100), density=False)


plt.show()