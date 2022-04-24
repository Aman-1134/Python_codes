import pandas as pd
import numpy as np

df = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\train.csv')
# df = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\test.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

num_var = df.select_dtypes(['int64', 'float64'])
miss_num_var = [var for var in num_var if num_var[var].isnull().sum() > 0]
cat_vars = ['LotConfig', 'Exterior2nd', 'KitchenQual']
for cat_var, miss in zip(cat_vars, miss_num_var):
    for var_class in df[cat_var].unique():
        df.update(df[df.loc[:, cat_var] == var_class][miss].replace
              (np.nan, df[df.loc[:, cat_var] == var_class][miss].mean()))

cat_var = df.select_dtypes('O')
miss_cat_var = [var for var in cat_var if cat_var[var].isnull().sum() > 0]
for var in miss_cat_var:
    df.update(cat_var.fillna(cat_var[var].mode()[0]))

df = pd.get_dummies(df, drop_first=True)

X = df.drop(columns='SalePrice')
y = df['SalePrice']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

# Polynimial Regression
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree=2)
poly_reg.fit(X_train)
X_train_poly = poly_reg.transform(X_train)
X_test_poly = poly_reg.transform(X_test)
print(X_test_poly.shape)
print(X_train_poly.shape)

lr = LinearRegression()
lr.fit(X_train_poly, y_train)

print('Accuracy = ', float(lr.score(X_train_poly, y_train)*100))

# print(lr.predict([X_test_poly[0, :]]))
y_pred = lr.predict(X_test_poly)
print(y_pred)
print(y_test)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f'mse = {mse} rmse = {rmse}')
