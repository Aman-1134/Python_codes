import pandas as pd
df = pd.read_csv('D:\\Excel Demo\\missing_value.csv', na_values=['not avaliable', 'no value'])
print(df)
print()

print(df.fillna(0))          # fills 0 in place of NaN
print()
print('Data frame with dictionary use:')
print(df.fillna({'Division': 'Fail', 'Roll No': 'Unknown', 'Marks': 0}))
print()

print('Using method forward fill:')
print(df.fillna(method='ffill'))      # ffill = forward fill that fills the forward value to nan
print()                               # ffill = pad and, bfill opposite of ffill

print('Using ffill with axis:')
print(df.fillna(method='ffill', axis=1))  # axis always used with method or value
print()

print('fillna with limit and value:')
print(df.fillna(6, limit=2))      # fills 6 in only 2 places in a column
print()                           # can be used with method

print('fillna with value and inplace:')
print(df.fillna(15, inplace=False))     # modifies existing dataframe



