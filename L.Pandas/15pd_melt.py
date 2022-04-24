import pandas as pd

df = pd.read_csv('D:\Excel Demo\Student_results.csv')
print(df)
print()

print('id_vars')
print(pd.melt(df, id_vars=['Division', 'Rank']))
print()

print('id_vars and Value_vars')
print(pd.melt(df, id_vars=['Division'], value_vars=['Marks']))
print()

print('var_name changes the name of value_vars to specified in var_name and value_name does that for value_vars value(ie elements)')
print(pd.melt(df, id_vars=['Division'], value_vars=['Marks'], var_name='Category',
              value_name='Data'))
print()