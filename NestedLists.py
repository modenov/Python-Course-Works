#  Copyright (c) Vladimir Modenov.
#  Created: 18.10.2022, 15:15
#  Project: SkepikPythonWorks
#  File: NestedLists.py

# Чему будет равно list1[1][1] после выполнения следующего фрагмента кода:

list1 = [[1] * 3] * 3
print(list1)
list1[0][1] = 5
print(list1)
print(list1[0][1])
print('-----')

a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
b = [[1] * 3] * 3
print('a =', a)
print('b =', b)
a[0][1] = 5
b[0][1] = 5
print('-----')
print('a =', a)
print('b =', b)
print('-----')

my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    maximum = max(row)
    minimum = min(row)

print(maximum + minimum)
print('-----')

my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    if max(row) > maximum:
        maximum = max(row)
    if min(row) < minimum:
        minimum = min(row)

print(maximum + minimum)
