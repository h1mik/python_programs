x = int(input())
i = x
k = 0
while x != 0:
    if x > i:
        k += 1
    i = x
    x = int(input())
print(k)
