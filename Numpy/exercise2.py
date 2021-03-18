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

print(arr)

for i in arr:
    diff = 5
    n = str(i)
    for dig in n:
        if diff == -5:
            diff = int(dig)
        else:
            diff -= int(dig)

    print(diff)
    if diff == -1 or diff == 1:
        print(i)
