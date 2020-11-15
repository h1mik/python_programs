n = int(input())
i = 1
while n > 2:
    n = n / 2
    i += 1
if n == 1:
    print(0)
else:
    print(i)
