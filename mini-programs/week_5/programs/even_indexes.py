# fun = input().split(' ')
#
# a = len(fun)
# if a % 2 == 0:
#     for i in range(0, a):
#         if i % 2 == 0:
#             print(fun[i], end=" ")
# elif a % 2 == 1:
#     for i in range(0, a + 1):
#         if i % 2 == 0:
#             print(fun[i], end=" ")
print(*input().split()[::2])