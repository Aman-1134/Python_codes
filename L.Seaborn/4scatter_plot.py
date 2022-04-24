import seaborn as sns
import matplotlib.pyplot as plt

titanic_df = sns.load_dataset('titanic')

sns.set()
plt.figure(figsize=(10,7))

sns.scatterplot(x="age", y="fare", data=titanic_df, hue="sex", style='who', size='who',
                sizes=(50, 150))


# sns.scatterplot(x="who", y="fare", data=titanic_df, hue="alive", style='alive', size='who',
#                 sizes=(50, 150))

# sns.scatterplot(x='age', y='fare', data=titanic_df, hue='sex', style='who')
# sns.lineplot(x='age', y='fare', data=titanic_df)
# sns.barplot(x='age', y='fare', data=titanic_df)

# style categorize as child, man and woman as per data column 'who'
# size gives each data a different size
# sizes takes a tuple that is the range of sizes of the data presented in plot
plt.show()

