s = 'abcd abc abd'
print(s.rfind('abc'))
print(s.replace('abc', '1234'))
print(s.replace('abc', '1234', 1))
a = 'aaaaaa'
print(a.replace('aa', 'a'))

a = 'aaaaaa'
while a.find('aa') != -1:
    a = a.replace('aa', 'a', 1)
print(a)

a = 'aaaaaa'
s = 'abcdefabc'
print(a.count('aa', 1))
