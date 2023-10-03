# 让对象支持常见的Python特性、特殊方法的使用、 类封装技术、继承、内存管理以及有用的设计模式。


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 是占位符，表示你希望在这两个位置上填入某些值。而!r则表示将值使用repr()函数进行格式化。
    def __repr__(self):
        return "Pair({0.x!r}, {0.y!r})".format(self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # 格式化代码 {0. x} 对应的是第1个参数的x属性。 因此，在下面的函数中，0实际上指的就是self本身
    # def __str__(self):
    #     return "({0.x!s}, {0.y!s})".format(self)

    # 作为这种实现的一个替代，你也可以使用 % 操作符
    def __str__(self):
        return 'Pair(%r, %r)' % (self.x, self.y)


print(Pair(1, 2))
print(Pair(1, 2).__repr__())

#格式化
_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }

# 类的访问范围类似于java中的内部类，这里没有严格的访问权限限制
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


date = Date(2023,10,2)
print(date.__format__('mdy'))

# 'The end is {:%d %b %Y}. Goodbye'.format(d)


# 让对象支持上下文管理协议 (with语句)
# 为了让一个对象兼容 with 语句，你需要实现 __enter__() 和 __exit__() 方法
# 在需要管理一些资源比如文件、网络连接和锁的编程环境中，使用上下文管理器是很普遍的。 这些资源的一个主要特征是它们必须被手动的关闭或释放来确保程序的正确运行
from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None

# 初始化的时候并不会做任何事情(比如它并没有建立一个连接)。 连接的建立和关闭是使用 with 语句自动完成的


from functools import partial

conn = LazyConnection(('www.python.org', 80))
# Connection closed
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed
    print(resp)


# 嵌套链接  LazyConnection 类可以被看做是某个连接工厂。在内部，一个列表被用来构造一个栈
from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()

# Example use
from functools import partial

conn = LazyConnection(('www.python.org', 80))
with conn as s1:
    pass
    with conn as s2:
        pass
        # s1 and s2 are independent sockets


# 创建大量对象时节省内存方法  程序要创建大量(可能上百万)的对象，导致占用很大的内存  给类添加 __slots__ 属性来极大的减少实例所占的内存
# 当你定义后，Python就会为实例使用一种更加紧凑的内部表示。 实例通过一个很小的固定大小的数组来构建，而不是为每个实例定义一个字典，这跟元组或列表很类似。 在中列出的属性名在内部被映射到这个数组的指定小标上。 使用slots一个不好的地方就是我们不能再给实例添加新的属性了，只能使用在 中定义的那些属性名。
# 更多的是用来作为一个内存优化工具。
class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

# 类中封装属性名  你想封装类的实例上面的“私有”数据，但是Python语言并没有访问控制。
# Python程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命名规约来达到这个效果
# Python并不会真的阻止别人访问内部名称。但是如果你这么做肯定是不好的，可能会导致脆弱的代码 如果你看到某个模块名以单下划线开头(比如_socket)，那它就是内部实现。 类似的，模块级别函数比如 sys._getframe() 在使用的时候就得加倍小心了

# 第一个约定是任何以单下划线_开头的名字都应该是内部实现
# 在前面的类B中，私有属性会被分别重命名为 _B__private 和 _B__private_method 。 这时候你可能会问这样重命名的目的是什么，答案就是继承——这种属性通过继承是无法被覆盖的。
# 大多数而言，你应该让你的非公共名称以单下划线开头。但是，如果你清楚你的代码会涉及到子类， 并且有些内部属性应该在子类中隐藏起来，那么才考虑使用双下划线方案
class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1 # Does not override B.__private

    # Does not override B.__private_method()
    def __private_method(self):
        pass



# 创建可管理的属性
# 想给某个实例attribute增加除访问与修改之外的其他处理逻辑，比如类型检查或合法性验证
# properties可以实现优雅的编程接口，但有些时候你还是会想直接使用getter和setter函数
#不要大量的写getter/setter
class Person:
    def __init__(self, first_name):
        self._first_name = first_name

    # Getter function
    @property   #通过Property包装
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")
# 三个方法的名字都必须一样。 第一个方法是一个 getter 函数，它使得 first_name 成为一个属性。 其他两个方法给 first_name 属性添加了 setter 和 deleter 函数。 需要强调的是只有在 first_name 属性被创建后， 后面的两个装饰器 @first_name.setter 和 @first_name.deleter 才能被定义。



# 调用父类方法
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)








    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value) # Call original __setattr__
        else:
            setattr(self._obj, name, value)

# __setattr__() 的实现包含一个名字检查。 如果某个属性名以下划线(_)开头，就通过 super() 调用原始的 __setattr__() ， 否则的话就委派给内部的代理对象 self._obj 去处理。 这看上去有点意思，因为就算没有显式的指明某个类的父类， super() 仍然可以有效的工作


# 更复杂的涉及到多继承的代码中就有可能导致很奇怪的问题发  super().__init__() 好于Base.__init__() ，后者会调用两次
# Python会计算出一个所谓的方法解析顺序(MRO)列表。 这个MRO列表就是一个简单的所有基类的线性顺序表
# 为了实现继承，Python会在MRO列表上从左到右开始查找基类，直到找到第一个匹配这个属性的类为止。
# 所要知道的就是MRO列表中的类顺序会让你定义的任意类层级关系变得有意义。


# 子类中扩展property

