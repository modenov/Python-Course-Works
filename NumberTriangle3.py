#  Copyright (c) Vladimir Modenov.
#  Created: 25.08.2022, 12:04
#  Project: SkepikPythonWorks
#  File: NumberTriangle3.py

# Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой равной n,
# в соответствии с примером:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# ...

n = int(input())
num = 1

for row in range(1, n + 1):
    for column in range(1, row + 1):
        print(num, end=" ")
        num += 1
    print()
