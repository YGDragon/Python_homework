# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
#
# - 6782     -> 23
# - 0,56     -> 11
# - 187,6778 -> 44


# вычисление суммы цифр
def sum_num(value):
    sum = 0
    for i in value:
        sum += 0 if i == '.' or i == '-' else int(i)
    return sum


# проверка ввода числа
def check_input(value):
    while type(value) == str:
        try:
            float(value)
        except ValueError:
            print('Ошибка ввода!')
            print(f'-> требуется ввести число: -> ', end='')
            value = input()
        else:
            break
    return value


num = check_input(input('введите вещественное число: '))
print(f'{num} -> {sum_num(num)}')