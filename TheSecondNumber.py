#  Copyright (c) Vladimir Modenov.
#  Created: 23.08.2022, 11:26
#  Project: SkepikPythonWorks
#  File: TheSecondNumber.py

# Дано натуральное число n (n > 9). Напишите программу, которая определяет его вторую (с начала) цифру.
#  На вход программе подается одно натуральное число, состоящее как минимум из двух цифр.

n = int(input())

while n > 9:
    last_digit = n % 10
    n = n // 10

print(last_digit)
