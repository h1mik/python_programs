s = input()
print(s[::3].replace('', ''))
a = len(s)
i = 1
for i in range(10):
    if i % 3 == 0:
        s[i].replace('','')
print(s, end="")
