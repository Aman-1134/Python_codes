import numpy as np
import pandas as pd

from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
# print(data.data)                          # Gives data
# print(data.feature_names)                 # Gives the name of columns
# print(data.target)                        # Target / Output column info
# print(data.target_names)                  # Malignant or Benign

df = pd.DataFrame(np.c_[data.data, data.target], columns=[list(data.feature_names) + ['target']])
# print(df.shape)

X = df.iloc[:, 0: -1]
y = df.iloc[:, -1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2020)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

# SVC
from sklearn.svm import SVC

# classification_rbf = SVC(kernel='rbf')            # 0.956140350877193
classification_rbf = SVC(kernel='linear')           # 0.9649122807017544
classification_rbf.fit(X_train, y_train)
print(classification_rbf.score(X_test, y_test))

# patient1 = X_test[0, :]
# patient1 = [2.65231762,  1.77811311,  2.60622732,  2.96324283, -0.06609518,  1.2865035,
#   1.39134077,  2.02614144,  0.42575834,  0.06852025,  2.34529764, -0.45881107,
#   2.12990317,  2.49940587, -0.22502254,  0.20659226,  0.40832774,  0.84422126,
#  -0.53992908, -0.25877397,  3.13514068,  1.44385864,  3.02114476,  3.71998397,
#   0.68780346,  1.1121591,   1.58152563,  2.28828386,  0.3734377,   0.20303736]
#
# # print(patient1)
#
# patient1_sc = sc.transform(np.array(patient1).reshape(1, 30))
# print(patient1_sc)

y_pred = classification_rbf.predict(X_test)
print(y_pred)
print(y_test)
