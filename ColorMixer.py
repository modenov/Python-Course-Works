# Напишите программу, которая считывает названия двух основных цветов для смешивания.
# На вход программе подаются две строки, каждая на отдельной строке.

color1 = input()
color2 = input()

if ((color1 == "красный") or (color1 == "зеленый") or (color1 == "желтый") or (color1 == "синий")) and ((
        color2 == "красный") or (color2 == "зеленый") or (color2 == "желтый") or (color2 == "синий")):
    if color1 == color2:
        print(color1)
    elif ((color1 == "красный") and (color2 == "синий")) or ((color1 == "синий") and (color2 == "красный")):
        print("фиолетовый")
    elif ((color1 == "красный") and (color2 == "желтый")) or ((color1 == "желтый") and (color2 == "красный")):
        print("оранжевый")
    elif ((color1 == "синий") and (color2 == "желтый")) or ((color1 == "желтый") and (color2 == "синий")):
        print("зеленый")
else:
    print("ошибка цвета")
