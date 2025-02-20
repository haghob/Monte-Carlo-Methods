def inv(u):
    if u < (1/3):
        z = 3*u
    elif u < (2/3):
        z = 1
    else:
        z = 3*u-1
    return (z)
import random
import matplotlib.pyplot as plt
n= random.uniform(1,0)
print(inv(n))
plt.hist(n)
plt.show()
