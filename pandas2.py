import numpy as np
import pandas as pd

s = pd.Series([i*2 for i in range(1,11)])
dates = pd.date_range("20170301",periods=8)
df = pd.DataFrame(np.random.randn(8,5),index = dates,columns = list("ABCDE"))
df1 = df.reindex(index = dates[:4],columns = list("ABCD")+["G"])
df1.loc[dates[0]:dates[1],"G"] = 1
print(df1)
print(df1.dropna())
print(df1.fillna("2"))
print(df.mean())
print(df.var())
s = pd.Series([1,2,4,np.nan,5,7,9,10],index = dates)
print(s)
print("shift:",s.shift(2))
print(s.diff())
# s[2]=2.0
print(s.value_counts())
print(df)
print(df.apply(np.cumsum))
print(df.apply(lambda x:x.max()-x.min()))

pieces = [df[:3],df[-3:]]

# pieces1 = [df[-3:]]

print("pieces",pieces)
# print(pieces1)
print(pd.concat(pieces))


left = pd.DataFrame({"key":["x","y"],"value":[1,2]})
right = pd.DataFrame({"key":["x","y"],"value":[3,4]})
print("LEFT",left)
print("RIGHT",right)
print(pd.merge(left,right,on="key",how="left"))
df3 = pd.DataFrame({"X":list("ABCD"),"Y":range(1,5)})
print(df3)
df4 = pd.DataFrame({'A':['one','two','three','four']*6,
                    'B':['a','b','c']*8,
                    'C':np.random.randn(24),
                    'D':np.random.randn(24)})
print(df4)
print(pd.pivot_table(df4,values=['D'],index=['B','A'],columns='C'))
# 
import time
t_time = pd.date_range("20170301",periods=10,freq="S")
print(t_time)
# 
ts=pd.Series(np.random.randn(1000),index=pd.date_range("20170301",periods=1000))
ts=ts.cumsum()
from pylab import *
ts.plot()
show()
# 
# df6 = pd.read_csv("./data/tset.csv")
print("df4:",df4)
df4.to_csv("test.csv")


