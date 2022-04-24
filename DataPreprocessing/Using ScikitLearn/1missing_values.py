# link to scikit learn official site = https://scikit-learn.org/stable/

from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd

train = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\train.csv')
test = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\test.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# print('Shape of Train Data Frame is = ', train.shape)
# print('Shape of Test Data Frame is = ', test.shape)

X_train = train.drop(columns='SalePrice')
y_train = train['SalePrice']

# print('Shape of X_Train Data Frame is = ', X_train.shape)              # (1460, 80)
# print('Shape of y_train Data Frame is = ', y_train.shape)              # (1460,)

# -------------- Numerical Value Imputation ----------------------#

num_vars = X_train.select_dtypes(['int64', 'float64']).columns
# print(num_vars)

# print(X_train[num_vars].isnull().sum())

imputer_mean = SimpleImputer(strategy='mean')
# imputer_mean = SimpleImputer(strategy='constant', fill_value=10)

imputer_mean.fit(X_train[num_vars])                 # Calculates the mean for each column and stores it
# print(imputer_mean.statistics_)                   # Gives the calculated mean values in an array
# print(imputer_mean.transform(X_train[num_vars]))    #

X_train[num_vars] = imputer_mean.transform(X_train[num_vars])
test[num_vars] = imputer_mean.transform(test[num_vars])
# print(X_train[num_vars].isnull().sum())

# ---------------------------------------------------------------------------- #

# ----------------- Categorical value imputation ------------------------------#

cat_vars = X_train.select_dtypes(['O']).columns
# print(cat_vars)

# print(X_train[cat_vars].isnull().sum())
imputer_mode = SimpleImputer(strategy='most_frequent')
imputer_mode.fit(X_train[cat_vars])

# print(imputer_mode.statistics_)
X_train[cat_vars] = imputer_mode.transform(X_train[cat_vars])
test[cat_vars] = imputer_mode.transform(test[cat_vars])
print(X_train[cat_vars].isnull().sum())
