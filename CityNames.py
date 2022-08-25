# вычисляем самое длинное слово (город) и самое короткое
city1 = input()
city1_numb = len(city1)
city2 = input()
city2_numb = len(city2)
city3 = input()
city3_numb = len(city3)
minimum = min(city1_numb, city2_numb, city3_numb)
maximum = max(city1_numb, city2_numb, city3_numb)
if minimum == city1_numb:
    print(city1)
elif minimum == city2_numb:
    print(city2)
elif minimum == city3_numb:
    print(city3)
if maximum == city1_numb:
    print(city1)
elif maximum == city2_numb:
    print(city2)
elif maximum == city3_numb:
    print(city3)
