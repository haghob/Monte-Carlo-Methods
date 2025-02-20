from numpy import random
import numpy as np
import matplotlib.pyplot as plt
n = 1000
y = np.zeros((n-2))
j = np.linspace(2, n-1, n-2)
i = 1
while (y[i] >= 0) and (i+1 < len(y)):
    x = random.normal(0, 1, i)
    y[i] = np.mean(x**4)
    i = i + 1
d = np.mean(y)
print(d)
plt.plot(j, y)
plt.show()
