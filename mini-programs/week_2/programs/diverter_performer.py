a = int(input())
b = int(input())
bl = True

while bl:
    if a < 2 * b:
        a -= 1
        print("-1")
    elif a % 2 == 0:
        a = a // 2
        print(":2")
    elif a % 2 == 1:
        a -= 1
        print("-1")
    if a == b:
        bl = False
