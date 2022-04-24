import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------- Data cleaning according to the class of domain -------- #

df = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\train.csv')

pd.set_option('display.max_columns', None)    # to get all columns in the data frame
pd.set_option('display.max_rows', None)
missing_value_per = df.isnull().sum()/df.shape[0]*100  # nan percentage calculation in each column
missing_value_col = missing_value_per[missing_value_per > 20].keys()
df2_drop_col = df.drop(columns=missing_value_col)         # ignoring columns where nan % > 20
df3_num = df2_drop_col.select_dtypes(['int64', 'float64'])     # select numerical variable columns

# print(df3_num.isnull().sum())
# missing_num_var = ['LotFrontage', 'MasVnrArea', 'GarageYrBlt']  # same result by below
missing_num_var = [var for var in df3_num.columns if df3_num[var].isnull().sum() > 0]  # columns still having nan
# print(df3_num[missing_num_var][df3_num[missing_num_var].isnull().any(axis=1)])    # print columns still having nan

# print('Types of object variables in LotConfig::')
unique = df['LotConfig'].unique()
# print(unique)

# print(df[df.loc[:, 'LotConfig'] == 'Inside']['LotFrontage'])   # print LotFrontage with LotConfig == Inside

# print(df[df.loc[:, 'LotConfig'] == 'Inside']['LotFrontage'].replace
#       (np.nan, df[df.loc[:, 'LotConfig'] == 'Inside']['LotFrontage'].mean()))  # does for a single class in LotConfig
# impute mean of Domain 'LotConfig' with class 'Inside' and place in nan values in 'LotFrontage'

df_copy_mean = df.copy()
# for var_class in df['LotConfig'].unique():      # does for all classes in LotConfig
#     df_copy.update(df[df.loc[:, 'LotConfig'] == var_class]['LotFrontage'].replace
#           (np.nan, df[df.loc[:, 'LotConfig'] == var_class]['LotFrontage'].mean()))


missing_num_var = ['LotFrontage', 'MasVnrArea', 'GarageYrBlt']
# cat_vars = ['LotConfig', 'MasVnrType', 'GarageType']
# Here domain LotConfig has data and remaining both has nan so cannot impute mean
cat_vars = ['LotConfig', 'Exterior2nd', 'KitchenQual']
for cat_var, miss in zip(cat_vars, missing_num_var):
    for var_class in df[cat_var].unique():
        df_copy_mean.update(df[df.loc[:, cat_var] == var_class][miss].replace
              (np.nan, df[df.loc[:, cat_var] == var_class][miss].mean()))

df_copy_median = df.copy()
for cat_var, miss in zip(cat_vars, missing_num_var):
    for var_class in df[cat_var].unique():
        df_copy_median.update(df[df.loc[:, cat_var] == var_class][miss].replace
              (np.nan, df[df.loc[:, cat_var] == var_class][miss].median()))

# print(df_copy[missing_num_var].isnull().sum())

for i, var in enumerate(missing_num_var):
    plt.subplot(2, 2, i+1)
    sns.distplot(df[var], bins=20, kde_kws={'linewidth': 2, 'color': 'k'}, label='Original')
    sns.distplot(df_copy_mean[var], bins=20, kde_kws={'linewidth': 2, 'color': 'y'}, label='Mean')
    sns.distplot(df_copy_median[var], bins=20, kde_kws={'linewidth': 2, 'color': 'g'}, label='Median')

plt.show()

# print('Checking for outliers using boxplot')
# for i, var in enumerate(missing_num_var):
#     plt.subplot(3, 1, 1)
#     sns.boxplot(df[var])
#     plt.subplot(3, 1, 2)
#     sns.boxplot(df_copy_mean[var])
#     plt.subplot(3, 1, 3)
#     sns.boxplot(df_copy_median[var])
# plt.show()




















# i = 0
# for category in cat_vars:
#     i += 1
#     for var_class in df[category].unique():
#         df_copy.update(df[df.loc[:, category] == var_class][missing_num_var[i]].replace
#                    (np.nan, df[df.loc[:, category] == var_class][missing_num_var[i]].mean()))
#
# print(df_copy.isnull().sum().sum())