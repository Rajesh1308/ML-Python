import numpy as np

def disp(str):
    print("*"*40 + str + "*"*40)

arr = np.array([[8,4,6],[6,3,2]])
array = np.array([5,3,6])

# here the arr has the dimension of 2 x 1 but array has the order of 1 x 1
# But it computes something
# Here the array had broadcasted itself in such a way that it could add up to arr
# In array [5,3,6] has converted into [[5,3,6],[5,3,6]] while adding (inorder to match with other array)
# This is called broadcasting 
sum = arr + array
print(sum)

