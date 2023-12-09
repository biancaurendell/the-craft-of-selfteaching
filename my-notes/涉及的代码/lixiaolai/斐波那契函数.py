def fib_between(start, end):
    r = []
    a, b = 0, 1
    while a <end:
        if a >= start:
            r.append(a)
            #print(a, end= ' ')
        a, b = b, a + b
    return r

print(fib_between(100, 100000))

