# 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
#
# - Для n=4 [2, 2.25, 2.37, 2.44]
# Сумма 9.06


# формирование последовательности чисел
def sequence(value):
    value = int(value)
    result = []
    for i in range(1, value + 1):
        result.append(round((1 + 1 / i) ** i, 2))
    return result


# проверка ввода числа
def inp_check(value):
    while type(value) == str:
        try:
            int(value)
        except ValueError:
            print('Ошибка ввода!')
            print(f'-> требуется ввод целого числа: -> ', end='')
            value = input()
        else:
            break
    return int(value)


# проверка ввода числа
def n0_check(value):
    while value <= 0:
        print('Ошибка ввода!')
        print(f'-> требуется ввод числа > 0: -> ', end='')
        value = inp_check(input())
    return int(value)


num = n0_check(inp_check(input('ввод числа: ')))
print(f'для n = {num} -> {sequence(num)}')
print(f'сумма {sum(sequence(num))}')
