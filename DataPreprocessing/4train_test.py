import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split

df = sns.load_dataset('titanic')

df2 = df[['survived', 'pclass', 'age', 'parch']]
df3 = df2.fillna(df2.mean())

X = df3.drop(columns='survived')          # read as X matrix
y = df3['survived']                       # and y vector

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)
print(X_train)