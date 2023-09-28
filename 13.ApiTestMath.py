# 当一个值刚好在两个边界的中间的时候， round 函数返回离它最近的偶数。 也就是说，对1.5或者2.5的舍入运算都会得到2
import math
import struct

print(round(1.23, 1))
print(round(-1.22, 1))
print(round(1.5, 0)) #2.0
print(round(2.5, 0)) #2.0


# 传给 round() 函数的 ndigits 参数可以是负数，这种情况下， 舍入运算会作用在十位、百位、千位等上面
print(round(127343, -1))

x = 11.63456
print(format(x, '0.2f'))
print(format(x, '0.3f'))
print(format(x, '1.0f'))
print(format(x, '2.0f'))
print('value is {:0.3f}'.format(x))

from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)

print((a + b) == Decimal(6.3)) #False
print((a + b) == Decimal('6.3')) #True

#本地上下文
from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)


nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))
# math.fsum() 所提供的更精确计算能力来解决
import math
math.fsum(nums)

x = 1234.56789
print(format(x, '0.2f'))
print(format(x, '>10.2f'))
print(format(x, '<10.2f'))
print(format(x, '^10.1f'))
print(format(x, '0,.2f')) # 1,234.57

# 使用指数记法，将f改成e或者E(取决于指数输出的大小写形式
print(format(x, 'e'))
print(format(x, '0.2E'))

# 同时指定宽度和精度的一般形式是 '[<>^]?width[,]?(.digits)?' ， 其中 width 和 digits 为整数，？代表可选部分
print('The value is {:0,.2f}'.format(x))

#千分位
swap_separators = { ord('.'):',', ord(','):'.' }
print(format(x, ',').translate(swap_separators))

print('%0.2f' % x)  #1234.57
print('%10.1f' % x)

x = 1234
print(bin(x))
print(oct(x))
print(hex(x))
# 去掉其中的0b,0o,0x
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

# 字节到大整数的打包与解包\在一些应用领域有时候也会出现，比如密码学或者网络
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))

print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))

import struct
hi,lo = struct.unpack('>QQ',data)
print((hi << 64) + lo)

# 如果你试着将一个整数打包为字节字符串，那么它就不合适了，你会得到一个错误。 如果需要的话，你可以使用 int.bit_length() 方法来决定需要多少字节位来存储这个值。


#复数
print(complex(2, 4))
b = 3 - 5j
print(b)

print(b.real)
print(b.imag)
print(b.conjugate())



# 复数函数比如正弦、余弦或平方根 ==> numpy
import cmath

print(cmath.sin(a))


# 正无穷、负无穷或NaN(非数字)的浮点数

from fractions import Fraction
a = Fraction(5,4)
b = Fraction(7,16)
print(a+b)
print(a * b)

# 大型数组运算  你需要在大数据集(比如数组或网格)上面执行计算。
# 涉及到数组的重量级运算操作，可以使用 NumPy 库。 NumPy 的一个主要特征是它会给Python提供一个数组对象，相比标准的Python列表而已更适合用来做数学运算

x = [1,2,3,4]
y = [5,6,7,8]
# x+10.print()
c = x + y
print(c)
# d = x + 10
# print(d)

import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])

# ax * 2
# array([2, 4, 6, 8])
print(ax + ay)

# NumPy 还为数组操作提供了大量的通用函数，这些函数可以作为 math 模块中类似函数的替代
print(np.sqrt(9))
print(np.cos(0.1))

# 底层实现中， NumPy 数组使用了C或者Fortran语言的机制分配内存。 也就是说，它们是一个非常大的连续的并由同类型数据组成的内存区域。 所以，你可以构造一个比普通Python列表大的多的数组。 比如，如果你想构造一个10,000*10,000的浮点数二维网格
# NumPy 是Python领域中很多科学与工程库的基础，同时也是被广泛使用的最大最复杂的模块。 即便如此，在刚开始的时候通过一些简单的例子和玩具程序也能帮我们完成一些有趣的事情。
grid = np.zeros(shape=(10000,10000), dtype=float)
print(grid)
grid += 9
print(grid)
print(np.sin(grid))

# 关于 NumPy 有一点需要特别的主意，那就是它扩展Python列表的索引功能 - 特别是对于多维数组。
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[1])
print(a[:, 1])
print(a[1:3, 1:3])

# 矩阵与线性代数运算
# 执行矩阵和线性代数运算，比如矩阵乘法、寻找行列式、求解线性方程组等等
# 操作数组和向量的话， NumPy 是一个不错的入口点
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print(m)

# Return transpose
print(m.T)


# Return inverse
print(m.I)


# Create a vector and multiply
v = np.matrix([[2],[3],[4]])
print(v)

print(m * v)


import numpy.linalg

# Determinant
print(numpy.linalg.det(m))
## Determinant
print(numpy.linalg.eigvals(m))


#随机选择 random 模块使用 Mersenne Twister 算法来计算生成随机数。这是一个确定性算法， 但是你可以通过 random.seed() 函数修改初始化种子
# random模块还包含基于均匀分布、高斯分布和其他分布的随机数生成函数。 比如， random.uniform() 计算均匀分布随机数， random.gauss() 计算正态分布随机数
# random.uniform() 计算均匀分布随机数， random.gauss() # 计算正态分布随机数

import random
values = [1,2,3,4,5,6]
print(random.choice(values))
print(random.sample(values, 2))
print(random.sample(values, 3))
#仅仅只是想打乱序列中元素的顺序
values2 = [1,2,3,4,5,6]
print(random.shuffle(values2)) #None
print(values2)

print(random.random())

# 要获取N位随机位(二进制)的整数
print(random.getrandbits(200))

random.seed(3)

# 在 random 模块中的函数不应该用在和密码学相关的程序中。 如果你确实需要类似的功能，可以使用ssl模块中相应的函数。 比如， ssl.RAND_bytes() 可以用来生成一个安全的随机字节序列