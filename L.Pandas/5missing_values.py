import pandas as pd
import numpy as np

df = pd.read_csv('D:\\Excel Demo\\missing_value.csv', na_values=['not avaliable', 'no value'])
print('Data frame with missing values:')
print('Note that some strings like #N/A, null, #NA, nan etc are also interpreted as NaN:')
# or use dictionary as < na_values={'Roll No': 'no value'} >
print()
print(df)

print()
print("Using na_values to show 'not avaliable' and 'no values' as NaN:")
df1 = pd.read_csv('D:\\Excel Demo\\missing_value.csv', na_values=['not avaliable', 'no value'], keep_default_na=False)
print(df1)

print('Using na_filter:')
print('If true filters null values and prints instead:')
df2 = pd.read_csv('D:\\Excel Demo\\missing_value.csv', na_filter=True)
print(df2)

print('To see places where null values are present:')
print(df.isnull())
print('Gives header name and number of null values in that column:')
print(df.isnull().sum())
print('Total number of null values in a dataframe:', df.isnull().sum().sum())
print()

# similar for df.notnull()

sr = pd.Series([1, 3, np.NaN, 8, np.nan])
print(sr)
print()

print(sr.isnull())
print('Total no of null=', sr.isnull().sum())

# print(df.dropna())             # removes rows with null values
# print(df.dropna(axis=1))       # removes columns with null values

# print(df.dropna(how='any'))      # same as dropna
# print(df.dropna(how='all'))      # if all terms of data frame are null
print('With threshold value')
print(df.dropna(thresh=1))         # thresh=1, means only the rows that have minimum of one not null element is printed
print()
print('With subset Marks')
print(df.dropna(subset=['Marks']))   # Row 'Marks' with null is not printed
print()
print('Inplace prints the rows that has no null elements:')
print(df.dropna(inplace=False))       # removes all rows with null

