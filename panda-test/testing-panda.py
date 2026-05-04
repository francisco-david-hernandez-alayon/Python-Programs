import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
print(s.array)
print(s.index.array)
print(s.to_numpy)

dates = pd.date_range("20130101", periods=6, freq='YS')
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

long_series = pd.Series(np.random.randn(1000))
print(long_series.head())
print(long_series.tail(3))

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)

print(df2[:2])
df2.columns = [x.lower() for x in df2.columns]
print(df2)

print(df.describe()) # little summary of data
print(df.T) # Transponse data
print(df.sort_index(axis=0, ascending=False)) # order
print(df.sort_index(axis=0, ascending=True)) # order
print(df.sort_index(axis=1, ascending=False)) # order
print(df.sort_index(axis=1, ascending=True)) # order
dfT = df.T
print(dfT)
print(dfT.sort_values(by="2013-01-01", ascending=False))
print(dfT.sort_values(axis=1, by=["A", "B"], ascending=True))
print(dfT.sort_values(axis=1, by=["B", "A"], ascending=True))



