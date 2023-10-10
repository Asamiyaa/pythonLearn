import akshare as ak
import datetime

'''
https://akshare.xyz/data/stock/stock.html#id134
'''

# print(ak.stock_sse_summary())
#
# sz_name_code_df = ak.stock_info_sz_name_code()
# sh_name_code_df = ak.stock_info_sh_name_code()
# print(ak.stock_individual_info_em("603777", 100))
# print(sh_name_code_df)
# # print(sz_name_code_df)
# fdf1 = sz_name_code_df[['A股代码','A股简称','所属行业']]
# fdf2 = sh_name_code_df[['证券代码','证券简称','所属行业']]
#
# ff = fdf1.merge(fdf2)
# print(ff.to_string())
# file_name = str(datetime.date.today()) + '_codeName.csv'
# ff.to_csv('../data'+file_name, index=False)


# sz_name_code_df = ak.stock_info_sz_name_code()
# print(sz_name_code_df)
# fdf1 = sz_name_code_df[['A股代码','A股简称','所属行业']]
#
# file_name = str(datetime.date.today()) + '_codeName.csv'
# ff.to_csv('../data'+file_name, index=False)


aa = ak.stock_zh_a_spot_em()
need_col = ['代码','名称','涨跌幅','量比','5分钟涨跌','涨速']
pd = aa[need_col]
pd = pd[(pd['涨跌幅'] > 9) & (pd['涨跌幅'] < 11)]
print(pd)


