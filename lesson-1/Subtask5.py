def exec_subtask5():
    str_numbers = '1234567890.'
    str_number = input_numbers(str_numbers, 'charge')
    charge = int(str_number)
    str_number = input_numbers(str_numbers, 'proceeds')
    proceeds = int(str_number)
    profit = proceeds - charge
    if profit >= 0:
        print(f'Total profit : {profit}')
    elif profit < 0:
        print(f'The loss was : {-profit}')
    if not proceeds == 0:
        profitability = profit / proceeds
    else:
        profitability = 0
    print(f'Profitability : {profitability}')
    str_number = input_numbers(str_numbers, 'amount of employees')
    amount_of_employees = int(str_number)
    if amount_of_employees > 0:
        profit_per_employee = profit / amount_of_employees
    else:
        profit_per_employee = 0
    print(f'Profit per employee : {profit_per_employee}')


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
    exec_subtask5()