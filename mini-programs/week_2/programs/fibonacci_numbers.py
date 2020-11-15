n = int(input())
sum = 0
p = 1
pp = 0
i = 1
if n == 1:
    print(1)
else:
    while i < n:
        sum = p + pp
        pp = p
        p = sum
        i += 1
    print(sum)
