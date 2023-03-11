import pandas as pd
covid = pd.read_csv(r"C:\Users\rajes\OneDrive\Desktop\Country-wise-COVID-cases.csv")

def disp(str):
    print("*"*40 + str + "*"*40)

#Changing the data type of data in csv file
covid.Country_Name = covid.Country_Name.astype(str)


print(covid)
print(covid["Death_%"])

#Each column in data frame is a series
print(type(covid))
print(type(covid.Country_Name))

#To print first n rows
print(covid.head(10))
#To print last n rows
print(covid.tail(10))

print(covid.shape)

#prints informations about the file
print(covid.info())

#Counting null data in columns
print(covid.info(null_counts=True))

#Min and Max
print(covid.max())
print(covid.min())

#Statistical functions
disp("Statistical fn")
disp("Mean")
print(covid.mean())
disp("Median")
print(covid.median())
disp("Standard deviation")
print(covid.std())

#Accessing specific value
disp("Standard devisation of specific column")
print(covid["Death_%"].std())

#Count for not null
disp("Count")
print(covid.count())

#Decribe function do all above for us
disp("Describe")
print(covid.describe())

###################################Cleaning##############################################
#renameing column
covid = covid.rename(columns={'Death_%' : 'Death'})
print(covid)

#Filling the mean value in blank space -> fillin function will be used for this
covid.Total_Recovered = covid.Total_Recovered.fillna(covid.Total_Recovered.mean())
print(covid.info())

