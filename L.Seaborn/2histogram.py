import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd

tips_df = sns.load_dataset("tips")
# print(tips_df)
# print(tips_df.total_bill.sort_values())               # gives the sorted total_bill values
plt.figure(figsize=(10, 6))
sns.set()
bins = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
# sns.distplot(tips_df["total_bill"], hist=True, kde=True, bins=bins, rug=True, fit=norm, color='r',
#              vertical=False, norm_hist=False, axlabel='Total Bill', label='Total Bill',
#              hist_kws={"color": 'm', "edgecolor": 'r', "linewidth": 5, "linestyle": '--', "alpha": 0.8},
#              kde_kws={"color": 'g', "linewidth": 5, "linestyle": '--', "alpha": 1},
#              rug_kws={"color": 'y', "edgecolor": 'b', "linewidth": 2, "linestyle": '--', "alpha": 0.8},)

sns.distplot(tips_df["total_bill"], color='r', fit=norm,
             fit_kws={"color": 'g', "linestyle": '--', "alpha": 0.6, "linewidth": 4})
# plt.xticks(bins)
# plt.legend()

# hist = False hides the and shows only KDE = Kernel Density Estimator <ie the line plot>
# kde = false to hide the line plot
# to use norm, scipy.stats is required
# axlabel to give name to x axis
# if fit parameter is to be used, kde must be false

plt.show()