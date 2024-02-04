import random

n = random.randint(1,10)
u = int(input('угадай число '))
if u == n:
    print('молодец правильно')
else:
    print(f'не правильно, было загадано {n}')

