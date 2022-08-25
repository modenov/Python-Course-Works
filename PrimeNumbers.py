#  Copyright (c) Vladimir Modenov.
#  Created: 25.08.2022, 17:03
#  Project: SkepikPythonWorks
#  File: PrimeNumbers.py

# На вход программе подается два натуральных числа a и b (a < b). Напишите программу, которая находит все
# простые числа от a до b включительно.

a = int(input())
b = int(input())

for i in range(a, b + 1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
