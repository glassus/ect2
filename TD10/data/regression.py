import numpy as np
import matplotlib.pyplot as plt

plt.clf()


x = np.array([4775, 1350, 5680, 5872, 7964, 3072, 1942, 8802])
y = np.array([63, 45, 62, 69, 81, 56, 50, 83])


coeff = np.corrcoef(x, y)[0, 1]

plt.scatter(x, y)
print(coeff)

a, b = np.polyfit(x, y, 1)
plt.plot(x, a*x + b, 'g-')


plt.show()
