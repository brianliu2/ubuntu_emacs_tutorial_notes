#!/home/xinliu/anaconda3/bin/python


import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
sns.regplot(x="total_bill", y="tip", data=tips)
plt.show()

