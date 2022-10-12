# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def n_mult(data):
    n = r_check(data)
    data_cut = data[n[0] : n[1] + 1]
    from math import prod
    print(f'индексы от {n[0]} до {n[1]} -> произведение для {data_cut} равно {prod(data_cut)}')
    
# формирование списка элементов
def lst_inp(num):
    from random import randint
    lst = [randint(-num, num) for i in range(-num, num + 1)]
    print(f'список элементов {lst}')
    return lst

# проверка ввода индексов
def r_check(data):
    lst = [0, 0]
    lst[0] = n1_check(inp_check(input('нижний индекс: ')))
    while lst[0] > len(data) - 1:
        print('Ошибка ввода!')
        lst[0] = n1_check(inp_check(input(f'- > требуется ввод нижнего индекса < {len(data)}: ')))
    lst[1] = n0_check(inp_check(input('верхний индекс: ')))
    while (lst[1] > len(data) or lst[0] >= lst[1] ):
        print('Ошибка ввода!')
        if lst[1] > len(data): print(f'- > требуется ввод верхнего индекса < {len(data)}', end='')
        elif lst[0] >= lst[1]: print(f'- > требуется ввод верхнего индекса > {lst[0]}', end='')
        lst[1] = n0_check(inp_check(input()))
    return lst
    
# проверка числа при вводе
def inp_check(value):
    while type(value) == str:
        try:
            int(value)
        except ValueError:
            print('Ошибка ввода!', end=' ')
            print('Требуется ввести целое число : ', end='')
            value = input()
        else:
            break
    return int(value)
    
    
def n0_check(value):
    while value <= 0:
        print('Ошибка ввода!', end=' ')
        print(f'Введите число > ноля: ', end='')
        value = inp_check(input())
    return int(value)


def n1_check(value):
    while value < 0:
        print('Ошибка ввода!', end=' ')
        print(f' Введите число >= 0: ', end='')
        value = inp_check(input())
    return int(value)

num = n0_check(inp_check(input('Введите число: ')))
n_mult(lst_inp(num))
