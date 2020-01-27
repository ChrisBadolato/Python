import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,11,45,23,45,15,80]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages, bins, histtype='bar', rwidth = 0.8)



#ids = [x for x in range(len(population_ages))]
#distribution
#plt.bar(ids, population_ages)

plt.xlabel('x')
plt.ylabel('y')
plt.title('interesting graph')
plt.legend()
plt.show()
