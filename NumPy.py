import numpy as np
arr = np.array([[1,2,3],[4,"Hello",6],[7,8,9]])
for i in range(0,3):
    for j in range(0,3):
        print(arr[i][j], end=',')

print(type(arr[0][1]))

def disp(str):
    print("*"*40 + str + "*"*40)
#zeros attribute initializes an array with zeros of the order provided (With float data type)
disp("zeros")
zero_mat = np.zeros((4,3))
print(zero_mat)
print(type(zero_mat[0][0]))

#arange attribute generates an array of elements with interval given and also with the step value
#data type -> integer
disp("arange")
arrange = np.arange(10,25,2)
print(arrange)
print(type(arrange[0]))

#linespace attribute divides the range provided into a number od dividions
disp("linspace")
division = np.linspace(10,15,10)
print(division)

#full attribute unlike zeros fill the space with a value provided
disp("full")
fill = np.full((2,4),5)
print(fill)

#random.random attribute fills the array with random values when the order is provided
disp("random")
random = np.random.random((2,5))
print(random)

# var.shape -> provides the order of the matrix which is in the form of array
disp("shape")
print("For arange = ", arrange.shape)
print("For zeros = ", zero_mat.shape)
print("For random = ", random.shape)

#shape can also be used to re shape the array order untill the the no of elements in both array are equal
disp("re-shape with shape")
random.shape = (5,2)
print(random)

#size is used to find total number elements in the array
disp("size")
print(zero_mat.size)

#ndim returns the dimensions of the array (exaple - 1D, 2D, 3D)
disp("dimension")
print("Foe random =", random.ndim)
print("For arrange =", arrange.ndim)

#dtype returns the array data type
disp("dtype")
print("Data type of fill ndarray = ",fill.dtype)
print("Data type of arr ndarray = ",arr.dtype)
# in <U11 U stands dor unicode and 11 is the length of the array
# All strings in numpy array are of unicode datatype by default

# 