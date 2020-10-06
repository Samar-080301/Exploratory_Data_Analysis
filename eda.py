import pandas as pd 
import numpy as np
from sklearn import preprocessing
df = pd.read_csv(r'train.csv',index_col='Id')
print(df.shape)
df.head()
colsNum = df.select_dtypes(np.number).columns
colsObj = df.columns.difference(colsNum)

df[colsNum] = df[colsNum].fillna(df[colsNum].mean()//1)
df[colsObj] = df[colsObj].fillna(df[colsObj].mode().iloc[0])

label_encoder = preprocessing.LabelEncoder() 
for col in colsObj:
    df[col] = label_encoder.fit_transform(df[col])
df.head()
for col in colsObj:
    df[col] = label_encoder.inverse_transform(df[col])
df.head()
