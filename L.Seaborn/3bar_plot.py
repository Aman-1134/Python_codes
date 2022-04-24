import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")
# print(tips)

sns.set()
order = ['Sun', 'Thur', 'Fri', 'Sat']            # list given to maintain the order of days in x-axis
hue_order = ['Female', 'Male']                   # To maintain hue order ie first female and then male
kwargs = {'alpha': 0.8, 'linestyle': ':', 'linewidth': 3, 'edgecolor': 'm'}      # can be given as a parameter also
ax = sns.barplot(x=tips.day, y=tips.total_bill, hue=tips.sex, order=order, hue_order=hue_order,
            estimator=np.max, palette='Accent', errcolor='0.5', **kwargs)
            # ci=12, saturation=0.2, errwidth=10, capsize=1, , dodge=False)
ax.set(title='Barplot', xlabel='Days', ylabel='Total Bill')

# estimator adjusts the value in y axis according to data provided
# n_boot and ci(confidence interval) adjusts the position of black line<ie error line> in the chart
# orient = 'h' or 'v' for horizontal or vertical chart
# errcolor changes the color of error line
# dodge = False to overlap both the bars of male and females

plt.show()