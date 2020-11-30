def perimeter_triangle(x1, y1, x2, y2, x3, y3):
    res_1 = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    res_2 = (((x3 - x2) ** 2) + ((y3 - y2) ** 2)) ** 0.5
    res_3 = (((x1 - x3) ** 2) + ((y1 - y3) ** 2)) ** 0.5
    return res_1 + res_2 + res_3


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

print(perimeter_triangle(x1, y1, x2, y2, x3, y3))
