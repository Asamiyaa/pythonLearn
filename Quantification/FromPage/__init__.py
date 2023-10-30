# import requests
# from openpyxl.reader.excel import load_workbook

'''
自己尝试抓，不熟练
'''
import datetime

from Quantification.Akshare.Ak_share_client import get_zixuangu_df, get_ruozhuanqiang_df
from Quantification.FromPage.fenshi_rik import geturl
from Quantification.FromPage.ths_zixuan import get_ths_zixuan, get_ths_ruozhuanqiang, get_ths_maodian
from Quantification.FromPage.zhijiehuoqutupian import get_k_jpg

from Quantification.Akshare import Ak_share_client

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
定时任务 +excel
'''

import pywencai
import pandas as pd
from datetime import date
from datetime import datetime,timedelta
# from openpyxl import Workbook
# from openpyxl.utils.dataframe import dataframe_to_rows
import xlwings as xw
import warnings
import Quantification.sendToWetchat as wx
from workalendar.asia import China

warnings.filterwarnings("ignore")
def get():
    # 创建一个中国日历对象
    cal = China()
    # print("=========== zt =============")
    current_date = date.today()

    # 判断今天是否是节假日
    # if not cal.is_working_day(current_date):
    #     # print("")
    # # else:
    #     # 获取前一个工作日的日期
    #     current_date = cal.find_following_working_day(current_date - timedelta(days=1))
    # 如果今天不是工作日，找到上一个工作日（上一个周五）
    while not cal.is_working_day(current_date):
        current_date -= timedelta(days=1)

    cur_date_str =  '[' + str(current_date.strftime("%Y%m%d")) + ']'
    # print(cur_date_str)

    res_zt = pywencai.get(query='今日涨停和涨停原因非ST 首次涨停时间排序 行业', sort_key='', sort_order='涨停类型')
    # print(res_zt)
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

    # print("--------zhanban--------")
    # print(res_zb)

    # file_name = 'zb.csv'
    # res[filter_col].to_csv('./data/' + file_name, index=False)
    # print(res)



    ret_rqb = pywencai.get(query='当前人气排名 行业 ')
    filter_col_hx = ['code', '股票简称', '最新涨跌幅','最新价',#'个股热度排名'+cur_date_str ,
                    '所属同花顺行业','所属概念'
                     ]

    # 自定义锚点，通过find带入
    # 自选
    # maodian_hx = ['002855', '600588']
    df = get_ths_zixuan()
    zixuan = df['代码'].values.tolist()
    # print("===自选---", zixuan)

    # ddf = pd.DataFrame
    ret_zixuangu = get_zixuangu_df()#pywencai.get(query='集合竞价 涨速 最高板块 ', find=zixuan)
    # ret_zixuangu.to_csv("./FromPage/zixuan.csv")
    # print("==zixuan---",ret_zixuangu)
    filter_col_zixuangu = ['股票代码','股票简称', '最新涨跌幅', '最新价', '最新涨跌幅'# '个股热度排名'+cur_date_str ,
                    # '所属同花顺行业', '所属概念'
                     ]

    ret_dieting = pywencai.get(query='今日跌停')
    # ret_zixuangu.to_csv("./FromPage/zixuan.csv")
    # print("==zixuan---",ret_zixuangu)
    filter_col_dieting = ['股票代码', '股票简称'  # '个股热度排名'+cur_date_str ,
                           # '所属同花顺行业', '所属概念'
                           ]

    ret_diedayu5 = pywencai.get(query='今日跌幅大于5% 非St 非30开头  非688开头 非83开头 非87开头  所属行业')
    filter_col_diedayu5 = ['股票代码', '股票简称' ,'所属同花顺行业' # '个股热度排名'+cur_date_str ,
                          # '所属同花顺行业', '所属概念'
                          ]

    '''
    有bug ,这里查询条件和问财一样，但效果不一样
    执行次数少，且无需通知
    '''
    # ret_hangyezhangfu = pywencai.get(query='行业涨幅从大到小')
    # print("---",ret_hangyezhangfu)
    # filter_col_hangyezhangfu = ['指数简称', '涨跌幅'+cur_date_str#, '所属同花顺行业'  # '个股热度排名'+cur_date_str ,
    #                        # '所属同花顺行业', '所属概念'
    #                        ]
    #
    # ret_gainianzhangfu = pywencai.get(query='概念涨幅 排序')
    # print("---", ret_gainianzhangfu)
    # filter_col_gainianzhangfu = ['指数简称', '涨跌幅'+cur_date_str # '个股热度排名'+cur_date_str ,
                           # '所属同花顺行业', '所属概念'
                           # ]

    '''
    竞价抢筹 - 只执行一次
    早盘和尾盘使用，确定方向
    是否应该使用竞价金额替换竞价量？
    '''

    # ret_jihejiangjia1 = pywencai.get(query='集合竞价 高开2%  成交量前30 非30开头 非688开头 非st 竞价量从大到小')
    # filter_col_gainianzhangfu1 = ['股票代码', '股票简称', '竞价量' + cur_date_str, '最新涨跌幅', '竞价涨幅' + cur_date_str]
    # # ret_jihejiangjia1.to_csv("./a.csv")
    # # print("---", ret_jihejiangjia1)

    ret_jihejiangjia2 = pywencai.get(query='集合竞价 竞价抢筹 非688开头 非30开头 非新股;非st 涨幅大于1  竞价量从大到小')
    filter_col_gainianzhangfu2 = ['股票代码', '股票简称', '竞价量'+cur_date_str, '涨跌幅:前复权'+ cur_date_str , '竞价涨幅' + cur_date_str
                                  # '个股热度排名'+cur_date_str ,
                                  # '所属同花顺行业', '所属概念'
                                  ]
    # ret_jihejiangjia2.to_csv("./a.csv")
    # print("---", ret_jihejiangjia2)
    df_list = ret_jihejiangjia2[filter_col_gainianzhangfu2]    #[ret_jihejiangjia1[filter_col_gainianzhangfu1],ret_jihejiangjia2[filter_col_gainianzhangfu2]]
    ret_jihejiangjia = df_list    #pd.concat(df_list,   ignore_index=True)
    # ret_jihejiangjia = pd.merge(ret_jihejiangjia1[filter_col_gainianzhangfu1],ret_jihejiangjia2[filter_col_gainianzhangfu2],on='股票代码',how='')
    # ret_jihejiangjia.to_csv("./b.csv")
    # ret_jihejiangjia = ret_jihejiangjia1[filter_col_gainianzhangfu1].set_index('股票代码').combine_first(
    #                             ret_jihejiangjia2[filter_col_gainianzhangfu2].set_index('股票代码')).reset_index()
    # print("---", ret_jihejiangjia)

    # ret_jihejiangjia = ret_jihejiangjia1.me

    '''
    替换其他方式比如ashare
    '''
    '''
    昨日涨停
    '''
    ret_zuorizhangting = pywencai.get(query='昨日涨停  非688开头  非ST 涨停时间从小到大')
    ret_zuorizhangting.to_csv("./zrzt.csv")
    filter_col_zuorizhangting = ['股票代码', '股票简称', '竞价量' + cur_date_str, '最新涨跌幅',
                                  '竞价涨幅' + cur_date_str]


    '''
    锚点 - 近期热点
    '''
    df = get_ths_maodian()
    moaodian_list = df['代码'].values.tolist()
    # ret_maodian = pywencai.get(query='集合竞价 涨速 最高板块 ', find = moaodian_list)

    ret_maodian = Ak_share_client.get_info(moaodian_list)
    # print("xxx",ret_maodian)

    # ret_maodian.to_csv("./md.csv")
    # filter_col_maodian = ['股票代码', '股票简称', '竞价量' + cur_date_str, '最新涨跌幅',
    #                               '竞价涨幅' + cur_date_str]

    '''
    弱转强
    '''
    df = get_ruozhuanqiang_df()
    ruozhuanqiang_list = df['代码'].values.tolist()
    # ret_ruozhuanqiang = pywencai.get(query='集合竞价 涨速 最高板块 ' ,find = ruozhuanqiang_list)
    # ret_ruozhuanqiang.to_csv("./rzq.csv")
    # filter_col_ruozhuanqiang = ['股票代码', '股票简称', '竞价量' + cur_date_str, '最新涨跌幅',
    #                               '竞价涨幅' + cur_date_str]

    ret_ruozhuanqiang = get_ths_ruozhuanqiang()#Ak_share_client.get_info(ruozhuanqiang_list)



    #写到一个excel不同sheet
    # with pd.ExcelWriter('./data/stronger.xlsx') as writer:
    #     res_zt[filter_col_zt].to_excel(writer, sheet_name='Sheet1', index=False)
    #     res_dy5[filter_col_dy5].to_excel(writer, sheet_name='Sheet2', index=False)
    #     res_zb[filter_col_zb].to_excel(writer, sheet_name='Sheet3', index=False)
    #     ret_rqb.to_excel(writer, sheet_name='Sheet4', index=False)

    # 创建一个新的工作簿
    # workbook = Workbook()
    #
    # # 获取当前活动的工作表
    # sheet = workbook.active
    #
    # # # 向单元格写入数据
    # sheet['A1'] = 'Hello'
    # sheet['B1'] = 'World'
    #
    '''
    直接load可以不 - 不行 --不行
    '''
    # 获取当前活动的工作表
    # first_sheet = workbook.active

    # # 保存工作簿
    # workbook.save('./data/stronger.xlsx')
    # 创建一个Excel工作簿
    # workbook = Workbook()
    try:
        #每次都打开新的，相当于半个创建
        workbook = xw.Book('./data/stronger.xlsx')

        # 获取已经运行的Excel应用程序实例，如果没有运行的实例，则会启动一个新的Excel应用程序
        # app = xw.apps.active
        # 打开现有的Excel工作簿，如果文件不存在，则会创建一个新的工作簿
        # workbook = app.books.open('./data/stronger.xlsx')  #修改为你的Excel文件路径

        # print("--1--")
    except FileNotFoundError:
        # print("--2--")
        workbook = xw.Book()
        # 创建其他工作表并指定名称
        sheet_names = ['Sheet2', 'Sheet3', 'Sheet4','Sheet5','Sheet6','Sheet7','Sheet8','Sheet9',
                       'Sheet10','Sheet11','Sheet12','Sheet13','Sheet14','Sheet15','Sheet16',]
        # 使用循环创建并指定多个工作表的名称
        for sheet_name in sheet_names:
            workbook.sheets.add(sheet_name,after=workbook.sheets[-1])
            # workbook.create_sheet(title=sheet_name)
        # 必须保存，否则加载找不到
        workbook.save('./data/stronger.xlsx')
    # sheet = workbook.active

    # 创建WPS表格应用程序实例
    # app = xw.App(visible=True, add_book=False, spec='wps')

    # 打开现有的Excel工作簿，如果文件不存在，则会创建一个新的工作簿
    # try:
    #     workbook = app.books.open('./data/stronger.xlsx')  # 修改为你的Excel文件路径
    # except Exception as e:
    #     print(f"Error: {e}")
    # sheet_names = ['Sheet2', 'Sheet3', 'Sheet4','Sheet5']
    # # 使用循环创建并指定多个工作表的名称
    # for sheet_name in sheet_names:
    #     # workbook.sheets.add(sheet_name,after=workbook.sheets[-1])
    #     # workbook.create_sheet(title=sheet_name)
    #     new_sheet = workbook.sheets.add(sheet_name, after=workbook._sheets[-1])

        # 创建第一个sheet页并写入第一个DataFrame数据
    # sheet1 = workbook.active
    # sheet1.title = 'Sheet1'

    # 获取工作簿中的所有工作表
    # all_sheets = workbook._sheets
    # print(all_sheets)

    sheet2=workbook.sheets['Sheet2']          #.sheets[0]
    # for row in dataframe_to_rows(res_zt, index=False, header=True):#[filter_col_zt]
    #     # sheet1.append(row)
    #     sheet1.range.value

        # # 在空白行写入数据
        # for i, data in enumerate(row_data):
        #     sheet1.range(f'A{empty_row + i}').value = data

    # 将DataFrame写入Excel的指定单元格
    # workbook.get_sheet_by_name("Sheet1").
    is_refresh = compare_and_notify("zt",sheet2, res_zt[filter_col_zt])

    #写入之前clear ,避免和昨天的混淆
    #如果compare为False,也没有必要写入，减少磁盘

    if is_refresh:
        clear_and_setFormat(sheet2)
        res_zt = get_fill_url(res_zt)
        #添加url列
        filter_col_zt.append('url')

        sheet2.range('A1').value = res_zt[filter_col_zt]  # 将DataFrame写入A1单元格，xlwings会自动处理整个DataFrame

        # 添加图片列
        get_k_jpg(sheet2)

    #
    # # 创建第二个sheet页并写入第二个DataFrame数据
    # # sheet2 = workbook.create_sheet(title='Sheet2')
    # sheet2 = workbook.active
    # sheet2.title = 'Sheet2'
    sheet3=workbook.sheets['Sheet3']
    # for row in dataframe_to_rows(res_dy5, index=False, header=True):#[filter_col_dy5]
    #     sheet2.append(row)
    is_refresh = compare_and_notify("dy5",sheet3, res_dy5[filter_col_dy5])
    if is_refresh:
        # print("---sheet3-refresh-")
        clear_and_setFormat(sheet3)
        res_dy5 = get_fill_url(res_dy5)
        filter_col_dy5.append('url')
        sheet3.range('A1').value = res_dy5[filter_col_dy5]

        get_k_jpg(sheet3)


    #
    # sheet3 = workbook.active
    # sheet3.title = 'Sheet3'
    sheet4=workbook.sheets['Sheet4']
    # for row in dataframe_to_rows(res_zb, index=False, header=True):#[filter_col_zb]
    #     sheet3.append(row)
    is_refresh = compare_and_notify("zb",sheet4,res_zb[filter_col_zb])
    # print("===sheet4===",is_refresh)
    if is_refresh:
        clear_and_setFormat(sheet4)
        res_zb = get_fill_url(res_zb)
        filter_col_zb.append('url')
        sheet4.range('A1').value = res_zb[filter_col_zb]

        get_k_jpg(sheet4)



    # 创建第二个sheet页并写入第二个DataFrame数据
    # sheet4 = workbook.active
    # sheet4.title = 'Sheet4'
    sheet5=workbook.sheets['Sheet5']
    # for row in dataframe_to_rows(ret_rqb, index=False, header=True):#[filter_col_hx]
    #     sheet4.append(row)



    #-------对比 触发-----------
    #
    #
    # # 显式地关闭Excel文件
    # # workbook.close()
    # # before_pd = pd.read_excel("./data/stronger.xlsx")
    # # print(before_pd.to_string())
    # # before_pd
    # # print(sheet4.range('A1').value)
    # # 从 Sheet3 获取数据并转换为 Pandas DataFrame
    # data_before = sheet4.range('A1').expand().options(pd.DataFrame, header=True, index=False).value
    # # print(data_range)
    #
    # #两个中code类型不同  -> 为什么有的DataFrame不能是哦那个
    # data_before['code'] = data_before['code'].astype(str)
    # ret_rqb[filter_col_hx]['code'] = ret_rqb[filter_col_hx]['code'].astype(str)
    #
    # #重置序号，否则少数据，多数据序号也会算
    # data_before.reset_index(drop=True)
    # ret_rqb[filter_col_hx].reset_index(drop=True)
    #
    # merged_df = pd.merge(data_before, ret_rqb[filter_col_hx], on='code', how='outer', indicator=True)
    # # print("---",merged_df)
    # # print("====",data_before)
    # # print("+++",ret_rqb[filter_col_hx])
    #
    # # 只保留来自左边DataFrame的行（_merge列的值为'left_only'）
    # diff_df_left_xzb = merged_df[merged_df['_merge'] == 'left_only']
    # diff_df_right_xzt = merged_df[merged_df['_merge'] == 'right_only']
    #
    # notify_col = ['code', '股票简称_x', '所属同花顺行业_x']
    # if not diff_df_left_xzb.empty:
    #
    #     msg = diff_df_right_xzt[notify_col].to_string()
    #     # print("--->>notify me <----",diff_df_left_xzb[notify_col])
    #     wx.send_msg_toWechat(msg)
    #
    # if not diff_df_right_xzt.empty:
    #     msg = diff_df_right_xzt[notify_col].to_string()
    #     # print("--->>notify me <----",)
    #     wx.send_msg_toWechat(msg)
    #

    # compare_and_notify(sheet5,ret_rqb[filter_col_hx])

    #------------------

    #写最新信息到文档
    is_refresh = compare_and_notify("rqb",sheet5,ret_rqb[filter_col_hx])
    if is_refresh:
        clear_and_setFormat(sheet5)
        ret_rqb = get_fill_url(ret_rqb)
        filter_col_hx.append('url')
        sheet5.range('A1').value = ret_rqb[filter_col_hx]

        # get_k_jpg(sheet5)


    #自选股这里直接保存，不判断是否存在问题
    sheet6 = workbook.sheets['Sheet6']
    # is_refresh = compare_and_notify("zixuangu", sheet5, ret_zixuangu[filter_col_zixuangu])
    # if is_refresh:
    # clear_and_setFormat(sheet5)
    ret_zixuangu = get_fill_url(ret_zixuangu)
    filter_col_zixuangu.append('url')
    sheet6.range('A1').value = ret_zixuangu[filter_col_zixuangu]


    sheet7 = workbook.sheets['Sheet7']
    clear_and_setFormat(sheet7)
    sheet7.range('A1').value = ret_dieting[filter_col_dieting]

    sheet8 = workbook.sheets['Sheet8']
    clear_and_setFormat(sheet8)
    sheet8.range('A1').value = ret_diedayu5[filter_col_diedayu5]



    # sheet9 = workbook.sheets['Sheet9']
    # clear_and_setFormat(sheet9)
    # sheet8.range('A1').value = ret_hangyezhangfu[filter_col_hangyezhangfu]
    #
    # sheet10 = workbook.sheets['Sheet10']
    # clear_and_setFormat(sheet10)
    # sheet8.range('A1').value = ret_gainianzhangfu[filter_col_gainianzhangfu]

    sheet11 = workbook.sheets['Sheet11']
    clear_and_setFormat(sheet11)
    sheet11.range('A1').value = ret_jihejiangjia

    sheet15 = workbook.sheets['Sheet15']
    clear_and_setFormat(sheet15)
    sheet15.range('A1').value = ret_maodian
    # sheet16 = workbook.sheets['Sheet16']
    # clear_and_setFormat(sheet16)
    # sheet16.range('A1').value = ret_ruozhuanqiang

    # sheet16 = workbook.sheets['Sheet16']
    # is_refresh = filter_zhangsu_yidong("T", ret_T,sheet16)
    # #每次都刷新，但是上面的通知是满足条件后再通知,通知了再去看吧。一般都是烂股，清理中
    # # is_refresh = True
    # if is_refresh:
    #     clear_and_setFormat(sheet16, False)
    #     ret_T = get_fill_url(ret_T)
    #     filter_col_zb.append('url')
    #     sheet16.range('A1').value = ret_T

    #     # get_k_jpg(sheet16)

    # 保存Excel文件
    print('-- refresh --',datetime.now(),"-------")

    # workbook.save('./data/stronger.xlsx')    save会导致出现每次一个文件

def clear_and_setFormat(sheet):
    # 获取所有图片对象
    pictures = sheet.pictures

    # 删除所有图片
    for picture in pictures:
        picture.delete()

    sheet.clear_contents()
    # sheet.range('A1').expand().number_format = '@' #先清空，后这么设置不生效

def get_fill_url(df):
    #便利DataFrame
    # 遍历行

    #不传sheet ,传 DataFrame进去
    # num_rows = sheet.api.UsedRange.Rows.Count
    # print("--num_rows--",num_rows)
    #
    # # 遍历Sheet中的每一行
    # for row in range(1, num_rows + 1):
    #     # 获取指定行的数据（假设是第1列）
    #     # cell_value = xw.Range(sheet, (row, 1)).value
    #     cell_value = sheet.range('B2').value
    #     print(f'Row {row}: {cell_value}')
    #     print("sheet row items ")
    #     # print(f'code: {sheet_row["code"]}')
    #     # #获取超链接
    #     # sheet_row['name'] = geturl(sheet_row['code'])

    #添加新列  -- 不用循环吗？
    # df['url'] = []
    # for index,row in df.iterrows():
    #     # print("-------df -----",index,row['code'])
    #     # df.iat[index, 0] = geturl(row['code'])
    #     df.insert()['url'] = geturl(row['code'])
    #     print(df.to_string())
    # 为DataFrame添加新列url，使用apply函数调用geturl函数
    try:
        df['url'] = df['code'].apply(geturl)
    except:
        df['url'] = df['代码'].apply(geturl)

    # print("===>>",df['url'].to_string())

    return df





'''
对涨速、异动策略，
    1.去除噪音
    2.准确率
'''
def filter_zhangsu_yidong(msg_type,ret,sheet):
    # print('msgtype111',msg_type)
    # print('--msg111--ret',ret)
    #这里策略
    # if (ret['涨跌幅'] >= 1.0) & ((ret['涨速'] > 1.0) | (ret['5分钟涨跌'] > 1.0) | (ret['量比'] > 1)):
    # 遍历DataFrame,再每行判断，区分开下面这种
    # ZhangTing_df = df[((df["changepercent"] > 9.5) & (df['code'] < '609999') & (df["changepercent"] < 11) & (
    #             (df['code'] > '309999') | (df['code'] < '111111'))) | (
    #                               # df["changepercent"] > 19)]  # & (df['name']) 不知道如何强转

    # ret = ret[(ret['涨跌幅'] >= 1.0) & ((ret['涨速'] > 1.0) | (ret['5分钟涨跌'] > 1.0) | (ret['量比'] > 1))]

    '''
    自选 + 涨幅>= 1.0  --todo : 现在未起作用 -- 应该可以
    已持有的话大于1就去通知
    '''
    ret1 = None
    ret2 = None
    ret3 = None
    ret4 = None
    if 'T' == msg_type:
    # ret = ret[(ret['涨跌幅'] >= 1.0)  | (ret['涨速'] >= 0.5) ]
    # if '2.0T' == msg_type:
    #     ret = ret[(ret['涨跌幅'] >= 2.0)  | (ret['涨速'] >= 0.5) ]
    # if '3.0T' == msg_type:
    #     ret = ret[(ret['涨跌幅'] >= 3.0)  | (ret['涨速'] >= 0.5) ]

        ''''
        分组逻辑
        '''
        ret1 = ret[((ret['涨跌幅'] >= 1.0) & (ret['涨跌幅'] < 2.0))]
        ret2 = ret[((ret['涨跌幅'] >= 2.0) & (ret['涨跌幅'] < 3.0))]
        ret3 = ret[((ret['涨跌幅'] >= 3.0) & (ret['涨跌幅'] < 4.0))]
        ret4 = ret[((ret['涨跌幅'] >= 4.0) & (ret['涨跌幅'] < 10.0))]

        # print("ret1-->",ret1)
        # print("ret2-->", ret2)
        # print("ret3-->", ret3)
        # print("ret4-->", ret4)

    '''
    自选的话大于3去通知
    '''
    if 'zx' == msg_type:
        ret = ret[(ret['涨跌幅'] >= 3.0) | (ret['量比'] >= 1.5) | (ret['涨速'] >= 0.5)]


    # print("===1===ret is ",ret)

    if 'jhjj' == msg_type:
        current_date = date.today()
        cur_date_str = '[' + str(current_date.strftime("%Y%m%d")) + ']'
        # print(cur_date_str)
        f='涨跌幅:前复权'+ cur_date_str
        # ret = ret[(float(ret[f]) >= 3.0)]
        tolerance = 0.000001  # 容忍误差
        ret = ret[(ret[f].astype(float) >= 3.0 - tolerance)]
        # ret = ret[(ret[f] >= '3.0')]
        # print("==>>>",ret)
        ret.rename(columns={'股票代码': 'code'}, inplace=True)

    '''
    全市场异动(异动精灵) + (自选+人气榜+其他自己提前过滤过的)
    
    获取实时股票数据：使用股票数据接口获取实时的股票数据，可以选择使用第三方的股票数据API或者爬取股票信息网站的数据。
    定义筛选策略：定义异动精灵的策略，例如涨幅超过一定百分比、成交量大幅增加、股价突破前高等等。根据策略筛选符合条件的股票。
    提醒机制：根据筛选出的股票，可以选择通过邮件、短信、微信推送等方式进行提醒，通知用户有异动的股票出现。
    
    '''

    '''
    这里不应该这么写，因为不用对比，他的票没有新增概念，而是监控票涨幅和涨速问题，所以不用compare 
    但是又考虑到每次都要报警所以加入关闭功能
    '''
    if 'T' == msg_type:
        no_notify_list = get_no_notify_list();
        no_notify_list_2T = get_no_notify_list_2T();
        no_notify_list_3T = get_no_notify_list_3T();
        no_notify_list_4T = get_no_notify_list_4T();
        '''
        这里过滤的是1.0T 情况
        '''
        # if 'T' == msg_type:
        #     ret = ret[(~ret['code'].isin(no_notify_list))]
        # if '2.0T' == msg_type:
        #     ret = ret[(~ret['code'].isin(no_notify_list_2T))]
        # if '3.0T' == msg_type:
        #     ret = ret[(~ret['code'].isin(no_notify_list_3T))]

        ret1 = ret1[(~ret1['code'].isin(no_notify_list))]
        ret2 = ret2[(~ret2['code'].isin(no_notify_list_2T))]
        # print("ret222-->",ret2)
        ret3 = ret3[(~ret3['code'].isin(no_notify_list_3T))]
        # print("ret333-->", ret3)
        ret4 = ret4[(~ret4['code'].isin(no_notify_list_4T))]
        # print("not is in ",ret)


        # compare_and_notify(msg_type,sheet,ret)
        ret1 = ret1[['code','股票简称']].reset_index(drop=True)
        msg1 = ret1.to_string(header=False, index=False)
        # print("retggggg-->", ret2)
        ret2 = ret2[['code', '股票简称']].reset_index(drop=True)
        # print("retggggg-->", ret2)
        msg2 = ret2.to_string(header=False, index=False)
        ret3 = ret3[['code', '股票简称']].reset_index(drop=True)
        msg3 = ret3.to_string(header=False, index=False)
        ret4 = ret4[['code', '股票简称']].reset_index(drop=True)
        msg4 = ret4.to_string(header=False, index=False)
        # print("--ret--",ret)
    #如果sheet中已存在、说明已经关注到了，不在通知
        '''
        异动 - 斜率计算  ret值和sheet值对比
        '''
        if not ret1.empty:
            msg1 = "============1T============\n" + msg1
            qywx.send_text(msg1)
            # return True
        if not ret2.empty:
            msg2 = "============2T============\n" + msg2
            qywx.send_text(msg2)
            # return True
        if not ret3.empty:
            msg3 = "============3T============\n" + msg3
            qywx.send_text(msg3)
            # return True
        if not ret4.empty:
            msg4 = "============4T============\n" + msg4
            qywx.send_text(msg4)
            # return True

    # print("========<<<<<")
    if not ret.empty:


        if msg_type == 'zx':
            ret = ret[['code', '股票简称']].reset_index(drop=True)
            msg = ret.to_string(header=False, index=False)

            msg = "============zx============\n" + msg
            qywx.send_text(msg)
            # return True

        if msg_type == 'jhjj':
            current_date = date.today()
            cur_date_str = '[' + str(current_date.strftime("%Y%m%d")) + ']'
            # print(cur_date_str)
            f = '涨跌幅:前复权' + cur_date_str
            ret = ret[['code', '股票简称',f]].reset_index(drop=True)
            msg = ret.to_string(header=False, index=False)

            msg = "============jhjj============\n" + msg
            qywx.send_text(msg)
            # return True

        if msg_type == 'wufenzhong':
            ret = ret[['code', '股票简称','最新涨跌幅']].reset_index(drop=True)
            msg = ret.to_string(header=False, index=False)

            msg = "============wufenzhong============\n" + msg
            qywx.send_text(msg)

    return True






import Quantification.send.Qiyewx as qywx
def compare_and_notify(msg_type,current_sheet,filter_ret_x):

    # 显式地关闭Excel文件
    # workbook.close()
    # before_pd = pd.read_excel("./data/stronger.xlsx")
    # print(before_pd.to_string())
    # before_pd
    # print(sheet4.range('A1').value)
    # 从 Sheet3 获取数据并转换为 Pandas DataFrame
    data_before = current_sheet.range('A1').expand().options(pd.DataFrame, header=True, index=False).value
    # print(data_range)

    #首次加载，数据没有
    try:
        data_before['code']
    except:
        # print("---code is None---")
        return True


    # 两个中code类型不同  -> 为什么有的DataFrame不能是哦那个
    data_before['code'] = data_before['code'].astype(str)
    filter_ret_x['code'] = filter_ret_x['code'].astype(str)

    # 重置序号，否则少数据，多数据序号也会算
    data_before.reset_index(drop=True)
    filter_ret_x.reset_index(drop=True)

    # print("没加载进去吗?",data_before)

    merged_df = pd.merge(data_before, filter_ret_x, on='code', how='outer', indicator=True)

    # print("--sheet3 -compaer")
    # print(data_before)
    # print(filter_ret_x)

    # print("---",merged_df)
    # print("====",data_before)
    # print("+++",ret_rqb[filter_col_hx])

    # 只保留来自左边DataFrame的行（_merge列的值为'left_only'）
    #去掉原因是：炸板有对应的语句查询无需这里对比

    #把不经常用的左连接放到了下面，减少代码操作
    diff_df_right_xzt = merged_df[merged_df['_merge'] == 'right_only']

    # print("--------1--------")
    # print(diff_df_left_xzb)
    # diff_df_left_xzb.to_csv("./ttt.csv")
    # print("--------2--------")
    # print(diff_df_right_xzt)


    notify_col_left = ['code', '股票简称_x']
    notify_col_right = ['code', '股票简称_y']
    #
    # #往下移动，减少代码执行，早点return
    # diff_df_left_xzb = merged_df[merged_df['_merge'] == 'left_only']
    # #左连接存在说明老数据多，现在清理下，比如当天清理昨天也是这个道理，不用发消息，自动退出就行
    # if not diff_df_left_xzb.empty:
    #     return True;





    '''
    # diff_df_left_xzb = diff_df_left_xzb[notify_col_left].reset_index(drop=True)
    # msg = diff_df_left_xzb.to_string(header=False,index=False)
    # # print("--->>notify me <----",diff_df_left_xzb[notify_col])
    # # wx.send_msg_toWechat(msg)
    # if msg_type == 'zt':
    #     msg = "============zt============\n" + msg
    # if msg_type == 'dy5':
    #     msg = "============dy5============\n" + msg
    # if msg_type == 'zb':
    #     msg = "============zb============\n" + msg
    #
    # qywx.send_text(msg)
    '''


    if not diff_df_right_xzt.empty:
        diff_df_right_xzt =  diff_df_right_xzt[notify_col_right].reset_index(drop=True)
        msg = diff_df_right_xzt.to_string(header=False,index=False)
        # print("--->>notify me <----",)
        # wx.send_msg_toWechat(msg)
        if msg_type == 'zt':
            msg = "============zt============\n" + msg
        if msg_type == 'dy5':
            msg = "============dy5============\n" + msg
        if msg_type == 'zb':
            msg = "============zb============\n" + msg
        if msg_type == 'rqb':
            return True

        qywx.send_text(msg)

        return True


    #往下移动，减少代码执行，早点return
    diff_df_left_xzb = merged_df[merged_df['_merge'] == 'left_only']
    # print("左连接",diff_df_left_xzb)
    #左连接存在说明老数据多，现在清理下，比如当天清理昨天也是这个道理，不用发消息，自动退出就行
    if not diff_df_left_xzb.empty:
        return True



    return False



def get_alway_doing():
    current_date = date.today()

    cur_date_str =  '[' + str(current_date.strftime("%Y%m%d")) + ']'

    res_zt = pywencai.get(query='今日涨停和涨停原因非ST 首次涨停时间排序 行业', sort_key='', sort_order='涨停类型')
    filter_col_zt = ['code','股票简称','最新价',
                  '首次涨停时间'+cur_date_str,'涨停原因类别'+cur_date_str,'涨停类型'+cur_date_str,
                  '连续涨停天数'+cur_date_str,'几天几板' + cur_date_str,
                  '涨停封单量'+cur_date_str,'涨停封单额'+cur_date_str,'涨停开板次数'+cur_date_str
                  ]


    # res_dy5 = pywencai.get(query='今日涨幅大于5 非30开头 非 688开头 非ST 非涨停 展示行业 ', sort_key='', sort_order='')
    # filter_col_dy5 = ['code','股票简称','最新价',
    #               '成交量' + cur_date_str, '所属同花顺行业',
    #               '涨停价'+ cur_date_str
    #               ]

    res_dy8 = pywencai.get(query='今日涨幅大于8 非30开头 非 688开头 非ST 非涨停 展示行业 ', sort_key='', sort_order='')
    filter_col_dy8 = ['code', '股票简称', '最新价',
                      '成交量' + cur_date_str, '所属同花顺行业',
                      '涨停价' + cur_date_str
                      ]

    res_zb = pywencai.get(query='今日炸板不含ST 所属行业', sort_key='', sort_order='')
    filter_col_zb = ['code','股票简称','最新价',
                  '涨停时间明细'+cur_date_str,'涨停开板次数'+cur_date_str,
                  '所属同花顺行业',
                  '涨停价'+ cur_date_str
                  ]

    ret_jihejiangjia2 = pywencai.get(query='集合竞价 竞价抢筹 非688开头 非30开头 非新股;非st 涨幅大于1  竞价量从大到小')
    filter_col_gainianzhangfu2 = ['股票代码', '股票简称', '竞价量' + cur_date_str, '涨跌幅:前复权' + cur_date_str,
                                  '竞价涨幅' + cur_date_str
                                  # '个股热度排名'+cur_date_str ,
                                  # '所属同花顺行业', '所属概念'
                                  ]

    ret_T = get_T()

    try:
        workbook = xw.Book('./data/stronger.xlsx')

        # 获取已经运行的Excel应用程序实例，如果没有运行的实例，则会启动一个新的Excel应用程序
        # app = xw.apps.active
        # 打开现有的Excel工作簿，如果文件不存在，则会创建一个新的工作簿
        # workbook = app.books.open('./data/stronger.xlsx')  #修改为你的Excel文件路径

        # print("--1--")
    except FileNotFoundError:
        # print("--2--")
        workbook = xw.Book()
        # 创建其他工作表并指定名称
        sheet_names = ['Sheet2', 'Sheet3', 'Sheet4','Sheet5','Sheet6','Sheet7','Sheet8','Sheet9','Sheet10','Sheet11','Sheet12','Sheet13','Sheet14']
        # 使用循环创建并指定多个工作表的名称
        for sheet_name in sheet_names:
            workbook.sheets.add(sheet_name,after=workbook.sheets[-1])
        workbook.save('./data/stronger.xlsx')

    sheet2=workbook.sheets['Sheet2']          #.sheets[0]
    is_refresh = compare_and_notify("zt",sheet2, res_zt[filter_col_zt])

    if is_refresh:
        clear_and_setFormat(sheet2,False)
        res_zt = get_fill_url(res_zt)
        filter_col_zt.append('url')
        sheet2.range('A1').value = res_zt[filter_col_zt]  # 将DataFrame写入A1单元格，xlwings会自动处理整个DataFrame
        # get_k_jpg(sheet2)

    # # dayu 5 的不提示，直接
    # sheet3=workbook.sheets['Sheet3']
    # # is_refresh = compare_and_notify("dy5",sheet3, res_dy5[filter_col_dy5])
    # is_refresh = True
    # if is_refresh:
    #     clear_and_setFormat(sheet3,False)
    #     res_dy5 = get_fill_url(res_dy5)
    #     filter_col_dy5.append('url')
    #     sheet3.range('A1').value = res_dy5[filter_col_dy5]

    #     # get_k_jpg(sheet3)



    sheet15=workbook.sheets['Sheet15']
    is_refresh = compare_and_notify("dy8",sheet15, res_dy8[filter_col_dy8])
    # is_refresh = True
    if is_refresh:
        clear_and_setFormat(sheet15,False)
        res_dy8 = get_fill_url(res_dy8)
        filter_col_dy8.append('url')
        sheet15.range('A1').value = res_dy8[filter_col_dy8]

        # get_k_jpg(sheet15)

    sheet4 = workbook.sheets['Sheet4']
    is_refresh = compare_and_notify("zb", sheet4, res_zb[filter_col_zb])
    if is_refresh:
        clear_and_setFormat(sheet4, False)
        res_zb = get_fill_url(res_zb)
        filter_col_zb.append('url')
        sheet4.range('A1').value = res_zb[filter_col_zb]

        # get_k_jpg(sheet4)

    sheet11 = workbook.sheets['Sheet11']
    is_refresh = filter_zhangsu_yidong("jhjj", ret_jihejiangjia2[filter_col_gainianzhangfu2],sheet11)
    clear_and_setFormat(sheet11, True)
    sheet11.range('A1').value = ret_jihejiangjia2[filter_col_gainianzhangfu2]
   
    sheet16 = workbook.sheets['Sheet16']
    is_refresh = filter_zhangsu_yidong("T", ret_T,sheet16)
    #每次都刷新，但是上面的通知是满足条件后再通知,通知了再去看吧。一般都是烂股，清理中
    # is_refresh = True
    ret_T = ret_T[(ret_T['涨跌幅'] >= 1.0)]
    # print("0000",ret_T)
    if is_refresh:
        clear_and_setFormat(sheet16, False)
        ret_T = get_fill_url(ret_T)
        filter_col_zb.append('url')
        sheet16.range('A1').value = ret_T

        # get_k_jpg(sheet16)

    # sheet9 = workbook.sheets['Sheet9']
    # is_refresh = filter_zhangsu_yidong("zx", ret_zx, sheet9)
    # # 每次都刷新，但是上面的通知是满足条件后再通知,通知了再去看吧。一般都是烂股，清理中
    # # is_refresh = True
    # if is_refresh:
    #     clear_and_setFormat(sheet9, False)
    #     ret_zx = get_fill_url(ret_zx)
    #     filter_col_zb.append('url')
    #     sheet9.range('A1').value = ret_zx

    # 保存Excel文件
    print('-- refresh --',datetime.now(),"-------")



def getJiange():
    ret_wufenzhong = pywencai.get(query='"五分钟涨幅最快 前30 非30开头 非688开头 非83开头 非87开头 非ST"', sort_key='',
                                  sort_order='')
    # ret_wufenzhong.to_csv("./wufenzhong.csv")
    filter_col_wufenzhong = ['code', '股票简称', '最新涨跌幅']

    try:
        workbook = xw.Book('./data/stronger.xlsx')

        # 获取已经运行的Excel应用程序实例，如果没有运行的实例，则会启动一个新的Excel应用程序
        # app = xw.apps.active
        # 打开现有的Excel工作簿，如果文件不存在，则会创建一个新的工作簿
        # workbook = app.books.open('./data/stronger.xlsx')  #修改为你的Excel文件路径

        # print("--1--")
    except FileNotFoundError:
        # print("--2--")
        workbook = xw.Book()
        # 创建其他工作表并指定名称
        sheet_names = ['Sheet2', 'Sheet3', 'Sheet4','Sheet5','Sheet6','Sheet7','Sheet8','Sheet9','Sheet10','Sheet11','Sheet12','Sheet13','Sheet14']
        # 使用循环创建并指定多个工作表的名称
        for sheet_name in sheet_names:
            workbook.sheets.add(sheet_name,after=workbook.sheets[-1])
        workbook.save('./data/stronger.xlsx')

    sheet6 = workbook.sheets['Sheet6']
    ret_wufenzhong = ret_wufenzhong[(ret_wufenzhong['最新涨跌幅'] >= str(1.0))]
    is_refresh = filter_zhangsu_yidong("wufenzhong", ret_wufenzhong, sheet6)

    # print("===>",ret_wufenzhong)
    if True:
        clear_and_setFormat(sheet6, False)
        ret_wufenzhong = get_fill_url(ret_wufenzhong)
        filter_col_wufenzhong.append('url')
        sheet6.range('A1').value = ret_wufenzhong[filter_col_wufenzhong]

    print('-- refresh wufenzhong --',datetime.now(),"-------")




import qstock as qs
def duanxianjingling():

    duaxianjingling_df = qs.realtime_change('火箭发射')
    duaxianjingling_df.rename(columns={'代码': 'code','名称': '股票简称'}, inplace=True)

    duaxianjingling_df = duaxianjingling_df[((duaxianjingling_df['code'] < '609999') & (duaxianjingling_df['code'] > '309999')) | (duaxianjingling_df['code'] < '111111') ]  #& (df['name']) 不知道如何强转
    print(duaxianjingling_df)

    filter_col_duanxianjingling = ['code', '股票简称', '板块']

    try:
        workbook = xw.Book('./data/stronger.xlsx')
    except FileNotFoundError:
        workbook = xw.Book()
        sheet_names = ['Sheet2', 'Sheet3', 'Sheet4', 'Sheet5', 'Sheet6', 'Sheet7', 'Sheet8', 'Sheet9', 'Sheet10',
                       'Sheet11', 'Sheet12', 'Sheet13', 'Sheet14']
        for sheet_name in sheet_names:
            workbook.sheets.add(sheet_name, after=workbook.sheets[-1])
        workbook.save('./data/stronger.xlsx')

    sheet12 = workbook.sheets['Sheet12']
    is_refresh = compare_and_notify("duanxianjingling", sheet12, duaxianjingling_df)
    if True:
        clear_and_setFormat(sheet12, False)
        duaxianjingling_df = get_fill_url(duaxianjingling_df)
        filter_col_duanxianjingling.append('url')
        sheet12.range('A1').value = duaxianjingling_df[filter_col_duanxianjingling]

    print('-- refresh duaxianjingling --', datetime.now(), "-------")





''''

1.就像同花顺一样，一直更新，就像视频聊天一样 。 拉取所有，再栓选需要的 ...===> 想要这个，就需要记录上次的index,这次从index取到最后，实现推的效果。防止重复和遗漏
2.自选股的提示 -- 匹配自选  + 连续大笔买入，或者火箭发射
3.刷新频率、与其他的协调，是否耗时
4.其他接口信息开发，比如北向资金、咨询、
5.近期总结，能否使用代码量化，这么多接口和数据
6.东方财富网还有哪些有用的数据可以爬取

'''

import qstock as qs


def get_dabimairu_dui():
    changes_list = ['火箭发射', '快速反弹', '加速下跌', '高台跳水', '大笔买入',
                    '大笔卖出', '封涨停板', '封跌停板', '打开跌停板', '打开涨停板', '有大买盘',
                    '有大卖盘', '竞价上涨', '竞价下跌', '高开5日线', '低开5日线', '向上缺口',
                    '向下缺口', '60日新高', '60日新低', '60日大幅上涨', '60日大幅下跌']
    dxjl_all = qs.realtime_change()
    filter_col_duanxianjingling = ['时间', '代码', '名称', '板块']
    dxjl_all = dxjl_all[filter_col_duanxianjingling]
    '''
    每三秒刷新一次
    '''
    dxjl_part = dxjl_all[(dxjl_all['板块'] == '大笔买入')]

    '''
    统计指定时间的大笔买入
    '''
    dxjl_part = dxjl_part.head(20)
    dxjl_part_ct = dxjl_part['名称'].value_counts()
    # print(dxjl_part_ct)

    # 判断出现次数是否大于2，如果是，打印一句话
    for category, count in dxjl_part_ct.items():
        if count > 2:
            # print(f"类别 '{category}' 出现次数大于2。次数是'{count}'")
            msg = "============大笔大于2============\n"+f" '{category}' 出现次数大于2。次数是'{count}'"
            qywx.send_text(msg)

    '''
    统计当天前几的大单买入，参考意义不大
    '''
    # dxjl_part_counts = dxjl_part['名称'].value_counts()
    # print(dxjl_part_counts.head().to_string())

    # print(dxjl_part.head(20))

    '''
    自选在当日的  短线精灵  中的表现，统计意义较大，及时性不好
    '''
    # dxjl_zx = dxjl_all[(dxjl_all['代码'].isin(list_zixuangu))]
    # if not dxjl_zx.empty:
    #     msg2 = dxjl_zx.reset_index(drop=True).to_string(header=False, index=False)
    #     msg = "============火箭-自选============\n" + msg2
    #     qywx.send_text(msg)

    '''
    自选 短线精灵中出现 ，关注
    '''
    dxjl_zx = dxjl_part[(dxjl_part['代码'].isin(list_zixuangu))]
    if not dxjl_zx.empty:
        msg2 = dxjl_zx.reset_index(drop=True).to_string(header=False, index=False)
        msg = "============大笔-自选============\n" + msg2
        qywx.send_text(msg)


'''
如何避免丢失呢
'''

def save_point(index):
    file = open("./index.txt", 'w')
    file.write(str(index))
    file.close()
def get_point():
    with open('./index.txt') as f:
        return f.read()


def get_xx():
    changes_list = ['火箭发射', '快速反弹', '加速下跌', '高台跳水', '大笔买入',
                    '大笔卖出', '封涨停板', '封跌停板', '打开跌停板', '打开涨停板', '有大买盘',
                    '有大卖盘', '竞价上涨', '竞价下跌', '高开5日线', '低开5日线', '向上缺口',
                    '向下缺口', '60日新高', '60日新低', '60日大幅上涨', '60日大幅下跌']
    dxjl_all = qs.realtime_change()

    # print(dxjl_all.head(10))
    '''
    从新index开始计算输出
    '''
    index = int(get_point())
    save_point(dxjl_all.shape[0])

    dxjl_all = dxjl_all.iloc[0:(dxjl_all.shape[0] - index)]

    dxjl_part = dxjl_all[(dxjl_all['板块'] == '火箭发射') | ((dxjl_all['板块'] == '大笔买入')) | ((dxjl_all['板块'] == '封涨停板'))  | ((dxjl_all['板块'] == '打开跌停板')) ]

    filter_col_duanxianjingling = ['时间', '代码', '名称', '板块']
    if not dxjl_part.empty:
        msg2 = "============精灵============\n"+dxjl_part[filter_col_duanxianjingling].reset_index(drop=True).to_string(header=False, index=False)
        qywx.send_text_B(msg2)

    '''
    这样可以看到当天所有的改票的异动情况！！！
        # dxjl_zx = dxjl_part[(dxjl_part['代码'].isin(list_zixuangu))]
    '''
    dxjl_zx = dxjl_part[(dxjl_part['代码'].isin(list_zixuangu))]
    if not dxjl_zx.empty:
        msg2 = dxjl_zx.reset_index(drop=True).to_string(header=False, index=False)
        msg = "============精灵-自选============\n" + msg2
        qywx.send_text_B(msg)
        qywx.send_text(msg)

''''
感知总体

1.两市成交额、增量
2.北向资金
3.资金流入板块
4.资金流入个股最多
5.上涨下跌家数
6.新闻电报

'''


def quanjushuju():
    # 获取概念板块最新行情指标
    # df = qs.realtime_data('概念板块')
    # 查看前几行
    # print(df.head(50))

    # df=qs.realtime_data('ETF')
    #查看前几行
    # print(df.head(50))

    df = qs.realtime_data(code=['深证指数','上证指数'])
    filter_colume = ['名称','最新','最高','最低','今开','成交额']
    # print(df[filter_colume])

    qywx.send_text_B("============quanju============\n"+df[filter_colume].reset_index(drop=True).to_string(index=False))

    # 个股20日资金流数据
    # df = qs.ths_money('个股', n=1)
    # print(df.head(20))
    # # 行业板块10日资金流数据
    # df = qs.ths_money('行业', n=1)
    # print(df.head(20))
    # # 概念板块5日资金流数据
    # df = qs.ths_money('概念', n=1)
    # print(df.head(20))

    # 北向资金每日净流入数据
    df = qs.north_money()
    # print(df.tail())
    qywx.send_text_B("============beixiang-jin5tian============\n" + df.tail().to_string(index=False))

    df = qs.north_money('行业',1)
    df = df.sort_values(by='涨跌幅',ascending=[False])
    # df.tail()
    # print(df.head(10))
    filter_colume = ['名称','涨跌幅', '增持最大股市值', '减持最大股市值', '增持最大股占总市值比','减持最大股占总市值比']
    qywx.send_text_B("============beixiang-hangye============\n" + df.head(10)[filter_colume].reset_index(drop=True).to_string(index=False))

    df = qs.north_money('概念', 1)
    df = df.sort_values(by='涨跌幅',ascending=[False])
    qywx.send_text_B("============beixiang-gainian============\n" + df.head(10)[filter_colume].reset_index(drop=True).to_string(index=False))

    df = qs.north_money('个股', 1)
    df = df.sort_values(by='涨幅',ascending=[False])
    filter_colume = ['代码', '名称', '涨幅', '今日增持股数', '今日增持市值','今日增持市值增幅','所属板块']
    qywx.send_text_B("============beixiang-gegu============\n" + df.head(100)[filter_colume].reset_index(drop=True).to_string(index=False))

    # df = qs.north_money('个股', 1)
    df = df.sort_values(by='今日增持市值', ascending=[False])
    filter_colume = ['代码', '名称', '涨幅', '今日增持股数', '今日增持市值', '今日增持市值增幅', '所属板块']
    qywx.send_text_B(
        "============beixiang-gegu2============\n" + df.head(100)[filter_colume].reset_index(drop=True).to_string(
            index=False))

    # 默认参数输出财联社电报新闻数据
    df = qs.news_data()
    qywx.send_text_B("============xiaoxi - cailianshe============\n" + df.tail(20).to_string())

    # 市场快讯数据
    # df = qs.news_data('js')
    # print(df.tail(20))


def daban_paichedan():
    '''
    获取指定个股买一数量，排撤，告警
    
     1.如何预估自己位置？ 参考软件
     2.

    '''
    paiche = "600418"
    df = qs.stock_snapshot(paiche)
    # print(df)
    filter_colume = ['代码','名称','买1数量']
    '''
    记录是否封单加大
    '''
    print(df[filter_colume])
    # 使用逻辑运算符 & 和适当的条件函数
    condition = (df['买1数量'] < 99999999)
    # 选择符合条件的行
    filtered_df = df[condition]
    if not filtered_df.empty:
        # print("------快开板了---撤单---")
        qywx.send_text(f"------快开板了---撤单--"+paiche+df['名称'].to_string())



'''
暂时不用了
'''
def get_duanxianjingling():

    duaxianjingling_df = qs.realtime_change('火箭发射')
    duaxianjingling_df = qs.realtime_change('火箭发射')
    duaxianjingling_df.rename(columns={'代码': 'code','名称': '股票简称'}, inplace=True)

    duaxianjingling_df = duaxianjingling_df[((duaxianjingling_df['code'] < '609999') & (duaxianjingling_df['code'] > '309999')) | (duaxianjingling_df['code'] < '111111') ]  #& (df['name']) 不知道如何强转
    # print(duaxianjingling_df)

    filter_col_duanxianjingling = ['时间','code', '股票简称', '板块']

    ''''
    短线精灵作为及时性，保存的意义不大
    '''

    try:
        workbook = xw.Book('./data/stronger.xlsx')
    except FileNotFoundError:
        workbook = xw.Book()
        sheet_names = ['Sheet2', 'Sheet3', 'Sheet4', 'Sheet5', 'Sheet6', 'Sheet7', 'Sheet8', 'Sheet9', 'Sheet10',
                       'Sheet11', 'Sheet12', 'Sheet13', 'Sheet14']
        for sheet_name in sheet_names:
            workbook.sheets.add(sheet_name, after=workbook.sheets[-1])
        workbook.save('./data/stronger.xlsx')

    sheet12 = workbook.sheets['Sheet12']
    # is_refresh = compare_and_notify("duanxianjingling", sheet12, duaxianjingling_df)
    duaxianjingling_df = duaxianjingling_df[filter_col_duanxianjingling].head(20)
    duaxianjingling_df = duaxianjingling_df.reset_index(drop=True)
    msg = "============火箭============\n"+duaxianjingling_df.to_string(header=False, index=False)

    qywx.send_text(msg)

    msg2 = duaxianjingling_df[(duaxianjingling_df['code'].isin(list_zixuangu))].reset_index(drop=True).to_string(header=False, index=False)
    if not duaxianjingling_df.empty:
        msg = "============火箭-自选============\n" + msg2
        qywx.send_text(msg)

    if True:
        clear_and_setFormat(sheet12)
        duaxianjingling_df = get_fill_url(duaxianjingling_df)
        filter_col_duanxianjingling.append('url')

        # current_time_str = duaxianjingling_df['时间'].strftime("%H:%M:%S")
        # print("==>>>time is ", current_time_str)
        # duaxianjingling_df['时间'] = current_time_str
        # 将时间对象转换为字符串
        duaxianjingling_df['时间'] = duaxianjingling_df['时间'].apply(lambda x: x.strftime("%H:%M:%S"))


        sheet12.range('A1').value = duaxianjingling_df[filter_col_duanxianjingling]

    print('-- refresh duaxianjingling --', datetime.now(), "-------")




