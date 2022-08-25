#  Copyright (c) Vladimir Modenov.
#  Created: 12.08.2022, 13:02
#  Project: SkepikPythonWorks
#  File: AmountOfNumbers.py

"""
На вход программе подаются два целых числа a и b (a ≤ b).
Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b включительно,
куб которых оканчивается на 4 или 9.
"""

a = int(input())
b = int(input())

counter = 0
for i in range(a, b + 1):
    if (i**3 % 10 == 4) or (i**3 % 10 == 9):
        counter = counter + 1
print(counter)