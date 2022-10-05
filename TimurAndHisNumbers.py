#  Copyright (c) Vladimir Modenov.
#  Created: 05.10.2022, 16:33
#  Project: SkepikPythonWorks
#  File: TimurAndHisNumbers.py

# Тимур загадал число от 1 до n. За какое наименьшее количество вопросов (на которые Тимур отвечает "больше" или
# "меньше") Руслан может гарантированно угадать число Тимура?

def guess_how(n):
    total = 0
    while n // 2 > 0:
        n -= n // 2
        total += 1
    return total


n = int(input())

print(guess_how(n))
