a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
m1 = max(a1, b1, c1)
m2 = max(a2, b2, c2)
n1 = min(a1, b1, c1)
n2 = min(a2, b2, c2)
ser1 = a1 + b1 + c1 - m1 - n1
ser2 = a2 + b2 + c2 - m2 - n2
v1 = a1 * b1 * c1
v2 = a2 * b2 * c2
if m1 >= m2 and ser1 >= ser2:
    if v1 > v2 and not ((a2 - n1 > 0) and (b2 - n1 > 0) and (c2 - n1 > 0)):
        print("The first box is larger than the second one")
    elif v1 == v2:
        print("Boxes are equal")
    else:
        print("Boxes are incomparable")
elif m2 >= m1 and ser2 >= ser1:
    if v2 > v1 and not ((a1 - n2 > 0) and (b1 - n2 > 0) and (c1 - n2 > 0)):
        print("The first box is smaller than the second one")
    elif v1 == v2:
        print("Boxes are equal")
    else:
        print("Boxes are incomparable")
else:
    print("Boxes are incomparable")
