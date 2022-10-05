#  Copyright (c) Vladimir Modenov.
#  Created: 04.10.2022, 14:29
#  Project: SkepikPythonWorks
#  File: EquationRoots.py

# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты
# квадратного уравнения ax2+bx+c=0 и возвращает его корни в порядке возрастания.

# объявление функции
def solve(a, b, c):
    d = (b ** 2) - 4 * a * c
    x1 = ((-1 * b) - d ** 0.5) / (2 * a)
    x2 = ((-1 * b) + d ** 0.5) / (2 * a)

    return min(x1, x2), max(x1, x2)


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
