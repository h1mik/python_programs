# example_1

now = int(input())
sumSeq = now
while now != 0:
    now = int(input())
    sumSeq += now
print(sumSeq)

# example_2

now = int(input())
while now != 0:
    if now > 0:
        print(now)
    now = int(input())

# example_3

now = -1
while now != 0:
    now = int(input())
    if now <= 0:
        continue
    print(now)