#  Copyright (c) Vladimir Modenov.
#  Created: 16.08.2022, 16:33
#  Project: SkepikPythonWorks
#  File: TheEndWord.py

# На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является
# слово «КОНЕЦ» (без кавычек). Напишите программу, которая выводит члены данной последовательности.

word = input()

while word != "КОНЕЦ":
    print(word)
    word = input()
