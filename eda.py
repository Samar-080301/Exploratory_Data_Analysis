import pandas as pd 
from sklearn import preprocessing
df = pd.read_csv(r'train.csv',index_col='Id')
df.head()
label_encoder = preprocessing.LabelEncoder() 
for col in df.columns:
      
    if df[col].dtype == 'O':
        df[col] = label_encoder.fit_transform(df[col])
    print(col) #to check the malacious column
print(df) 
