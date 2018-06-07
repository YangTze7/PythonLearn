import pandas as pd
import numpy as np



def unique_element(x):
    a=len(np.unique(x))
    return a

df = pd.read_excel("20170209.xlsx")
print(unique_element(df['ID']))
