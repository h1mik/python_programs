a2, b2, c2 = int(input()), int(input()), int(input())
a1, b1 = int(input()), int(input())
m2 = max(a2, b2, c2)
n1 = min(a1, b1)
n2 = min(a2, b2, c2)

ser2 = a2 + b2 + c2 - m2 - n2
s1 = a1 * b1
s2 = n2 * ser2
if s1 >= s2 and (n1 >= n2):
    print("YES")
else:
    print("NO")
