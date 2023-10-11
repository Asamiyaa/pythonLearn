import requests

'''
自己尝试抓，不熟练
'''
# url = 'http://www.iwencai.com/stockpick/load-data?rsh=3&typed=0&preParams=&ts=1&f=1&qs=result_original&selfsectsn=&querytype=stock&searchfilter=&tid=stockpick&w=%E4%BB%8A%E6%97%A5%E6%B6%A8%E5%81%9C%E5%92%8C%E6%B6%A8%E5%81%9C%E5%8E%9F%E5%9B%A0%E9%9D%9EST+%E9%A6%96%E6%AC%A1%E6%B6%A8%E5%81%9C%E6%97%B6%E9%97%B4%E6%8E%92%E5%BA%8F&queryarea='
# response = requests.get(url)
#
# # 打印网页内容
# print(response.text)
'''
借助问财 
https://github.com/zsrl/pywencai

调试关键词，让其匹配同花顺对应查询条件  -- prompt
'行业简称', --不确定匹配上
'''

import pywencai
import pandas as pd
from datetime import date


def get():

    # print("=========== zt =============")
    current_date = date.today()
    cur_date_str =  '[' + str(current_date.strftime("%Y%m%d")) + ']'

    res_zt = pywencai.get(query='今日涨停和涨停原因非ST 首次涨停时间排序 行业', sort_key='', sort_order='涨停类型')
    filter_col_zt = ['code','股票简称','最新价',
                  '首次涨停时间'+cur_date_str,'涨停原因类别'+cur_date_str,'涨停类型'+cur_date_str,
                  '连续涨停天数'+cur_date_str,'几天几板' + cur_date_str,
                  '涨停封单量'+cur_date_str,'涨停封单额'+cur_date_str,'涨停开板次数'+cur_date_str

                  ]
    # print(res[filter_col])
    # file_name = 'zt.csv'
    # res_zt[filter_col].to_csv('./data/' + file_name, index=False)


    # print("=========== >%5 =============")
    res_dy5 = pywencai.get(query='今日涨幅大于5 非30开头 非 688开头 非ST 非涨停 展示行业 ', sort_key='', sort_order='')
    # print(res)
    filter_col_dy5 = ['code','股票简称','最新价',
                  '成交量' + cur_date_str, '所属同花顺行业',
                  '涨停价'+ cur_date_str
                  ]
    # file_name = 'dy5.csv'
    # res[filter_col].to_csv('./data/' + file_name, index=False)



    # print("=========== zb =============")
    res_zb = pywencai.get(query='今日炸板不含ST 所属行业', sort_key='', sort_order='')
    filter_col_zb = ['code','股票简称','最新价',
                  '涨停时间明细'+cur_date_str,'涨停开板次数'+cur_date_str,
                  '所属同花顺行业',
                  '涨停价'+ cur_date_str
                  ]

    # file_name = 'zb.csv'
    # res[filter_col].to_csv('./data/' + file_name, index=False)
    # print(res)

    #写到一个excel不同sheet
    with pd.ExcelWriter('./data/stronger.xlsx') as writer:
        res_zt[filter_col_zt].to_excel(writer, sheet_name='Sheet1', index=False)
        res_dy5[filter_col_dy5].to_excel(writer, sheet_name='Sheet2', index=False)
        res_zb[filter_col_zb].to_excel(writer, sheet_name='Sheet3', index=False)
'''
定时任务 +excel 
'''
