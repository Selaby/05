import pandas as pd

df = pd.read_csv('sample_pandas_normal.csv', index_col=0)
print(df)

name = "Ellen"
print(df.at[name, 'age'])