#  Copyright (c) Vladimir Modenov.
#  Created: 12.08.2022, 16:28
#  Project: SkepikPythonWorks
#  File: AsymptoticApproximation.py

# На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения.

from math import log

n = int(input())
num = 0

for i in range(1, n + 1):
    num += (1 / i)
    num2 = num - log(n)
print(num2)
