import io
import sys

with open('somefile.txt','wt') as f:
    f.write("abc")
    f.write("ddd今天国庆节")

with open("somefile.txt",'rt') as f:
    data = f.read()
    print(data)

#指定编码

with open("somefile.txt",'rt',encoding='latin-1') as f:
    data = f.read()
    print(data)

'''
另外一个问题是关于换行符的识别问题，在Unix和Windows中是不一样的(分别是 \n 和 \r\n )。 默认情况下，Python会以统一模式处理换行符。 这种模式下，在读取文本的时候，Python可以识别所有的普通换行符并将其转换为单个 \n 字符。 类似的，在输出时会将换行符 \n 转换为系统默认的换行符。 如果你不希望这种默认的处理方式，可以给 open() 函数传入参数 newline='' 
'''
with open('somefile.txt', 'rt', newline='') as f:
    print(f.read())

#忽略编码错误

with open('somefile.txt', 'rt', encoding='ascii',errors='replace') as f:
    print(f.read())

with open('somefile.txt', 'rt', encoding='ascii',errors='ignore') as f:
    print(f.read())


#打印输出至文件中
with open('somefile.txt','wt') as f:
    print('helloworld',file=f)


#分隔符、行终止符打印、改变默认
print("abc",50,55)
print("abc",50,55,sep=",")
print("abc",50,55,sep=",",end="!!\n")

#使用end参数设置禁止换行
for i in range(5):
    print(i,end='')

print(','.join(('ACME','50','91.5')))

#str.join() 的问题在于它仅仅适用于字符串。这意味着你通常需要执行另外一些转换才能让它正常工作
row = ('ACME', 50, 91.5)
# print(','.join(row))
print(','.join(str(x) for x in row))

print(*row, sep=',')




#读写字节数据
# 在读取二进制数据时，需要指明的是所有返回的数据都是字节字符串格式的，而不是文本字符串。 类似的，在写入的时候，必须保证参数是以字节形式对外暴露数据的对象(比如字节字符串，字节数组对象等)

with open('somefile.bin','wb') as f:
    f.write(b'abcddd')

with open('somefile.bin','rb') as f:
    print(f.read())

# 在读取二进制数据的时候，字节字符串和文本字符串的语义差异可能会导致一个潜在的陷阱。 特别需要注意的是，索引和迭代动作返回的是字节的值而不是字节字符串

# 从二进制模式的文件中读取或写入文本数据，必须确保要进行解码和编码操作
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))

'''
二进制I/O还有一个鲜为人知的特性就是数组和C结构体类型能直接被写入，而不需要中间转换为自己对象。比如：

import array
nums = array.array('i', [1, 2, 3, 4])
with open('data.bin','wb') as f:
    f.write(nums)
这个适用于任何实现了被称之为”缓冲接口”的对象，这种对象会直接暴露其底层的内存缓冲区给能处理它的操作。 二进制数据的写入就是这类操作之一。
'''

#文件不存在才能写入  如果文件是二进制的，使用 xb 来代替 xt
# with open("x1x.txt",'xt') as f:
#     f.write("abc")

import os
if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
         f.write('Hello\n')
else:
        print('File already exists!')



#字符串io操作  想使用操作类文件对象的程序来操作文本或二进制字符串
s = io.StringIO()
print(s.write("helloworl\n"))

print(s.getvalue())
#上面get后没了，再付一次值
s = io.StringIO("dfdfdfrr")
print(s.read(2))
print(s.read())

# io.StringIO 只能用于文本。如果你要操作二进制数据，要使用 io.BytesIO 类来代替


#读写压缩文件 读写一个gzip或bz2格式的压缩文件


import  gzip

with gzip.open('somefile.gz','wt') as f:
    f.write("abdjdncd")

with gzip.open('somefile.gz','rt') as f:
    text = f.read()
    print(text)

# import bz2
# with bz2.open("somefile.gz",'rt') as f:
#     text = f.read()

'''
大部分情况下读写压缩数据都是很简单的。但是要注意的是选择一个正确的文件模式是非常重要的。 如果你不指定模式，那么默认的就是二进制模式，如果这时候程序想要接受的是文本数据，那么就会出错。 gzip.open() 和 bz2.open() 接受跟内置的 open() 函数一样的参数， 包括 encoding，errors，newline 等等
compresslevel 这个可选的关键字参数来指定一个压缩级别
'''
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)




#固定大小记录的文件迭代  在一个固定长度记录或者数据块的集合上迭代，而不是在一个文件中一行一行的迭代
# functools.partial 用来创建一个每次被调用时从文件中读取固定数目字节的可调用对象。 标记值 b'' 就是当到达文件结尾时的返回值
from functools import partial

RECORD_SIZE = 32

with open('somefile.bin', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        pass


#读取二进制文件到可变缓冲区 直接读取二进制数据到一个可变缓冲区中，而不需要做任何的中间复制操作。 或者你想原地修改数据并将它写回到一个文件中去

import os.path
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename,'rb') as f:
        f.readinto(buf)
    return buf

with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')
buf = read_into_buffer('sample.bin')
print(buf)

'''
文件对象的 readinto() 方法能被用来为预先分配内存的数组填充数据，甚至包括由 array 模块或 numpy 库创建的数组。 和普通 read() 方法不同的是， readinto() 填充已存在的缓冲区而不是为新对象重新分配内存再返回它们。 因此，你可以使用它来避免大量的内存分配操作。 比如，如果你读取一个由相同大小的记录组成的二进制文件时
'''
record_size = 32 # Size of each record (adjust value)

buf = bytearray(record_size)
with open('somefile', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break


'''
memoryview ， 它可以通过零复制的方式对已存在的缓冲区执行切片操作，甚至还能修改它的内容
'''
m1 = memoryview(buf)
m2 = m1[-5:]
print(m2)
m2[:] = b'WORLD'
print(buf)


'''
使用 f.readinto() 时需要注意的是，你必须检查它的返回值，也就是实际读取的字节数。
如果字节数小于缓冲区大小，表明数据被截断或者被破坏了(比如你期望每次读取指定数量的字节)。
最后，留心观察其他函数库和模块中和 into 相关的函数(比如 recv_into() ， pack_into() 等)
'''

#内存映射的二进制文件
# 想内存映射一个二进制文件到一个可变字节数组中，目的可能是为了随机访问它的内容或者是原地做些修改

import os
import mmap
def memeroy_map(filename,access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename,os.O_RDWR)
    return mmap.mmap(fd,size,access=access)

size = 100000
with open('somefile.txt','wb') as f:
    f.seek(size - 1)
    f.write(b'\x00')

m = memeroy_map('somefile.txt')
print(len(m))

print(m[0:10])

m[0:11]=b'Hellwolddfd'
m.close()

with open('somefile.txt','rb') as f:
    print(f.read(6))



#mmap同样可以作为一个上下文管理器来使用,这时候会底层的文件自动关闭

# 如果你想在本地修改数据，但是又不想将修改写回到原始文件中，可以使用 mmap.ACCESS_COPY

'''
需要强调的一点是，内存映射一个文件并不会导致整个文件被读取到内存中。 也就是说，文件并没有被复制到内存缓存或数组中。相反，操作系统仅仅为文件内容保留了一段虚拟内存。 当你访问文件的不同区域时，这些区域的内容才根据需要被读取并映射到内存区域中。 而那些从没被访问到的部分还是留在磁盘上。所有这些过程是透明的，在幕后完成
如果多个Python解释器内存映射同一个文件，得到的 mmap 对象能够被用来在解释器直接交换数据。 也就是说，所有解释器都能同时读写数据，并且其中一个解释器所做的修改会自动呈现在其他解释器中。 很明显，这里需要考虑同步的问题。但是这种方法有时候可以用来在管道或套接字间传递数据。
'''



#文件路径名操作
import os
path = "c:\\Users"
print(os.path.basename(path))

print(os.path.dirname(path))

#join 、 expanduser 、splitext


print(os.path.exists('/etc/passwd'))
print(os.path.isfile('c:\\Users'))
print(os.path.isdir('c:\\Users'))

print(os.path.getsize("c:\\Users"))
print(os.path.getmtime("c:\\Users"))
import time

print(time.ctime(os.path.getmtime("c:\\Users")))

'''
文件测试是很简单的。 在写这些脚本时，可能唯一需要注意的就是你需要考虑文件权限的问题，特别是在获取元数据时候
'''

print(os.listdir('c:\\Users'))
names = [name for name in os.listdir('c:\\Users') if os.path.isfile('c:\\Users')]
print(names)

names = [name for name in os.listdir('c:\\Users') if os.path.isdir('c:\\Users')]
print(names)


#文件名匹配
import glob

print(glob.glob('C:\\User\All*'))
from fnmatch import fnmatch
# files = [name1 for name1 is os.listdir('') if fnmatch(name1,'*py')]

# 想获取其他的元信息，比如文件大小，修改时间等等， 你或许还需要使用到 os.path 模块中的函数或着 os.stat() 函数来收集数据



#忽略文件名编码

print(sys.getfilesystemencoding())

#打印不合法文件名 在编写必须处理文件系统的程序时一个不太常见但又很棘手的问题。 默认情况下，Python假定所有文件名都已经根据 sys.getfilesystemencoding() 的值编码过了。 但是，有一些文件系统并没有强制要求这样做，因此允许创建文件名没有正确编码的文件。 这种情况不太常见，但是总会有些用户冒险这样做或者是无意之中这样做了( 可能是在一个有缺陷的代码中给 open() 函数传递了一个不合规范的文件名
def bad_filename(filename):
    return repr(filename)[1:-1]

# try:
#     print(filename)
# except UnicodeEncodeError:
#     print(bad_filename(filename))
#

# 在 bad_filename() 函数中怎样处置取决于你自己。 另外一个选择就是通过某种方式重新编码
def bad_filename(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')

# 增加或改变已打开文件的编码
import urllib.request
import io

u = urllib.request.urlopen("http://www.baidu.com")
f = io.TextIOWrapper(u,encoding='utf-8')
text = f.read()
print(text)
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='latin-1')
print(sys.stdout.encoding)


'''
I/O系统由一系列的层次构建而成。你可以试着运行下面这个操作一个文本文件的例子来查看这种层次
io.TextIOWrapper 是一个编码和解码Unicode的文本处理层， io.BufferedWriter 是一个处理二进制数据的带缓冲的I/O层， io.FileIO 是一个表示操作系统底层文件描述符的原始文件。 增加或改变文本编码会涉及增加或改变最上面的 io.TextIOWrapper 层
detach() 方法会断开文件的最顶层并返回第二层，之后最顶层就没什么用了。一旦断开最顶层后，你就可以给返回结果添加一个新的最顶层
'''
f = open('sample.txt','w')
print(f)
print(f.buffer)
print(f.buffer.raw)



#创建临时文件和文件夹
from tempfile import TemporaryFile
with TemporaryFile('w+t') as f:
    f.write("hellow world")
    f.write("testTTT")

    f.seek(0)
    print(f.read())


# 在大多数Unix系统上，通过 TemporaryFile() 创建的文件都是匿名的，甚至连目录都没有。 如果你想打破这个限制，可以使用 NamedTemporaryFile() 来代替。
# f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
from tempfile import NamedTemporaryFile
with NamedTemporaryFile('w+t', delete=False) as f:
    f.write("hellow world")
    f.write("testTTT")

    f.seek(0)
    print(f.read())
    print('filename is:', f.name)


#与串行端口的数据通信
# 使用第三方包如 pySerial 的一个原因是它提供了对高级特性的支持 (比如超时，控制流，缓冲区刷新，握手协议等等)。举个例子，如果你想启用 RTS-CTS 握手协议， 你只需要给 Serial() 传递一个 rtscts=True 的参数即可。 其官方文档非常完善，因此我在这里极力推荐这个包。
# 时刻记住所有涉及到串口的I/O都是二进制模式的。因此，确保你的代码使用的是字节而不是文本 (或有时候执行文本的编码/解码操作)。 另外当你需要创建二进制编码的指令或数据包的时候，struct 模块也是非常有用的

import serial
# ser = serial.Serial('/dev/tty.usbmodem641', # Device name varies
#                     baudrate=9600,
#                     bytesize=8,
#                     parity='N',
#                     stopbits=1)


#序列话对象
# 将一个Python对象序列化为一个字节流，以便将它保存到一个文件、存储到数据库或者通过网络传输它
import pickle
# class Test:
#     def __int__(self, value):
#         self.value = value
# data = Test("dbc") # Some Python object
class Test:
    def __init__(self, value):
        self.value = value

data = Test("dbc")
print("===>>>",data)
print(pickle.dumps(data))
# Restore from a file
f = open('somefile', 'wb')
# Restore from a string
# data = pickle.loads(s)









































































