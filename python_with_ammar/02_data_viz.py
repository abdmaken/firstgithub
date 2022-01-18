# step1 import libraies
import seaborn as sns
import  matplotlib.pyplot as plt

#step 2 set a theme
sns.set_theme(style="ticks", color_codes=True)

# step 3 import data set
kashti= sns.load_dataset("titanic")
# print(kashti)
# # step 4 plot basic graph
# p = sns.countplot(x="sex", data= kashti)
# plt.show()
#step 5 use hue wth count plot having 2 variables
p = sns.countplot(x="sex", data=kashti, hue="class")
plt.show()
#step 6 use hue wth count plot having 2 variables
p = sns.countplot(x="sex", data=kashti, hue="class")
p.set_title("baba_ammar ka count plot for kashti")
plt.show()