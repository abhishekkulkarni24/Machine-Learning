#Create random vector of size 10 and replace the maximum value by 0


import numpy as np

vector = np.random.random(10)
print(vector)
vector[vector.argmax()] = 0 
print(vector)

'''
Output

[0.01786029 0.94713919 0.74541354 0.30847086 0.25722718 0.55252997
 0.13957466 0.1592468  0.40922771 0.94977814]
[0.01786029 0.94713919 0.74541354 0.30847086 0.25722718 0.55252997
 0.13957466 0.1592468  0.40922771 0.        ]

'''