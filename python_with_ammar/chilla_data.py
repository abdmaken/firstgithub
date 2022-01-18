import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
#improt dat from csv file
chilla= pd.read_csv("data_viz.csv")
print(chilla)

p=sns.countplot(x="Gender", data=chilla, hue="Age")
plt.show()