import random
#
# n = 10
# a_list = [random.randrange(1, 100) for i in range(n)]
# print(f'a_list comprehends {len(a_list)} random numbers: {a_list}')
#
# b_list = [x for x in a_list if x % 2 == 0]
# print(f'... and it has has {len(b_list)} even numbers: {b_list}')


#列表的操作符
a_list = [1, 2, 3]
b_list = [4, 5, 6]
c_list = a_list + b_list * 3
print(c_list)
print(7 not in c_list)
print(a_list > b_list)


