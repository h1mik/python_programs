a = list(map(int, input().split()))
n = a[0]
for i in a[1:]:
    if i > n:
        print(i, end=' ')
    n = i
