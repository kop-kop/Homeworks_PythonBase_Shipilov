def exec_subtask4():
    x = float(input_(only_positive=True, text_dialog="Введите положительное число для возведения в степень"))
    y = 0
    while (y >= 0):
        y = int(input_(only_positive=False, text_dialog="Введите отрицательное целое число"))
    val_result = my_func(x, y)
    print(val_result)


def my_func(x, y):
    res = 1
    for i in range(abs(y)):
        res = res / x
    return res


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
    exec_subtask4()
