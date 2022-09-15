#  Copyright (c) Vladimir Modenov.
#  Created: 15.09.2022, 17:33
#  Project: SkepikPythonWorks
#  File: SumsOfTwo.py

# На вход программе подается натуральное число n ≥ 2, а затем n целых чисел. Напишите программу, которая создает
# из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).

n = int(input())
myList = []
counter = 0

for i in range(n):
    number = int(input())
    counter += number
    myList.append(counter)
    counter = number

print(myList[1:])
