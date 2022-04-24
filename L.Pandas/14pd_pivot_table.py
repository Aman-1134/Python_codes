import pandas as pd

df = pd.read_csv('D:\Excel Demo\Student_results.csv')
print(df)
print('Pivot table with index = Division only')
df1 = df.pivot_table(index='Division')        # name column is neglected as it is a string
print(df1)
print()

print('Pivot table with index=Division and column=Rank')
df1 = df.pivot_table(index='Division', columns='Rank')
print(df1)
print()

print('Pivot table with index=Division and column=Rank and aggfunc')
df1 = df.pivot_table(index='Division', columns='Rank', aggfunc='sum', fill_value='None',
                     margins=True)
# aggfunc = mean<default>, sum, count, max, SD and many more
# fill_values replace nan with given value
print(df1)
# if any column has all elements nan, it will be ignored and if you want to print them, use dropna=True
# margin adds an all column and row to the data frame
