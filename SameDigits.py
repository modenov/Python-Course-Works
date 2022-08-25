#  Copyright (c) Vladimir Modenov.
#  Created: 23.08.2022, 11:40
#  Project: SkepikPythonWorks
#  File: SameDigits.py

# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
# На вход программе подается одно натуральное число.
# Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.

n = input()

mini = min(n)
maxi = max(n)

if mini == maxi:
    print("YES")
else:
    print("NO")
