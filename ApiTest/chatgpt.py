import openai
import requests
import json
# openai.api_key = "sk-sqbw93nxpidIYuaGxXroo2paCaCfE1dAuDDgx07lYocHTEgH"
# openai.api_base = "https://api.chatanywhere.com.cn/v1/chat/completions"
# chat_completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         # system message first, it helps set the behavior of the assistant
#         {"role": "system", "content": "You are a helpful assistant."},
#         # I am the user, and this is my prompt
#         {"role": "user", "content": "What's the best star wars movie?"},
#         # we can also add the previous conversation
#         # {"role": "assistant", "content": "Episode III."},
#     ],
# )
# print(chat_completion.choices[0].message.content)

api_key = "sk-sqbw93nxpidIYuaGxXroo2paCaCfE1dAuDDgx07lYocHTEgH"
api_url = "https://api.chatanywhere.com.cn/v1/chat/completions"
def translate(text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }

    payload = {
        "text": text
        # "target_language": "zh"
    }

    #报错 500？
    response = requests.post(api_url, headers=headers, json= json.dumps(payload) ) #json= json.dumps(payload)
    print(response)


    if response.status_code == 200:
        # raise Exception("---->>>>")
        return response.json()["translations"][0]["translation"]
    else:
        return None


text = "Hello, world!"  # 要翻译的英文文本
translation = translate(text)
print(translation)