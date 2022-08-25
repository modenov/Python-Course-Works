#  Copyright (c) Vladimir Modenov.
#  Created: 25.08.2022, 13:33
#  Project: SkepikPythonWorks
#  File: NumberTriangle4.py

# Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой равной n,
# в соответствии с примером:
# 1
# 121
# 12321
# 1234321
# 123454321
# ...

n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")

    for k in range(i, 1, -1):
        print(k - 1, end="")
    print()
