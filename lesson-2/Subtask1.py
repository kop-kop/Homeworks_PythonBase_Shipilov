def exec_subtask1():
    result_list = []
    result_list.append(1)
    result_list.append("2")

    bonus_list = ['3', 4]
    result_list.extend(bonus_list)

    new_value1 = 5
    new_value2 = [6, 7.8]
    result_list.insert(2, new_value1)
    result_list.insert(5, new_value2)

    i = 0
    for element in result_list:
        element_type = type(element)
        print(f'list item with the #{i + 1} has the type {element_type} and value = {element}')
        i = i + 1


if __name__ == '__main__':
    exec_subtask1()
