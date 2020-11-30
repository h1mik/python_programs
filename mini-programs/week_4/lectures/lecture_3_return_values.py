# example_1

def max2(a, b):
    if a > b:
        return a
    else:
        return b


def max3(a, b, c):
    return max2(max(a, b), c)


def sort2(a, b):
    if a < b:
        return a, b
    return b, a


def isEven(n):
    return n % 2 == 0


print(max2(2, 5))
print(max2(7, 3))
print(max2(2, 2))
print(max3(6, 7, 3))
print(sort2(7, 5))
minim, maxim = sort2(8, 9)
print(minim, maxim)
print(isEven(6))
n = int(input())
if isEven(n):
    print('EVEN')
else:
    print('ODD')