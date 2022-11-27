import csv


# добавление записи в базу данных
def new_entry(filename: str,
              data: dict,
              fieldnames: tuple):
    with open(filename, mode='a', newline='', encoding='utf-8') as fl:
        f_wr = csv.DictWriter(fl, delimiter=',', lineterminator='\r', fieldnames=fieldnames)
        f_wr.writerow(data)


# определение следующего id
def next_id(filename: str) -> str:
    last_id = 0
    with open(filename, mode='r', newline='', encoding='utf-8') as fl:
        f_rd = csv.DictReader(fl, delimiter=',')
        for row in f_rd:
            if not row:
                num = 1
            else:
                num = int(row['id'])
            if num > last_id:
                last_id = num
    return str(last_id + 1)


# извлечение записи по id из базы данных
def get_entry(id_: str,
              nid: str,
              filename: str) -> dict:
    with open(filename, mode='r', newline='', encoding='utf-8') as fl:
        f_rd = csv.DictReader(fl, delimiter=',')
        for row in f_rd:
            if row['id'] == id_:
                if nid == 'N':
                    del row['id']
                    return row
                elif nid == 'Y':
                    return row


# обновление записи по id в базе данных
def update_entry(id_: str,
                 data: list,
                 new_data: dict,
                 filename,
                 fieldnames):
    for dct in data:
        if dct['id'] == id_:
            dct.update(new_data)
            break
    with open(filename, mode='w', newline='', encoding='utf-8') as fl:
        f_wr = csv.DictWriter(fl, delimiter=',', lineterminator='\r', fieldnames=fieldnames)
        f_wr.writeheader()
        f_wr.writerows(data)


# удаление записи по id в базе данных
def delete_entry(id_: str,
                 data: list,
                 filename: str,
                 fieldnames: tuple):
    for dct in data:
        if dct['id'] == id_:
            data.remove(dct)
            break
    with open(filename, mode='w', newline='', encoding='utf-8') as fl:
        f_wr = csv.DictWriter(fl, delimiter=',', lineterminator='\r', fieldnames=fieldnames)
        f_wr.writeheader()
        f_wr.writerows(data)


# Импорт базы данных
def import_db(filename: str,
              need_id: str) -> list:
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        f_reader = csv.DictReader(file, delimiter=',')
        data = []
        if need_id == 'N':
            for row in f_reader:
                del row['id']
                data.append(row)
        elif need_id == 'Y':
            data = list(f_reader)
        return data


# Экспорт базы данных
def export_db(need_id: str,
              data: list,
              fieldnames: tuple,
              db_name1='export_id.csv',
              db_name2='export.csv'):
    if need_id == 'Y':
        with open(db_name1, mode='w', newline='', encoding='utf-8') as file:
            f_writer = csv.DictWriter(file, delimiter=',', lineterminator='\r', fieldnames=fieldnames)
            f_writer.writeheader()
            f_writer.writerows(data)
    elif need_id == 'N':
        for dct in data:
            del dct['id']
        with open(db_name2, mode='w', newline='', encoding='utf-8') as file:
            f_writer = csv.DictWriter(file, delimiter=',', lineterminator='\r', fieldnames=fieldnames[1:])
            f_writer.writeheader()
            f_writer.writerows(data)


# поиск записей по базе данных
def select_db(field: str, search: str, filename: str) -> list:
    with open(filename, mode='r', newline='', encoding='utf-8') as fr:
        f_reader = csv.DictReader(fr, delimiter=',')
        data = []
        for row in f_reader:
            if search in row[field]:
                data.append(row)
        if not data:
            print('Данные не найдены!')
        return data


# проверка правильности ввода id
def check_id(id_: str) -> str:
    while not id_.isdigit():
        id_ = input('Неверный ввод id! Повторный ввод id -> ')
    else:
        return id_
