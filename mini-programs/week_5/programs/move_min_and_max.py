ls = list(map(int, input().split()))
mx = max(ls)
mn = min(ls)
mx_id = ls.index(mx)
mn_id = ls.index(mn)
ls[mn_id], ls[mx_id] = ls[mx_id], ls[mn_id]
print(*ls)
