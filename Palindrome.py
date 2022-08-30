#  Copyright (c) Vladimir Modenov.
#  Created: 30.08.2022, 15:04
#  Project: SkepikPythonWorks
#  File: Palindrome.py

# На вход программе подается одно слово, записанное в нижнем регистре. Напишите программу, которая определяет
# является ли оно палиндромом.

s = input().lower()
s_reverse = s[::-1]

if s == s_reverse:
    print("YES")
else:
    print("NO")
