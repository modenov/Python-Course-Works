#  Copyright (c) Vladimir Modenov.
#  Created: 30.08.2022, 16:57
#  Project: SkepikPythonWorks
#  File: TwoHalves.py

# На вход программе подается строка текста. Напишите программу, которая разрежет ее на две равные части, переставит
# их местами и выведет на экран.

s = input()
s_len = len(s)
s_index = (s_len // 2) + (s_len % 2)

print(s[s_index:] + s[:s_index])
