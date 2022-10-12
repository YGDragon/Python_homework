# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def mult_num(value):
    result = []
    mul = 1
    for i in range(0, value):
        mul *= i + 1
        result.append(mul)
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
print(f'N = {num} -> {mult_num(num)}')
