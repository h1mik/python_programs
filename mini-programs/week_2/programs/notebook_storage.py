a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
v1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
v2 = (a1 // a2) * (b1 // c2) * (c1 // b2)
v3 = (a1 // b2) * (b1 // a2) * (c1 // c2)
v4 = (a1 // b2) * (b1 // c2) * (c1 // a2)
v5 = (a1 // c2) * (b1 // a2) * (c1 // b2)
v6 = (a1 // c2) * (b1 // b2) * (c1 // a2)
if v1 > v2:
    v2 = v1
if v2 > v3:
    v3 = v2
if v3 > v4:
    v4 = v3
if v4 > v5:
    v5 = v4
if v5 > v6:
    v6 = v5
print(v6)
