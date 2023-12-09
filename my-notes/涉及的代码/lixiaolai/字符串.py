#age = input('please tell me your age:')#这里会报错，因为无法界定输入数据的类型。因为 age 是由 input() 传递过来的字符串
# age = int(input('please tell me your age:'))#这样就可，因为把输入的数据变为了Int类型
# if age <18:
#     print('I can not sell you dringks')
# else:
#     print('Have a nice dring!')

s = '曾璠宇最帅'
for char in s:
    print(s.index(char), char)

s = '曾璠宇最帅'
for i in range(len(s)):
    print(s[i])

#简介写法
for i in s:
    print(i)

#提取操作
print(s [1])
print(s[2:])
print(s[2:5])
print(s[3:5])
print(s[1:5:2])

#处理字符串的内建函数
# print(ord('\n'))
# print(ord('\t'))
# print(ord('\r'))
# print(chr(65))# 与ord()相对应的函数
# s =input('请照抄一遍这个数字 3.14:')
# print(int('3'))
# # int(s)这句会报错
# print(float(s) * 9)
# print(len(s))
# print(s*3)

# 处理字符串的Method
# 大小写转换

print('Now is better than never.'.upper())
# 在python命令行工具中，单个下划线，是个特殊变量
# 保存着最近的雨具或者表达式的结果
#上个cell执行过后，_中保存着'NOWIS BETTER THAN NEVER
#rint(_.lower())

print('\u0132'.lower())
print(len('\u0132'.lower()))

b = 'Now is better than never.'
print(b.capitalize())
print(b.title())

print(b.swapcase())
print(b.title())
print(b.title().swapcase())
print(s.encode()) #处理中文字符常用，转换成a码

print(s.lower().count('曾璠'))
print(s.lower().count('曾璠',3))
print(s.lower().count('曾璠',1, 2))

print('曾璠宇最帅 你想找哪个字():')
c = """Simple is better than comples.
Comples is better than complicated."""
print(c.lower().find('mpl'))
print(c.lower().find('mpl', 10))
print(c.lower().find('mpl', 10, 20))

#rfind的作用返回最后一次出现的地方位置，而find是返回第一次出现的位置
print('Example of str.rfind():')
print(c.lower().rfind('mpl'))
print(c.lower().rfind('mpl', 10))
print(c.lower().rfind('mpl', 10, 20))

#index作用与find()相同，但是如果没有找到的话会出发ValueError异常
print('Example of str.index():')
print(c.lower().index('mpl'))
print(c.lower().rindex('mpl'))

print(s.lower().endswith('.'))

print(s.lower().startswith('曾'))
print(s.lower().startswith('璠', 10))
print(c.lower().startswith('e',11, 20))

#endwith用法
print(c.lower().endswith('.'))
print(c.lower().endswith('.', 10))
print(c.lower().endswith('.', 10, 20))

#事先找是否有这个字符串

print('mpl' in s)

#能搜索，应该就能替换,str.replace()
print("c.lower().replace('mp', '[ ]', 2):\n")
print(c.lower().replace('mp', '[ ]', 2))

#替换tab的函数 str.expandtabs( tabsize=8),其实tab指的是\t
v = 'fdsfsdf        \t fhd\tfdsfjosdkf      '
print(v.expandtabs())
print(v.expandtabs(2))

#去除子字符

n = "\r \t Simple is better than complex.    \t \n"
print(n.strip())
m = 'Simple is better than complex.'
print(m.strip('six.p'))
print(m.strip('pSix.mle'))

# 拆分字符串
k = """Name,Age,Location
John,18,New York
Mike,22,San Francisco
Janny,25,Miami
Sunny,21,shanghai"""
print(k.splitlines())#返回成列表模式的方法函数

#还可以进行取出操作
r = k.splitlines()[2]
print(r)
print(r.split())
print(r.split(','))
#上一行也可以这么写
print(r.split(','))
#print(sep=',', maxsplit=1) 这里不能输出好像是Maxsplit是非法字符for print
r.split(sep=',', maxsplit=1)
r.split(sep=',', maxsplit=0)  # 0 次，即不拆分
r.split(sep=',', maxsplit=-1) # 默认值是 -1，拆分全部

#拼接字符串
o = ''
t = ['曾', '璠', '宇', '最', '帅']
print(s.join(t))
#这里输出结果为什么会是'曾曾璠宇最帅璠曾璠宇最帅宇曾璠宇最帅最曾璠宇最帅帅'

#字符串排版，将字符串居中放置——前提是设定整行的长度 'str.center(width[,fillchar])'

print(s.title().center(60))
print(s.title().center(60, '='))
print(s.title().center(2, '='))#如果宽度参数小于字符串长度，则返回原字符串

print(s.title().rjust(60))
print(s.title().rjust(60, '.'))

#将字符串靠左或靠右对齐放置
#str.ljust(width)
#str.rjust(width)

for i in range(1, 11):
    filename = str(i).zfill(3) + '.mp3'
    print(filename)

#格式化字符串
#指的是将特定变量插入字符串特定位置的过程，常用的Methods有两个，一个是str.format(),另一个是f-string
name = 'John'
age = 25
print('{} is {} yeaers old'.format(name, age))
# 两个连续使用的大括号，不被认为是占位符；且只打印出一对大括号
print('Are you {0}? :-{{+}}'.format(name))
#str.format()里可以直接写表达式
print('{} is a grown up? {}'.format(name, age >= 18))

#使用f-string
#f-string 和str.format()的功用差不多，知识写法简洁一些——在字符串便是之前加上一个字母f:
# https://docs.python.org/3/library/stdtypes.html#printf-style-bytes-formatting
# f-string

print(f'{name} is {age} years old.')
print(f'{name} is {age} years old.{age >= 18}')

#但是str.format()索引顺序可以任意指定
print("{1} is {0} years old.".format(name, age))

#字符串属性
print("'1234567890'.isalnum():", \
      '1234567890'.isalnum())
print("'abvdefghij'.isalpha()", \
      'abcdefghid'.isalpha())
print("'山巅一寺一壶酒'.isascii():", \
      '山巅一寺一壶酒'.isascii())
print("")
# 还有好几个，等下有空来慢慢敲







