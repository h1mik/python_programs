p = 100 + int(input())
x = int(input())
y = int(input())
k = int(input())
i = 0
num = (x * 100 + y)
while i < k:
    num = int(num * p / 100)
    i += 1
print((num // 100), (num % 100), sep=" ")
print(112 // 100)
