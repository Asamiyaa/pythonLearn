'''
python中成员、变量、访问问题
    ■ 不像java需要定义class,进来就能定义输出和def
    ■ class相当于java中的内部类，内外部都能访问
    ■ 变量定义没有类型、
    ■ 方法定义
'''
import functools
import html

'''
内容包括默认参数、任意数量参数、强制关键字参数、注解和闭包。 另外，一些高级的控制流和利用回调函数传递数据的技术
'''


'''
vim下v-下选择多行或者多个字符

'''

def avg(first,*rest):
    return ((first) + sum(rest)) / (1+len(rest))

print(avg(1,2))
print(avg(1, 2, 3, 4))

import html
# 接受任意数量关键字参数
def make_element(name,value,**attrs):
    keyvalues = [' %s="%s"'  % item for item in attrs.items()]
    attr_str = ''.join(keyvalues)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name = name,
        attrs = attr_str,
        value = html.escape(value)
    )
    return element


print(make_element('item', 'Albat', size='large', quantity=6))
print(make_element('p', '<spam>'))


#同时接受任意数量的位置参数和关键字参数

def anyargs(*args,**kwargs):
    print(args)
    print(kwargs)

anyargs(1,2,3,name="asamiya",age="19")

'''
一个*参数只能出现在函数定义中最后一个位置参数后面，而 **参数只能出现在最后一个参数。 有一点要注意的是，在*参数后面仍然可以定义其他参数。
这种参数就是我们所说的强制关键字参数
'''
def b(x, *args, y, **kwargs):
    pass

# 将强制关键字参数放到某个*参数或者单个*后面就能达到这种效果
# 利用这种技术，我们还能在接受任意多个位置参数的函数中指定关键字参数
def recv(maxsize,*,block):
    'recive'
    # pass
    print(maxsize,block)
# recv(1024,True)
recv(1024,block=True)


def mininum(*values,clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


print(mininum(1, 5, 2, -5, 10))
print(mininum(1, 5, 2, -5, 10,clip=0))

'''
很多情况下，使用强制关键字参数会比使用位置参数表意更加清晰，程序也更加具有可读性
使用强制关键字参数也会比使用**kwargs参数更好，因为在使用函数help的时候输出也会更容易理解
'''


# 你写好了一个函数，然后想为这个函数的参数增加一些额外的信息，这样的话其他使用者就能清楚的知道这个函数应该怎么使用
# python解释器不会对这些注解添加任何的语义。它们不会被类型检查，运行时跟没有加注解之前的效果也没有任何差距。 然而，对于那些阅读源码的人来讲就很有帮助啦
def add(x:int ,y:int) -> int:
    return x + y


print(add(1, 2))
print(add.__annotations__)


# 返回多值
def myfun():
    return 1,3,"dfd"
#返回的是元组
d = (1,2)
d2 = 1,2
print(d)
print(d2)

# 默认参数



a,b,c = myfun()
print(myfun())


def spam(a,b=42):
    print(a,b)

spam(1)
spam(1, 2)
#默认是一个可修改的容器比如列表，集合或者字典，可以使用None
def spam2(a,b=None):
    if b is None:
        b = (1,2)
    a = a + 1
    return a,b


print(spam2(1))


# 默认参数的值应该是不可变的对象，比如None、True、False、数字或字符串。 特别的，千万不要像下面这样写代码：
#
# def spam(a, b=[]): # NO>>> def spam(a, b=[]):
# ...     print(b)
# ...     return b
# ...
# >>> x = spam(1)
# >>> x
# []
# >>> x.append(99)
# >>> x.append('Yow!')
# >>> x
# [99, 'Yow!']
# >>> spam(1) # Modified list gets returned!
# [99, 'Yow!'


# 为了解决这个问题，你可以创建一个独一无二的私有对象实例，就像上面的_no_value变量那样。 在函数里面，你可以通过检查被传递参数值跟这个实例是否一样来判断。 这里的思路是用户不可能去传递这个_no_value实例作为输入。 因此，这里通过检查这个值就能确定某个参数是否被传递进来了。
# 这里对 object() 的使用看上去有点不太常见。object 是python中所有类的基类。 你可以创建 object 类的实例，但是这些实例没什么实际用处，因为它并没有任何有用的方法， 也没有任何实例数据(因为它没有任何的实例字典，你甚至都不能设置任何属性值)。 你唯一能做的就是测试同一性。这个刚好符合我的要求，因为我在函数中就只是需要一个同一性的测试而已。


#定义匿名或内联函数
add = lambda x,y:x+y
print(add(1, 2))

#lambda表达式典型使用场景是排序或者数据reduce等
names = ['David Beazley', 'Brian Jones',
        'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))

print("abc".split()[-1])

'''
尽管lambda表达式允许你定义简单函数，但是它的使用是有限制的。 你只能指定单个表达式，它的值就是最后的返回值。也就是说不能包含其他的语言特性了， 包括多个语句、条件表达式、迭代以及异常处理等等。

你可以不使用lambda表达式就能编写大部分python代码。 但是，当有人编写大量计算表达式值的短小函数或者需要用户提供回调函数的程序的时候， 你就会看到lambda表达式的身影了。
'''
# 匿名函数捕获变量值
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10))
print(b(10))
# 这其中的奥妙在于lambda表达式中的x是一个自由变量， 在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的。 因此，在调用这个lambda表达式的时候，x的值是执行时的值。
x = 10
a = lambda y, x = x: x + y
x = 20
b = lambda y,x = x : x + y
print(a(10))
print(b(10))

# 减少可调用对象的参数个数
def spam(a,b,c,d):
    print(a,b,c,d)
# partial() 固定某些参数并返回一个新的callable对象。这个新的callable接受未赋值的参数， 然后跟之前已经赋值过的参数合并起来，最后将所有参数传递给原始函数
# 类似于重载
from functools import partial
spam(1,2,3,4)

s1 = functools.partial(spam,1)
s1(2,3,4)

s2 = functools.partial(spam,d = 99)
s2(1,2,3)
#
# def output_result(result, log=None):
#     if log is not None:
#         log.debug('Got: %r', result)
#
# # A sample function
# def add(x, y):
#     return x + y
#
# if __name__ == '__main__':
#     import logging
#     from multiprocessing import Pool
#     from functools import partial
#
#     logging.basicConfig(level=logging.DEBUG)
#     log = logging.getLogger('test')
#
#     p = Pool()
#     p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
#     p.close()
#     p.join()


#将单方法的类转换为函数 你有一个除 __init__() 方法外只定义了一个方法的类。为了简化代码，你想将它转换成一个函数
# 一个闭包就是一个函数， 只不过在函数内部带上了一个额外的变量环境。闭包关键特点就是它会记住自己被定义时的环境。 因此，在我们的解决方案中，opener() 函数记住了 template 参数的值，并在接下来的调用中使用它。
# 任何时候只要你碰到需要给某个函数增加额外的状态信息的问题，都可以考虑使用闭包。 相比将你的函数转换成一个类而言，闭包通常是一种更加简洁和优雅的方案。

# from urllib.request import urlopen
#
# class UrlTemplate:
#     def __init__(self, template):
#         self.template = template
#
#     def open(self, **kwargs):
#         return urlopen(self.template.format_map(kwargs))
#
# # Example use. Download stock data from yahoo
# yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
# for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
#     print(line.decode('utf-8'))
#
#
# def urltemplate(template):
#     def opener(**kwargs):
#         return urlopen(template.format_map(kwargs))
#     return opener
#
# # Example use
# yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
# for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
#     print(line.decode('utf-8'))


#带额外状态信息返回的回调函数
# 你的代码中需要依赖到回调函数的使用(比如事件处理器、等待后台任务完成后的回调等)， 并且你还需要让回调函数拥有额外的状态值，以便在它的内部使用到






