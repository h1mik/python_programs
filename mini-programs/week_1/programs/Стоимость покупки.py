rub = int(input())
kop = int(input())
n = int(input())
sum = (rub * 100) + kop
total_sum = sum * n
print(total_sum // 100, total_sum % 100, sep=" ")
