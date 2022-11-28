# проверки ввода игрока
def check(num):
    while not num.isdigit():
        try:
            num = int(num)
        except ValueError:
            print(f'Ошибка ввода числа.', end=' ')
            num = input(f'Игрок попробуй еще раз: ')
    return int(num)


# проверки ввода количества конфет
def min_max(num, l_min, l_max):
    while num <= l_min - 1 or num > l_max:
        print(f'Ошибка ввода количества конфет!', end=' ')
        num = int(check(input(f'Попробуй еще раз: ')))
    return num
