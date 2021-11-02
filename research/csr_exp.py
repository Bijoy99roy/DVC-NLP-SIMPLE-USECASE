import numpy as np
from scipy.sparse import csr_matrix

A = np.array([
    [1,0,0,1,0,0],
    [0,0,2,0,0,1],
    [0,0,0,2,0,0]
])

print(A)

s = csr_matrix(A)
print(s)
B = s.todense()

print(B)