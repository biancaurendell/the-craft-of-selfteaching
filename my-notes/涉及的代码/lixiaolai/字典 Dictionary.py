phonebook = {'ann':6575, 'bob':8982, 'joe':2598, 'zoe':1225}
print(phonebook)
print(phonebook['bob'])

#更新某个元素
phonebook['joe'] = 5802
print(phonebook)

#添加元素
phonebook2 = {'john':9876, 'mike':5603, 'stan':6898, 'eric':7898}
phonebook.update(phonebook2)
print(phonebook)

#删除某个元素

del phonebook['ann']
print(phonebook)

#逻辑操作符
print('bob' in phonebook)
print(5982 in phonebook.values())

#可用来操作的内建函数
print(len(phonebook))
print(max(phonebook))
print(min(phonebook))
print(list(phonebook))
print(tuple(phonebook))
print(set(phonebook))
print(sorted(phonebook))
print(sorted(phonebook, reverse=True))

#常用Methods
phonebook3 = phonebook2.copy()
print(phonebook3)

phonebook3.clear()
print(phonebook3)

p = phonebook2.popitem()
print(p)

p = phonebook2.pop('adam',3538)
print(p)

p = phonebook2.get('adam', 3538)
print(p)

p = phonebook2.setdefault('adam',1518)
print(p)

#迭代各种容器中的元素
s = 'Python'
for i, c in enumerate(s):
    print(i, c)
for i, v in enumerate(range(3)):
    print(i, v)
L = ['ann', 'bob', 'joe', 'john', 'mike']
for i, L in enumerate(L):
    print(i, L)
t = ('ann', 'bob', 'joe', 'john', 'mike')
# for i, t in enumerate(t):
#     print(i, t)

# for i, t in enumerate(sorted(t)):
#     print(i, t)

# for i, t in enumerate(sorted(t, reverse=True)):
#     print(i, t)

# for i ,t in enumerate(reversed(t)):
#     print(i, t)

#同时迭代多个容器，zip

chars = 'abcdefghijklmnopqrstuvwxyz'
nums = range(1, 27)
for c, n in zip(chars, nums):
    print(f"Let's assume {c} represents {n}.")

#迭代字典中的元素

for key in phonebook:
    print(key, phonebook[key])


    
