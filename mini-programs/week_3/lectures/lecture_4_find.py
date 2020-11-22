s = "abcdef"
print(s[::-1])
print(len(s))
print(s[-2])
print(s[0:2])
print(s[::2])
a = 'abcd abc abd'
print(a.find('abc'))
pos = 0


while a.find('abc', pos) != -1:
    print(a.find('abc', pos))
    pos = a.find('abc', pos) + 1

string = input()
substring = input()
pos = string.find(substring)
while pos != -1:
    print(pos)
    pos = string.find(substring, pos + 1)