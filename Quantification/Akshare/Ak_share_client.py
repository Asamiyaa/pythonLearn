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
'002803',	
'002640',	
'601113',	
'601127',	
'601633',	
'600686',	
'603109',	
'603119',	
'002708',	
'600159',	
'603616',	
'603051',	
'002146',	
'002475',	
'002145',	
'002490',	
'002805',	
'001278',	
'600085',	
'000766',	
'002728',	
'002385',	
'603363',	
'002041',	
'000680',	
'001331',	
'300342',	
'002380',	
'603163',	
'003015',	
'000677',	
'002682',	
'002487',	
'002364',	
'002931',	
'603003',	
'002139',	
'603679',	
'002881',	
'600811',	
'603969',	
'002322',	
'603863',	
'002953',	
'300789',	
'603083',	
'002300',	
'600153',	
'603296',	
'002929',	
'603399',	
'002977',	
'002869',	
'002456',	
'605258',	
'603050',	
'002278',	
'002671',	
'002670',	
'002460',	
'605111',	
'002077',	
'002510',	
'510760',	
'002835',	
'600895',	
'002253',	
'300255'

]


list_ruozhuanqiang = [
'600159',
'603399',
'300342',
'002456',
'603003',
'603679'


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



