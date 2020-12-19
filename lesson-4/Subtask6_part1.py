from itertools import count


def exec_subtask6_1():
    start_num = int(input_(text_dialog='Введите начальное значение'))
    for i in count(start=start_num, step=1):
        if float(i) % 1000 == 0:
            val = input_(str_numbers='', text_dialog="Для завершения работы введите q ")
            if val == "q":
                quit()
        print(i)


def input_(only_positive=True, str_numbers='1234567890', text_dialog=""):
    while True:
        str_value = input(f'{text_dialog} : ')
        if not str_numbers == '':
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
    exec_subtask6_1()
