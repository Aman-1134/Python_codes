from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset('titanic')

df2 = df[['survived', 'pclass', 'age', 'parch']]
df3 = df2.fillna(df2.mean())
X = df3.drop(columns='survived')
y = df3['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# ____________________ Standard Scaler _________________________ #
sc = StandardScaler()
sc.fit(X_train)
# print(sc.mean_)              # Gives mean value in each column
# print(sc.scale_)             # Gives standard deviation
# print(X_train.describe())

X_train_sc = sc.transform(X_train)
X_test_sc = sc.transform(X_test)

X_train_sc_df = pd.DataFrame(X_train_sc, columns=['pclass', 'age', 'parch'])
X_test_sc_df = pd.DataFrame(X_test_sc, columns=['pclass', 'age', 'parch'])

# print(X_train_sc_df.head())
# print(X_train_sc_df.describe().round(2))
# ____________________________________________________________________ #

# _____________________ Min Max Scaler _______________________________ #
mmc = MinMaxScaler()
mmc.fit(X_train)

X_train_mmc = mmc.transform(X_train)
X_test_mmc = mmc.transform(X_test)

X_train_mmc_df = pd.DataFrame(X_train_mmc, columns=['pclass', 'age', 'parch'])
X_test_mmc_df = pd.DataFrame(X_test_mmc, columns=['pclass', 'age', 'parch'])
# print(X_train_mmc_df.head())
# print(X_train_mmc_df.describe().round(2))
sns.pairplot(X_train)
plt.show()

sns.pairplot(X_train_sc_df)
plt.show()

sns.pairplot(X_train_mmc_df)
plt.show()
# Data distribution is not affected while normalization and standardization ie distribution remains same
