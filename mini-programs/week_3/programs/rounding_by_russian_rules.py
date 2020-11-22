from math import floor, ceil

n = float(input())
a = floor(n)
b = n - a
if b < 0.5:
    print(floor(n))
else:
    print(ceil(n))
