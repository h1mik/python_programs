a, b, c = int(input()), int(input()), int(input())
if (a == b) and (a == c) and (b == c):
    print(3)
elif ((a == b) or (a == c)) and ((a != b) or (a != c)):
    print(2)
elif ((b == a) or (b == c)) and ((b != a) or (b != c)):
    print(2)
elif ((c == a) or (c == b)) and ((c != a) or (c != b)):
    print(2)
elif (a != b) and a != c and c != b:
    print(0)
