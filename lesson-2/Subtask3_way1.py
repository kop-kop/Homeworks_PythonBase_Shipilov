def exec_subtask3():
    _list_months = ['Январь', 'Февраль', 'Март', 'Апрель', "Май", 'Июнь', 'Июль', 'Август', "Сентябрь", "Октябрь",
                    "Ноябрь", "Декабрь"]
    winter = [_list_months[0], _list_months[1], _list_months[11]]
    spring = [_list_months[2], _list_months[3], _list_months[4]]
    summer = [_list_months[5], _list_months[6], _list_months[7]]
    while True:
        val = int(input_('123456789', "Введите номер месяца"))
        if 1 <= val <= 12:
            month = _list_months[val - 1]
            if month in winter:
                print('Зима')
            elif month in spring:
                print('Весна')
            elif month in summer:
                print("Лето")
            else:
                print("Осень")
            break
        else:
            print("Месяца с таким номером не существует. Попробуйте снова.")


def input_(str_numbers, text_dialog, only_positive=True):
    while True:
        str_value = input(f'{text_dialog} : ')
        if str_value == '':
            print("Вы ничего не ввели. Пустое значение не подходит.")
            continue
        elif not str_numbers == '':
            invalid_character = False
            if only_positive:
                for character in str_value:
                    if str_numbers.find(character) == -1:
                        print('Введен недопустимый символ. Попробуйте снова.')
                        invalid_character = True
                        break
            else:
                i = 0
                for character in str_value:
                    if str_numbers.find(character) == -1 and not (i == 0 and character == "-"):
                        print('Введен недопустимый символ. Попробуйте снова.')
                        invalid_character = True
                        break
                    i = i + 1
            if invalid_character:
                continue
            else:
                return str_value
        else:
            return str_value


if __name__ == '__main__':
    exec_subtask3()
