# import numpy as np
import pandas as pd
# import matplotlib

df = pd.read_csv('datasett/housing.csv')

print(df) #this file has 20k lines
df.head() #this prints out how many rows and column
df.info() #this prints out the info, can't be bothered to understand it tho
df.plot.scatter(x = 'median_income', y = 'median_house_value')