def step(n):
    if n <= 0:
        print('请输入正整数')
    # a , b = 1 , 2
    result = 1
    for i in range(1 , n + 1):
        # a , b = 1 , 2
        # c = a
        # b = a*b
        # a = a + 1
        result *= i
    return result
n = int(input("请输入一个正整数:"))
print(step(n))