s = input()
a = s[:].find('f')
b = s.rfind('f')
c = s[a + 1:].find('f')

if a == -1:
    print(-2)
elif a == b:
    print(-1)
else:
    print(a + 1 + c)
