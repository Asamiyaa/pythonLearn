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