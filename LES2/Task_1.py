# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
## - 6782     -> 23
# - 0,56     -> 11
# - 187,6778 -> 44


# вычисление суммы цифр
def sum_num(value):
    result = 0
    for i in value:
        result += 0 if i == '.' or i == '-' else int(i)
    return result


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


number = check_input(input('введите вещественное число: '))
print(f'{number} -> {sum_num(number)}')
