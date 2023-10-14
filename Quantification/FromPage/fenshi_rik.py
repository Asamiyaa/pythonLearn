'''

    1.获取分时和日K展示
    2.
'''
import requests
from bs4 import BeautifulSoup
import tkinter as tk
import webbrowser



base_url = "https://quote.eastmoney.com/{}.html#fullScreenChart"
base_url = "https://quote.eastmoney.com/concept/{}.html" #极速版


def geturl(code):

    url = None

    if str(code).startswith("00"):
        url = str.format(base_url,"sz"+code)
        # print(url)

    if str(code).startswith("60"):
        url = str.format(base_url,"sh"+code)
        # print(url)

    return url
    #300先不处理




# geturl("002424")


'''
下面想解析出小图显示在excel列上，暂时需要学习前段的东西多，暂时不行
'''

#
# # 发送HTTP请求获取文章页面内容
# response = requests.get(base_url)
#
# print(response.text)
# # print(response.text)
# # 检查响应状态码，确保请求成功
# if response.status_code == 200:
#     # 使用BeautifulSoup解析页面内容
#     # soup = BeautifulSoup(response.text, 'html.parser')
#
#     # root = tk.Tk()
#     # root.title('Web Page Viewer')
#     #
#     # text = tk.Text(root, wrap='word')
#     # text.insert(tk.END, response.text)  # 将网页内容插入到文本框中
#     # text.pack(expand=True, fill='both')
#
#     # with open('web_page.html', 'w', encoding='utf-8') as f:
#     #     f.write(response.text)  # 将网页内容保存为本地文件
#     # print('Web page saved as web_page.html')
#
#
#     with open('web_page.html', 'w', encoding='utf-8') as f:
#         f.write(response.text)  # 将网页内容保存为本地文件
#     webbrowser.open('web_page.html')  # 在默认浏览器中打开保存的网页文件
#
#     # title = soup.find( id="cnblogs_post_description").get_text()
#     #
#     #
#     # content = soup.find(id="cnblogs_post_body").get_text()
#     # non_empty_lines = [line for line in content.splitlines() if line.strip() != ""]
#     #
#     #
#     # with open(f'pythonTest.txt', 'w', encoding='utf-8') as file:
#     #     file.write(f'Title: \source\myPythonTest\n\n')
#     #     file.write(f'Content:\n{content}')
#     #
#     # print(f'Article downloaded and saved as {title}.txt')
# else:
#     print('Failed to retrieve the article.')
#
#

