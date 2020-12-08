def exec_subtask2():
    count = int(input_('1234567890', 'Enter how many items will be in the list'))
    _list = []
    for i in range(count):
        _list.append(input_('', f'Enter value #{i + 1}'))
    max_range_val = count if count / 2 == count // 2 else count - 1
    for i in range(0, max_range_val, 2):
        val1 = _list.pop(i)
        val2 = _list.pop(i)
        _list.insert(i, val2)
        _list.insert(i + 1, val1)
    print(_list)


def input_(str_numbers, text_dialog, only_positive=True):
    while True:
        str_value = input(f'{text_dialog} : ')
        if str_value == '':
            print("You didn't enter anything")
            continue
        elif not str_numbers == '':
            invalid_character = False
            if only_positive:
                for character in str_value:
                    if str_numbers.find(character) == -1:
                        print('You entered an invalid character')
                        invalid_character = True
                        break
            else:
                i = 0
                for character in str_value:
                    if str_numbers.find(character) == -1 and not (i == 0 and character == "-"):
                        print('You entered an invalid character')
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
