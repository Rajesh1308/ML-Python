import numpy as np
import pandas as pd

# One dimensions - SeriesObject
# Two dimensions - DataFrams
# Three dimensions - PanelData

data = [5,6,4,9,1]
srs = pd.Series(data)
print(srs)

#indexing
data = [5,6,4,9,1]
srs = pd.Series(data, index = ['a','b','c','d','e'])
print(srs['a'])
print(srs['a':'c'])

# DataFrames - support columns of different types
#            - Mutable size, Label access and arithematic operations on rows and columns
# In dataframes all individual columns are a series object 


#List to DataFrame
data = [[1,2,3,4,5,0],[6,7,8,9]]
df = pd.DataFrame(data)
print(df)

#Dictionary to DataFrame
data = {"col1" : [1,2,3,4,5],"col2" : [6,7,8,9,10]}
df1 = pd.DataFrame(data)
print(df1)

data = {"col3" : [11,22,33,44,55],"col4" : [60,70,80,90,100]}
df2 = pd.DataFrame(data)
print(df2)

#another example
dict = {"Fruit" : ["Apple","Mango","Orange","Pineapple"], "Count" : [60,54,89,25]}
df = pd.DataFrame(dict)
print(df)

# np array to dataframes
arr = np.array([[2,3,54,87,98],[6,5,3,2,1]])
dfa = pd.DataFrame(arr)
print(dfa)

#concat joins the one dataframe at the bottom of another dataframe
print(pd.concat([df1,df2])) # This is outer join
print(pd.concat([df1,dfa], axis=1,join="inner")) # A fun happens for array and dictionary
print(pd.concat([df1,df2], axis=1,join="inner")) # properly adds the data to the column since axis is set 1




