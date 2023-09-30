import calendar
import cmath
import time

print("this is test String module")


#字符串和文本处理

#基础类型定义
a = "test"
print(a)
b = "df dd, tt   ty"
print(b)
print(",".join(b))

i = 1
print(i)

y = 2
i = i+y
print(i)

print(i / y)

#定义方法
def testm(a, b):
    print(a + b + 1)
    if a + b < 2:
        print("ggg")
    elif a + b > 3 and (a > 1 or b < 3):
        print("rrr")
    else:
        print("ttt")


testm(1, 2)
#集合

tuple = (1,2,4.5)
print(tuple)

#不换行
print("a")
print("b")

print("a"),
print("b"),


list = {2,44,6,6,5}
# l = "=>>>"
for e in list:
    print("this "+ str(e))
print(list)

#如何定义对象？
class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} 对象已创建")

    def __del__(self):
        print(f"{self.name} 对象将被销毁")

# 创建对象
obj1 = MyClass("对象1")
obj2 = MyClass("对象2")

# 销毁对象
del obj1



'''
这是多行注释
'''
#定义方法  -- 为什么不识别
def testm(a,b):
    print(a + b + 1)


# raw_in#put("按下 enter 键退出，其他任意键显示...\n")

#多变量赋值
a,b,c = 1,2,"dfd"
print(a,b,c)


del a,b
#print(a,b,c) #NameError: name 'a' is not defined  因为del


'''
python 的字串列表有 2 种取值顺序:

从左到右索引默认 0 开始的，最大范围是字符串长度少 1
从右到左索引默认 -1 开始的，最大范围是字符串开头
'''
s = "23kfdiufd"
print(s[0])
print(s[0 : 3])
print(s[-2])


#加号（+）是字符串连接运算符，星号（*）是重复操作
print(1+3)
print("dr"*2)

list = [1,"eee","t",9]
print(list[1])
print(list[1:3])
print(list[2:])
print(list * 2)

list[2] ="tttt"
print(list[2])


#tuple类似上面的string和list
#tuple不允许更新、list允许
tuple1 = (2,3,4)
# tuple1[1] = 9  #不输出，不阻断后面，注意排查
print(tuple1[1])

#dictionary
print("dicccccc")
dic = {"1":3,"e":4}
print(dic["1"])
# print(dic[5]) #不报错，阻断后面
print(dic.keys())


'''
Python 数据类型转换

'''
j = 2323
print(j)
# print(j + "11")  报错  TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(j) + "11")

print("1+3")
print(eval("1+3"))


'''
转换函数不行，不生效!!!
'''
# print(tuple("134"))
# print(list("134")) 需要申明
ss = "1234"
# ll = list(ss)

my_string = "hello"
# my_list = list(my_string)
# 结果：['h', 'e', 'l', 'l', 'o']



'''
运算符、比较符、逻辑运算符 and 、or、not 、身份运算符 is is not 判断两个标识符是否引子同一对象  == 比较值
运算符优先级 - 查看对应表格
'''
c = 9//5
print(c)

print(1/2)

o1 = 1
o2 = 2
bb = o1 < o2
print(bb)


le = [2,8]
if 3 in le:
    print("in")
else:
    print("not in")



'''
循环语句
'''

lll = [9,3,4,5,66]
for e in lll:
    print(e)

count = 1
while count < 7:
    count+=1
    if count == 2:
        print("break")
        break    #continue  #pass
    print(e)


import math
'''
数学工具 math、cmath  ===> 其他数学操作
'''
print(cmath.pi)
print(cmath.sqrt(9))

print(math.floor(34))


'''
String的函数

方法	描述
string.capitalize()

把字符串的第一个字符大写

string.center(width)

返回一个原字符串居中,并使用空格填充至长度 width 的新字符串

string.count(str, beg=0, end=len(string))

返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

string.decode(encoding='UTF-8', errors='strict')

以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除 非 errors 指 定 的 是 'ignore' 或 者'replace'

string.encode(encoding='UTF-8', errors='strict')

以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'

string.endswith(obj, beg=0, end=len(string))

检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

string.expandtabs(tabsize=8)

把字符串 string 中的 tab 符号转为空格，默认的空格数 tabsize 是 8.

string.find(str, beg=0, end=len(string))

检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1

string.index(str, beg=0, end=len(string))

跟 find() 方法一样，只不过如果 str 不在 string 中会报一个异常.

string.isalnum()

如果 string 至少有一个字符并且所有字符都是字母或数字则返

回 True,否则返回 False

string.isalpha()

如果 string 至少有一个字符并且所有字符都是字母则返回 True,

否则返回 False

string.isdecimal()

如果 string 只包含十进制数字则返回 True 否则返回 False.

string.isdigit()

如果 string 只包含数字则返回 True 否则返回 False.

string.islower()

如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

string.isnumeric()

如果 string 中只包含数字字符，则返回 True，否则返回 False

string.isspace()

如果 string 中只包含空格，则返回 True，否则返回 False.

string.istitle()

如果 string 是标题化的 (见 title()) 则返回 True，否则返回 False

string.isupper()

如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

string.join(seq)

Merges (concatenates)以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

string.ljust(width)

返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串

string.lower()

转换 string 中所有大写字符为小写.

string.lstrip()

截掉 string 左边的空格

string.maketrans(intab, outtab])

maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

max(str)

返回字符串 str 中最大的字母。

min(str)

返回字符串 str 中最小的字母。

string.partition(str)

有点像 find()和 split() 的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.

string.replace(str1, str2,  num=string.count(str1))

把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.

string.rfind(str, beg=0,end=len(string) )

类似于 find()函数，不过是从右边开始查找.

string.rindex( str, beg=0,end=len(string))

类似于 index()，不过是从右边开始.

string.rjust(width)

返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串

string.rpartition(str)

类似于 partition()函数,不过是从右边开始查找.

string.rstrip()

删除 string 字符串末尾的空格.

string.split(str="", num=string.count(str))

以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串

string.splitlines(num=string.count('\n'))

按照行分隔，返回一个包含各行作为元素的列表，如果 num 指定则仅切片 num 个行.

string.startswith(obj, beg=0,end=len(string))

检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.

string.strip([obj])

在 string 上执行 lstrip()和 rstrip()

string.swapcase()

翻转 string 中的大小写

string.title()

返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())

string.translate(str, del="")

根据 str 给出的表(包含 256 个字符)转换 string 的字符,

要过滤掉的字符放到 del 参数中

string.upper()

转换 string 中的小写字母为大写

string.zfill(width)

返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0

string.isdecimal()

isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于 unicode 对象。
'''
# "dfd".translate(s,"")
org = "abCCC"
print(org.capitalize())
print(org.center(10))
print(org.count("C", 0, len(org)))
print(org.find("a", 1, 10))
print(",".join(org))
print(max(org))
print(org.startswith("J", 0, len(org)))
print(org.zfill(10).zfill(20))  # 链式调用


l1 = [2,3,"44","4",9.0,0.004]
print(l1.count(3))
print(l1.index("4", 0, 9))
print(l1.insert(3, 100))
print(l1)
print(l1.copy())
del l1[0]
print(l1)
print(len(l1))
print([1, 2, 3] + [4, 5, 6])
print(["hi"] * 4)
print(3 in [1, 2, 3])
for x in [1,2,3]:print(x)

print(l1[1:])

# print(max(l1))  没反应

# print(l1.reverse()) #? 为什么是None?
l2 = [10,3,9]
# print(l2.sort()) #不应该print 隐含报错
l2.sort()
print(l2)
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
my_list.sort()
print(my_list)


tuplenew = (1,2,3,555,6,4)
print(tuplenew[2:])
# tuplenew[0]= 999
del tuplenew
# print(tuplenew)
print(3 in (1, 2, 3))
#类似于list


#dictionary 键必须不可变，所以可以用数，字符串或元组充当，所以用列表就不行
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8  # update existing entry
dict['School'] = "DPS School"  # Add new entry

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

# dict1 = {['Name']: 'Zara', 'Age': 7} 数组不会报错，但不会正常打印，因为数组可变，不可作为key
dict1 = {('Name'): 'Zara', 'Age': 7}
print("dict['Name']: ", dict1['Name'])

dict1.update({"Name":999})
print(dict1)


'''
日期、时间

'''

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print(calendar.month(2011, 1))



'''
def

'''

def addSum(a,b,c):
    return a+b+c+100


print(addSum(1, 2, 3))


sum = lambda a,b : a/b   #lambda写法
print(sum(10, 20))


'''
model
from modelTest import addSumTest


当你导入一个模块，Python 解析器对模块位置的搜索顺序是：

当前目录
如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
如果都找不到，Python 会察看默认路径。UNIX下，默认路径一般为 /usr/local/lib/python/
'''
print(addSum(1, 2, 3))



'''
reload() 函数
当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。

因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。语法如下：

reload(module_name)
'''


'''
IO

'''
print("dfd","1232")
# raw_input
# input("enter you input:")

# print(open("D:\test\summary.txt","wb"))  #错误的输出导致后面不执行
ip = open("D:\\test\\summary.txt", "wb")
print("---", ip.name, ip.mode, ip.closed)

ip.write('add summing !!!'.encode("utf-8"))
ip.close()

# 打开一个文件以进行写入（如果文件不存在则创建文件，如果存在则覆盖文件内容）
# file_path = "source\example.txt"
# with open(file_path, "w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is a sample file.\n")
#     file.write("Python is awesome!\n")
#
# # 文件写入完成后，自动关闭文件
#
# # 若要追加内容到文件而不覆盖原有内容，可以使用 "a" 模式：
# with open(file_path, "a") as file:
#     file.write("Appending some additional text.\n")

# 再次文件写入完成后，自动关闭文件




'''
异常
'''
# print("3"*2+1)   异常不提示
# try:
#     ff = open("testfile", "wb")
#     ff.write("ddd".encode("utf-8"))
# except IOError:
#     print("--->>>>>")
# # finally:
#     # ff.close()

try:
    if 0 < 1:
        raise Exception("--@@@-->>>")
except Exception:
    print("<<<<<<<<########")










