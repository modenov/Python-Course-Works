#  Copyright (c) Vladimir Modenov.
#  Created: 04.10.2022, 13:43
#  Project: SkepikPythonWorks
#  File: Random.py

# Random method

import random

again = 'y'

while again.lower() == 'y':
    print('Бросаем кубики... ')
    print('Значения граней:', random.randint(1, 6), random.randint(1, 6))
    again = input('Бросить кубики еще раз? (y = да, n = нет): ')
