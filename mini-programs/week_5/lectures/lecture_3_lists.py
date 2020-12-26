# example_1
me_list = [1, 2, 3]
b = me_list[:]
me_list[0] = 4
print(b)
print(me_list)


# example_2
def replaceFirst(fList):
    fList[0] = 0


def reverse(fList):
    b = fList[::-1]
    fList = b[:]



a = [1, 2, 3]

reverse(a)
print(a)
