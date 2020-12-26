ls = list(map(int, input().split()))
n = int(input())
ls.append(0)
if n > ls[0]:
    print(1)
else:
    for i in range(0, (len(ls)) - 1):
        if ls[i] >= n > ls[i + 1]:
            print(i + 2)
            break
