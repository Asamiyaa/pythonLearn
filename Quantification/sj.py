from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from lxml import etree
import time
firfox_options=Options()
firfox_options.add_argument('--headless')
# driver = webdriver.ChromiumEdge(executable_path=r"C:\Users\73699\vuedemo\node_modules\chromedriver\lib\chromedriver\chromedriver.exe",firefox_options=firfox_options)
driver = webdriver.ChromiumEdge()
start_url='http://q.10jqka.com.cn/gn/index/field/addtime/order/desc/page/{}/ajax/1/'

# data_dict={}
# for i in range(1,22):
#     driver.get(start_url.format(i))
#     print('现在抓取{}'.format(start_url.format(i)))
#     html=etree.HTML(driver.page_source)
#     block_name=html.xpath('//td[2]/a/text()')
#     print(block_name)#需要查看是否有网页没有正常打开
#     page_url=html.xpath('//td[2]/a/@href')
#     data_dict.update(dict(zip(block_name,page_url)))
#     time.sleep(20)


# import requests
# from lxml import etree
# url='http://q.10jqka.com.cn/gn/'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
# response=requests.get(url,headers=headers)
# html=etree.HTML(response.content)
# block_name=html.xpath('//div[contains(@class,"cate_inner")]/div/div/a/text()')
# block_url=html.xpath('//div[contains(@class,"cate_inner")]/div/div/a/@href')
# data_dict=dict(zip(block_name,block_url))
# data_dict
# page_start_url='http://q.10jqka.com.cn/gn/detail/field/264648/order/desc/page/{}/ajax/1/code/307408'
# code_data_dict={}
# for i in range(1,int(pages)+1):
#     driver.get(page_start_url.format(i))
#     print('现在抓取{}'.format(page_start_url.format(i)))
#     code=html.xpath('//tbody/tr/td[2]/a/text()')
#     code_name=html.xpath('//tbody/tr/td[3]/a/text()')
#     print(code_name)
#     code_data_dict.update(zip(code,code_name))
#     time.sleep(20)