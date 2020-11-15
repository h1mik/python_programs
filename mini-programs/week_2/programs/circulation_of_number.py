n = int(input())
s = ""
if n < 10:
    print(n)
else:
    while True:
        s = s + str(n % 10)
        n = n // 10
        if n < 10:
            s = s + str(n)
            break
    print(s)
