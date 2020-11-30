def summa():
    a = int(input())
    if a != 0:
        a = a + summa()
    return a


print(summa())
