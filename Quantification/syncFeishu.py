'''

https://blog.csdn.net/weixin_45546132/article/details/116274371

# https://open.feishu.cn/open-apis/bot/v2/hook/cf1993d6-dcc6-43a7-af66-8a5df577809b
'''

import requests


# Feishu API请求地址
api_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/cf1993d6-dcc6-43a7-af66-8a5df577809b'

# 要发送的消息内容

def send(text):
    message = {
        "msg_type": "text",
        "content": {
            "text":  text
        }
    }

    # 发送POST请求到Feishu API
    response = requests.post(api_url, json=message)

    # 检查响应状态码
    if response.status_code == 200:
        print("消息发送成功！")
    else:
        print("消息发送失败，状态码：", response.status_code)
        print(response.text)





