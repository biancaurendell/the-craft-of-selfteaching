#目标是写一个判断是否闰年的程序
# # 假定都不是闰年，判断是否能除以4 满足上面条件后如果能被100整除但不能被400整除的就不是闰年
# def is_leap(year):
#     r = False
#     if year % 4 == 0:
#         r = True
#         if year % 100 ==0 :
#             if year % 400 !=0:
#                 r = False
#     return r
#
# print(is_leap(2001))
# print(is_leap(200))
# print(is_leap(220))
# print(is_leap(400))








# def is_leap(year):
#     s = False
#     if year % 4 == 0:
#         s = True
#         if year % 100 == 0 and year % 400 !=0:
#             #if year % 400 !=0:
#                 s = True
#     return s
#
# print(is_leap(40))
# print(is_leap(200))


def is_leap(year):
    if year % 4 and (year % 100 != 0 or year % 400 ==0 ):
        s = True
    else:
        s = False
    return s

print(is_leap(2004))









