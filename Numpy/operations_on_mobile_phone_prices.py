'''
 Perform the following operations on an array of mobile phones prices 6999, 7500, 11999,
27899, 14999, 9999.
a. Create a 1d-array of mobile phones prices
b. Convert this array to float type
c. Append a new mobile having price of 13999 Rs. to this array
d. Reverse this array of mobile phones prices
e. Apply GST of 18% on mobile phones prices and update this array.
f. Sort the array in descending order of price
g. What is the average mobile phone price
h. What is the difference b/w maximum and minimum price

'''

import numpy as np

arr = np.array([6999, 7500, 11999,
27899, 14999, 9999]);  #Create a 1d-array of mobile phones prices

print(arr)

arr = arr.astype(np.float); #Convert this array to float type

print(arr)

arr2 = np.append(arr , 13999) #Append a new mobile having price of 13999 Rs. to this array

print(arr2)

arr2 = arr2[::-1] #Reverse this array of mobile phones prices

print(arr2)

m = (arr2 != 0)

arr2[m] = arr2[m] - (arr2[m] * (18 /100)) #Apply GST of 18% on mobile phones prices and update this array.

print(arr2)

arr2 = np.sort(arr2)[::-1] #Sort the array in descending order of price

print(arr2)

print(np.average(arr2)) #What is the average mobile phone price

print(arr2.max() - arr2.min()) #What is the difference b/w maximum and minimum price

'''
Output

[ 6999  7500 11999 27899 14999  9999]
[ 6999.  7500. 11999. 27899. 14999.  9999.]
[ 6999.  7500. 11999. 27899. 14999.  9999. 13999.]
[13999.  9999. 14999. 27899. 11999.  7500.  6999.]
[11479.18  8199.18 12299.18 22877.18  9839.18  6150.    5739.18]
[22877.18 12299.18 11479.18  9839.18  8199.18  6150.    5739.18]
10940.439999999999
17138.0

'''