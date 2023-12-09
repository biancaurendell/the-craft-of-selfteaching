# s = '曾璠宇最帅'
# # for char in s:
# #     print(s.index(char), char)
#
# # print(b'www.example.com'.strip(b'cmowz.'))
# #
# # s = "www.google.com"
# # print(s.strip('gocow.'))
#
# for i in range(1, 11):
#     print(str(i).zfill(3).center(60) + ".mp3" )
#
# print(f'{s} is the best')
# print('{} is the best'.format(s))
#
# a_list =[2**x for x in range(8)]
# print(a_list, f'the length of {len(a_list)}')
import random
n = 3
a_list = [random.randrange(1, 100) for i in range(n)]
print(f'a_list comprehends {len(a_list)} random numbers: {a_list}')

b_list = [x for x in a_list if x % 2 == 0]
print(f'偶数是{b_list},长度是{len(b_list)}')

#那我写一个判断奇数的
c_list = [y for y in a_list if y % 2 != 0]
print(f'奇数是{c_list},长度是{len(c_list)}')

d_list = [chr(random.randrange(65, 91) for i in range(n))]
print(d_list)