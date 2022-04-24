import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\train.csv')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
miss_val_per = df.isnull().sum()/df.shape[0]*100
miss_val_col = miss_val_per[miss_val_per > 20].keys()
df = df.drop(columns=miss_val_col)

num_var_col = df.select_dtypes(['int64', 'float64'])
miss_num_col = [var for var in num_var_col if num_var_col[var].isnull().sum() > 0]
cat_vars = ['LotConfig', 'Exterior2nd', 'KitchenQual']

for cat, miss in zip(cat_vars, miss_num_col):
    for var in df[cat].unique():
        df.update(df[df.loc[:, cat] == var][miss].replace
                  (np.nan, df[df.loc[:, cat] == var][miss].mean()))

cat_var_col = df.select_dtypes('O')
miss_cat_col = [var for var in cat_var_col if cat_var_col[var].isnull().sum() > 0]

for var in miss_cat_col:
    cat_var_col[var].fillna(cat_var_col[var].mode()[0], inplace=True)

df.update(cat_var_col)
print(df.isnull().sum())

sns.heatmap(df.isnull())
plt.show()
