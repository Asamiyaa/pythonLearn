import itchat
from wxauto import *


'''
1.会让登出

'''
#
# # 登录微信账号，会弹出二维码，扫描二维码登录
# itchat.auto_login(hotReload=True)  # hotReload=True表示使用缓存的登录信息
#
# # 要发送消息的微信好友的备注名或微信昵称
# friend_name = 'Asamiya'
#
# # 要发送的消息内容
# message_content = 'Hello, 这是通过Python发送的消息！'
#
# # 查找好友
# friends = itchat.search_friends(name=friend_name)
# if len(friends) > 0:
#     # 获取好友的UserName
#     friend_username = friends[0]['UserName']
#     # 发送消息
#     itchat.send_msg(msg=message_content, toUserName=friend_username)
#     print('消息发送成功！')
# else:
#     print('未找到指定的好友。')
#


'''
https://github.com/cluic/wxauto
https://zhuanlan.zhihu.com/p/557314845

'''
def send_msg_toWechat(msg):

    wx = WeChat()
    wx.GetSessionList()

    msg = msg
    who = 'Asamiya'
    wx.ChatWith(who)  # 打开`文件传输助手`聊天窗口
    wx.SendMsg(msg,who)  # 向`文件传输助手`发送消息：你好~

'''
sendfile
'''

'''
本地打开csv查看即可
'''