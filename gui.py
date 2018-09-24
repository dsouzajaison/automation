import tkinter
from  tkinter import filedialog
import  pandas as pd
from keras.models import load_model
from scipy.fftpack import fft
import numpy as np


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
if __name__ == "__main__":
    main()