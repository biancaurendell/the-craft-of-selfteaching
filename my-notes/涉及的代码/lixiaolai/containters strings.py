import random
n = 10

a_list = [chr(random.randrange(65, 91)) for i in range(n)]
#chr()函数会返回指定ascii码的字符,ord('A')是65
print(f'a_list comprehends {len(a_list)} random string elements:\n', a_list)

a_list.sort()
print('the list sorted:\n', a_list)
a_list.sort()
print('the list sorted:\n', a_list)

print()

b_list = [chr(random.randrange(65, 95)) +\
             chr(random.randrange(97, 123))\
             for i in range(n)]#这里就是把两个字母给它加起来了而已，这里却看着如此复杂
print(f'b_list comprehends {len(b_list)} random string elements:\n', b_list)

b_list.sort()
print('the sorted:\n', b_list)
b_list.sort(key=str.lower, reverse=True)

print('the sorted reversely:\n', b_list)