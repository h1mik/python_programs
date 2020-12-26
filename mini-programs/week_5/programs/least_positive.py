ls = list(map(int, input().split()))
n = max(ls)

for i in ls:
    if 0 < i < n:
        n = i
print(n)
