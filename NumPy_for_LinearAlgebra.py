# numpy can be used for linear algebra as well 
# that helps in arithematics operations of array
import numpy as np

def disp(str):
    print("*"*40 + str + "*"*40)

# funcions include
# sum, subtract, multiply, divide, exp, sqrt, sin, cos, log
arr = np.array([8.0,4,1,5,9])
array = np.array([5.0,3,6,8,5])

disp("Array data types")
print(array.dtype)
print(arr.dtype)

# sum attribute is used o add all the elements of ndarray
disp("sum")
ans = np.sum(array)
print(ans)
#for row wise sum set axis = 1
disp("row wise sum")
ans = np.sum((array,arr), axis=1)
print(ans)

#for column wise sum set axis = 0
disp("column wise sum")
ans = np.sum((array,arr), axis=0)
print(ans)


#other attributes - it can take values alone or take whole arrays with same no of elements
disp("subtract")
ans = np.subtract(arr,array)
print(ans)

# exp attribute  compute the e power of array elements
disp("exp")
ans = np.exp(arr)
print(ans)

disp("sin")
ans = np.sin(arr)
print(ans)

disp("Multiply")
ans = np.multiply(arr,array)
print(ans)