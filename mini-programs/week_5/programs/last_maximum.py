ls = list(map(int, input().split()))
max = 0
a = 0
max_id = 0
for i in ls:
    if i >= max:
        max = i
        max_id = a
    a += 1
print(max, max_id)
