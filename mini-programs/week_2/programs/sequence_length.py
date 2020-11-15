counter = -1
n = 1
while n != 0:
    n = int(input())
    counter += 1
while True:
    n = input()
    if n == "":
        break
print(counter)
