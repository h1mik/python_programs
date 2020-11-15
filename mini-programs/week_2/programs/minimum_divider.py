n = int(input())
mind = True
i = 1
while mind:
    i += 1
    if n % i == 0:
        mind = False
print(i)
