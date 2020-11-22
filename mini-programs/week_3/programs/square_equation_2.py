a = float(input())
b = float(input())
c = float(input())

des = b ** 2 - 4 * a * c
sqrt_des = des ** 0.5
if a == 0 and b != 0:
    print(1, (-1 * c) / b)
elif a == 0 and b == 0 and c == 0:
    print(3)
elif des < 0 or (a == 0 and b == 0 and c != 0):
    print(0)
elif des == 0:
    print(1, ((-1 * b) / (2 * a)))
elif des > 0:
    x1 = (((-1 * b) + sqrt_des) / (2 * a))
    x2 = (((-1 * b) - sqrt_des) / (2 * a))
    sorted([x2, x1])
    if a > 0:
        print(2, x2, x1)
    elif a < 0:
        print(2, x1, x2)
