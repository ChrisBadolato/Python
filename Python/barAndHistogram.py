import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

x = [2,4,6,8,10]
y = [6,7,8,2,4]



x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]

plt.bar(x,y, label = 'bars1', color = 'blue')
plt.bar(x2,y2, label = 'bars2', color = 'g')

plt.xlabel('x')
plt.ylabel('y')
plt.title('interesting graph')
plt.legend()
plt.show()
