# Learning video link = https://www.youtube.com/watch?v=sbk1mzLquz4&list=PLfP3JxW-T70HkhNxdgZeApdpiOfL6KAQE&index=15

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd

train = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\train.csv')
test = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\test.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

X_train = train.drop(columns='SalePrice')
y_train = train['SalePrice']
x_test = test.copy()

isnull_sum = X_train.isnull().sum()
# print(isnull_sum)

num_vars = X_train.select_dtypes(['int64', 'float64']).columns
num_vars_miss = [var for var in num_vars if X_train[var].isnull().sum() > 0]
# print(num_vars_miss)

cat_vars = X_train.select_dtypes(['O']).columns
cat_vars_miss = [var for var in cat_vars if X_train[var].isnull().sum() > 0]
# print(cat_vars_miss)
# -------------- List of columns(numerical and categorical) -------------------- #
num_var_mean = ['LotFrontage']
num_var_median = ['MasVnrArea', 'GarageYrBlt']

cat_var_mode = ['Alley', 'MasVnrType', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1',
                'BsmtFinType2', 'Electrical', 'FireplaceQu']
cat_var_missing = ['GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PoolQC',
                    'Fence', 'MiscFeature']
# ------------------------------------------------------------------------------- #

# -------------  Creating Pipelines for their processing ------------------------ #
num_var_mean_imputer = Pipeline(steps=[('imputer', SimpleImputer(strategy='mean'))])
num_var_median_imputer = Pipeline(steps=[('imputer', SimpleImputer(strategy='median'))])
cat_var_mode_imputer = Pipeline(steps=[('imputer', SimpleImputer(strategy='most_frequent'))])
cat_var_missing_imputer = Pipeline(steps=[('imputer', SimpleImputer(strategy='constant', fill_value='Missing'))])
# ---------------------------------------------------------------------------------- #

preprocessor = ColumnTransformer(transformers=[('mean_imputer', num_var_mean_imputer, num_var_mean),
                                ('median_imputer', num_var_median_imputer, num_var_median),
                                ('mode_imputer', cat_var_mode_imputer, cat_var_mode),
                                ('constant_imputer', cat_var_missing_imputer, cat_var_missing)])

preprocessor.fit(X_train)

# print(preprocessor.named_transformers_['mean_imputer'].named_steps['imputer'].statistics_)
# print(train['LotFrontage'].mean())

X_train_clean = preprocessor.transform(X_train)
x_test_clean = preprocessor.transform(x_test)

# print(X_train_clean)

# print(preprocessor.transformers_)           # see remainder. those columns that dont have nan are dropped

X_train_clean_miss_var = pd.DataFrame(X_train_clean, columns=num_var_mean+num_var_median+cat_var_mode+cat_vars_miss)
print(X_train_clean_miss_var.head(6))

# print(train['Alley'].value_counts())
# print(X_train_clean_miss_var['Alley'].value_counts())