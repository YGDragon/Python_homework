# выбор действия из меню
def select_menu(menu: tuple) -> str:
    print('_'*20)
    for op in menu:
        print(f'{op}')
    print('_'*20)
    action = input(f'Какое действие выполнить? -> ')
    return action


# получение данных от пользователя
def get_data(entry: tuple) -> list:
    return [input(f'{fld}: ') for fld in entry]


# вывод результата
def print_data(data: list):
    print('Импортированные данные')
    print(data)
