# import requests
# from openpyxl.reader.excel import load_workbook

'''
自己尝试抓，不熟练
'''
import datetime

from Quantification.FromPage.fenshi_rik import geturl
from Quantification.FromPage.ths_zixuan import get_ths_zixuan
from Quantification.FromPage.zhijiehuoqutupian import get_k_jpg

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
    if not cal.is_working_day(current_date):
        # print("")
    # else:
        # 获取前一个工作日的日期
        current_date = cal.find_following_working_day(current_date - timedelta(days=1))

    cur_date_str =  '[' + str(current_date.strftime("%Y%m%d")) + ']'

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
    ret_zixuangu = pywencai.get(query='集合竞价 涨速 最高板块 ', find=zixuan)
    # ret_zixuangu.to_csv("./FromPage/zixuan.csv")
    # print("==zixuan---",ret_zixuangu)
    filter_col_zixuangu = ['股票代码','股票简称', '最新涨跌幅', '最新价', '最新涨跌幅'# '个股热度排名'+cur_date_str ,
                    # '所属同花顺行业', '所属概念'
                     ]

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
        sheet_names = ['Sheet2', 'Sheet3', 'Sheet4','Sheet5','Sheet6']
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
    df['url'] = df['code'].apply(geturl)
    # print("===>>",df['url'].to_string())

    return df





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







