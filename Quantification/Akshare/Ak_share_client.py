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
'002487',	
'002869',	
'001336',	
'603309',	
'002145',	
'600853',	
'002385',	
'510760',	
'002921',	
'002708',	
'002510',	
'001380',	
'001278',	
'603266',	
'603119',	
'603109',	
'603048',	
'600335',	
'601633',	
'601127',	
'600686',	
'600418',	
'600006',	
'603300',	
'603123',	
'002803',	
'002640',	
'605136',	
'601113',	
'002508',	
'603605',	
'605337',	
'603477',	
'002041',	
'001317',	
'600153',	
'002881',	
'002475',	
'002139',	
'688260',	
'603890',	
'603296',	
'600203',	
'002667',	
'002460',	
'603616',	
'002671',	
'002652',	
'002457',	
'600326',	
'002146',	
'600895',	
'600683',	
'600322',	
'003036',	
'002490',	
'002278',	
'000680',	
'603956',	
'002931',	
'002122',	
'603969',	
'600592',	
'002796',	
'002792',	
'002194',	
'603083',	
'600159',	
'002953',	
'002805',	
'002364',	
'002300',	
'603861',	
'603050',	
'002579',	
'002077',	
'605258',	
'605111',	
'002380',	
'002322',	
'002253',	
'600410',	
'300789',	
'002835',	
'603496',	
'300342',	
'603363',	
'600811',	
'002456',	
'603773',	
'603679',	
'002292',	
'605577',	
'300255',	
'000766',	
'603977',	
'603970',	
'000677',	
'002977',	
'003015',	
'002876',	
'002864',	
'002728',	
'600085',	
'002670',	
'002788',	
'000815',	
'603863',	
'001331',	
'000593'

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



