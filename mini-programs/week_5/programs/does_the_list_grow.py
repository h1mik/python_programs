def IsAscending(ls):
    i = 0
    a = True
    while i < (len(ls) - 1) and a == True:
        a = ls[i] > ls[i + 1]
        i += 1


ls = list(map(int, input().split()))
if IsAscending(ls):
    print("YES")
else:
    print("NO")
