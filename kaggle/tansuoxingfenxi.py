#https://www.bilibili.com/video/BV1yz4y1K7Sw/?p=34&spm_id_from=pageDriver&vd_source=1138e0bd4d669ff2571d56c9377aa33d

import numpy as np
import scipy.stats as ss

norm_dist = ss.norm.rvs(size = 20)
print(norm_dist)

#卡方检验
print(ss.chi2_contingency([[15, 95], [85, 5]]))

#独立分布t检验
print(ss.ttest_ind(ss.norm.rvs(size=10), ss.norm.rvs(size=20)))

#方差检验
print(ss.f_oneway([49, 50, 39, 40, 43], [28, 32, 30, 26, 34], [38, 40, 45, 42, 48]))

#qq图 判断是否正态分布
from statsmodels.graphics.api import qqplot
from matplotlib import pyplot as plt


# plt.show(qqplot(ss.norm.rvs(size=100)))  TypeError: _Backend.show() takes 1 positional argument but 2 were given

#回归
