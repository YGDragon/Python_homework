# функция проверки ввода
def check(num):
    while not num.isdigit():
        try:
            num = int(num)
        except ValueError:
            print(f'Ошибка ввода.', end=' ')
            num = input(f'Игрок попробуй еще раз: ')
    return int(num)


# функция проверки по количеству кофет
def min_max(num, limit0, limit1):
    while num == limit0 or num > limit1:
        print(f'Ошибка по количеству конфет!', end=' ')
        num = int(check(input(f'Попробуй еще раз: ')))
    return num
