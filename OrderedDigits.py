#  Copyright (c) Vladimir Modenov.
#  Created: 23.08.2022, 14:00
#  Project: SkepikPythonWorks
#  File: OrderedDigits.py

# Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре
# справа налево упорядоченной по неубыванию.
# На вход программе подается одно натуральное число.

a = int(input())
flag = True
b = a % 10

while a != 0:
    n = a % 10
    if n < b:
        flag = False
    else:
        b = n
    a = a // 10

if flag == False:
    print("NO")
else:
    print("YES")
