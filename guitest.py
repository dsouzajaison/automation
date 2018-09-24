import tkinter
from  tkinter import filedialog
import  pandas as pd
from keras.models import load_model
from scipy.fftpack import fft
import numpy as np
from tkinter import *


def main():

    tkinter.Tk().withdraw() # Close the root window
    in_path =filedialog.askopenfilename()
    print (in_path)
    data= pd.read_excel(in_path)
    print(data)
    data = fft(data)
    data = abs(data)
    print(data)
    fm = np.mean(data, axis=1)
    fsd = np.std(data, axis=1)
    fv = np.var(data, axis=1)
    d = pd.DataFrame()
    d['mean'] = fm
    d['std'] = fsd
    d['var'] = fv
    d.to_excel("FeatureData.xlsx")
    clf = load_model('my_model.h5')
    result = clf.predict_classes(d)
    print(result)
    root=Tk()
    root.title("Automation Results")
    root.geometry("400x400")
    Results = Label( text=result)
    Results.grid(row=1, column=1)
    Results.pack()
    root.mainloop()
if __name__ == "__main__":
    main()