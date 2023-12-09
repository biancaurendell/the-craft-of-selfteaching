def if_prime(num):
    if num <= 1:
        return False
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True



num = int(input("请输入一个整数:"))
if if_prime(num):
    print(f'{num}是一个素数')
else:
    print(f'{num}不是一个素数')