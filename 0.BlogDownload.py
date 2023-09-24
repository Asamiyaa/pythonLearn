import requests
from bs4 import BeautifulSoup

# 博客园博客的文章URL
article_url = 'https://www.cnblogs.com/lovesqcc/p/14033784.html'

# 发送HTTP请求获取文章页面内容
response = requests.get(article_url)

# print(response.text)
# 检查响应状态码，确保请求成功
if response.status_code == 200:
    # 使用BeautifulSoup解析页面内容
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)

    # 找到文章标题
    # title = soup.find('h1', class_='title').get_text()  //页面元素定位
    title = soup.find( id="cnblogs_post_description").get_text()
    print("title is ===>>> "+title)


    # 找到文章内容
    # content = soup.find('div', class_='body').get_text()
    content = soup.find(id="cnblogs_post_body").get_text()
    non_empty_lines = [line for line in content.splitlines() if line.strip() != ""]
    print("content is ===>>>" +  "\n".join(non_empty_lines))


    # 将文章内容保存到文件
    # with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    with open(f'pythonTest.txt', 'w', encoding='utf-8') as file:
        file.write(f'Title: \source\myPythonTest\n\n')
        file.write(f'Content:\n{content}')

    print(f'Article downloaded and saved as {title}.txt')
else:
    print('Failed to retrieve the article.')

