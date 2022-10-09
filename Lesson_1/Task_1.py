"""
1. Напишите программу, которая принимает на вход цифру,
   бозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
"""


def check_day(value):
    num_list = ['1', '2', '3', '4', '5', '6', '7']
    while value not in num_list:
        print('Неверный ввод!')
        value = input('Введите номер дня недели: ')
    if value in num_list[5:]:
        print(f'{value} -> Выходной день')
    elif value in num_list[:-2]:
        print(f'{value} -> Невыходной день')


w_day = input('Введите номер дня недели: ')
check_day(w_day)
