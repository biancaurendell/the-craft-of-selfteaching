admins = {'Moose', 'Joker', 'Joker'}
moderators = {'Ann', 'Chris', 'Jane', 'Moose', 'Zero'}

print(admins)# 去重操作
print('Joker' in admins)
print('Joker' in moderators)
print(admins | moderators) #并集
print(admins & moderators)#交集
print(admins - moderators)
print(admins ^ moderators)

#使用Mthods方法去维护
print(admins = {moderators})
print(admins.intersection(moderators))
print(admins.difference(moderators))
print(admins.symmetric_difference(moderators))

#逻辑运算

#更新
#add remove discard pop clear

#冻结集合

