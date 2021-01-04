from shipilov import input_


class AddToListError(ValueError):

    def __init__(self, value):
        self.message = f'Нельзя произвести добавление "{value}" в список, так как значение не является числом.'

    def __str__(self):
        return self.message


class NumberList(list):

    def append(self, value):
        err = False
        try:
            convert_value = int(value)
        except ValueError:
            print(AddToListError(value))
            err = True
        if not err:
            super(NumberList, self).append(convert_value)

    def __str__(self):
        str_data = ""
        for element in self:
            str_data += str(element) + ", "
        return str_data[:len(str_data) - 2]


def exec_subtask3():
    mylist = NumberList()
    while True:
        value = input_(text_dialog="Введите данные для нового элемента списка", str_numbers="")
        mylist.append(value)
        while True:
            add_new_element = True
            res = input_(text_dialog="Попробовать произвести добавление еще раз? (y/n)", str_numbers="")
            if "y" in res.lower():
                break
            elif "n" in res.lower():
                add_new_element = False
                break
            else:
                continue
        if not add_new_element:
            break
    print(mylist)


if __name__ == '__main__':
    exec_subtask3()
