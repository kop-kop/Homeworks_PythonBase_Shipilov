def exec_subtask1():
    print('Please enter several values')

    # Input integer
    str_numbers = '1234567890'
    str_value = input_numbers(str_numbers, 'integer')
    int_value = int(str_value)

    # Input float
    str_numbers = '1234567890.'
    float_value = input_numbers(str_numbers, 'float')

    # Input string
    str_value = input_string()
    str_value2 = input_string('again')

    # Output results
    print(f'Wonderful! You have completed entering values.\n{int_value}\n{float_value}\n{str_value}\n{str_value2}')


def input_string(additional_sescription=''):
    while True:
        str_value = input(f'Entered string {additional_sescription}: ')
        if str_value == '':
            print("You didn't enter anything")
            continue
        else:
            return str_value


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
    exec_subtask1()