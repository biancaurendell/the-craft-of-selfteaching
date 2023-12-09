# x = 2025
# if x <= 1:
#     return False
# if x % 4 == 0:
#     if x % 100 == 0:
#         if x % 400 != 0:
#             print(f'{x} 是一个素数')
# else:
#     print(f'{x} 不是一个素数')
def is_leap_year(numbers):
    if numbers <= 1:
        return False
    if numbers % 4 == 0:
        if numbers % 100 != 0:
            return True
    return False
    if numbers % 400 == 0:
        return True
is_leap_year(2005)
    if True:
        print('是闰年')
    else:
        print('不是闰年')
