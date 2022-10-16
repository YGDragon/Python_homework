"""
1. Задайте список из нескольких чисел.
   Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
   Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""


def inp_check(numb):
    while not numb.isdigit():
        print('ошибка ввода!')
        numb = input('-> повторный ввод длины списка: ')
    return numb


len_lst = int(inp_check(input('ввод длины списка: ')))
new_lst = []
neg_lst = []
for i in range(len_lst):
    from random import randint
    new_lst.append(randint(1, len_lst))
    if i % 2 != 0:
        neg_lst.append(new_lst[i])

print(f'список элементов -> {new_lst}')
print(f'на нечетных позициях элементы {neg_lst} -> ', end='')
print(f'их сумма равна {sum(neg_lst)}')
