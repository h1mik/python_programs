# a = 1.234e10
# print(a)
# b = 2.0e-54
# print(b)

# x = float(input())
# y = float(input())
# print(x+y) #0.30000000000000004

if 0.1 + 0.2 == 0.3:
    print("YeS")
else:
    print("No")

# print(25.0 ** 100) #6.223015277861142e+139

print('{0:.25f}'.format(0.1))

print(float(2 ** 100).as_integer_ratio())
# 64         1(symbol)  11(exp) 52(mantissa)
print(11 % 2.5)
x = 0.1
print('{0:.25f}'.format(x))
x = float(input())
y = float(input())
epsilon = 10 ** -6
if abs(x - y) < epsilon:
    print('Equal')
else:
    print('Not equal')