s = input()
a = s[:].find(' ')
word = s[a + 1:] + ' ' + s[:a]
print(word)
