import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
DF = pd.read_excel('State11.xlsx', sheet_name ='Tabelle1', header=None)
x=DF[0:1]
plt.plot(x)
plt.show()