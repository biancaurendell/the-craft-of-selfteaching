import random
n = 3
a_list = [random.randrange(65, 91) for i in range(n)]
b_list = [chr(random.randrange(65, 91)) for i in range(n)]
print(a_list)
c_list = a_list + b_list + a_list * 2
print(c_list)

#在末尾追加一个元素
c_list.append('100')
print(c_list)

#清空序列
print()
print(a_list)
a_list.clear()
print(a_list)

print()
#拷贝一个列表
d_list = c_list.copy()
print(d_list)
del d_list[6:8]
print(d_list)
print(c_list)

print()
#演示拷贝，.copy与赋值 = 的不同
e_list = d_list
del e_list[6:8]
print(e_list)
print(d_list)

#在末尾追加一个列表
print()
print(a_list)
a_list.extend(c_list)
print(a_list)

#在某索引位置插入一个元素

print()
print(a_list)
a_list.insert(1, 'example')
a_list.insert(3, 'exmple')
print(a_list)

#排序
print()
print(a_list)
a_list.reverse()
print(a_list)
x = a_list.reverse() #reverse()只对当前序列操作，并不返回一个逆序列表；返回值是None
print(x)

import random
n = 3
a_list = [random.randrange(65, 91) for i in range(n)]
print(a_list)

# 插入
print()
a_list.insert(1, 'example')   # 在索引 1 的位置插入 'example'

# 删除
print()
print(a_list)
a_list.remove('example')      # 去除 'example' 这个元素，如果有多个 'example'，只删除第一个
print(a_list)

# pop() 删除并返回被删除的值

print()
print(a_list)
p = a_list.pop(2)      # 去除索引为 2 的元素，且返回元素的值，赋值给 p
print(a_list)
print(p)

# pop() 与 del，或者 remove() 的区别
print()
a_list.insert(2, 'example')
a_list.insert(2, 'example')
print(a_list)
del a_list[2]
print(a_list)

print()
print(a_list.remove('example')) # a_list.remove() 这个 Method 的返回值是 None
print(a_list)