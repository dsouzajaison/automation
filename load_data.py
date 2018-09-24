import numpy as np
import pandas as pd

def load_data():
    print(" reading data from excel sheets")
    # import state 1 and stste2 data from excelsheet
    DF = pd.read_excel('State11.xlsx', sheet_name='Tabelle1', header=None)
    DF1 = pd.read_excel('State12.xlsx', sheet_name='Tabelle1', header=None)
    # merge state1 data from two different  excel files
    print("merging two files")
    merge1 = DF.append(DF1)
    merge1 = merge1.reset_index(drop=True)
    print("Merging Completed")
    return merge1


def load_data2():
    print("Loading state2 data")
    DF2 = pd.read_excel('State2.xlsx', sheet_name='Tabelle1', header=None)
    return DF2