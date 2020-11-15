# example_1

i = 0
while i <= 100:
    print(i, end=" ")
    i += 10
print("!")

# example_2

now = int(input())
maxn = now
while now != 0:
    now = int(input())
    if now == 0:
        break
    if now > maxn:
        maxn = now
print(maxn)
# while - else(not "break")