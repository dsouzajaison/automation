import numpy as np
import  pandas as pd
from fourier import fourier_transform1
from fourier import fourier_transform2

#fftsignal1 = fourier_transform1()
#fftsignal2 = fourier_transform2()


def featuretraction():
    print(" Extract few features")
    fsm1 = np.mean(fftsignal1, axis=1)
    fsm2 = np.mean(fftsignal2, axis=1)
    fssd1 = np.std(fftsignal1, axis=1)
    fssd2 = np.std(fftsignal2, axis=1)
    ffv1 = np.var(fftsignal1, axis=1)
    ffv2 = np.var(fftsignal2, axis=1)
    d1 = pd.DataFrame()
    d1['mean'] = fsm1
    d1['std'] = fssd1
    d1['var'] = ffv1
    state1 = 'state1'
    d1['state'] = state1
    d2 = pd.DataFrame()
    d2['mean'] = fsm2
    d2['std'] = fssd2
    d2['var'] = ffv2
    state2 = 'state2'
    d2['state'] = state2
    df = pd.concat([d1, d2], ignore_index=True)
    df=df.reset_index(drop=True)
    df.to_excel("FeatureData123.xlsx")
    df=df.iloc[np.random.permutation(len(df))]
    print("saved feature file")
