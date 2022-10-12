# 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
#
# - Для n=4 [2, 2.25, 2.37, 2.44]
# Сумма 9.06


def sequence(value):
    value = int(value)
    result = []
    sum = 0
    for i in range(1, value + 1):
        result.append(round((1 + 1 / i) ** i, 2))
        sum += result[i - 1]
        i += 1
    return result


def check_in(value):
    while type(value) == str:
        try:
            int(value)
        except ValueError:
            print('Ошибка ввода!', end=' ')
            print(f'Требуется ввести целое число : ', end='')
            value = input()
        else:
            break
    return int(value)


def check_neg(value):
    while value <= 0:
        print('Ошибка ввода!', end=' ')
        print(f'Введите положительное число: ', end='')
        value = input()
        value = check_in(value)
    return int(value)


num = check_neg(check_in(input('Введите число: ')))
print(f'Для n = {num} -> {sequence(num)}')
print(f'Сумма {sum(sequence(num))}')
