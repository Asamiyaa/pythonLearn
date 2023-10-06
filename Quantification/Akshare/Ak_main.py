import akshare as ak
import datetime

'''
https://akshare.xyz/data/stock/stock.html#id134
'''

# print(ak.stock_sse_summary())

sz_name_code_df = ak.stock_info_sz_name_code()
# print(sz_name_code_df)
fdf = sz_name_code_df[['A股代码','A股简称','所属行业']]
print(fdf.to_string())
file_name = str(datetime.date.today()) + '_codeName.csv'
fdf.to_csv('../data'+file_name, index=False)


