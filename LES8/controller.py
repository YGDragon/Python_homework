import model
import view

# действия в меню
acts = ('0.EXIT',
        '1.CREATE',
        '2.READ',
        '3.UPDATE',
        '4.DELETE',
        '5.IMPORT DB',
        '6.EXPORT DB',
        '7.SELECT'
        )

entry = ('id',
         'Фамилия',
         'Имя',
         'Отдел'
         )

# список информационных сообщений
text = ['Программа остановлена',  # 0
        'Создана новая запись',  # 1
        'Запись по id:',  # 2
        'Запись по id обновлена',  # 3
        'Запись по id удалена',  # 4
        'Импортированные записи:',  # 5
        'База данных экспортирована:',  # 6
        'Результат поиска: ']  # 7


def actions(base):
    view.out_list(acts)
    act = view.do_it()
    if act not in [str(i) for i in range(0, len(acts))]:
        act = '0'
    while act:
        # выход из программы
        if act == '0':
            view.message(text[0])
            break
        # добавление новой записи в базу данных
        elif act == '1':
            user_data = view.get_data(entry)
            user_data['id'] = model.next_id(base)
            model.new_entry(
                base, user_data, entry
            )
            view.message(text[1])
            return actions(base)
        # извлечение записи по id из базы данных
        elif act == '2':
            user_id = model.check_id(
                view.get_id()
            )
            data = model.get_entry(
                user_id, view.need_id(), base
            )
            view.message(text[2])
            view.print_one(data)
            return actions(base)
        # обновление записи по id в базе данных
        elif act == '3':
            user_id = model.check_id(
                view.get_id()
            )
            data = model.import_db(base, 'Y')
            model.update_entry(
                user_id, data, view.get_data(entry), base, entry
            )
            view.message(text[3])
            return actions(base)
        # удаление записи по id в базе данных
        elif act == '4':
            user_id = model.check_id(
                view.get_id()
            )
            data = model.import_db(base, 'Y')
            model.delete_entry(
                user_id, data, base, entry
            )
            view.message(text[4])
            return actions(base)
        # импорт базы данных в консоль
        elif act == '5':
            data = model.import_db(base, view.need_id())
            view.message(text[5])
            view.print_entry(data)
            return actions(base)
        # экспорт базы данных в csv
        elif act == '6':
            model.export_db(
                view.need_id(), model.import_db(base, 'Y'), entry
            )
            view.message(text[6])
            return actions(base)
        # поиск записей по базе данных
        elif act == '7':
            view.out_list(entry[1:])
            field = view.search_field()
            search = view.search_data()
            view.message(text[7])
            view.print_entry(
                model.select_db(field, search, base)
            )
            return actions(base)
