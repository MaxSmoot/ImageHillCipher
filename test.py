import HillCipher as Hill
import numpy as np
from sympy import Matrix




x = np.array([[1,2,3],[4,5,6],[7,8,9]])
a = Hill.generateKey(3)
y = np.mod(np.matmul(a, x),256)
# print(x)
# print(y)
# print(np.mod(np.matmul(Hill.invertKey(a), y), 256))
print(a)
print(Hill.invertKey(a))