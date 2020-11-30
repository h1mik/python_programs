# functions

def hypot(a, b):
    sqrSum = a ** 2 + b ** 2
    return sqrSum ** (1 / 2)


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def c_n_k(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


print(int(hypot(3, 4)))
print(factorial(5))
print(c_n_k(4, 2))
