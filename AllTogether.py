#  Copyright (c) Vladimir Modenov.
#  Created: 22.08.2022, 17:04
#  Project: SkepikPythonWorks
#  File: AllTogether.py

# Дано натуральное число. Напишите программу, которая вычисляет:
#     сумму его цифр;
#     количество цифр в нем;
#     произведение его цифр;
#     среднее арифметическое его цифр;
#     его первую цифру;
#     сумму его первой и последней цифры.

n = int(input())
sum_counter = 0
total_counter = 0
mul_counter = 1
arif = 0
last = n % 10

while n != 0:
    first_digit = n % 10
    sum_counter += first_digit
    total_counter += 1
    mul_counter = mul_counter * first_digit
    arif = sum_counter / total_counter
    n = n // 10

print(sum_counter)
print(total_counter)
print(mul_counter)
print(arif)
print(first_digit)
print(first_digit + last)
