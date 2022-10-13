# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# вычисление произведения чисел
def mult_num(value):
    result = []
    mul = 1
    for i in range(0, value):
        mul *= i + 1
        result.append(mul)
        i += 1
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


number = n0_check(inp_check(input('введите число: ')))
print(f'N = {number} -> {mult_num(number)}')
