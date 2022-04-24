# Pair plot gives scatter plot of all the columns present in the data frame taking two at a time

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer
cancer_data = load_breast_cancer()
# print(cancer_data)

cancer_df = pd.DataFrame(np.c_[cancer_data['data'], cancer_data['target']],
                         columns=np.append(cancer_data['feature_names'], ['target']))
# print(cancer_df)

sns.pairplot(cancer_df)
plt.show()