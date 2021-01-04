
from shipilov import input_

class Error_divide_by_zero(Exception):

        def __init__(self,value):
            self.message = f'Нельзя произвести деление {value} на ноль.'

        def __str__(self):
            return self.message

def exec_subtask2():

    while True:
        value1 = int(input_(str_numbers='1234567890',only_positive=False,text_dialog="Введите делимое"))
        value2 = int(input_(str_numbers='1234567890', only_positive=False, text_dialog="Введите делитель"))
        try:
            if value2 == 0:
                raise Exception(Error_divide_by_zero(value1))
            value3 = value1/value2
        except Exception as err:
            print(err)
        else:
            print(f'Результат деления {value1} на {value2} равен {value3}')
        res = input_(text_dialog="Попробовать произвести деление еще раз? (y/n)", str_numbers="")
        if "y" in res.lower():
            continue
        elif "n" in res.lower():
            quit()
        else:
            continue

if __name__ == '__main__':
    exec_subtask2()