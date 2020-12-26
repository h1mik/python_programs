# example_1

a = 1
b = 2
c = 3
a, b, c = b, a, c
print(a, b, c)

# example_2
myRange = range(10)
print(tuple(myRange))

# example_3
print(tuple('abcde'))

# example_3

for color in ('red', 'green', 'yellow'):
    print(color, 'apple')

# example_4
for i in range(25):
    print(i, end=' ')

print()

# example_5
for i in range(10, 21):
    print(i, end=" ")
print()

# example_6
for i in range(10, 21, 2):
    print(i, end=" ")
print()

# example_7
for i in range(10, -1, -1):
    print(i, end=" ")
print()
print()

# example_8
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()
print()
print()

# example_8
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
