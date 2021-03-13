#Create a 10x10 array with random values and find the minimum and maximum values



import numpy as np

vector = np.random.random((10,10))
print(vector)

vectormin, vectormax = vector.min(), vector.max()
print("Min and Max Values are {} {}".format(vectormin, vectormax))

'''
Output

[[0.12550501 0.67354724 0.46976306 0.17857004 0.41799088 0.79748651
  0.71952001 0.67197944 0.30374412 0.64959602]
 [0.65427897 0.07051475 0.44225515 0.07487936 0.68088358 0.14297235
  0.73003527 0.11935787 0.90218136 0.52497425]
 [0.57581764 0.14687619 0.68110441 0.86164149 0.63427569 0.32625567
  0.2201331  0.51133801 0.43185914 0.48434923]
 [0.47827802 0.18948726 0.69063049 0.4547992  0.68245391 0.64868934
  0.88133822 0.86382666 0.27706851 0.62753515]
 [0.07620602 0.38404498 0.69373068 0.87047015 0.77550584 0.58227092
  0.264905   0.57504966 0.41908174 0.14360464]
 [0.41530401 0.71306006 0.59813264 0.79708473 0.67856933 0.00334452
  0.26554785 0.69453177 0.27561135 0.09676075]
 [0.74159265 0.85420118 0.20406314 0.84174059 0.82338553 0.11215458
  0.79702707 0.4095897  0.30692367 0.98764861]
 [0.86437091 0.92877053 0.46193379 0.62741333 0.20199029 0.81197367
  0.44542966 0.22565584 0.63500462 0.07265691]
 [0.08469258 0.48588447 0.87393032 0.28152369 0.89722044 0.85493987
  0.88664323 0.36820411 0.2887893  0.28213185]
 [0.99492061 0.99792388 0.71199794 0.61248477 0.99659416 0.52472807
  0.34090647 0.15698089 0.4833254  0.02724507]]
Min and Max Values are 0.00334451832370275 0.9979238793424652

'''