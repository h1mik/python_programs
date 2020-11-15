# example_1
x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)

# example_2
x = int(input())
# if x==1:
#     print("One")
# else:
#     if x==2:
#         print("Two")
#     else:
#         if x==3:
#             print("Three")
#         else:
#             print("Other")
if x == 1:
    print("One")
elif x==2:
    print("Two")
elif x==3:
    print("Three")
else:
    print("Other")

# example_3
# По заданному количеству глаз и ног нужно научиться отличать кошку, паука, морского гребешка и жучка.
# У морского гребешка бывает более сотни глаз, а у пауков их восемь.
# Также у пауков восемь ног, а у морского гребешка их нет совсем.
# У кошки четыре ноги, а у жучка – шесть ног, но глаз у обоих по два.
# Решение:
eyes = int(input())
legs = int(input())
if eyes >= 8:
    if legs == 8:
        print("spider")
    else:
        print("scallop")
else:
    if legs == 6:
        print("bug")
    else:
        print("cat")