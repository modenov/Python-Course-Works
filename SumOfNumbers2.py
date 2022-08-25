#  Copyright (c) Vladimir Modenov.
#  Created: 19.08.2022, 14:20
#  Project: SkepikPythonWorks
#  File: SumOfNumbers2.py

# На вход программе подается последовательность целых чисел, каждое число на отдельной строке.
# Концом последовательности является любое отрицательное число.
# Напишите программу, которая выводит сумму всех членов данной последовательности.

n = int(input())
sum = 0

while n >= 0:
    sum = sum + n
    n = int(input())

print(sum)
