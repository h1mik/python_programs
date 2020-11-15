i = 1
ii = 0
p = 0
n = int(input())
b = i
while n != 0:
    if n == p:
        i = i + 1
    if b == i:
        i = 1
    if i >= ii:
        ii = i
    p = n
    b = i
    n = int(input())
print(ii)
