# Link of video = https://www.youtube.com/watch?v=pW-OCP9azz4&list=PLfP3JxW-T70HkhNxdgZeApdpiOfL6KAQE&index=16

# One Hot Encoding :- Some categorical variables contain informations that cant be dropped
# and have to be converted to numerical variables. This process is called One Hot Encoding.
# And the numerical values obtained after is called Dummy Variables

# ___________________ Encoding Using Pandas ___________________________ #
import pandas as pd

df = pd.read_csv('D:\Excel Demo\Kaggle\House Price\\train.csv', usecols=[0, 1, 2, 5, 7, 10])
pd.set_option('display.max_columns', None)
# dummy_df = pd.get_dummies(df)         # Creates Dummy variable of each classes in categorical Variables
# print(df.head())

dummy_df = pd.get_dummies(df, drop_first=True)
# drop first :- To drop one column in each column class
# print(dummy_df.shape)

# _______________________________________________________________________________ #

# _________________________ Using Scikit Learn __________________________________ #

from sklearn.preprocessing import OneHotEncoder

oh_enc = OneHotEncoder(sparse=False)
oh_enc_arr = oh_enc.fit_transform(df[['MSZoning', 'Street', 'LotShape', 'LotConfig']])
# print(oh_enc_arr)
# print(dummy_df.keys())
oh_enc_df = pd.DataFrame(oh_enc_arr, columns=['Id', 'MSSubClass', 'MSZoning_C (all)', 'MSZoning_FV', 'MSZoning_RH',
       'MSZoning_RL', 'MSZoning_RM', 'Street_Grvl', 'Street_Pave',
       'LotShape_IR1', 'LotShape_IR2', 'LotShape_IR3', 'LotShape_Reg',
       'LotConfig_Corner', 'LotConfig_CulDSac', 'LotConfig_FR2'])

print(oh_enc_df.head())