from datetime import datetime

class MyDate:

    def __init__(self, str_date):
        self.date = MyDate.str_date__to__number(str_date)

    @classmethod
    def str_date__to__number(cls, str_date):
        return int(str_date.replace('-', ""))

    @staticmethod
    def str_date__validation(str_date):
        err = False
        try:
            datetime.strptime(str_date, '%d-%m-%Y')
        except:
            err = True
        return not err


def exec_subtask1():
    data = ["14-05-2020", "09-13-2020", "01-01-2021", "02-03-F006"]
    for str_date in data:
        if MyDate.str_date__validation(str_date):
            date_obj = MyDate(str_date)
            print(f'Создан объект класса MyDate - {date_obj.date}')
        else:
            print(f'Значение "{str_date}" не прошло проверку валидации')


if __name__ == '__main__':
    exec_subtask1()
