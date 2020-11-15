n = int(input())
i = 0
m = 1
while n >= m:
    anti_m = str()
    k = 1
    while k <= m:
        anti_m = anti_m + str((m % (k * 10)) // k)
        k = k * 10
    if str(m) == anti_m:
        i = i + 1
    m = m + 1
print(i)
