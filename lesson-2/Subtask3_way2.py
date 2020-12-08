def exec_subtask3():
    _dict_months = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: "Май", 6: 'Июнь', 7: 'Июль', 8: 'Август',
                    9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
    winter = [_dict_months.get(1), _dict_months.get(2), _dict_months.get(12)]
    spring = [_dict_months.get(3), _dict_months.get(4), _dict_months.get(5)]
    summer = [_dict_months.get(6), _dict_months.get(7), _dict_months.get(8)]
    while True:
        val = int(input_('123456789', "Введите номер месяца"))
        if 1 <= val <= 12:
            month = _dict_months.get(val)
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
