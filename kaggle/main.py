import numpy as np
import pandas as pd

df = pd.read_csv("./HR.csv")
print(df.head(10))

print(type(df))

print(df["satisfaction_level"].median())
print(df["satisfaction_level"].aggregate)

# df.quantile(q=0.25)  四分位数
# 众数
print(df["satisfaction_level"].quantile(q=0.25))

print(df.mode())

print(type(df["sales"].mode()))

print(df["satisfaction_level"].std())

print(df.sum())

#偏态系数 负 ->
print(df["satisfaction_level"].skew())
#峰度系数
print(df["satisfaction_level"].kurt())

#分布函数
import scipy.stats as ss

print(ss.norm)
print(ss.norm.stats(moments='mvsk'))
print(ss.norm.pdf(0.0))
print(ss.norm.cdf(2))
# print(ss.norm.size(size=10))

#抽样
print(df.sample(n=10))
print(df.sample(frac=0.001))



#异常值分析
print(df["satisfaction_level"].isnull())
print(df["satisfaction_level"][df["satisfaction_level"].isnull()])

print(df[df["satisfaction_level"].isnull()])

#丢弃
print(df["satisfaction_level"].dropna())

#再次查看中位数等，查看数据分布
''''
理解统计上的含义，关联,来看数据是否清洗完成；每个列都要处理异常值
'''
df_l = df["satisfaction_level"]
print(df_l.max())
print(df_l.min())
print(df_l.skew())
print(df_l.std())
print(df_l.mean())



#直方图
print(np.histogram(df_l.values, bins=np.arange(0.0, 1.1, 0.1)))



'''
每个列都按照这种分析
    异常值需要根据具体场景确认，是否去掉
'''
print(df['left'].sum())
# print(df['left'].isnull.sum())

df_s = df['salary']
print(df_s.value_counts())

#去掉异常值
# print(df_s.where(df_s != 'nme').dropna())


'''
对比分析
'''
df = df.dropna(axis=0,how='any')
print(df)

'''
去掉其他异常值
'''
df = df[df['satisfaction_level'] <= 1][df['salary'] != 'nme'] [df['left'] < 1]
print(df)

#以部门分组

print(df.groupby('salary').mean())

#todo:api聚合
# df.loc[:,['satisfaction_level','salary']].groupby('salary)['sati...level'].apply(lambda x:x.max() - x.min())




































