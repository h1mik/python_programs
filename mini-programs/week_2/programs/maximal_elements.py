n = 1
mx = 0
counter = 0
while n != 0:
    n = int(input())
    if n == mx:
        counter += 1
    if n == 0:
        break
    elif n > mx:
        mx = n
        counter = 1

print(counter)
