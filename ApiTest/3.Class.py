# coding=utf-8
class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


'''
创建实例对象
要创建一个类的实例，你可以使用类的名称，并通过__init__方法接受参数。
'''
#__init__("epy",10)
emp = Employee("eyp",10)   #不能有空格,有空格不能执行
print(emp.displayEmployee()) #没返回,所以不能print
# emp.displayEmployee()

emp.name="1111"
emp.displayEmployee()

del emp.name
# emp.displayEmployee()  #直接修改代码、删除了属性
print(hasattr(emp, "name"))
print(getattr(emp, "salary"))
# setattr() delattr  类似于封装的反射



'''
Python 内置类属性
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块 mymod 中，那么 className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了以个由所有父类组成的元组）
'''

print("Employee.__doc__:", emp.__doc__)
# print("Employee.__name__:", emp.__name__)  #有这些导致程序不往下执行，报错，但是不显示
print("Employee.__module__:", emp.__module__)
# print("Employee.__bases__:", emp.__bases__)
print("Employee.__dict__:", emp.__dict__)


class Son(Employee):
    def __init__(self, sonname):
        self.sonname = sonname

    def sonnameM(self):
        print("Total", self.sonname)


son = Son("sonnn")
son.sonnameM()
# TypeError: 'str' object is not callable    这种错误通常发生在你尝试使用括号 () 来调用一个字符串变量，


'''
正则
re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None；而 re.search 匹配整个字符串，直到找到一个匹配。
'''

import re

line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")






phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)





# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))