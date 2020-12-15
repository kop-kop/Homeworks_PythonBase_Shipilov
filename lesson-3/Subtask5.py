def exec_subtask5():
    stop = input_(text_dialog="Введите стоп-слово", str_numbers='')
    save_sum = 0
    while True:
        list_val = input_(
            text_dialog=f'Введите набор чисел через пробел. Для окончания операции введите стоп-слово "{stop}"',
            str_numbers='').split(" ")
        if len(list_val) == 1 and list_val[0] == stop:
            quit()
        current_sum = 0
        for element in list_val:
            if element == stop:
                break
            try:
                float_element = float(element)
                current_sum = float_element + current_sum
            except:
                break
        save_sum = current_sum + save_sum
        print(save_sum)


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
    exec_subtask5()
