import pandas as pd

df = pd.read_csv('D:\Excel Demo\loc_iloc.csv')
print(df)

print('Groups by Section ie A, B and C:')
df2 = df.groupby('Section')
print(df2.groups)
print()

print('Groups by Section ie A, B and C:')
df1 = df.groupby(['Section', 'Class'])
print(df1.groups)
print()

for Section, df_1 in df2:            # try df1 yourself
    print(Section)
    print(df_1)

print()
print('Creating a list of groups in df2:')
print(list(df2))
print()

print('Getting groups that are fo class 10 only:')
df3 = df.groupby('Class').get_group(10)
print(df3)
print()

# print(df2.sum())
# print(df2.mean())
print('Detail description of the dataframe is:')
print(df2.describe())
print()

print('Giving the sum, max and the mean of all labels:')
print(df2.agg(['sum', 'max', 'mean']))

