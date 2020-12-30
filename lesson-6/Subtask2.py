import shipilov


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    @classmethod
    def sum_mass_asphalt(cls, obj, mass=1, height=1):
        return (obj._length * obj._width * mass * height) / 1000


def exec_subtask2():
    while True:
        width = int(shipilov.input_(only_positive=True, text_dialog="Введите ширину дороги (м)"))
        length = int(shipilov.input_(only_positive=True, text_dialog="Введите длину дороги (м)"))
        road = Road(length, width)

        mass = int(shipilov.input_(only_positive=True, text_dialog="Введите массу асфальта на 1 кв.м дороги (кг)"))
        height = int(shipilov.input_(only_positive=True, text_dialog="Введите толщину полотна (см)"))

        result = Road.sum_mass_asphalt(road, mass, height)
        print(f'Масса асфальта, необходимого для покрытия дорожного полотка составит: {result}')

        result = shipilov.input_(text_dialog='Хотите произвести еще один расчёт? Введите "Да" чтобы продолжить расчёт',
                                 str_numbers="")
        if not result.lower() == "да":
            quit()


if __name__ == '__main__':
    exec_subtask2()
