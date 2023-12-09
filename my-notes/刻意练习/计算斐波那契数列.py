# def fibonacci_iterative(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

def fibonacci_iterative(n):
    if n <= 0:
        # print("输入数据有误")
        return "请输入一个正整数"
    if n > 0:
        a, b = 0, 1
        for _ in range(n):
            # c = b
            # b = a + b
            # a = c
            a, b = b, a + b
        return b





n = int(input("请输入一个整数:"))

print("第",n, '项的斐波那契数列的值是:',fibonacci_iterative(n))

