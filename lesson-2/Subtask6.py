def exec_subtask6():
    count = int(input_('1234567890', 'Сколько продуктов вы намерены ввести'))

    products_list = []
    default_properties_names = ["Наименование", "Цена", "Количество", "Ед.изм"]
    for i in range(count):
        position_number = i + 1
        product_properties = {}
        for _property in default_properties_names:
            val = input_(text_dialog=f'Продукт №{position_number}. Введите значение свойства "{_property}"')
            product_properties.update({_property: val})
        position_data = (position_number, product_properties)
        products_list.append(position_data)
    print(products_list)

    analytics = {}
    for element in products_list:
        for key_name in element[1].keys():
            if not key_name in analytics.keys():
                position_data = [element[1].get(key_name)]
            else:
                position_data = analytics.get(key_name)
                position_data.append(element[1].get(key_name))
            analytics.update({key_name: position_data})
    print("Аналитика о товарах:")
    print(analytics)


def input_(str_numbers='', text_dialog='', only_positive=True):
    while True:
        str_value = input(f'{text_dialog} : ')
        if str_value == '':
            print("Вы ничего не ввели. Пустое значение не подходит.")
            continue
        elif not str_numbers == '':
            invalid_character = False
            if only_positive:
                for character in str_value:
                    if str_numbers.find(character) == -1:
                        print('Введен недопустимый символ. Попробуйте снова.')
                        invalid_character = True
                        break
            else:
                i = 0
                for character in str_value:
                    if str_numbers.find(character) == -1 and not (i == 0 and character == "-"):
                        print('Введен недопустимый символ. Попробуйте снова.')
                        invalid_character = True
                        break
                    i = i + 1
            if invalid_character:
                continue
            else:
                return str_value
        else:
            return str_value


if __name__ == '__main__':
    exec_subtask6()
