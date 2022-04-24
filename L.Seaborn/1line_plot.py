import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# kalaiya_temp = [20, 25, 20, 28, 34, 30, 25, 29, 35, 33, 19, 29, 28, 39, 37]
# birgung_temp = [25, 35, 33, 42, 36, 39, 40, 32, 29, 28, 23, 36, 38, 40, 38]
# seaborn always reads data frames so convert days and temperature to data frames first
# temp_df = pd.DataFrame({"Days": days, "Temperature": kalaiya_temp})

tips_df = sns.load_dataset("tips")                      # loading tips data set from github
# print(tips_df)
sns.set(style="darkgrid")                               # similar to style.use('ggplot')
plt.figure(figsize=(10, 6), facecolor='r', edgecolor='b')
# sns.lineplot(x="total_bill", y="tip", data=tips_df)
# sns.lineplot(x=tips_df.total_bill, y=tips_df.tip, data=tips_df)      # can leave data column as x and y are data frames

# sns.lineplot(x="size", y="total_bill", data=tips_df, hue="sex", style="sex", palette='Accent',
#              markers=["o", ">"], legend="full")

sns.lineplot(x="size", y="total_bill", data=tips_df, hue="day", style="day", palette='Accent',
             markers=["o", ">", "<", "o"], legend="full")

plt.xlabel("Size", fontsize=15, color='g')
plt.ylabel("Total Bill", fontsize=15, color='g')
plt.title("Size vs Bill", fontsize=20, color='r')

# X and Y labels are automatically set according to data frame but can be set as user demand also
# data takes the name of data frame
# hue gives multiple plots for certain category and automatically gives legend
# palette = color map of lines <i.e. styles of lines>
# style = linestyle

plt.show()