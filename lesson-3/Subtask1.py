def exec_subtask1():
    val_1 = float(input_(only_positive=False, text_dialog="Введите делимое"))
    val_2 = 0
    while val_2 == 0:
        val_2 = float(input_(only_positive=False, text_dialog="Введите делитель (не равный нулю)"))
    val_result = divide_values(val_1, val_2)
    print(f'Результат: {val_result}')


def divide_values(val_1, val_2):
    return val_1 / val_2


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
    exec_subtask1()
