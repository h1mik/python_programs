n = 1
mx = 0
c = 0
while n != 0:
    n = int(input())
    if n == 0:
        break
    elif n > mx:
        c = mx
        mx = n
    elif n > c:
        c = n
print(c)
