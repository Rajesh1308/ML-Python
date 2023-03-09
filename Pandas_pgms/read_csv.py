import pandas as pd
covid = pd.read_csv(r"C:\Users\rajes\OneDrive\Desktop\Country-wise-COVID-cases.csv")
print(covid)
print(covid["Death %"])