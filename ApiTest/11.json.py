import json

# 使用json.dumps()方法可以将Python对象（如字典或列表）转换为JSON格式的字符串。
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_data = json.dumps(data)
print(json_data)


# 使用json.loads()方法可以将JSON格式的字符串解析为Python对象。
json_data = '{"name": "John", "age": 30, "city": "New York"}'

data = json.loads(json_data)
print(data)
# class才能使用setattr
# setattr(data,"name","asamiyaTest")
data["name"] = "asamiyaTest"
print(data)


# 如果你想将Python对象写入一个JSON文件，可以使用json.dump()方法。
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open("output.json", "w") as json_file: #FileNotFoundError: [Errno 2] No such file or directory: '\\source\\output.json'
    json.dump(data, json_file)
