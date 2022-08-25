#  Copyright (c) Vladimir Modenov.
#  Created: 22.08.2022, 16:39
#  Project: SkepikPythonWorks
#  File: Max&Min.py

# Дано натуральное число n, (n ≥ 10). Напишите программу, которая определяет его максимальную и минимальную цифры.

# without while
n = int(input())
s = str(n)

print('Максимальная цифра равна', max(s))
print('Минимальная цифра равна', min(s))

# with while
n, x, m = int(input()), -1, 10

while n:
    x = max(x, n % 10)
    m = min(m, n % 10)
    n //= 10

print('Максимальная цифра равна', x)
print('Минимальная цифра равна', m)