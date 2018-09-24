import keras
import numpy as np
import pandas as pd
from scipy.fftpack import fft
from  fourier import  fourier_transform2,fourier_transform1
from feature_extraction import  featuretraction
#Import required libraries
 #library for neural network#loading data in table form
#import seaborn as sns #visualisation
#import matplotlib.pyplot as plt #visualisation
from sklearn.preprocessing import normalize #machine learning algorithm library
from keras.models import Sequential
from keras.layers import Dense,Activation,Dropout
from keras.layers.normalization import BatchNormalization
from keras.utils import np_utils
from model import model_nn

def main():
    global data
    global data2
    global  df
    #data=fourier_transform1()
    print("FFt Data1 completed")
    #data2= fourier_transform2()
    print("FFt Dat2 completed")
    #featuretraction()
    print("Features are extracted")
    df = pd.read_excel("FeatureData.xlsx")
    X = df[['mean', 'std', 'var']]
    y = df['state']
    print("x nd y")
    model_nn()




if __name__ == '__main__':
    main()



newy = new_df['state']
X_normalized = newX
total_length = len(new_df)
train_length = int(0.8 * total_length)
test_length = int(0.2 * total_length)

X_train = X_normalized[:train_length]
X_test = X_normalized[train_length:]
y_train = newy[:train_length]
y_test = newy[train_length:]
print("Length of train set x:", X_train.shape[0], "y:", y_train.shape[0])
print("Length of test set x:", X_test.shape[0], "y:", y_test.shape[0])
model = Sequential()
model.add(Dense(1000, input_dim=3, activation='relu'))
model.add(Dense(500, activation='relu'))
model.add(Dense(300, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(2, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

score = model.evaluate(X_test, y_test, verbose=1)
print('Test accuracy:', score[1])
#from importlib import reload
#reload(keras.models)
