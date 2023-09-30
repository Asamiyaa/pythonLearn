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

from collections import deque, defaultdict


class linehistory:
    def __init__(self,lines,histlen = 3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno,line in enumerate(self.lines,1):
            self.history.append((lineno,line))
            yield line
    def clear(self):
        self.history.clear()


with open('C:\\Users\\73699\\PycharmProjects\\pythonLearn\\source\\test.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno,hline),end='')


#迭代器切片
# 迭代器和生成器不能使用标准的切片操作，因为它们的长度事先我们并不知道(并且也没有实现索引)。 函数 islice() 返回一个可以生成指定元素的迭代器，它通过遍历并丢弃直到切片开始索引位置的所有元素。 然后才开始一个个的返回元素，并直到切片结束索引位置。
# 这里要着重强调的一点是 islice() 会消耗掉传入的迭代器中的数据。 必须考虑到迭代器是不可逆的这个事实。 所以如果你需要之后再次访问这个迭代器的话，那你就得先将它里面的数据放入一个列表中
#
def count(n):
    while True:
        yield n
        n += 1
c = count(0)
# print(c[10:20])
# TypeError: 'generator' object is not subscriptable

import itertools
for x in itertools.islice(c,10,20):
    print(x)

# 跳过可迭代对象的开始部分
#  islice() 函数最后那个 None 参数指定了你要跳过前面3个元素，获取第4个到最后的所有元素， 如果 None 和3的位置对调，意思就是仅仅获取前三个元素恰恰相反， (这个跟切片的相反操作 [3:] 和 [:3] 原理是一样的)。
from itertools import dropwhile

linenow = [1,2,3,4,5,6]
for e in linenow:
    print(e)
for e in dropwhile(lambda e : not e > 1,linenow):
    print(e)
for e in itertools.islice(linenow,3,None):
    print(e)

# 这样写确实可以跳过开始部分的注释行，但是同样也会跳过文件中其他所有的注释行。 换句话讲，我们的解决方案是仅仅跳过开始部分满足测试条件的行，在那以后，所有的元素不再进行测试和过滤了。
# with open('/etc/passwd') as f:
#     # Skip over initial comments
#     while True:
#         line = next(f, '')
#         if not line.startswith('#'):
#             break
#
#     # Process remaining lines
#     while line:
#         # Replace with useful processing
#         print(line, end='')
#         line = next(f, None)

# 排列组合的迭代
items = [1,2,3,4,5]
from itertools import permutations

for item in permutations(items):
        print(item)
for item in permutations(items,3):
        print(item)

# 对于 combinations() 来讲，元素的顺序已经不重要了。 也就是说，组合 ('a', 'b') 跟 ('b', 'a') 其实是一样的(最终只会输出其中一个)

# 在计算组合的时候，一旦元素被选取就会从候选中剔除掉(比如如果元素’a’已经被选取了，那么接下来就不会再考虑它了)。 而函数 itertools.combinations_with_replacement() 允许同一个元素被选择多次，比如：
for c in itertools.combinations_with_replacement(item,3):
    print(c)



# 迭代一个序列的同时跟踪正在被处理的元素索引
my_list = ['a','b','c']
for idx ,val in enumerate(my_list):
    print(idx,val)

for idx ,val in enumerate(my_list,1):
    print(idx,val)



# 如果你处理完文件后打印 word_summary ，会发现它是一个字典(准确来讲是一个 defaultdict )， 对于每个单词有一个 key ，每个 key 对应的值是一个由这个单词出现的行号组成的列表。 如果某个单词在一行中出现过两次，那么这个行号也会出现两次， 同时也可以作为文本的一个简单统计
# word_summary = defaultdict(list)
#
# with open('C:\\Users\\73699\\PycharmProjects\\pythonLearn\\source\\test.txt', 'r') as f:
#     lines = f.readlines()
#
# for idx, line in enumerate(lines):
#     # Create a list of words in current line
#     words = [w.strip().lower() for w in line.split()]
#     for word in words:
#         word_summary[word].append(idx)
#
#     print(word_summary)

data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

# Correct!
for n, (x, y) in enumerate(data):
    print('{},{}',n,(x,y))



# 同时迭代多个序列，每次分别从一个序列中取一个元素。

#按短的迭代
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x,y in zip(xpts,ypts):
    print(x,y)

#按长的迭代
for x,y in itertools.zip_longest(xpts, ypts):
    print(x,y)

# zip() 会创建一个迭代器来作为结果返回。 如果你需要将结对的值存储在列表中，要使用 list() 函数


# 想在多个对象执行相同的操作，但是这些对象在不同的容器中，你希望代码在不失可读性的情况下避免写重复的循环
from itertools import chain
a = [1,2,3,4]
b = ['x','y','z']

for x in chain(a,b):
    print(x)

# 第一种方案中， a + b 操作会创建一个全新的序列并要求a和b的类型一致。 chian() 不会有这一步，所以如果输入序列非常大的时候会很省内存。 并且当可迭代对象类型不一样的时候 chain() 同样可以很好的工作# Inefficent
# for x in a + b:
#     ...
#
#     # Better
# for x in chain(a, b):
#     ...


# 想以数据管道(类似Unix管道)的方式迭代处理数据。 比如，你有个大量的数据需要处理，但是不能将它们一次性放入内存中
# 生成器函数是一个实现管道机制的好办法
import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path,name)

def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence.
    '''
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)


# 如果将来的时候你想扩展管道，你甚至可以在生成器表达式中包装数据。 比如，下面这个版本计算出传输的字节数并计算其总和。
lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
bytecolumn = (line.rsplit(None,1)[1] for line in pylines)
bytes = (int(x) for x in bytecolumn if x != '-')
print('Total', sum(bytes))


'''
以管道方式处理数据可以用来解决各类其他问题，包括解析，读取实时数据，定时轮询等。

为了理解上述代码，重点是要明白 yield 语句作为数据的生产者而 for 循环语句作为数据的消费者。 当这些生成器被连在一起后，每个 yield 会将一个单独的数据元素传递给迭代处理管道的下一阶段。 在例子最后部分， sum() 函数是最终的程序驱动者，每次从生成器管道中提取出一个元素。

这种方式一个非常好的特点是每个生成器函数很小并且都是独立的。这样的话就很容易编写和维护它们了。 很多时候，这些函数如果比较通用的话可以在其他场景重复使用。 并且最终将这些组件组合起来的代码看上去非常简单，也很容易理解。

使用这种方式的内存效率也不得不提。上述代码即便是在一个超大型文件目录中也能工作的很好。 事实上，由于使用了迭代方式处理，代码运行过程中只需要很小很小的内存。

在调用 gen_concatenate() 函数的时候你可能会有些不太明白。 这个函数的目的是将输入序列拼接成一个很长的行序列。 itertools.chain() 函数同样有类似的功能，但是它需要将所有可迭代对象作为参数传入。 在上面这个例子中，你可能会写类似这样的语句 lines = itertools.chain(*files) ， 这将导致 gen_opener() 生成器被提前全部消费掉。 但由于 gen_opener() 生成器每次生成一个打开过的文件， 等到下一个迭代步骤时文件就关闭了，因此 chain() 在这里不能这样使用。 上面的方案可以避免这种情况。

gen_concatenate() 函数中出现过 yield from 语句，它将 yield 操作代理到父生成器上去。 语句 yield from it 简单的返回生成器 it 所产生的所有

'''
from collections.abc import Iterable
# 展开嵌套的序列  想将一个多层嵌套的序列展开成一个单层列表
#todo:还在报错
# def flatten(items,ignore_types=(str,bytes)):
#     for x in items:
#         if isinstance(x,Iterable) and not isinstance(x,ignore_types):
#             yield from flatten(x)
#         else:
#             yield x
#
# items = [1,2,[3,4,[5,6],7],8]
# for e in flatten(items):
#     print(e)
from collections.abc import Iterable

# def flatten(items, ignore_types=(str, bytes)):
#     if not isinstance(ignore_types, (type, tuple)):
#         raise TypeError("ignore_types must be a type or a tuple of types")
#
#     for x in items:
#         if isinstance(x, Iterable) and not isinstance(x, ignore_types):
#             yield from flatten(x, ignore_types)  # 传递 ignore_types 参数
#         else:
#             yield x
#
# items = [1, 2, [3, 4, [5, 6], 7], 8]
# for x in flatten(items):
#     print(x)


from collections.abc import Iterable

# def flatten(items, ignore_types=(str, bytes)):
#     if not isinstance(ignore_types, (type, tuple)):
#         raise TypeError("ignore_types must be a type or a tuple of types")
#     for x in items:
#         if isinstance(x, Iterable) and not isinstance(x, ignore_types):
#             yield from flatten(x, ignore_types)
#         else:
#             yield x
#
# items = [1, 2, [3, 4, [5, 6], 7], 8]
# for x in flatten(items):
#     print(x)



# from collections.abc import Iterable
#
# def flatten(items, ignore_types=(str, bytes)):
#     if not isinstance(ignore_types, (type, tuple)):
#         raise TypeError("ignore_types must be a type or a tuple of types")
#     for x in items:
#         if isinstance(x, Iterable) and not isinstance(x, ignore_types):
#             yield from flatten(x, ignore_types)
#         else:
#             yield x
#
# items = [1, 2, [3, 4, [5, 6], 7], 8]
# for x in flatten(items):
#     print(x)

# 顺序迭代合并后的排序迭代对象
print("----------")
import heapq
a = [1,4,5,1]
b = [2,3,5,6]
for c in heapq.merge(a,b):
    print(c) #必须是不同元素才有效

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a,b):
    print(c)
'''
heapq.merge 可迭代特性意味着它不会立马读取所有序列。 这就意味着你可以在非常长的序列中使用它，而不会有太大的开销
有一点要强调的是 heapq.merge() 需要所有输入序列必须是排过序的。 特别的，它并不会预先读取所有数据到堆栈中或者预先排序，也不会对输入做任何的排序检测。 它仅仅是检查所有序列的开始部分并返回最小的那个，这个过程一直会持续直到所有输入序列中的元素都被遍历完。
with open('sorted_file_1', 'rt') as file1, \
    open('sorted_file_2', 'rt') as file2, \
    open('merged_file', 'wt') as outf:

    for line in heapq.merge(file1, file2):
        outf.write(line)
'''



# 迭代器代替while无限循环

'''
CHUNKSIZE = 8192

def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)
'''
CHUNKSIZE = 8192
def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        pass
        # process_data(data)
import sys
f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10), ''):
     n = sys.stdout.write(chunk)
'''
iter 函数一个鲜为人知的特性是它接受一个可选的 callable 对象和一个标记(结尾)值作为输入参数。 当以这种方式使用的时候，它会创建一个迭代器， 这个迭代器会不断调用 callable 对象直到返回值和标记值相等为止。
这种特殊的方法对于一些特定的会被重复调用的函数很有效果，比如涉及到I/O调用的函数。 举例来讲，如果你想从套接字或文件中以数据块的方式读取数据，通常你得要不断重复的执行 read() 或 recv() ， 并在后面紧跟一个文件结尾测试来决定是否终止。这节中的方案使用一个简单的 iter() 调用就可以将两者结合起来了。 其中 lambda 函数参数是为了创建一个无参的 callable 对象，并为 recv 或 read() 方法提供了 size 参数
'''







