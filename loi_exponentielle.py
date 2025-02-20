from numpy import random
import numpy as np
import matplotlib.pyplot as plt
n = 1000
l = 2
u = random.uniform(0, 1, n)
z = -(np.log((1 - u)/ l))
print(u)

plt.hist(z)
plt.show()
