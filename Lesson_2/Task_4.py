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
# проверка значений границ диапазона

# нахождение произведения элементов
# в ограниченном диапазоне
def n_mult(data):
    n = r_check(data)
    data_cut = data[n[0] : n[1] + 1]
    from math import prod
    print(f'Произведение для {data_cut} равно {prod(data_cut)}')
    

# формирование списка элементов
def lst_inp(num):
    from random import randint
    lst = [randint(-num, num) for i in range(-num, num + 1)]
    print(lst)
    return lst


def r_check(data):
    lst = [0, 0]
    lst[0] = inp_check(input('Нижняя граница: '))
    lst[1] = inp_check(input('Верхняя граница: '))
    while lst[0] >= lst[1]:
        print('Ошибка ввода!')
        lst[0] = inp_check(input('Нижняя граница: '))
    while (lst[1] > len(data) or lst[1] == 0):
        print('Ошибка ввода!')
        lst[1] = inp_check(input('Верхняя граница: '))
    return lst
    
# проверка числа при вводе
def inp_check(value):
    while (type(value) == str or int(value) < 0):
        try:
            int(value)
        except ValueError:
            print('Ошибка ввода!', end=' ')
            print(f'Требуется ввести целое положительное число : ', end='')
            value = input()
        else:
            break
    return int(value)


num = inp_check(input('Введите число: '))
n_mult(lst_inp(num))
