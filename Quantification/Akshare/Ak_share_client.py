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
	
'002848',	
'000948',	
'600449',	
'002316',	
'600258',	
'002657',	
'600100',	
'003040',	
'000727',	
'000801',	
'603985',	
'000546',	
'301517',	
'002077',	
'002119',	
'002156',	
'603388',	
'605398',	
'003007',	
'002369',	
'603861',	
'603186',	
'000413',	
'603266',	
'002387',	
'002708',	
'603716',	
'002456',	
'605016',	
'601136',	
'601881',	
'605588',	
'600839',	
'002269',	
'002640',	
'603108',	
'002623',	
'002218',	
'002449',	
'002845',	
'000739',	
'000338',	
'603912',	
'600127',	
'603288',	
'300322',	
'002855',	
'300255',	
'688166',	
'001298',	
'600355',	
'002261',	
'601127',	
'000980',	
'603000',	
'001309',	
'002176',	
'600895',	
'000536',	
'601633',	
'000153',	
'605177',	
'300584',	
'000908'
]


list_ruozhuanqiang = [
	
'002369',	
'600839',	
'600100',	
'002771',	
'002657',	
'600449',	
'003007',	
'605398',	
'002038',	
'603139',	
'000756',	
'002286',	
'605016',	
'000680',	
'002828',	
'603353',	
'001331',	
'300164',	
'000554',	
'603619',	
'002629',	
'603727',	
'002207',	
'603223',	
'001337',	
'600026',	
'001324',	
'603982',	
'603211',	
'603768',	
'600733',	
'603037',	
'002420',	
'003009',	
'688629',	
'002339',	
'600630',	
'603779',	
'603615',	
'603863',	
'603985',	
'603276'	
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
    '002855',
    '000766',
    '000727'
]

def get_T():
    aa = ak.stock_zh_a_spot_em()
    need_col = ['代码', '名称', '涨跌幅', '量比', '涨速']
    df = aa[need_col]
    df = df[(df['代码'].isin(list_T))]
    # print(df)
    df.rename(columns={'代码': 'code','名称':'股票简称'}, inplace=True)

    return df
