def exec_subtask4():
    str_numbers = '1234567890'
    str_number = input_numbers(str_numbers, 'integer')
    input_number = int(str_number)
    current_number = input_number
    max_number = 0
    while current_number > 0:
        check_number = current_number % 10
        if check_number > max_number:
            max_number = check_number
        current_number = current_number // 10
    print(f'Maximum digit in a number : {max_number}')


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
    exec_subtask4()