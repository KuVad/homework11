# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств
 
def enter_num(a):
    list_a = list()
    print("Введите числа набора: ")
    i = 0
    while i < a:
        x = int(input())
        list_a.append(x)
        i += 1
    return list_a


n = int(input("Введите количество чисел в первом наборе: "))
m = int(input("Введите количество чисел во втором наборе: "))

list_n = enter_num(n)
list_m = enter_num(m)

#print(list_n)
#print(list_m)

i, j = 0, 0
list_nm = list()
for i in range(len(list_n)):
    for j in range(len(list_m)):
        if list_m[j] == list_n[i]:
            list_nm.append(list_m[j])
        j += 1
    i += 1

#print(list_nm)

list_res = sorted(set(list_nm))
print(f"Числа, которые встречаются в обоих наборах: {list_res}")