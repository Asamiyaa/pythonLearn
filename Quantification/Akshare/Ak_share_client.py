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
'002790',	
'603408',	
'600675',	
'600846',	
'002322',	
'002965',	
'603636',	
'603859',	
'603990',	
'003007',	
'605376',	
'000762',	
'603282',	
'000715',	
'603890',	
'002045',	
'000682',	
'003021',	
'603728',	
'002850',	
'002812',	
'002962',	
'002484',	
'002436',	
'600186',	
'002757',	
'000638',	
'600501',	
'002519',	
'600435',	
'002755',	
'002940',	
'603332',	
'603003',	
'600423',	
'600684',	
'002208',	
'003010',	
'002988',	
'600258',	
'600754',	
'600223',	
'603130',	
'001896',	
'002707',	
'002336',	
'603611',	
'603556',	
'600119',	
'600645',	
'603779',	
'001300',	
'603605',	
'000892',	
'600520',	
'002384',	
'603283',	
'002791',	
'002068',	
'002557',	
'002748',	
'002952',	
'002232',	
'603912',	
'605398',	
'603005',	
'002426',	
'603061',	
'002916',	
'300604',	
'002106',	
'605111',	
'002077',	
'601138',	
'603338',	
'601777',	
'600276',	
'002864',	
'600079',	
'600351',	
'002422',	
'002901',	
'600062',	
'002262',	
'301201',	
'603127',	
'600422',	
'603998',	
'002292',	
'002667',	
'603477',	
'002385',	
'601113',	
'000417',	
'603163',	
'601858',	
'001322',	
'000818',	
'002444',	
'603026',	
'002345',	
'600114',	
'002240',	
'002703',	
'600733',	
'600773',	
'603123',	
'002991',	
'605055',	
'002602',	
'603335',	
'000800',	
'000550',	
'000868',	
'603119',	
'603009',	
'603085',	
'603788',	
'605007'



]


list_ruozhuanqiang = [
'002602',
'002931',
'603633',
'603322',
'002235',
'603061',
'600006',
'601188',
'002042',
'002750',
'002796',
'300985',
'603158',
'600776',
'603131',
'300604',
'600326',
'603196',
'002729',
'603003',
'000010',
'000410'
        


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



