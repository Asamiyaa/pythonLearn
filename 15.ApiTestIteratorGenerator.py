# 迭代是Python最强大的功能之一

list = [1,2,3,4,5]
print(list)

for e in list:
    print(e)

# for e in list if 2 in list :


def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass


# with open('/etc/passwd') as f:
#     while True:
#         line = next(f, None)
#         if line is None:
#             break
#         print(line, end='')


it = iter(list)
print(next(it))
print(next(it))
print(next(it))


# 代理迭代
# 你构建了一个自定义容器对象，里面包含有列表、元组或其他可迭代对象。 你想直接在你的这个新容器对象上执行迭代操作
# 实际上你只需要定义一个 __iter__() 方法，将迭代操作代理到容器内部的对象上去
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    child3 = "1"            #可以添加任意类型参数
    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)
    # Outputs Node(1), Node(2)
    for ch in root:
        print(ch)

#使用生成器创建新的迭代模式
# 想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样
# 一个生成器函数主要特征是它只会回应在迭代中使用到的 next 操作。 一旦生成器函数返回退出，迭代终止
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x   #一个函数中需要有一个 yield 语句即可将其转换为一个生成器。 跟普通函数不同的是，生成器只能用于迭代操作
        x += increment

for n in frange(0,4,1):
    print(n)



# 实现迭代器协议
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
    # Outputs Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)


# Python的迭代协议要求一个 __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成

#反向迭代
# 反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效。 如果两者都不符合，那你必须先将对象转换为一个列表才行
a = [1,2,3,4]
for e in reversed(a):
    print(e)


# 定义一个反向迭代器可以使得代码非常的高效， 因为它不再需要将数据填充到一个列表中然后再去反向迭代这个列表
class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):    # todo :没看懂
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:    # todo :没看懂
            yield n
            n += 1

for rr in reversed(Countdown(3)):
    print(rr)
for rr in Countdown(3):
    print(rr)


# 带有外部状态的生成器函数

from collections import deque
class linehistory:
    def _init_(self,lines,histlen = 3):
        self.lines = lines;
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno,line in enumerate(self.lines,1):
            self.history.append(lineno,line)
            yield line
    def clear(self):
        self.history.clear()


with open('text.txt') as f :
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}',format(lineno,hline),end='')
