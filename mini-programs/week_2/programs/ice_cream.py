n = int(input())
if n == 1 or n == 4:
    print("NO")
elif (n % 3 == 0) or (n % 5 == 0) or (n % 5 % 3 == 0) \
        or ((n % 5) + 5) % 3 == 0 or (n % 11 == 0):
    print("YES")
else:
    print("NO")
