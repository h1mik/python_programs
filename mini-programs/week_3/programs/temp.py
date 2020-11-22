from math import sqrt

a = []
while True:
    n = int(input())
    if n == 0:
        break
    a.append(n)
s = sum(a) / len(a)
count = 0
for i in range(len(a)):
    count += (a[i] - s) ** 2
count /= len(a) - 1
print(sqrt(count))
