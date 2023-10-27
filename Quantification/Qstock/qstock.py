#导入qstock模块
import qstock as qs
import pandas as pd

pd.set_option('display.max_columns', 1000) #显示完整的列
pd.set_option('display.max_rows', None) #显示完整的行
pd.set_option('display.width', 1000) #显示最大的行宽
pd.set_option('display.max_colwidth', 1000) #显示最大的列宽

# qs.stock_snapshot('中国平安')
# df = qs.realtime_data(code=['中国平安','300684','锂电池ETF','BK0679','上证指数'])
# print(df)

#异动类型：火箭发射
changes_list=['火箭发射', '快速反弹']
df=qs.realtime_change('火箭发射')
# df.to_csv("./qstock.csv")
#查看前几行
# dfhead = df.head()
print(df)

# 获取沪深A股最新行情指标
# df=qs.realtime_data()
# # 查看前几行
# print(df.head())

# print(qs.stock_snapshot('用友网络'))

# df=qs.stock_billboard('20231027','20231027')
# print(df)

'''
获取交易日实时盘口异动数据，相当于盯盘小精灵。 realtime_change(flag=None):

flag：盘口异动类型，默认输出全部类型的异动情况。可选：
['火箭发射', '快速反弹','加速下跌', '高台跳水', '大笔买入', '大笔卖出', '封涨停板','封跌停板', '打开跌停板','打开涨停板','有大买盘','有大卖盘', '竞价上涨', '竞价下跌','高开5日线','低开5日线', '向上缺口','向下缺口', '60日新高','60日新低','60日大幅上涨', '60日大幅下跌'] 上述异动类型分别可使用1-22数字代替。

'''

# df=qs.financial_statement('yjyg')
# print(df)

# df=qs.north_money()
# print("北向资金",df.tail())

#北向资金增持行业板块5日排名
# df=qs.north_money('行业',1)
# print("北向资金增持行业",df.tail())


#默认参数输出财联社电报新闻数据
# df=qs.news_data()
# print(df.tail())

# df=qs.news_data('js')
# print(df.tail())

# import matplotlib as plot
# #如果notebook不显示pyecharts的图形，在前面加上以下代码(去掉前面注释)
# from pyecharts.globals import CurrentConfig, NotebookType
# CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
#
# #获取中国平安2022年至今前复权的数据
# df=qs.get_data('中国平安',start='2022-06-01',end='2022-10-20')
# df.tail()
#
# #使用默认参数
# plot.kline(df)















