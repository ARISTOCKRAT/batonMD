import numpy as np


np.seterr(divide="ignore")


a = np.array(range(10*10)).reshape((10, 10))
print(a)

# print(np.multiply(a[:, 1], a[:, 2]))

print(
    np.divide(a[:, 1], a[:, 0])
)

