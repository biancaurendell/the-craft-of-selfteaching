#列表可用的内建函数
#len()
#max()
#min()
import random
n = 3
#生成三个随机数，构成一个列表
a_list = [random.randrange(65, 91) for i in range(n)]
b_list = [chr(random.randrange(65, 91)) for i in range(n)]
print(a_list)
print(b_list)

#列表可以使用操作符 +和*
c_list = a_list + b_list + a_list * 2
print(c_list)

a_list *= 3
print(a_list)
#内建函数操作len() max() min()
print(len(c_list))
print(max(b_list))#内建函数内部做了异常处理，可以比较字符和数字 ——初学者最讨厌这种事情
print(min(b_list))# 注意，min() 和min() 应用的是b_list ,len()应用的是c_list ——

print('X' not in b_list)

#对列表进行Methods
a_list.sort()
print('the list sorted:\n', a_list)

a_list.sort(reverse=True) #reverse 参数默认是False
print('the list sorted reversely:\n', a_list)

