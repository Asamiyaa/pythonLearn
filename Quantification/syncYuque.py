from simple_pyyuque import SimplePyYuQueAPI

''''
超级会员才支持token >>.

https://github.com/Xarrow/simple-pyyuque
https://www.shumlab.com/tech/try-yuque-api/
'''

user_serializer = SimplePyYuQueAPI(token="token", app_name="py_yuque1").User().get_user()
print(user_serializer.base_response)
