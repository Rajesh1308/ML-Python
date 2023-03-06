import numpy as np

def disp(str):
    print("*"*40 + str + "*"*40)

arr1 = np.array([[8,4,6],[6,3,2]])
arr2 = np.array([[12,65,45],[21,54,87]])
array1 = np.array([5,3,6])
array2 = np.array([4,0,8])

# here the arr has the dimension of 2 x 1 but array has the order of 1 x 1
# But it computes something
# Here the array had broadcasted itself in such a way that it could add up to arr
# In array [5,3,6] has converted into [[5,3,6],[5,3,6]] while adding (inorder to match with other array)
# This is called broadcasting 
sum = arr1 + array1
#print(sum)

#slicing and indexing
print(arr1[:2])
print(arr1[:2][0])
print(arr1[:2][0][0:2])
print(arr1[:1,1:])

######################################################################
#                       Array Manipulation                           #
######################################################################

#concatenate joins two arrays of same (1D) dimension into a single array
print("Horizontal concatenate...")
conc = np.concatenate((arr1,arr2), axis=0)
print(conc)

#axis can be set 1 for 2 and multi dimensional arrays
print("Vertical concatenate...")
conc = np.concatenate((arr1,arr2), axis=1)
print(conc)
#Output will be
#[[ 8  4  6 12 65 45]
# [ 6  3  2 21 54 87]]

#vstack -> stackes vertically
print("vstack")
vstack = np.vstack((arr1,arr2))
print(vstack)
#Output will be
#[[ 8  4  6]
# [ 6  3  2]
# [12 65 45]
# [21 54 87]]

#hstack -> stacks horizontally
print("hstack")
hstack = np.hstack((arr1,arr2))
print(hstack)
#Output will be 
#[[ 8  4  6 12 65 45]
# [ 6  3  2 21 54 87]]

#colum_stack -> stackes the array to the next column
# Imagine everything as a matrix - It will be helpful to understand the concepts
print("Column stack")
col_stack = np.column_stack((arr1,arr2))
print(col_stack)
#Output will be
#[[ 8  4  6 12 65 45]
# [ 6  3  2 21 54 87]]

#Instead of using vstack nad hstack we can simply use stack and set axis as 1 and 0
#where 1 means vertical stack and 0 means horizontal stack

######## NOTE :
# Horizonatl concatenation and Vertical stacking are same
# Similarly, Vertical concatenation and Harizontal stacking are same


