"""
3. Задайте список из вещественных чисел.
   Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
   Пример:
   [1.1, 1.2, 3.1, 5, 10.01, 12.00] => 0.19
   Примечание:
   Обратите внимание на элемент 5 и и 12.0. Они не участвуют в процессе т.к. дробная часть ноль.
   В списке могут быть как числа float, так и числа int.
   Посмотрите на методы числа float, возможно пригодятся.
"""


# проверка ввода числа
def inp_check(numb):
    while not numb.isdigit():
        print('ошибка ввода!')
        numb = input('-> повторный ввод длины списка: ')
    return numb


len_lst = int(inp_check(input('ввод длины списка: ')))
new_lst = []
shot_lst = []
for i in range(len_lst):
    from random import uniform
    new_lst.append(round(uniform(1, 10), 2))
for el in new_lst:
    diff = round(el - int(el), 2)
    if diff > 0:
        shot_lst.append(diff)
high = round(max(shot_lst), 2)
low = round(min(shot_lst), 2)
print(f'исходный список => {new_lst}')
print(f'MAX = {high}, MIN = {low} -> {round((high - low), 2)}')
