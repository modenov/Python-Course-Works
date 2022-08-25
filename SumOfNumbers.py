#  Copyright (c) Vladimir Modenov.
#  Created: 12.08.2022, 13:25
#  Project: SkepikPythonWorks
#  File: SumOfNumbers.py

"""
На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке.
Напишите программу, которая подсчитывает сумму введенных чисел.
"""

n = int(input())
total = 0

for i in range(n):
    num = int(input())
    total = total + num
print(total)
