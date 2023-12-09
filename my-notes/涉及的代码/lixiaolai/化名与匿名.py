#给函数取一个化名
def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
year_leap_bool = _is_leap
year_leap_bool
print(year_leap_bool(800))

print(id(year_leap_bool))
print(id(_is_leap))

#lab函数
# def add(x, y):
#     print( x + y )
# add(3, 5)
#使用lambda关键字写函数
add = lambda x, y: print(x + y)
add(3, 5)

#使用地点是什么呢
#就是用起来很简洁了的问题啊