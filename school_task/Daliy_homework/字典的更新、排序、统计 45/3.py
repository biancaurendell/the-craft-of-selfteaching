import math

n = 20
s = 0

for i in range(1, n+1):
    s = s + math.factorial(i)

print(f"The sum of factorials from 1 to {n} is: {s}")
