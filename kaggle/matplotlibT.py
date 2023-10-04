'''
可视化  matplotlib、seaborn、plotly
'''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#改变样式,背景 + api
sns.set_style(style="darkgrid")
sns.set_palette("summer")
#seaborn是matplotlib封装，可以画图


df = pd.read_csv('./HR.csv')
#sns distplot
f = plt.figure()
f.add_subplot(1,3,1)
sns.displot(df['salary'],bins = 10)
plt.show()

# box plot
sns.boxplot(x = df['salary'],saturation=0.75,whis=3)
plt.show()

#line plot
sub_df = df.groupby('salary').mean()
sns.pointplot(sub_df.index)
plt.show()

#pie
lbs = df['salary'].value_counts().index
explodes = [0.1 if i == 'low' else 0 for i in lbs ]
plt.pie(df['salary'].value_counts(normalize=True),labels=lbs,explode = explodes)
plt.show()

#其他 比如散点图，气泡图... 不同场景下展示

plt.title("SALARY")
plt.xlabel("salary")
plt.ylabel("num")
# plt.xticks()  plt.axis
# 左右移动plt.bar(np.arange(len(df['salary'].value_counts())) + 0.5,df['salary'].value_counts())
plt.bar(np.arange(len(df['salary'].value_counts())),df['salary'].value_counts(),width=0.5)
# 标注
for x,y in zip(np.arange(len(df['salary'].value_counts())),df['salary'].value_counts()):
    plt.text(x,y,y,ha="center",va="bottom")
plt.show()








