import numpy as np
import  pandas as pd
import keras
from keras.layers import Dense,Activation,Dropout
from keras.models import Sequential
from keras.models import load_model
from importlib import reload
df = pd.read_excel("FeatureData.xlsx")
F = df.iloc[:94]
L = df.iloc[1020:]
new_df = F.append(L)
new_df = new_df.reset_index(drop=True)
new_df = new_df.iloc[np.random.permutation(len(new_df))]
new_df = new_df.reset_index(drop=True)
print(new_df)
newX = new_df[['mean', 'std', 'var']]
clf = load_model('my_model.h5')
result= clf.predict_classes(newX)
print(result)