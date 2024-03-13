#%%
import pandas as pd
import numpy as np

df = pd.read_csv('ML and DS\industry_sic.csv')
# print(df.head(10))
# print(df.tail(10))
# print(df.shape)
# print(df.size)
# print(df['SIC Code'])
# print(df['SIC Code'][:3])
# print(df.sort_values(['Description']))

print(df['SIC Code'].value_counts())