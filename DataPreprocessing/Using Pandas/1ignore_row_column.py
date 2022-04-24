import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\train.csv')
print(df.shape)                      # shape of original data frame

plt.figure(figsize=(25, 25))

# print('Getting all rows and columns in the data frame')
# print()
pd.set_option('display.max_columns', None)    # to get all columns in the data frame
pd.set_option('display.max_rows', None)       # to get all rows

# print('To get the info of the data frame')
# print()
# df.info()                                  # gives the names of columns indicating no. of nan values
# print(df.isnull().sum())                   # gives col name and nan number

# print('Observe heat map and look for nan values')
# sns.heatmap(df.isnull())
# # white indicates nan and black for data, nan value row and col has to be removed
# plt.show()

print('Calculate % of nan values in each column')
print()
null_var = df.isnull().sum()/df.shape[0]*100
# drop_columns = null_var[null_var > 20].key()
# print(drop_columns)

print('Drop columns that have nan values more than certain percentage')
print()
df2_drop_col = df.drop(columns=['LotFrontage', 'Alley', 'FireplaceQu', 'PoolQC', 'Fence', 'MiscFeature'])
# print(df2_drop_col.shape)        # check shape after dropping columns
# better see heat map too

print('Drop rows with nan values')
print()
df3_drop_rows = df2_drop_col.dropna()
print(df3_drop_rows.shape)         # check shape after dropping rows, see heat map too

# print(df3_drop_rows.isnull().sum())
# print(df3_drop_rows.isnull().sum().sum())

print('Selecting columns with numerical values')
print()
col_name = df3_drop_rows.select_dtypes(include=['int64', 'float64']).columns
col_name_1 = list(col_name)
col_name_1.remove('Id')            # removing Id column
# print(col_name_1)

# print('using loop to visualise histogram of all cols(original and cleaned) with numerical values')
# for i, var in enumerate(col_name_1):
#     plt.subplot(6, 6, i+1)
#     sns.distplot(df3_drop_rows[var], bins=20)
#     sns.distplot(df[var], bins=20)
# plt.show()

print('Selecting columns with variables object type')
print()
obj_col_name = df3_drop_rows.select_dtypes(include=['object']).columns
# print(obj_col_name)


print('function to view objects variables(original and cleaned) and compare the initial and final values')
def cat_var_dist(vars):
    return pd.concat([df[vars].value_counts()/df.shape[0]*100,
               df3_drop_rows[vars].value_counts()/df3_drop_rows.shape[0]*100], axis=1,
              keys=[vars + '_Org', vars + '_clean'])

x = cat_var_dist('MSZoning')
print(x)










# ---------- Actual needed code to remove row and column with nan ------------#
# df = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\train.csv')
#
# drop_columns = df.isnull().sum()/df.shape[0]*100
# drop_columns = drop_columns[drop_columns > 17]
# drop_columns = list(drop_columns.keys())
# print(drop_columns)
#
# df_drop_col = df.drop(columns=drop_columns)
# df_drop_row = df_drop_col.dropna()