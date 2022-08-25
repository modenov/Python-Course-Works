#  Copyright (c) Vladimir Modenov.
#  Created: 25.08.2022, 16:00
#  Project: SkepikPythonWorks
#  File: SumOfFactorials.py

# Дано натуральное число n. Напишите программу, которая выводит значение суммы 1! + 2! + 3! + … + n!.

num = int(input())
total = 0
factorial = 1

for i in range(1, num + 1):
    for j in range(1, i + 1):
        factorial *= j
    total += factorial
    factorial = 1
print(total)
