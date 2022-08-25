#  Copyright (c) Vladimir Modenov.
#  Created: 11.08.2022, 15:16
#  Project: SkepikPythonWorks
#  File: NumberSequence4.py

# Напишите программу, которая выводит все числа от m до n включительно удовлетворяющие хотя бы одному из условий:
# число кратно 17;
# число оканчивается на 9;
# число кратно 3 и 5 одновременно.

m = int(input())
n = int(input())

for i in range(m, n + 1):
    if (i % 10 == 9) or (i % 17 == 0) or (i % 15 == 0):
        print(i)
