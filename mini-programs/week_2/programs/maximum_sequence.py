n = 1
mx = 0
while n != 0:
    n = int(input())
    if n == 0:
        break
    elif n > mx:
        mx = n
print(mx)
