n = int(input())

print("+___ " * n, sep=" ")
for i in range(1, n + 1):
    print("|", i, " / ", sep="", end="")

print()
print("|__\\ " * n, sep=" ")
print("|    " * n, sep=" ")
