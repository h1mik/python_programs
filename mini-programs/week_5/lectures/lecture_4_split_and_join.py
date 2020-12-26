# example_1
a = list('abcde')
a[0] = 'f'
s = ''.join(a)
a = s[:]
print(a)

# example_2
"""
wordList = input().split(' ')
print(wordList)
"""

# example_3
intList = list(map(int, input().split()))
print(intList)
print(' '.join(map(str, intList)))
print(*intList)