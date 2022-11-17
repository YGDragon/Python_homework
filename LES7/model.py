# импорт из файла
def read_file(filename: str) -> str:
    with open(filename, mode="r", encoding="utf-8") as file:
        txt = file.read()
    return txt


# экспорт в файл
def write_file(filename: str, data: str):
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(data)


# заполнение пустых строк
def full_empty(data: list) ->list:
    for i in range(len(data)):
        data[i] = '-' if data[i] == '' else data[i]
    return data


# перевод данных в CSV формат
def convert_to_csv(data: list) -> str:
    return ','.join(data)


# перевод данных из CSV
def convert_of_csv(data: str) -> list:
    return data.split(',')
