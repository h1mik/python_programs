a, b, c = int(input()), int(input()), int(input())
if a >= b and a >= c:
    a, c = c, a
if b >= a and b >= c:
    b, c = c, b
if c >= a and c >= b:
    c = c
if a >= b:
    b, a = a, b
print(a, b, c)
