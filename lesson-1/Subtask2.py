def exec_subtask2():
    str_numbers = '1234567890'
    str_seconds = input_numbers(str_numbers, 'seconds')
    seconds = int(str_seconds)
    hours = (seconds // 3600) % 24
    minutes = (seconds // 60) % 60
    seconds = seconds % 60
    print(f'{hours}:{minutes}:{seconds}')


def input_numbers(str_numbers, type_of_value):
    while True:
        str_value = input(f'Enter an {type_of_value} : ')
        if str_value == '':
            print("You didn't enter anything")
            continue
        else:
            invalid_character = False
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


if __name__ == '__main__':
    exec_subtask2()