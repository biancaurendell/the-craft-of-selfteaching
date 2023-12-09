#迭代
for i in range(2, 500, 67):
    print(i)
for 帅 in '曾璠宇最帅':
    print(帅)
# 列表，有序
a_list = []
a_list.append(1)
a_list.append(2)
print(a_list, f'has a length of {len(a_list)}')

b_list = list(range(1,9))
b_list.append(11)
print(b_list, f'has a length of {len(b_list)}.')

c_list = [2**x for x in range(8)]
print(c_list, f'has a length of {len(c_list)}.')


