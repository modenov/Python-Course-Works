# Дано натуральное число n. Напишите программу, которая выводит таблицу умножения на n.

n = int(input())

for i in range(10):
    i = i + 1
    print(f"{n} x {i} = {n * i}")
