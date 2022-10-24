# функция записи строки в файл
def write_file(filename, row):
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write('\n' + '\n' + row)


# функция чтения строки из файла
def read_file(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        row = file.read()
    return row
