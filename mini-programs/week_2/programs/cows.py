number = int(input())
if number % 10 == 1 and (number != 11):
    print(number, 'korova', sep=" ")
elif (number % 10 == 0) or (number % 10 == 5):
    print(number, 'korov', sep=" ")
elif (number % 10 == 6) or (number % 10 == 7):
    print(number, 'korov', sep=" ")
elif (number % 10 == 8) or (number % 10 == 9) or (20 >= number >= 5):
    print(number, 'korov', sep=" ")
else:
    print(number, 'korovy', sep=" ")
