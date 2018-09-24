from scipy.fftpack import fft
from load_data import  load_data
from  load_data import  load_data2


def fourier_transform1():
    print("Fourier transform of state1")
    ff = fft(load_data())
    ftsignal1 = abs(ff)
    return ftsignal1
def fourier_transform2():
    print("Fourier transfrom of state2")
    ff2 = fft(load_data2())
    fftsignal2 = abs(ff2)
    return  fftsignal2
