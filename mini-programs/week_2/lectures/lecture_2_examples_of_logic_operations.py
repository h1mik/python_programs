# example_1
n = int(input())
is_even = n % 2 == 0
print(is_even)

# example_2
start_1 = int(input())
finish_1 = int(input())
start_2 = int(input())
finish_2 = int(input())
is_s1_in2 = start_2 <= start_1 <= finish_2
is_f1_in2 = start_2 <= finish_1 <= finish_2
is_s2_in1 = start_1 <= start_2 <= finish_1
is_f2_in1 = start_1 <= finish_2 <= finish_1
answer = is_f1_in2 or is_f2_in1 or is_s1_in2 or is_s2_in1
print(answer)

# example_2 (version 2)
start_1 = int(input())
finish_1 = int(input())
start_2 = int(input())
finish_2 = int(input())
answer = start_1 <= finish_2 and start_2 <= finish_1
print(answer)