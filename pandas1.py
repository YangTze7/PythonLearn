import pandas as pd
import numpy as np

s = pd.Series([i * 2 for i in range(1, 11)])
print(type(s))
dates = pd.date_range("20170301", periods=8)
df = pd.DataFrame(np.random.randn(8, 5), index=dates, columns=list("ABCDE"))
# print(df)
print(df.head(3))
print(df.tail(3))
#
print(df.index)
print(df.values)
print(df.sort_values("C"))
print(df.sort_index(axis=1, ascending=False))
print(df.describe())
#
print(type(df["A"]))
print(df[:3])
#
print(df["20170301":"20170304"])
print(df.loc[dates[0], "C"])
#
print(df.iloc[0:3, 2:4])
print(df.iloc[1, 4])
print(df.iat[1, 4])
#
print(df[df.B > 0][df.A > 0])
print(df[df > 0])
print(df[df.index.isin(["20170301", "20170303"])])
#
s1 = pd.Series(list(range(10,18)), index = pd.date_range("20170301", periods = 8))
df["F"] = s1
print(df)
df.at[dates[0],"A"] = 0
print(df)
df.iat[1,1] = 1
df.loc[:,"D"]=np.array([4]*len(df))
print(df)
print(len(df))
df2=df.copy()
df2[df2<0]=-df2
print(df2)

