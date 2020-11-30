import math


def MinDivisor(x):
    i = 2
    if x == 2:
        return "YES"
    while x % i != 0:
        i += 1
        if i > math.sqrt(x):
            return "YES"
    return "NO"


x = int(input())
print(MinDivisor(x))
