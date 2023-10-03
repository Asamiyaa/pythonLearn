import bisect
import re

'''
官方api联系 https://www.apiref.com/python-zh/library/index.html
'''


#二分法查找
# 注意：bisect 模块要求输入序列必须是已排序的，否则结果可能不准确。
sorted_list = [1, 3, 4, 6, 8, 9]
index = bisect.bisect_left(sorted_list, 4, 0, len(sorted_list))
print(index)

index2 = bisect.bisect_left(sorted_list, 8, 0, len(sorted_list))
print(index2)

bisect.insort_left(sorted_list,5)
print(sorted_list)


import csv
#csv
with open('../source/eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


#hash
import hashlib
seed = hashlib.sha256()
seed.update(b"Nobody inspects the spammish repetition")
print(seed.hexdigest())


'''
https://python3-cookbook.readthedocs.io/zh_CN/latest/chapters/p02_strings_and_text.html
'''
line = 'asdf fjdk; afed, fjek,asdf, foo'
print(line.split())
print(line.split(";"))
print(line.split(";",3))    #['asdf fjdk', ' afed, fjek,asdf, foo']
print(line.split(maxsplit=1))   #['asdf fjdk', ' afed, fjek,asdf, foo']  指定最大分割次数
#1.默认按照空格分隔   2.看不懂apijia简介
# def split(self: LiteralString, sep: LiteralString | None = ..., maxsplit: SupportsIndex = ...) -> list[LiteralString]: ...
#对应实现  def split(self, splitter=' ', maxsplit=0):
#问题：如何传入自定义的分隔符、形参中的maxsplit是在哪里指定?  split(xx)传入, 不传入不用传null,实现上splitter=' ', maxsplit=0就是默认值，想要指定值 则，maxsplit = 1


print(re.split(r'[;,\s]\s*', line)) #['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
print(re.split(r'(;|,|\s)\s*', line)) #['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
print(re.split(r'(?:,|;|\s)\s*', line)) #['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

print(re.match(r"asd", line).group())
'''
解释下面  list[1::2]
`list[1::2]` 是Python中列表（List）切片的一种使用方式，它表示从列表的索引1开始（包括索引1），以步长为2取出列表中的元素。让我详细解释一下：

- `list`：这是你要切片的列表对象。
- `[1::2]`：这是切片的语法。其中：
  - `1`：表示切片的起始索引。在这里，起始索引是1，即从列表的第二个元素开始切片，因为Python的索引是从0开始的。
  - `::`：这是用于分隔切片的语法，第一个冒号前面的部分用于指定起始索引，第一个冒号后面的部分用于指定结束索引，两个冒号之间为空，表示切片包含列表的所有元素。
  - `2`：表示切片的步长。步长为2表示从起始索引开始，每隔一个元素取一个元素。

下面是一个示例：

```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = my_list[1::2]

print(result)
```

在这个示例中，`my_list[1::2]` 从索引1开始（包括1），以步长为2取出列表中的元素，结果是 `[1, 3, 5, 7, 9]`，这是原列表中索引为奇数的元素。

'''

import os
filenames = os.listdir("..")
print(filenames)
#随意性、简化性
list = [name for name in filenames if name.endswith(".git")]
print(list)
print(any(name.endswith(".git") for name in filenames))
print(all(name.endswith(".py") for name in filenames))

# 因为没有类型,所以不能提
from urllib.request import urlopen
def read_data(name):
    if name.startswith(('http','https','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


print(read_data("https://www.baidu.com/"))

#上面的替换方案：url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'  或者  re.match('http:|https:|ftp:', url)


#用Shell通配符匹配字符串
# fnmatch() 函数匹配能力介于简单的字符串方法和强大的正则表达式之间。 如果在数据处理操作中只需要简单的通配符就能完成的时候，这通常是一个比较合理的方案。
# 如果你的代码需要做文件名的匹配，最好使用 glob 模块

from fnmatch import fnmatch,fnmatchcase

print(fnmatch("abc.ttt", "*.tt"))
print(fnmatch("abc.ttt", "*.ttt"))
print(fnmatch("Dat45.csv", "Dat[0-9]*"))
names =  ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, "Dat*.csv")])


datepat = re.compile(r'\d+/\d+/\d+')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位置， 使用 findall() 方法去代替
print(datepat.findall(text))

dategroup = re.compile(r'(\d+)/(\d+)/(\d+)')
m = dategroup.match("11/27/2012")
print(m.group(0))
print(m.group(1))
print(m.groups())  #('11', '27', '2012')


'''
搜索和替换
'''
text = "abctt,ttoo,yy"
print(text.replace("tt","pppp"))

print(text.join("|,{,}"))  #对比java

print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', "11/27/2012"))


# *? 非贪婪模式  *贪婪模式
str_pat = re.compile(r'"(.*)"')
str_pat2 = re.compile(r'"(.*?)"')
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
print(str_pat2.findall(text2))


#跨行匹配  在这个模式中， (?:.|\n) 指定了一个非捕获组 (也就是它定义了一个仅仅用来做匹配，而不能通过单独捕获或者编号的组)
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = ('/* this is a'
         'dfdfdfdf**/'
         'rrperere**')
print(comment.findall(text1))
print(comment.findall(text2)) #没有复现

commentHuanHang = re.compile(r'/\*((?:.|\n)*?)\*/')
print(commentHuanHang.findall(text1))
print(commentHuanHang.findall(text2))


#re.compile() 函数接受一个标志参数叫 re.DOTALL ，在这里非常有用。 它可以让正则表达式中的点(.)匹配包括换行符在内的任意字符


#标准化对于任何需要以一致的方式处理Unicode文本的程序都是非常重要的。 当处理来自用户输入的字符串而你很难去控制编码的时候尤其如此
import unicodedata
s = '\ufb01'
print(s)
unicodedata.normalize('NFD',s)

#正则中使用Unicode
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
print(arabic)


#去除无用字符
s = "           --abc===!!! "
print(s.strip())
print(s.strip().strip("-"))
print(s.strip().strip("-").strip("=!"))

#去除中间
ss = "hello World"
s1 = ss.replace(" ","")
print(s1)

s2 = re.sub("\s+","",ss)
print(s2)

#translate
# with open(ss) as f:
#     lines = (line.strip() for line in f)
#     for line in lines:
#         print(line)


#处理乱码
sl = "'pýtĥöñ\x0cis\tawesome\r\n'"
#空白字符 \t 和 \f 已经被重新映射到一个空格。回车字符r直接被删除
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None # Deleted
 }

a = sl.translate(remap)
print(a)

#以这个表格为基础进一步构建更大的表格。比如，让我们删除所有的和音符
import sys
# 通过使用 dict.fromkeys() 方法构造一个字典，每个Unicode和音符作为键，对应的值全部为 None
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                        if unicodedata.combining(chr(c)))
# 使用 unicodedata.normalize() 将原始输入标准化为分解形式字符
b = unicodedata.normalize('NFD', sl)
# 调用 translate 函数删除所有重音符
print(b.translate(cmb_chrs))

# 另一种清理文本的技术涉及到I/O解码与编码函数。这里的思路是先对文本做一些初步的清理， 然后再结合 encode() 或者 decode() 操作来清除或修改它

sl1 = unicodedata.normalize('NFD',sl)
sl1.encode('ascii','ignore').decode('ascii')
print(sl1)

text = "hello world"
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))

print(format(text, '=>20s'))
print(format(text, '*^20s'))

print('{:>10s} {:>10s}'.format('Hello', 'World'))

x = 1.23456
print(format(x, '>10'))
x = 1.23456
print(format(x, '^10.2f'))

print('%-20s' % text)
print('%20s' % text)

#合并拼接字符串
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(",".join(parts))
# 这样做的部分原因是你想去连接的对象可能来自各种不同的数据序列(比如列表，元组，字典，文件，集合或生成器等)， 如果在所有这些对象上都定义一个 join() 方法明显是冗余的。 因此你只需要指定你想要的分割字符串并调用他的 join() 方法去将文本片段组合起来。

a = 'Hello' 'World'
print(a)

b="dfd"
print('{} xx {}'.format(a,b))

# Version 1 (string concatenation)
# f.write(chunk1 + chunk2)

# Version 2 (separate I/O operations)
# f.write(chunk1)
# f.write(chunk2)

# 如果两个字符串很小，那么第一个版本性能会更好些，因为I/O系统调用天生就慢。 另外一方面，如果两个字符串很大，那么第二个版本可能会更加高效， 因为它避免了创建一个很大的临时结果并且要复制大量的内存块数据。 还是那句话，有时候是需要根据你的应用程序特点来决定应该使用哪种方案

# 字符串中插入变量
sss = '{name} is my {age}'
# print(sss.format("asay", "ttt"))
print(sss.format(name = "asay", age = "ttt"))


name = 'Guido'
age = 37
print(sss.format_map(vars()))

# print('%(name) has %(age) messages.' % vars())

import string
s = string.Template('$name has $age messages.')
print(s.substitute(vars()))


s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap
print(textwrap.fill(s, 30,initial_indent='sfsdfsd'))

s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
# print(p.unescape(s))


t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape

print(unescape(t))

# 字节操作
data = b'Hello World'
print(data)
print(data[0:5])
print(data[3]) #108

data = bytearray(b'Hello World')
print(data) #b'Hello'
print(data[0])  #72
print(data.decode("ascii")) #Hello World

print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii').decode("ascii"))

# 注意的是，使用字节字符串可能会改变一些操作的语义，特别是那些跟文件系统有关的操作。 比如，如果你使用一个编码为字节的文件名，而不是一个普通的文本字符串，会禁用文件名的编码/解码

#令牌 todo:scan技术 - 未完成  ** 文本解析匹配
# ?P<TOKENNAME> 用于给一个模式命名，供后面使用
# 通常来讲令牌化是很多高级文本解析与处理的第一步。 为了使用上面的扫描方法，你需要记住这里一些重要的几点。 第一点就是你必须确认你使用正则表达式指定了所有输入中可能出现的文本序列。 如果有任何不可匹配的文本出现了，扫描就会直接停止。这也是为什么上面例子中必须指定空白字符令牌的原因
text = 'foo = 23 + 42 * 10'
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
print(master_pat)


# 实现一个简单的递归下降分析器 todo
# 你想根据一组语法规则解析文本并执行命令，或者构造一个代表输入的抽象语法树。 如果语法非常简单，你可以不去使用一些框架，而是自己写这个解析器。
# 文本解析是一个很大的主题， 一般会占用学生学习编译课程时刚开始的三周时间。 如果你在找寻关于语法，解析算法等相关的背景知识的话，你应该去看一下编译器书籍。