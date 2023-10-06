import pandas_datareader.data as web
import matplotlib.pyplot as plt
import tushare as ts
from matplotlib.font_manager import FontProperties
import datetime
import pandas as pd

#todo: matplotlib的包引入导致了 UserWarning: The NumPy module was reloaded (imported a second time). This can in some cases result in small but subtle issues and is discouraged.
  # __import__(_dependency)

# Python 数据分析中金融数据的来源库和简单操作:https://www.cnblogs.com/banshaohuan/p/11405244.html


#=================画图=================
# 使用Pandas DataReader获取A股用友网络（600588.SS）的股票数据
# start_date = '2023-08-20'
# end_date = '2023-09-30'
# # stock_symbol = '600588.SS'
# stock_symbol = '600588'
# # stock_data = web.DataReader(stock_symbol, data_source='yahoo', start=start_date, end=end_date)  网络不通
# stock_data = ts.get_k_data(code=stock_symbol, start=start_date, end=end_date)
# print(stock_data)



# font = FontProperties(fname='C:/Windows/Fonts/simsun.ttc', size=12)  # 这里使用了宋体作为例子，请根据你的系统和需求选择合适的字体

# 绘制股价走势图
# plt.figure(figsize=(12, 6))
#绘制图表
# plt.plot(stock_data['date'],stock_data['close'], label='Close Price')
#在图片上添加文本
# plt.text(stock_data['date'],stock_data['close'], label='Close Price',fontdict=font)
# plt.text(-1, -1, '文本示例', fontsize=12, color='red', verticalalignment='bottom', horizontalalignment='right')
# 指定支持中文字体
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 或者其他支持中文的字体
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
#
# plt.title('A股用友网络（600588.SS）股票走势')
# plt.xlabel('日期')
# plt.ylabel('价格（人民币）')
# plt.legend()
# plt.grid(True)
# plt.show()

#=================画图=================



'''
获取涨停

        参考：https://zhuanlan.zhihu.com/p/110231478
        
        Ai助手：chatgpt -> Python与A
        接口：tushare -> pro
        DataFrame:灵活使用过滤，join其他列展示
        定时任务
        异常处理：替换接口 or 捕获  -- 没生效 --生效，因为这里定义的def 去job.py执行
            FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
                df = df.append(newdf, ignore_index=True)
        匹配行业输出  - dic构建和merge
        

'''

import warnings
warnings.filterwarnings("ignore")


import sendToWetchat as send

def get_more5_zhangting():

    # try:

    df = ts.get_today_all()
    # file_name = str(datetime.date.today()) + '_Astock.csv'
    # df.to_csv('./data/'+file_name)

    #__今日涨停的股票__
    # ZhangTing_df = df[(df["changepercent"]>9.5) & (df["changepercent"]<10.5) ]
    ZhangTing_df = df[(df["changepercent"]>9.5) & (df['code'] < '609999')]

    selected_columns = ['code', 'name']
    filter_ZhangTing_df = ZhangTing_df[selected_columns]

    # 匹配行业输出  - dic构建和merge
    dic_df = pd.read_csv('./Akshare/data2023-10-06_codeName.csv')
    dic_df['code'] = dic_df["A股代码"].map(lambda x: str(x))

    filter_ZhangTing_df['code'] = filter_ZhangTing_df['code'].apply(str)
    dic_df['code'] = dic_df['code'].apply(str)

    print(filter_ZhangTing_df['code'])
    print(dic_df['code'])

    temp = pd.merge(filter_ZhangTing_df, dic_df, how="inner",
                    on="code")
    print(temp)
    #
    #
    # file_name = str(datetime.date.today()) + '_Astock_zhangting.csv'
    # filter_ZhangTing_df.to_csv('./data/'+file_name,index=False)


    # send.send_msg_toWechat()

    # print(ZhangTing_df.head(100))

    # More5_df = df[(df["changepercent"]>5 & (df['changepercent']<10.5))]    #这种过滤方式错误，暂时没想到 - 不熟练  , api过滤简化，这里没陈工
    More5_df = df[(df["changepercent"]>5) & (df['changepercent']<9.5) & (df['code'] < '609999')]
    code_names = [More5_df["code"],More5_df["name"]]
    # print(code_names)

    New_pd = pd.DataFrame(code_names)
    #表格是横着的转竖
    New_pd = New_pd.T
    #过滤只考虑600/300
    # raise KeyError(key) from err
    # New2_pd = df[New_pd["code"].__str__().__contains__("600") & New_pd["code"].__str__().__contains__("300")]
    # print(New_pd['code'])
    New2_pd = New_pd[New_pd['code'] < '609999']  #pandas.errors.IndexingError: Unalignable boolean Series provided as indexer (index of the boolean Series and of the indexed object do not match).
    # 为什么上面也是这么比较的呀？
    # New2_pd = df[New_pd['code'].reset_index(drop=True) < '609999']

    file_name = str(datetime.date.today()) + '_Astock_more5.csv'
    file_path = './data/'+file_name
    New2_pd.to_csv(file_path,index=False)


        # send.send_msg_toWechat(New2_pd.to_string())

        # More5_df['code']. '688*'

        #再次读取处理？
        # dayu5 = pd.read_csv(file_path)
        # pddayu5['code'] < '609999'

    # except FutureWarning:
    #     print("---")
    # except UserWarning:
    #     print("---")
    # else:
    #     print("---")
    # finally:
    #     print("---")
# import JQData
# print(ts.get_industry_classified())
# print(ts.get_gem_classified())
# print(ts.get_stock_basics(None))














