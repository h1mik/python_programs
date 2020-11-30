import math


def MinDivisor(x):
    i = 2
    while x % i != 0:
        i += 1
        if i > math.sqrt(x):
            return x
    return i


x = int(input())
print(MinDivisor(x))
