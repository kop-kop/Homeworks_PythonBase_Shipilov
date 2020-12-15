def exec_subtask6():
    val_str = input_(text_dialog="Введите слово", str_numbers='')
    print(val_result(val_str))

def val_result(text):
    if len(text)>=1:
        return text[0].upper()+text[1:].lower()
    else:
        return "Что-то пошло не так"


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
    exec_subtask6()
