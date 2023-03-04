import numpy as np

def disp(str):
    print("*"*40 + str + "*"*40)

arr = np.array([8,4,6,5,9])
array = np.array([5,3,6,8,5])

#equal attribute checks each and every alement of the array
#and provides the boolean output -> True or False
disp("equal")
is_equal = np.equal(arr,array)
print(is_equal)

#array_equal checks the entire array
#and provides the boolean output -> True or False
disp("array equal")
is_array_equal = np.array_equal(arr,array)
print(is_array_equal)

#Minimum and Maximum
disp("min and max")
min = np.min(arr)
print("Minimum number of arr = ",np.min(arr))
max0 = np.max(arr)
print("Maximum number of arr = ",np.max(arr))

#statistical attributes in numpy
disp("Statistical fn")
print("All for arr")
print("Mean = ",np.mean(arr))
print("Median = ",np.median(arr))
print("Standard deviation = ",np.std(arr))
print("Correlation coefficient = ",np.corrcoef(arr))
