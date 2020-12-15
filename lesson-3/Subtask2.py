def exec_subtask2():
    person_info = dict.fromkeys(["Имя", "Фамилия", "Год рождения", "Город проживания", "E-mail", "Телефон"])
    for key in person_info:
        person_info[key] = input_(only_positive=False, str_numbers='', text_dialog=key)
    person_info_str = str(person_info)
    print(person_info_str[1:len(person_info_str)-1])


def input_(only_positive=True, str_numbers='1234567890', text_dialog=""):
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
    exec_subtask2()
