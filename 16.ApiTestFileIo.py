import io

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
























