import pandas_datareader.data as web
import matplotlib.pyplot as plt

'''
Python 数据分析中金融数据的来源库和简单操作:https://www.cnblogs.com/banshaohuan/p/11405244.html

'''


# 使用Pandas DataReader获取A股用友网络（600588.SS）的股票数据
start_date = '2023-09-20'
end_date = '2023-09-30'
stock_symbol = '600588.SS'
stock_data = web.DataReader(stock_symbol, data_source='yahoo', start=start_date, end=end_date)

# 绘制股价走势图
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label='Close Price')
plt.title('A股用友网络（600588.SS）股票走势')
plt.xlabel('日期')
plt.ylabel('价格（人民币）')
plt.legend()
plt.grid(True)
plt.show()
