# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
#
# - 6782     -> 23
# - 0,56     -> 11
# - 187,6778 -> 44


def sum_num(value):
    sum = 0
    for i in value:
        sum += 0 if i == '.' or i == '-' else int(i)
    return sum


def check_input(value):
    while type(value) == str:
        try:
            float(value)
        except ValueError:
            print('Ошибка ввода!', end=' ')
            print(f'Требуется ввести число : ', end='')
            value = input()
        else:
            break
    return value


num = check_input(input('Введите вещественное число: '))
print(f'{num} -> {sum_num(num)}')