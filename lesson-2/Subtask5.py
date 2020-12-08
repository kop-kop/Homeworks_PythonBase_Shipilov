def exec_subtask5():
    my_list = [7, 5, 3, 3, 2]
    while True:
        val = int(input_('123456789', "Введите число"))
        if not val in my_list:
            result_insert = False
            for i in range(0, len(my_list) - 1):
                if val > my_list[i]:
                    my_list.insert(i, val)
                    result_insert = True
                    break
            if not result_insert:
                my_list.append(val)
        else:
            my_list_reverse = my_list.copy()
            my_list_reverse.reverse()
            index_last = my_list_reverse.index(val)
            index_last = -1 if index_last == 0 else index_last * -1
            my_list.insert(index_last, val)
        print(my_list)


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
    exec_subtask5()
