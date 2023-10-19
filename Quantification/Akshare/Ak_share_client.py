import akshare as ak
import requests
import warnings

warnings.filterwarnings("ignore")

'''
新浪接口被禁止
'''
base_url = " http://hq.sinajs.cn/list="
def get_info(codelist):
    print("codelist ==>",codelist)



    # 使用逗号作为分隔符将列表转换为字符串
    # codes = ', '.join(str(item) for item in codelist)
    # codelist
    # url = base_url + codelist
    # print(url)
    #
    # response = requests.post(url)
    #
    # print(response)

    '''
    没有指定接口的数据让拿到
    '''
    #使用ak_share
    # ak.stock_zh_a_spot_em

    '''
    全量 - 匹配适合自己的？
    '''
    # 将字符串转换为列表，如果codelist最初是字符串形式的话
    # codelist = codelist.split(',')

    aa = ak.stock_zh_a_spot_em()
    aa.to_csv("./aaa.csv")
    need_col = ['代码', '名称', '涨跌幅', '量比', '5分钟涨跌', '涨速']
    df = aa[need_col]
    # df = df[(df['涨跌幅'] > 9) & (df['涨跌幅'] < 11)]
    # print(df)

    # 重命名
    # df.rename(columns={'代码': 'code', '名称': 'name', '涨跌幅': 'changepercent'}, inplace=True)
    df = df[(df['代码'].isin(codelist))]

    return df

# get_info("600706,001324")


list_zixuangu = [
'601127',	
'002590',	
'000158',	
'603266',	
'603220',	
'002261',	
'600418',	
'002253',	
'601136',	
'601633',	
'300584',	
'605398',	
'600127',	
'300255',	
'002456',	
'002156',	
'600355',	
'003040',	
'603985',	
'601881',	
'000980',	
'603779',	
'000065',	
'603211',	
'002387',	
'603912',	
'003007',	
'600019',	
'603288',	
'605588',	
'000338',	
'002623',	
'600895',	
'002657',	
'002640',	
'002848',	
'002449',	
'002369',	
'000908',	
'603861',	
'000948',	
'603186',	
'000739',	
'688166',	
'000153',	
'000536',	
'002845',	
'002077',	
'605177',	
'002218',	
'000766',	
'603108',	
'002176',	
'603000',	
'000801',	
'001309',	
'605016',	
'002269',	
'603716',	
'300322',	
'002708',	
'002099',	
'000628'
]


list_ruozhuanqiang = [
'600476',	
'601698',	
'003040',	
'002657',	
'002708',	
'603211',	
'000070',	
'000700',	
'000981',	
'603239',	
'002901',	
'002675',	
'600083',	
'001331',	
'300164',	
'000554',	
'603619',	
'002629',	
'603727',	
'002207',	
'603223',	
'000680',	
'002828',	
'605016',	
'002286',	
'000756',	
'603139',	
'002038'

]




def get_zixuangu_df():
    aa = ak.stock_zh_a_spot_em()
    # aa.to_csv("./aaa.csv")
    need_col = ['代码', '名称', '涨跌幅', '量比', '5分钟涨跌', '涨速']
    df = aa[need_col]
    # df = df[(df['涨跌幅'] > 9) & (df['涨跌幅'] < 11)]
    # print(df)

    # 重命名
    # df.rename(columns={'代码': 'code', '名称': 'name', '涨跌幅': 'changepercent'}, inplace=True)
    df = df[(df['代码'].isin(list_zixuangu))]

    print(df)
    return df


def get_ruozhuanqiang_df():
    aa = ak.stock_zh_a_spot_em()
    need_col = ['代码', '名称', '涨跌幅', '量比', '5分钟涨跌', '涨速']
    df = aa[need_col]
    df = df[(df['代码'].isin(list_ruozhuanqiang))]

    print(df)
    return df


list_T = [
    '605118',	
'605108',	
'603936',	
'603909',	
'603879',	
'603595',	
'301359',	
'603200',	
'601360',	
'601336',	
'601138',	
'601012',	
'600903',	
'600887',	
'600884',	
'600778',	
'600689',	
'600581',	
'600536',	
'600468',	
'600360',	
'600280',	
'600212',	
'003015',	
'002975',	
'002897',	
'002861',	
'002542',	
'002531',	
'002528',	
'002084',	
'002049',	
'001368',	
'001338',	
'001270',	
'000821',	
'000721',	
'000705',	
'000656',	
'000652',	
'000572',	
'000422',	
'000032',	
'600048',	
'002918',	
'600801',	
'601236',	
'001227',	
'002193',	
'002142',	
'002385',	
'601888',	
'002561',	
'002145',	
'000957',	
'002594',	
'002547',	
'002186',	
'001256',	
'002487',	
'603616'

]

no_notify_list=[
    '001270',
    '603595',
    '002623',
    '002145'

]

def get_T():
    aa = ak.stock_zh_a_spot_em()
    need_col = ['代码', '名称', '涨跌幅', '量比', '涨速']
    df = aa[need_col]
    df = df[(df['代码'].isin(list_T))]
    # print(df)
    df.rename(columns={'代码': 'code','名称':'股票简称'}, inplace=True)

    return df



def get_zixuanguAsCode_df():
    aa = ak.stock_zh_a_spot_em()
    # aa.to_csv("./aaa.csv")
    need_col = ['代码', '名称', '涨跌幅', '量比', '5分钟涨跌', '涨速']
    df = aa[need_col]
    # df = df[(df['涨跌幅'] > 9) & (df['涨跌幅'] < 11)]
    # print(df)

    # 重命名
    # df.rename(columns={'代码': 'code', '名称': 'name', '涨跌幅': 'changepercent'}, inplace=True)
    df = df[(df['代码'].isin(list_zixuangu))]
    df.rename(columns={'代码': 'code', '名称': '股票简称'}, inplace=True)
    # print(df)
    return df



def get_no_notify_list():
    return no_notify_list



