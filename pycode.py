import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler

ds = pd.read_csv('data.csv')
features = []
dtype = []
for feature, type in zip(features, dtype):
    ds[feature] = ds[feature].astype(type)
ds = pd.get_dummies(ds, columns=['sex'])             

print(ds)
s = MinMaxScaler()
s.fit(ds[['rate']] )
ds[['rate']] = s.transform(ds[['rate']] )

ds[['rate']] = s.transform(ds[['rate']] )

print(ds)ds.dropna(axis=0  , how='any' , inplace=True) 

print(ds)
std = StandardScaler()
ds[['age']] = std.fit_transform(ds[['age']] )

ds[['age']] = std.transform(ds[['age']] )

print(ds)