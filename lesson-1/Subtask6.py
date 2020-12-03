def exec_subtask6():
    str_numbers = '1234567890.'
    km = float(input_numbers(str_numbers, 'kilometers'))
    target_km = float(input_numbers(str_numbers, 'target kilometers'))
    days = 1
    progress = km
    progress_percent = 10
    while progress < target_km:
        progress = progress * (1 + (progress_percent / 100))
        days = days + 1
    result_days = int(days)
    print(f'на {result_days}-й день спортсмен достиг результата — не менее {target_km} км.')


def input_numbers(str_numbers, type_of_value):
    while True:
        str_value = input(f'Enter an {type_of_value} : ')
        if str_value == '':
            print("You didn't enter anything")
            continue
        else:
            invalid_character = False
            for character in str_value:
                if str_numbers.find(character) == -1:
                    print('You entered an invalid character')
                    invalid_character = True
                    break
            if invalid_character:
                continue
            else:
                return str_value


if __name__ == '__main__':
    exec_subtask6()