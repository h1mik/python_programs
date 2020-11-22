s = input()
a = s[:].find('h')
b = s.rfind('h')
print(s[:b], s[a + 1:], sep="")
