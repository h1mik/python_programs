a = list(map(int, input().split()))
b = list()
c = list()
i = 0
# c = a[len(a) - 1]
if len(a) % 2 != 0:
    for i in range(0, len(a) - 1):
        b.append(a[i])
    i = 0
    while i < len(b) - 1:
        c.append(b[i + 1])
        c.append(b[i])
        i += 2
    c.append(a[len(a) - 1])
    print(*c)
elif len(a) % 2 == 0:
    while i < len(a) - 1:
        b.append(a[i + 1])
        b.append(a[i])
        i += 2
    print(*b)
