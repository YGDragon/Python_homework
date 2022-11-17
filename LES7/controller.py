import model
import view

menu = ('1.Новая запись',
        '2.Импорт из файла',
        '3.Экспорт в файл',
        '4.Остановить программу'
        )
entry = ('Фамилия',
         'Имя',
         'Телефон',
         'Описание'
         )


def actions(imp_data):
    act = view.select_menu(menu)
    while act:
        if act == '1': # новая запись
            user = view.get_data(entry)
            full = model.full_empty(user)
            txt = model.convert_to_csv(full)
            model.write_file(input('Файл экспорта: ') + '.csv', txt)
            return actions(imp_data)
        elif act == '2': # импорт данных в файл
            txt = model.read_file(input('Файл импорта: ') + '.csv')
            imp_data = model.convert_of_csv(txt)
            view.print_data(imp_data)
            return imp_data, actions(imp_data)
        elif act == '3': # экспорт данных в файл
            txt = model.convert_to_csv(imp_data)
            model.write_file(input('Файл экспорта: ') + '.csv', txt)
            return actions(imp_data)
        elif act == '4': # выход из программы
            print('Программа остановлена')
            break
