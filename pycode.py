import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.feature_selection import SelectKBest, chi2
ds = pd.read_csv('data.csv')
features = []
dtype = []
for feature, type in zip(features, dtype):
    ds[feature] = ds[feature].astype(type)
ds.dropna(axis=0 , subset=['name'] , inplace=True) 
ds.drop(columns=['name', 'hometown'], inplace=True) 
ds.rename(columns={'rate': 'score'}, inplace=True) 

# ds['rank'] => {'VERY-BAD': 0, 'BAD': 1, 'GOOD': 2, 'EXCELENT': 3}
ds['rank'] = ds['rank'].map({'VERY-BAD': 0, 'BAD': 1, 'GOOD': 2, 'EXCELENT': 3}) 
ds = pd.get_dummies(ds, columns=['gender'])             

imp = SimpleImputer(missing_values=np.nan, strategy="mean")
ds[["age"]] = imp.fit(ds[["age"]]).transform(ds[["age"]]) 
ds = ds.astype({'age': 'int32'}, copy=False)kbest = SelectKBest(chi2, k=2).fit(ds.loc[:, ds.columns != 'rank'], ds['rank'])
selected_cols = kbest.get_support(indices=True)
k_best = ds.iloc[:,selected_cols]

kbest = None
selected_cols = None
print(ds)

print(k_best)

s3 = StandardScaler()
k_best[['score']] = s3.fit_transform(k_best[['score']] )

k_best[['score']] = s3.transform(k_best[['score']] )

s3 = StandardScaler()
k_best[['score']] = s3.fit_transform(k_best[['score']] )

print(ds)

print(k_best)

ds1 = pd.read_csv('data.csv')
features = []
dtype = []
for feature, type in zip(features, dtype):
    ds1[feature] = ds1[feature].astype(type)

print(ds1)

print(ds1)

print(ds1)

ds2 = pd.read_csv('data.csv')
features = []
dtype = []
for feature, type in zip(features, dtype):
    ds2[feature] = ds2[feature].astype(type)
ds2.dropna(axis=1  , inplace=True) 

print(ds2)

ds3 = pd.read_csv('data.csv')
features = []
dtype = []
for feature, type in zip(features, dtype):
    ds3[feature] = ds3[feature].astype(type)

ds3 = pd.read_csv('data.csv')
features = []
dtype = []
for feature, type in zip(features, dtype):
    ds3[feature] = ds3[feature].astype(type)

print(ds3)
ds3.dropna(axis=1 , subset=[2, 5] , inplace=True) 

print(ds3)

ds4 = pd.read_csv('data.csv')
features = []
dtype = []
for feature, type in zip(features, dtype):
    ds4[feature] = ds4[feature].astype(type)
ds.dropna(axis=0 , subset=['age'] , inplace=True) 

print(ds4)

ds10 = pd.read_csv('data.csv')
features = []
dtype = []
for feature, type in zip(features, dtype):
    ds10[feature] = ds10[feature].astype(type)

print(ds10)
ds10.dropna(axis=0 , subset=['name'] , inplace=True) 

print(ds10)
