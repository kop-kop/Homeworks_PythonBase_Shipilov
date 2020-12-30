
import shipilov
import json

class Worker:

    position = None

    def __init__(self):
        self.name = shipilov.input_(text_dialog='Введите имя сотрудника',
                                 str_numbers="")
        self.surname = shipilov.input_(text_dialog='Введите фамилию сотрудника',
                                 str_numbers="")
        income_wage = int(shipilov.input_(only_positive=True, text_dialog="Введите размер оклада"))
        income_bonus = int(shipilov.input_(only_positive=True, text_dialog="Введите размер премии"))
        self._income = {"wage": income_wage, "bonus": income_bonus}

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

class Position(Worker):

    full_name = None
    total_income = None

    def __init__(self):
        Worker.__init__(self)
        Position.set_position(self)

    @classmethod
    def set_position(cls,obj):
        obj.position = shipilov.input_(text_dialog='Название позиции сотрудника в Корпорации',
                                 str_numbers="")

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        income_data = getattr(self,"_income")
        return income_data.get("wage") * income_data.get("bonus")


def exec_subtask3():

    position1 = Position()
    position1.full_name = position1.get_full_name()
    position1.total_income = position1.get_total_income()

    print(position1)

if __name__ == '__main__':
    exec_subtask3()
