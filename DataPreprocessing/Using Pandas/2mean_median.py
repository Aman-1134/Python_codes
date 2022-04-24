import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# dataset_path = r"https://drive.google.com/file/d/1kPDgNUv9e9OQw-bhKap3CphbIJYMm2sf/view?usp=sharing"
# df = pd.read_csv(dataset_path)             # load dataset from google drive

df = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\train.csv')

pd.set_option('display.max_columns', None)    # to get all columns in the data frame
pd.set_option('display.max_rows', None)
# df.info()
# print(df.isnull().sum())
print('Percentage of missing values in columns')
missing_value_per = df.isnull().sum()/df.shape[0]*100
# print(missing_value_per)
print('After removing columns that have missing values more than 20%')
missing_value_col = missing_value_per[missing_value_per > 20].keys()
print(missing_value_col)
print('Droppig columns with nan values more than 20%')
df2_drop_col = df.drop(columns=missing_value_col)
# print(df2_drop_col.shape)

df3_num = df2_drop_col.select_dtypes(['int64', 'float64'])
# print(df3_num.head(6))

# print(df3_num[df3_num.isnull().any(axis=1)])           # Prints columns with nan values

# print(df3_num.isnull().sum())

print('Missing Numerical value columns:: Gives name of columns that have missing values')
missing_num_var = [var for var in df3_num.columns if df3_num[var].isnull().sum() > 0]
print(missing_num_var)

# for i, var in enumerate(missing_num_var):
#     plt.subplot(2, 2, i+1)
#     sns.distplot(df3_num[var], bins=20, kde={'linewidth': 5, 'color': 'k'})
# plt.show()


df4_num_mean = df3_num.fillna(df3_num.mean())
df5_num_median = df3_num.fillna(df3_num.median())

# print(df4_num_mean.isnull().sum().sum())

# for i, var in enumerate(missing_num_var):
#     plt.subplot(2, 2, i+1)
#     sns.distplot(df3_num[var], bins=20, kde_kws={'linewidth': 2, 'color': 'k'}, label='Original')
#     sns.distplot(df4_num_mean[var], bins=20, kde_kws={'linewidth': 2, 'color': 'y'}, label='Mean')
#     sns.distplot(df5_num_median[var], bins=20, kde_kws={'linewidth': 2, 'color': 'g'}, label='Median')
#
#     plt.legend()
# plt.show()


# print('Observing box plot of missing_num_var')
# for i, var in enumerate(missing_num_var):
#     plt.subplot(3, 1, 1)
#     sns.boxplot(df[var])
#     plt.subplot(3, 1, 2)
#     sns.boxplot(df4_num_mean[var])
#     plt.subplot(3, 1, 3)
#     sns.boxplot(df5_num_median[var])
# plt.show()

# print('Observing missing num var after filling nan values by mean and median')
# result = pd.concat([df3_num[missing_num_var], df4_num_mean[missing_num_var], df5_num_median[missing_num_var]])
# print(result[result.isnull().any(axis=1)])
