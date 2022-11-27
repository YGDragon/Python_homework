# ввод номера действия
def do_it() -> str:
    return input(f'Выбор номера действия -> ')


# ввод поля и данных для поиска
def search_field() -> str:
    return input(f'Ввод поля для поиска -> ').capitalize()


# ввод поля и данных для поиска
def search_data() -> str:
    return input(f'Ввод данные для поиска? -> ').capitalize()


# ввод ID
def get_id() -> str:
    return input('Ввод id: ')


# ввод необходимости ID
def need_id() -> str:
    print('Вывод с id: Y / N ? -> ', end='')
    return input().capitalize()


# ввод данных записи
def get_data(entry: tuple) -> dict:
    return {key: input(f'{key}: ').capitalize() for key in entry[1:]}


# вывод всех записей из базы данных
def print_entry(data: list):
    for dct in data:
        lst = []
        for key, val in dct.items():
            lst.append(val)
        print(','.join(lst))


# вывод одной записи из базы данных
def print_one(data: dict):
    lst = []
    for key, val in data.items():
        lst.append(val)
    print(','.join(lst))


# вывод списка меню
def out_list(menu: tuple):
    print('*' * 20)
    for point in menu:
        print(point)
    print('*' * 20)


# вывод сообщения
def message(data: str):
    print(data)
