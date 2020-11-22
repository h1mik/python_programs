a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
delta = a * d - b * c
delta_x = e * d - b * f
delta_y = a * f - e * c
if (a == 0 and b == 0) or (c == 0 and d == 0):
    print(0)
if a == 1 and b != 1:
    print(1, b, e)
elif a != 1 and b == 1:
    print(1, a, e)
if c == 1 and d != 1:
    print(1, d, f)
elif c != 1 and d == 1:
    print(1, c, f)
x = delta_x / delta
y = delta_y / delta
print(x, y)

#  1x   +   2y    =  4
#  x   +   y    =
