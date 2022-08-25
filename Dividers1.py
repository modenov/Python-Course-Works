#  Copyright (c) Vladimir Modenov.
#  Created: 25.08.2022, 13:51
#  Project: SkepikPythonWorks
#  File: Dividers1.py

# На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит
# натуральное число из отрезка [a; b] с максимальной суммой делителей.

a = int(input())
b = int(input())
sum_count = 0
max_x = 0

for i in range(a, b + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += j
        if count >= sum_count:
            sum_count = count
            max_x = j

print(max_x, sum_count)
