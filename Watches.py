#  Copyright (c) Vladimir Modenov.
#  Created: 24.08.2022, 12:11
#  Project: SkepikPythonWorks
#  File: Watches.py

# Сэмулируем часы несколькими циклами.

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)


