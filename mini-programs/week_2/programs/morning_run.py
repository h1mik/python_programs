x = int(input())
y = int(input())
i = 1
if x >= y:
    print(1)
else:
    while x < y:
        x = x * 1.1
        i += 1
    print(i)
