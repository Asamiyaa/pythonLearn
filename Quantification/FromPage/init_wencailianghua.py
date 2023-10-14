import wencai as wc

'''
1.提供iwencai 策略回测
2.目前包不能用，大多报错，如果用后续修改源码
'''

wc.set_variable(cn_col=True)

r = wc.get_strategy(query='非停牌；非st；今日振幅小于5%；量比小于1；涨跌幅大于-5%小于1%；流通市值小于20亿；市盈率大于25小于80；主力控盘比例从大到小',
                    start_date='2018-10-09',
                    end_date='2019-07-16',
                    period='1',
                    fall_income=1,
                    lower_income=5,
                    upper_income=9,
                    day_buy_stock_num=1,
                    stock_hold=2)

print(r)
'''
    data = self.content['backtestData'][0]
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
'''
# print(r.profit_data) # 累计收益数据
# print(r.backtest_data) # 报告评级
# print(r.condition_data) # 准确回测语句
# print(r.history_detail(period='1')) # 历史明细查询
# print(r.history_pick(trade_date='2019-07-16', hold_num=1)) # 策略选股


result = wc.search(query="当前热股")
print(result)