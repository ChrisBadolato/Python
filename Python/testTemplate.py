
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns



#df = pd.read_csv("pandaPractice.csv") #imports this csv file

#df = pd.read_csv("pandaPractice.csv", skiprows = 1) #skips 1 row from the top
# can also use header = 1
#df = pd.read_csv("pandaPractice.csv", header = None, names = ["extra row"])

df = pd.read_csv("pandaPractice.csv", nrows = 3) #read only 3 rows

df1 = pd.read_csv("pandaPractice.csv", na_values = ["not available", "n.a."]) #swaps out nas

df2 = pd.read_csv("pandaPractice.csv", na_values = { #will select our list and change what we want
    'eps': ["not available", "n.a."],
    'revenue': ["not available", "n.a.", -1],
    'people': ["not available", "n.a."],
    'price': ["not available", "n.a."]
    })
#df.to_csv("filename.csv", index = False) #writes without that number coulmn

#df.columns("filename.csv", index = False)

#df1.to_csv("new.csv", coulmns = ['eps', 'tickers']) #save only the rows we want

df3 = df2.groupby(['revenue'])
df4 = df2[2:4] #give us only the rows we want

#select rows by thier labels:

df5 = df2.loc[2:4, ['revenue', 'eps']] #print the rows and the columns that we want
df6 = df2.iloc[0]

df7 = df2.sort_values(by = 'revenue') #sort by the value we want
df7.head()

new_df = df2.fillna(0) #fills na with 0's

df9 = df2.fillna(method ="ffill") #carrys forward the previous value change to bfill fills from back

df10 = df2.interpolate()
