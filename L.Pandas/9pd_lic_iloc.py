# iloc = integer location-based indexing

import pandas as pd

df = pd.read_csv('D:\Excel Demo\loc_iloc.csv')
print(df)

print('Use loc to access any row:')
print(df.loc[0])
print()

print('Printing only desired rows acc to label provided:')
print(df.loc[[1, 4, 5]])
print()

print('Value of Class at label 4:')
print(df.loc[4, 'Class'])
print()

print('Range of value of a header:')
print(df.loc[0:3, 'Class'])
print()

print('all data frames that has class value less than 5:')
print(df.loc[df['Class'] < 5])
print()

print('Only the label percentage that have class value less than 5:')
print(df.loc[df['Class'] < 5, ['Percentage']])
print()

print('Accessing datas using iloc:')
print(df.iloc[[0]])
print()

print('Applying Sclicing to print student ids from 0-4 index:')
print(df.iloc[0:4, 1])
print()

