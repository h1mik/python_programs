n = int(input())

sum = 0
mult = 1

for i in range(1, n + 1):
    mult *= i
    sum += mult

print(sum)
