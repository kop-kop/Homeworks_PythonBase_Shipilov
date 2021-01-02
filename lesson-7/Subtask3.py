import shipilov
from random import randint

cells = {}

def exec_subtask3():
    Cell.create_base_cells()

    while True:

        make_order = False
        do_operation = False

        while True:
            res = shipilov.input_(str_numbers="123",only_positive=True,
                                  text_dialog="---------------------------------------------------\n"
                                              "Что хотите сделать?\n"
                                              "1 - Создать новую клетку\n"
                                              "2 - Выполнять операции с существующими клетками\n"
                                              "3 - Посмотреть отчет о содержимом клетки\n").lower()
            if "1" == res:
                Cell.create_cell()
            elif "2" == res:
                if len(cells) > 1:
                    do_operation = True
                    break
                else:
                    print("Недостаточно клеток для выполнения операций. Попробуйте добавить новую клетку...")
            elif "3" == res:
                make_order = True
                break

        if do_operation:
            operation = Cell.select_operation()
            cells_for_operations = Cell.select_cells_for_operations(2)
            operation(cells_for_operations[0], cells_for_operations[1])
        elif make_order:
            cell_for_operations = Cell.select_cells_for_operations(1)[0]
            child_cells_in_a_row = int(shipilov.input_(str_numbers="1234567890",only_positive=True,text_dialog="Введите максимальное количество дочерних клеток в строке отчета о содержимом"))
            cell_for_operations.make_order(child_cells_in_a_row)


class Cell:
    name = ""
    child_cells = 1

    def __init__(self, count_child_cells, name):
        if count_child_cells < 1:
            raise
        self.child_cells = count_child_cells
        self.name = name

    def __add__(self, other):
        count_child_cells = self.child_cells + other.child_cells
        name = self.name + other.name
        Cell.create_cell(name, count_child_cells)
        del cells[self.name]
        del cells[other.name]

    def __sub__(self, other):
        count_child_cells = self.child_cells - other.child_cells
        if count_child_cells<=0:
            print(f'Операция не может быть выполнена, т.к. в клетке {self.name} недостаточно дочерних клеток')
        else:
            self.child_cells = self.child_cells + count_child_cells
            other.child_cells = other.child_cells - count_child_cells
            print(f'Из клетки {other.name} было вычтено {count_child_cells} дочерних клеток в пользу клетки {self.name}')

    def __mul__(self, other):
        count_child_cells = self.child_cells * other.child_cells
        name = self.name + "x" + other.name
        Cell.create_cell(name, count_child_cells)

    def __truediv__(self, other):
        err = False
        count_child_cells = 0
        try:
            count_child_cells = self.child_cells // other.child_cells
        except ZeroDivisionError:
            err = True
            print(f'Не удалось разделить клетки. {other.name} содержит 0 дочерних клеток.')
        except:
            err = True
            print(f'Не удалось выполнить операцию деления.')
        if not err:
            name = self.name +"d"+ other.name
            Cell.create_cell(name, count_child_cells)

    def make_order(self,child_cells_in_a_row):
        order = ""
        child_cells = self.child_cells
        while child_cells>0:
            if child_cells >= child_cells_in_a_row:
                order += ("*" * child_cells_in_a_row)+"\n"
                child_cells = child_cells - child_cells_in_a_row
            else:
                order += ("*" * child_cells)+"\n"
                child_cells = 0
        print(order)

    @classmethod
    def select_cells_for_operations(cls,cells_count):
        cells_names = list(cells.keys())
        chose_cells = []
        count_cells_to_choose = len(cells)
        for number_cell in range(cells_count):
            number_cell = number_cell + 1
            fragment = ""
            for i in range(count_cells_to_choose):
                cell_name = cells_names[i]
                fragment += f'{i + 1}: {cell_name} (кол-во дочерних клеток: {cells.get(cell_name).child_cells})\n'
            while True:
                err = False
                index_cell = 0
                res = shipilov.input_(str_numbers="",
                                      text_dialog=f'Введите номер {number_cell}-ой клетки для выполнения операции.\n{fragment}')
                try:
                    index_cell = int(res) - 1
                    if index_cell < 0 or index_cell >= count_cells_to_choose:
                        raise
                except:
                    err = True
                    print("Не удалось выбрать клетку по введенному номеру. Попробуйте еще раз...")
                if not err:
                    chose_cells.append(cells.get(cells_names[index_cell]))
                    cells_names.pop(index_cell)  # к следующему выбору эта клетка не будет отображена
                    count_cells_to_choose = count_cells_to_choose - 1
                    break
        return chose_cells

    @classmethod
    def create_cell(cls, name=None, count_child_cells=None):
        if name == None and count_child_cells == None:
            name = shipilov.rand_name(2)
            while name in cells.keys():
                name = shipilov.rand_name(2)
            count_child_cells = int(shipilov.input_(str_numbers="1234567890", only_positive=True,
                                                    text_dialog=f'Введите количество дочерних клеток для новой клетки "{name}"'))
        new_cell = Cell(count_child_cells, name)
        cells[new_cell.name] = new_cell
        print(f'Создана клетка {name} (количество дочерних клеток {count_child_cells})')

    @classmethod
    def create_base_cells(cls):
        cell_a = Cell(randint(1, 15), "A")
        cell_b = Cell(randint(1, 15), "B")
        cells[cell_a.name] = cell_a
        cells[cell_b.name] = cell_b

    @classmethod
    def operations(cls):
        operations = []
        operation_element = {"Сложение": cls.__add__}
        operations.append(operation_element)
        operation_element = {"Вычитание": cls.__sub__}
        operations.append(operation_element)
        operation_element = {"Умножение": cls.__mul__}
        operations.append(operation_element)
        operation_element = {"Деление": cls.__truediv__}
        operations.append(operation_element)
        return operations

    @classmethod
    def select_operation(cls):
        question_text = "Введите номер операции, которую хотите произвести над клетками:"
        operations = cls.operations()
        count_operations = len(operations)
        for index_operation in range(count_operations):
            question_text += "\n" + str(index_operation + 1) + ". " + list(operations[index_operation].keys())[0]
        select_index_operation = 0
        while True:
            err = False
            try:
                index_operation = int(
                    shipilov.input_(str_numbers="123456789", only_positive=True, text_dialog=question_text))
                select_index_operation = index_operation - 1
                if select_index_operation < 0 or select_index_operation >= count_operations:
                    raise
            except:
                print("Не удалось определить операцию по введенному номеру. Повторите еще раз, пожалуйста...")
                err = True
                continue
            if not err:
                break
        return list(operations[select_index_operation].values())[0]


if __name__ == '__main__':
    exec_subtask3()
