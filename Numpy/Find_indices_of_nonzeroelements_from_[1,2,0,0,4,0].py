#Find indices of nonzeroelements from [1,2,0,0,4,0]

import numpy as np

vector = np.nonzero([1,2,0,0,4,0])
print(vector)

'''
Output

(array([0, 1, 4], dtype=int64),)

'''