n = int(input())
while n > 2:
    n = n / 2
if n % 2 == 0 or n == 1:
    print("YES")
else:
    print("NO")
