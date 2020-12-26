a = [1, 2, 3, 4, 2, 2, 3]
a.append(5)
print(a.count(2))

print(a)
b = [5, 6]
a.extend(b)
a.remove(2)
b = a.copy()
a.insert(1, 999)
b.insert(2, 999)
# a.reverse()
a.pop()
print(a)
print(b)
