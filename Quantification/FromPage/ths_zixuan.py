import pandas as pd
import re
'''
1.网页版并未找到接口，所以只能通过导出excel ,加载进去  
2.自动化
'''



def get_ths_zixuan():

    df = pd.read_csv(r"C:\Users\73699\Desktop\Table.xls", encoding='gbk')#,delimiter='\t', names=['代码', '名称', '涨幅', '竞价涨幅%', '所属行业', '细分行业', '首次涨停时间[20231013]', '量比', '换手%', '涨停封成比%[20231013]', '涨停次数[20231009-20231013]'])

    # print(df.columns)
    # 替换列名中的制表符
    df.columns = df.columns.str.replace('\t', '')
    # print(df.columns)
    # 使用列的索引来访问带有空格的列
    # print(df[df.columns[0]])  # 这里的索引 0 表示第一列，你可以根据实际列的位置来选择索引

    # dm = df['代码'].str.replace('\t','').to_string()
    # print(dm)
    # print(re.sub(r'a-zA-z','',dm))


    # 定义一个函数，用正则表达式去掉字符串中的英文字符


    # 在 '代码' 列上应用函数，去掉英文字符
    df['代码'] = df['代码'].apply(remove_english_chars)
    # print(df['代码'])

    return df


def get_ths_ruozhuanqiang():

    df = pd.read_csv(r"C:\Users\73699\Desktop\Table_ruozhuanqiang.xls", encoding='gbk')#,delimiter='\t', names=['代码', '名称', '涨幅', '竞价涨幅%', '所属行业', '细分行业', '首次涨停时间[20231013]', '量比', '换手%', '涨停封成比%[20231013]', '涨停次数[20231009-20231013]'])

    df.columns = df.columns.str.replace('\t', '')

    df['代码'] = df['代码'].apply(remove_english_chars)

    return df


def get_ths_maodian():

    df = pd.read_csv(r"C:\Users\73699\Desktop\Table_maodian.xls", encoding='gbk')#,delimiter='\t', names=['代码', '名称', '涨幅', '竞价涨幅%', '所属行业', '细分行业', '首次涨停时间[20231013]', '量比', '换手%', '涨停封成比%[20231013]', '涨停次数[20231009-20231013]'])

    df.columns = df.columns.str.replace('\t', '')

    df['代码'] = df['代码'].apply(remove_english_chars)

    return df



def remove_english_chars(text):
    return re.sub(r'[a-zA-Z]', '', text.replace('\t', ''))