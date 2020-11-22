n = int(input())
x = float(input())
i = 0
res = 0
while n >= i:
    a = float(input())
    res += (a * (x ** n))
    n -= 1
print(res)
