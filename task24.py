# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном списке урожайности грядки.

from random import randint

bushes = int(input("Введите количество кустов: "))
list_berry = list(randint(1, 100) for _ in range(bushes))

print(list_berry)

i, maximum = 0, 0
for i in range(bushes):
    if i == 0:
        res = list_berry[0]+list_berry[1]+list_berry[-1]
        if res > maximum:
            maximum = res
    elif i == len(list_berry):
        res = list_berry[-2]+list_berry[-1]+list_berry[0]
        if res > maximum:
            maximum = res
    else:
        res = list_berry[i-2]+list_berry[i-1]+list_berry[i]
        if res > maximum:
            maximum = res
    i += 1

print(maximum)