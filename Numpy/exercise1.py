'''

You are given a number N and following by an array of N numbers and followed by two
elements U and V. Find the minimum distance between the elements U and V in the array.
The array may have duplicates.
For example, if the array is (1, 5, 3, 7, 2, 8, 3, 4, 5, 9, 9, 3, 1, 3, 2, 9)
Minimum distance (U=4, V=7): 4
Input Format:
First Line contains integer representing number of elements N.
Second line contains N elements separated by spaces.
Third line contains two numbers separated by spaces representing U and V.
Output Format:
Output displays integer representing minimum distance

Sample Testcases:
Input 1
16
1 5 3 7 2 8 3 4 5 9 9 3 1 3 2 9
4 7
Output 1
4
Input 2
16
1 5 3 7 2 8 3 4 5 9 9 3 1 3 2 9
2 5
Output 2
3

'''
import numpy as np

no = int(input())

arr1 = list(map(int, input().split()))
arr = np.asarray(arr1)
arr = arr[:no]

nos1 = list(map(int, input().split()))
nos = np.asarray(nos1)


l1 =np.where(arr == nos[0])

l2 =np.where(arr == nos[1])


min = -5

for i in l1[0]:
    for j in l2[0]:
        if min == -5:
            min = i-j
            if min < 0:
                min *=-1
        else:
            t = i-j   
            if t < 0:
                t *=-1
            if t < min:
                min = t   

print(min)                  

'''
Output

16
1 5 3 7 2 8 3 4 5 9 9 3 1 3 2 9
4 7
4

'''