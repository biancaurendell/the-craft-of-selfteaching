#根据索引提取列表元素
import random
n = 3
a_list = [random.randrange(65, 91) for i in range(n)]
b_list = [chr(random.randrange(65, 91)) for i in range(n)]
print(a_list)
c_list = a_list + b_list + a_list * 2
print(c_list)

print()
#根据索引提取
print(c_list[3])
print(c_list[:])
print(c_list[5:])
print(c_list[:3])
print(c_list[2:6])

print()
#根据索引删除
del c_list[3]
print(c_list)
del c_list[5:8]
print(c_list)

print()
#根据索引替换
c_list[1:5:2] = ['a', 2] #s[start:stop:step] = t ,跟range的三个参数类似

print(c_list)
#列表List 是可变序列，而字符串str是不可变序列，所以，对字符串来说，索然也可以根据索引提取，但是没办法根据索引删除或者替换

s = 'Python'[2:5]
print(s)

s = 'Python'
L = list(s)
print(s)
print(L)
del L[2]
print(L) # 用 del 对 L 操作之后，L 本身少了 1 个元素
