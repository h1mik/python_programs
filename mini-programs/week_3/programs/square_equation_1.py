a = float(input())
b = float(input())
c = float(input())

des = b ** 2 - 4 * a * c
sqrt_des = des ** (0.5)
if des < 0:
    print()
if des == 0:
    print(((-1 * b) / (2 * a)))
if des > 0:
    x1 = (((-1 * b) + sqrt_des) / (2 * a))
    x2 = (((-1 * b) - sqrt_des) / (2 * a))
    sorted([x2, x1])
    if a > 0:
        print(x2, x1)
    elif a < 0:
        print(x1, x2)
