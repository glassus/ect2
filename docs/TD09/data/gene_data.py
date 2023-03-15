import numpy as np
import matplotlib.pyplot as plt

from random import randint

plt.clf()

z = np.arange(7)


k = 2


#y = [randint(0,20) for _ in range (len(x))]

#y = np.array([-1*(v-len(z)//2)**2+50+ 1*randint(-k,k) for v in z])


y = np.array([41, 47, 51, 50, 49, 48, 42])





plt.scatter(z,y)


# a, b, c = np.polyfit(z, y, 2)
# x = np.linspace(-2,8,100)
# plt.plot(x, a*x**2 + b*x + c, 'r-')


a, b, c, d, e, f, g = np.polyfit(z, y, 6)
x = np.linspace(-2,8,100)
plt.plot(x, a*x**6 + b*x**5 + c*x**4 + d*x**3 + e*x**2 + f*x + g, 'g-')

plt.xlim([-2, 8])
plt.ylim([25, 60])
plt.show()
