#  Copyright (c) Vladimir Modenov.
#  Created: 19.08.2022, 14:47
#  Project: SkepikPythonWorks
#  File: PayTheWitcher.py

# Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево, к тому же ведьмак
# не принимает купюры, он принимает только чеканные монеты. В мире ведьмака существуют монеты
# с номиналами 1,5,10,25.
# Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.

n = int(input())
counter = 0

while n >= 25:
    counter += 1
    n = n - 25

while n >= 10:
    counter += 1
    n = n - 10

while n >= 5:
    counter += 1
    n = n - 5

while n >= 1:
    counter += 1
    n = n - 1

print(counter)
