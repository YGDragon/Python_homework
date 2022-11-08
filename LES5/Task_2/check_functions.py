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
def min_max(num, lim0, lim1):
    while num <= lim0 - 1 or num > lim1:
        print(f'Ошибка по количеству конфет!', end=' ')
        num = int(check(input(f'Попробуй еще раз: ')))
    return num
