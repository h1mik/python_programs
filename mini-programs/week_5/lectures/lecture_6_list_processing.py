# example_1


a = list(map(int, input().split()))
i = 0
b = []

"""
while i < len(a):
    if a[i] % 2 != 0:
        a.pop(i)
    else: i += 1
print(*a)
"""
for now in a:
    if now % 2 == 0:
        b.append(now)
print(*b)

# example_2
numbers = list(map(int, input().split()))
newList = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        newList.append(numbers[i])
print(' '.join(map(str, newList)))
