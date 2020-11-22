from math import floor

n = float(input())
a = floor(n)
b = n % a * 100
print(a, round(b), sep=" ")
