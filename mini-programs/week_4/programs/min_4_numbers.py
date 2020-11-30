a = int(input())
b = int(input())
c = int(input())
d = int(input())


def min_four(a, b, c, d):
    res_1 = min(a, b)
    res_2 = min(c, d)
    return min(res_1, res_2)


print(min_four(a, b, c, d))
