# 4. Задайте список из элементов, заполненных числами из промежутка [-N, N].
# Задайте два числа - позиции(индексы) в исходном списке это границы диапазона.
# Найдите произведение элементов списка в указанном диапазоне индексов
# Пример:
# N = 6
# Пример списка чисел: [-2, -5, 4, 1, 4, 1, 2, -5, -3, 0, -6, -6, 5]
# границы диапазона: 2, 5
# Произведение для [4, 1, 4, 1] равно 16
# Примечание: Границы диапазона вводятся пользователем, надо корректно учесть, что они могут быть некорректными:
# больше длины списка, меньше нуля, первый больше второго и т.п.


# формирование списка элементов
def lst_inp(n_lst):
    from random import randint
    lst = []
    for i in range(-n_lst, n_lst + 1):
        lst.append(randint(-n_lst, n_lst))
    print(f'список элементов {lst}')
    return lst


# нахождение произведения элементов списка
def n_mult(data):
    n = r_check(data)
    data_cut = data[n[0]: n[1] + 1]
    from math import prod
    print(f'индексы от {n[0]} до {n[1]} -> произведение для {data_cut} равно {prod(data_cut)}')


# проверка ввода индексов
def r_check(data):
    lst = [0, 0]
    # ввод нижнего индекса
    lst[0] = n1_check(inp_check(input('нижний индекс: ')))
    while lst[0] > len(data) - 1:
        print('Ошибка ввода!')
        lst[0] = n1_check(inp_check(input(f'- > требуется ввод нижнего индекса < {len(data)}: -> ')))
    # ввод верхнего индекса
    lst[1] = n0_check(inp_check(input('верхний индекс: ')))
    while (lst[0] >= lst[1] or lst[1] > len(data) - 1):
        print('Ошибка ввода!')
        if lst[1] > len(data) - 1:
            print(f'- > требуется ввод верхнего индекса < {len(data)} -> ', end='')
        elif lst[0] >= lst[1]:
            print(f'- > требуется ввод верхнего индекса > {lst[0]} -> ', end='')
        lst[1] = n0_check(inp_check(input()))
    return lst


# проверка ввода чисел
def inp_check(value):
    while type(value) == str:
        try:
            int(value)
        except ValueError:
            print('Ошибка ввода!')
            print('-> требуется ввод целого числа : ', end='')
            value = input()
        else:
            break
    return int(value)


# проверка ввода чисел
def n0_check(value):
    while value <= 0:
        print('Ошибка ввода!')
        print(f'-> требуется ввод числа > 0: -> ', end='')
        value = inp_check(input())
    return int(value)


# проверка ввода чисел
def n1_check(value):
    while value < 0:
        print('Ошибка ввода!')
        print(f'-> требуется ввод числа >= 0: ', end='')
        value = inp_check(input())
    return int(value)


num = n0_check(inp_check(input('введите число: ')))
n_mult(lst_inp(num))
