from shipilov import input_


def exec_subtask7():
    print("Ввод первого комплексного числа")
    complex1 = ComplexNumber()
    print("Ввод второго комплексного числа")
    complex2 = ComplexNumber()
    complex3 = complex1 + complex2
    print(f'{complex1}+{complex2}={complex3}')
    complex4 = complex1 * complex2
    print(f'{complex1}*{complex2}={complex4}')

class ComplexNumber:

    def __init__(self):
        fragment1 = input_(str_numbers="1234567890",only_positive=False,text_dialog="Введите первый фрагмент комплексного числа")
        fragment2 = input_(str_numbers="1234567890ji",only_positive=False,text_dialog="Введите второй фрагмент комплексного числа").replace("i", "j")
        self.value = float(fragment1) + float(fragment2.replace("j", "")) * 1j

    def __add__(self, other):
        return self.value + other.value

    def __mul__(self, other):
        return self.value * other.value

    def __str__(self):
        return str(self.value)

if __name__ == '__main__':
    exec_subtask7()
