import tkinter
from  tkinter import filedialog
import  pandas as pd
from keras.models import load_model
import numpy as np
import pywt
from tkinter import *
from sklearn.metrics import classification_report,confusion_matrix

def main():

    tkinter.Tk().withdraw() # Close the root window
    in_path =filedialog.askopenfilename() #Select the file which you need to predict
    print (in_path)# Prints the path of the file
    print("Loading data.........")
    data= pd.read_excel(in_path,header=None)
    print(data)
    data = pd.DataFrame(data)
    #Discrete Wavelet Transform is peroformed
    cA, cD = pywt.dwt(data, 'haar')
    cA, cD = pywt.dwt(cA, 'haar')
    cA, cD = pywt.dwt(cA, 'haar')
    #Feature Extraction of the Raw data
    mfcA = np.mean(abs(cA), axis=1)
    mfcD= np.mean(abs(cD), axis=1)
    mfcA = np.max(abs(cA), axis=1)
    mfcD = np.max(abs(cD), axis=1)
    rmscA = np.square(cA)
    rmscA = np.mean(rmscA, axis=1)
    rmscA = np.sqrt(rmscA)
    rmscD = np.square(cD)
    rmscD = np.mean(rmscD, axis=1)
    rmscD = np.sqrt(rmscD)
    # Create a Dataframe
    d = pd.DataFrame()
    #Store the Extracted Features
    d['mfcA'] = mfcA
    d['mfcD'] = mfcD
    d['rmscA'] = rmscA
    d['rmscD'] = rmscD
    d['maxcA'] = mfcA
    d['maxcD'] = mfcD
    #Save to a excel Sheet
    d.to_excel("FeatureData_wavetranform.xlsx")
    print("Loading the model....")
    #Load the Pre-Trained Model
    clf = load_model('my_wavelet_model_full12.h5')
    print("Predicting the States......")
    #predict the Values
    result = clf.predict_classes(d[:])
    print(" The Value '0' Corresponds to State1                The Value '1' Corresponds to State2")
    print(result)
    #arrat to String Conversion
    str1 = '   '.join(str(e) for e in result)
    root = Tk()
    # optionally give it a title
    root.title("Machine State Result WIndow")
    Label(root,text=" The Value '0' Corresponds to State1                The Value '1' Corresponds to State2 ").pack()
    w = Label(root, text=str1)
    w.pack()
    root.mainloop()
if __name__ == "__main__":
    main()