# #创建元组
# a = (1, 2, 3)
# print(a)
# b = 45,
# print(b)#末尾的逗号意味着这就是第一个元组
# #元组的不可变是目前有的部分不可变

# a = 1,
# print(a)
# print(id(a))
# a += 3, 5
# print(a)
# print(id(a))

n = 1000
a = range(n)
b = tuple(a)
c = list(a)
print(a.__sizeof__())
print(b.__sizeof__())
print(c.__sizeof__())
