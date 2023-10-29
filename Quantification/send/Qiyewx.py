import requests
import json


# 发送文本消息
def send_text(content, mentioned_list=None, mentioned_mobile_list=None):

    webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=6a64b60a-808b-403e-b10e-b7645432dbae"

    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    data = {

        "msgtype": "text",
        "text": {
            "content": content
            , "mentioned_list": mentioned_list
            , "mentioned_mobile_list": mentioned_mobile_list
        }
    }
    data = json.dumps(data)
    info = requests.post(url=webhook, data=data, headers=header)


def send_text_B(content, mentioned_list=None, mentioned_mobile_list=None):

    webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=0c662554-5b02-48e6-9b24-3c70c0428a92"

    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    data = {

        "msgtype": "text",
        "text": {
            "content": content
            , "mentioned_list": mentioned_list
            , "mentioned_mobile_list": mentioned_mobile_list
        }
    }
    data = json.dumps(data)
    info = requests.post(url=webhook, data=data, headers=header)




# 发送markdown消息
def send_md(webhook, content):
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    data = {

        "msgtype": "markdown",
        "markdown": {
            "content": content
        }
    }
    data = json.dumps(data)
    info = requests.post(url=webhook, data=data, headers=header)


# send_text("","this is first python test !!!")
