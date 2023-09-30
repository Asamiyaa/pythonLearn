# Python处理各种不同方式编码的数据，比如CSV文件，JSON，XML和二进制包装记录
# 数据结构那一章不同的是，这章不会讨论特殊的算法问题，而是关注于怎样获取和存储这些格式的数据。

import csv
from collections import namedtuple

headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
         ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
         ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
       ]
with open('stock.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

with open('stock.csv') as f:
    f_r = csv.reader(f)
    headersr = next(f_r)
    for row in f_r:
        print(row)
    print(headersr)
    print(headersr[0])
    print(headersr[1])

#namedtuple可以解决上面用下表显示的问题  row['Change']

# 一个字典序列的数据
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]

with open('stocks.csv','w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

'''
csv 库可识别Microsoft Excel所使用的CSV编码规则。 这或许也是最常见的形式，并且也会给你带来最好的兼容性。 然而，如果你查看csv的文档，就会发现有很多种方法将它应用到其他编码格式上(如修改分割字符等)。 例如，如果你想读取以tab分割的数据
'''
# 下面这样在非法标识符上使用一个正则表达式替换

import re
with open('stock.csv') as f:
    f_csv = csv.reader(f)
    headers = [ re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv) ]
    Row = namedtuple('Row', headers)
    for r in f_csv:
        pass

# csv产生的数据都是字符串类型的，它不会做任何其他类型的转换。 如果你需要做这样的类型转换，你必须自己手动去实现。
col_types = [str, float, str, str, float, int]
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversions to the row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))

'''
如果你读取CSV数据的目的是做数据分析和统计的话， 你可能需要看一看 Pandas 包。Pandas 包含了一个非常方便的函数叫 pandas.read_csv() ， 它可以加载CSV数据到一个 DataFrame 对象中去。 然后利用这个对象你就可以生成各种形式的统计、过滤数据以及执行其他高级操作了
'''

import json
data = {'name':'aaa','age':23}
json_str = json.dumps(data)
print(json_str)

print(json.loads(json_str))

# 处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据


from urllib.request import urlopen
# import json
# # u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
# resp = json.loads("json.json")
# from pprint import pprint
# pprint(resp)

s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)


class JSONObject:
   def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)
print(data.name)

'''
对象实例通常并不是JSON可序列化的.如果你想序列化对象实例，你可以提供一个函数，它的输入是一个实例，返回一个可序列化的字典
'''

def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d

# Dictionary mapping names to known classes
# classes = {
#     'Point' : Point
# }
#
# def unserialize_object(d):
#     clsname = d.pop('__classname__', None)
#     if clsname:
#         cls = classes[clsname]
#         obj = cls.__new__(cls) # Make instance without calling __init__
#         for key, value in d.items():
#             setattr(obj, key, value)
#         return obj
#     else:
#         return d


'''
xml parse
'''
from urllib.request import urlopen
from xml.etree.ElementTree import  parse
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)
print(doc)

# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)

'''
ElementTree 模块中的每个元素有一些重要的属性和方法，在解析的时候非常有用。 tag 属性包含了标签的名字，text 属性包含了内部的文本，而 get() 方法能获取属性值。
lxml 完全遵循XML标准，并且速度也非常快，同时还支持验证，XSLT，和XPath等特
'''

#增量式解析大型xml文件
from xml.etree.ElementTree import iterparse

def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


#加载所有到内存 这个脚本唯一的问题是它会先将整个XML文件加载到内存中然后解析。 在我的机器上，为了运行这个程序需要用到450MB左右的内存空间
from xml.etree.ElementTree import parse
from collections import Counter

potholes_by_zip = Counter()

doc = parse('xmltest.xml')
for pothole in doc.iterfind('row/row'):
    potholes_by_zip[pothole.findtext('zip')] += 1
for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)


# 这个版本的代码运行时只需要7MB的内存–大大节约了内存资源
'''
start 事件在某个元素第一次被创建并且还没有被插入其他数据(如子元素)时被创建。 而 end 事件在某个元素已经完成时被创建。 尽管没有在例子中演示， start-ns 和 end-ns 事件被用来处理XML文档命名空间的声明。
这本节例子中， start 和 end 事件被用来管理元素和标签栈。 栈代表了文档被解析时的层次结构， 还被用来判断某个元素是否匹配传给函数 parse_and_remove() 的路径。 如果匹配，就利用 yield 语句向调用者返回这个元素。
在 yield 之后的下面这个语句才是使得程序占用极少内存的ElementTree的核心特性：
elem_stack[-2].remove(elem)
这个语句使得之前由 yield 产生的元素从它的父节点中删除掉。 假设已经没有其它的地方引用这个元素了，那么这个元素就被销毁并回收内存。
对节点的迭代式解析和删除的最终效果就是一个在文档上高效的增量式清扫过程。 文档树结构从始自终没被完整的创建过。尽管如此，还是能通过上述简单的方式来处理这个XML数据。
这种方案的主要缺陷就是它的运行性能了。 我自己测试的结果是，读取整个文档到内存中的版本的运行速度差不多是增量式处理版本的两倍快。 但是它却使用了超过后者60倍的内存。 因此，如果你更关心内存使用量的话，那么增量式的版本完胜。
'''
from collections import Counter

potholes_by_zip = Counter()

data = parse_and_remove('xmltest.xml', 'row/row')
for pothole in data:
    potholes_by_zip[pothole.findtext('zip')] += 1
for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)



from xml.etree.ElementTree import Element
def dict_to_xml(tag,d):
    elem = Element(tag)
    for key,val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

s = {'name':'agg','age':100}
e = dict_to_xml('stock',s)
print(e)

from xml.etree.ElementTree import tostring

print(tostring(e))

e.set('_id','1212')
print(tostring(e))


#xml命名空间 todo


#编码解码base64
s = b'hello'
import base64
a = base64.b64encode(s)
print(a)

print(base64.b64decode(a))



#累加与统计
# 对于任何涉及到统计、时间序列以及其他相关技术的数据分析问题，都可以考虑使用 Pandas库
'''
Pandas是一个拥有很多特性的大型函数库，我在这里不可能介绍完。 
但是只要你需要去分析大型数据集合、对数据分组、计算各种统计量或其他类似任务的话，这个函数库真的值得你去看一看
'''














