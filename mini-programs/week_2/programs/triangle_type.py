a = int(input())
b = int(input())
c = int(input())
d = max(a, b, c)
e = min(a, b, c)
f = a + b + c - d - e
if e + f > d:
    if d**2 == e**2 + f**2:
        print('rectangular')
    elif d**2 < e**2 + f**2:
        print('acute')
    elif d**2 > e**2 + f**2:
        print('obtuse ')
else:
    print('impossible')
