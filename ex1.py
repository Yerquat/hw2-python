# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монеток: '))
print(n)
reshka = 0
orel = 1
i = 0
summa1 = 0
summa2 = 0
while (i < n):
    k = int(input(f'Введите 0 или 1: '))
    if k == 0:
        summa1 = summa1 + 1
    else:
        summa2 = summa2 + 1
    i = i + 1
print(f'решкой выпало {summa1} монет')
print(f'орлом выпало {summa2} монет')
if (summa1 > summa2):
    print(f'надо перевернуть {summa2}, выпавших орлом монет')
else:
    print(f'надо перевернуть {summa1}, выпавших решкой монет')