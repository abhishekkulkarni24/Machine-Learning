#Given a 1D array, negate all elements which are between 3 and 8, in place


import numpy as np

arr = np.arange(8)
m = (arr > 2) & (arr < 8)
arr[m] *= -1
print(arr)

'''
Output

[ 0  1  2 -3 -4 -5 -6 -7]

'''