import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\train.csv')
pd.set_option('display.max_rows', None)
df2 = df[['KitchenQual', 'BldgType']]
# print(df2.head())
# ______________________ Label Encoding ___________________________ #
le = LabelEncoder()
df2['BldgType_l_enc'] = le.fit_transform(df2['BldgType'])

# print(df2['BldgType'].value_counts())

# _________________________ Ordinal Encoding __________________________ #
print(df2['KitchenQual'].value_counts())
order_label = {'Ex': 4, 'Gd': 3, 'TA': 2, 'Fa': 1}
df2['Kitchen_ord_enc'] = df2['KitchenQual'].map(order_label)
print(df2)
