#  Copyright (c) Vladimir Modenov.
#  Created: 04.10.2022, 14:10
#  Project: SkepikPythonWorks
#  File: AreaAndLength.py

# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает два
# значения: длину окружности и площадь круга, ограниченного данной окружностью.

from math import*

# объявление функции
def get_circle(radius):
    return 2*pi*radius, pi*(radius**2)


# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)
