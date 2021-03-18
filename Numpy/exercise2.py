'''

You are given a number ‘N’. Your task is to find all the numbers ranging from 1 to N with the
fact that absolute difference between consecutive digits of a number is 1.
Input format:
Input contains integer N
Output format:
Output displays all the numbers that satisfy the given condition and ‘-1’ if no number is
present.
Sample Testcases:
Input 1
30
Output 1
10 12 21 23
Input 2
9
Output 2
-1

'''
import numpy as np

no = int(input())

arr = np.arange(10,no+1)

arr2 = np.zeros(0)

for i in arr:
    diff = 0
    n = str(i)
    for dig in n:
        if diff == 0:
            diff = int(dig)
        else:
            diff -= int(dig)

    if diff == -1 or diff == 1:
        arr2 = np.append(arr2,i)

if len(arr2) == 0:
    print("-1")
else:
    print(arr2)

'''
Output

12
[10 11 12]
[10. 12.]
'''