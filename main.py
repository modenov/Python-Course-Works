# this is file for short examples.

from requests import get

total = 0
for i in range(1, 6):
    total += i
    print(total, end='')
print()

s = 'All you need is love'
if 'love' in s:
    print('❤')
else:
    print('💔')


print(get('https://stepic.org/favicon.ico').headers['Server'])