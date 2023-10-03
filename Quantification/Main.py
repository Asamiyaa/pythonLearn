import pandas_datareader.data as web
import matplotlib.pyplot as plt
import tushare as ts
from matplotlib.font_manager import FontProperties

#todo: matplotlib的包引入导致了 UserWarning: The NumPy module was reloaded (imported a second time). This can in some cases result in small but subtle issues and is discouraged.
  # __import__(_dependency)

# Python 数据分析中金融数据的来源库和简单操作:https://www.cnblogs.com/banshaohuan/p/11405244.html



# 使用Pandas DataReader获取A股用友网络（600588.SS）的股票数据
start_date = '2023-08-20'
end_date = '2023-09-30'
# stock_symbol = '600588.SS'
stock_symbol = '600588'
# stock_data = web.DataReader(stock_symbol, data_source='yahoo', start=start_date, end=end_date)  网络不通
stock_data = ts.get_k_data(code=stock_symbol, start=start_date, end=end_date)
print(stock_data)

font = FontProperties(fname='C:/Windows/Fonts/simsun.ttc', size=12)  # 这里使用了宋体作为例子，请根据你的系统和需求选择合适的字体

# 绘制股价走势图
plt.figure(figsize=(12, 6))
#绘制图表
plt.plot(stock_data['date'],stock_data['close'], label='Close Price')
#在图片上添加文本
# plt.text(stock_data['date'],stock_data['close'], label='Close Price',fontdict=font)
# plt.text(-1, -1, '文本示例', fontsize=12, color='red', verticalalignment='bottom', horizontalalignment='right')
# 指定支持中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或者其他支持中文的字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

plt.title('A股用友网络（600588.SS）股票走势')
plt.xlabel('日期')
plt.ylabel('价格（人民币）')
plt.legend()
plt.grid(True)
plt.show()
