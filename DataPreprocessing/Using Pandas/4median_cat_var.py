import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\train.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_row', None)

cat_var = df.select_dtypes(include='object')
# miss_val_per = df.isnull().sum()/df.shape[0]*100
miss_val_per = cat_var.isnull().mean()*100
miss_val_col = miss_val_per[miss_val_per > 20].keys()
cat_var = cat_var.drop(columns=miss_val_col)
print(miss_val_col)

isnull_per = cat_var.isnull().mean()*100
isnull_col = isnull_per[isnull_per > 0].keys()
# print(isnull_col)

# print(cat_var['MasVnrType'].value_counts())
# print(cat_var['MasVnrType'].mode())

# cat_var['MasVnrType'].fillna(cat_var['MasVnrType'].mode()[0])

for var in isnull_col:
    cat_var[var].fillna(cat_var[var].mode()[0], inplace=True)
    # print(var, '=', cat_var[var].mode()[0])

# df.update(cat_var)
# df.drop(columns=miss_val_col)
# print(df.select_dtypes(include='object').isnull().sum())

