import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns

df = pd.read_excel('people.xlsx',sheet_name = 'Sheet1', index_col=None, na_values =['NA'] , header = 1)

df1 = df.groupby(['Weight'])

df2 = df1.agg('mean')
