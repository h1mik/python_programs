m = int(input())
sum = 0
p = 1
pp = 0
i = 1
bl = True
if m == 0:
    print(1)
else:
    while bl:
        sum = p + pp
        pp = p
        p = sum
        i += 1
        if m == sum:
            break
        elif m < sum:
            i = -1
            break
    print(i)
