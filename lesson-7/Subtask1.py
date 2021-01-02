import shipilov


def exec_subtask1():

    while True:
        res = shipilov.input_(text_dialog="Вы хотите самостоятельно задать матрицы для расчётов? (y/n)", str_numbers="")

        if "y" in res.lower():
            matricies = Matrix.create_matricies_from_str()
            break
        elif "n" in res.lower():
            matricies = Matrix.create_matricies_from_template()
            break
        else:
            continue

    matrix_A = matricies.get("A")
    matrix_B = matricies.get("B")

    matrix_C = matrix_A + matrix_B
    print(matrix_C)

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = ""
        for i_y in range(len(self.matrix)):
            x_str = str(self.matrix[i_y])
            res = res + x_str[1:len(x_str) - 1] + "\n"
        return res

    def __add__(self, other):
        matrix_data = []
        for i_y in range(len(self.matrix)):
            matrix_string = []
            for i_x in range(len(self.matrix[i_y])):
                matrix_string.append(self.matrix[i_y][i_x] + other.matrix[i_y][i_x])
            matrix_data.append(matrix_string)
        return Matrix(matrix_data)


    @classmethod
    def create_matricies_from_template(cls):
        """
        Создаёт матрицы А и В по шаблону
        Return {"A": Matrix(list_a), "B": Matrix(list_b)}, typed dict
        """
        matrix_a = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
        matrix_b = Matrix([[1, 1, 1], [3, 4, 5], [10, 20, 30]])
        return {"A": matrix_a, "B": matrix_b}

    @classmethod
    def create_matricies_from_str(cls):
        """
        Создаёт матрицы А и В по пользовательским данным
        Return {"A": Matrix(list_a), "B": Matrix(list_b)}, typed dict
        """
        while True:
            matricies = []
            err = False
            sizes_of_matrices_str = shipilov.input_(
                text_dialog="Введите размерность матриц в формате 'x,y' (пример '3,3')",
                str_numbers="")
            try:
                sizes_of_matrices_arr = sizes_of_matrices_str.split(",")
                size_of_matrix_x = int(sizes_of_matrices_arr[0])
                size_of_matrix_y = int(sizes_of_matrices_arr[1])
                if size_of_matrix_x == 0 or size_of_matrix_y == 0:
                    raise
            except:
                print("Не удалось определить размерность матриц по введенным данным. Попробуйте еще раз.")
                continue
            if not err:
                for name_matrix in ["A", "B"]:
                    matrix_arr = []
                    for i_y in range(size_of_matrix_y):
                        while True:
                            line = shipilov.input_(
                                text_dialog=f'Введите через запятую {size_of_matrix_x} элемента(-ов) для строки №{i_y + 1} матрицы {name_matrix}',
                                str_numbers="")
                            try:
                                elements_x = list(map(float, line.split(",")))
                                if not len(elements_x) == size_of_matrix_x:
                                    raise
                            except:
                                print(
                                    f'Не удалось добавить строку №{i_y + 1} к матрице {name_matrix} - введены '
                                    f'некорректные данные. Попробуйте еще раз.')
                                continue
                            matrix_arr.append(elements_x)
                            break
                    matricies.append(matrix_arr)
            return {"A": Matrix(matricies[0]), "B": Matrix(matricies[1])}


if __name__ == '__main__':
    exec_subtask1()
