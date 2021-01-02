import shipilov


def exec_subtask2():

    clothes_objects = create_list_clothes()
    result_message = ""
    for clothes in clothes_objects:
        res_calc = clothes.calculation()
        result_message+=f'For {clothes.name} clothing, the fabric consumption will be {res_calc}\n'
    print(result_message)

def create_list_clothes():
    clothes_types = Clothes.types()
    clothes_objects = []
    while True:
        text_clothes_types_fragment = f'1: General\n'
        for i in range(len(clothes_types)):
            clothes_type = clothes_types[i]
            text_clothes_types_fragment += f'{i + 2}: {clothes_type}\n'
        question = f'Enter the number of the type of clothing for which you want to make the calculation\n{text_clothes_types_fragment}'
        while True:
            err = False
            res = shipilov.input_(str_numbers="", text_dialog=question)
            try:
                type_index = int(res) - 2
            except:
                err = True
                print("The clothing type number is entered incorrectly. Please try again...")
            if not err:
                break
        clothes_class = Clothes if type_index < 0 else \
        [this_class for this_class in Clothes.__subclasses__() if this_class.__name__ == clothes_types[type_index]][0]
        if clothes_class == Suit:
            parent_attributes_to_save = ["name","height"]
        else:
            parent_attributes_to_save = ["name"]
        initialization_class_parameters = {}
        for attr_name, type_of_value in shipilov.attrs_of_class_with_types(clothes_class,True,parent_attributes_to_save).items():
            while True:
                err = False
                value_str = shipilov.input_(str_numbers="", text_dialog=f'Enter the value of the "{attr_name}"')
                try:
                    # kolkhoz
                    if type_of_value == type(''):
                        value = value_str
                    else:
                        value = type_of_value(eval(value_str))
                        if int(value) == 0:
                            raise
                except:
                    err = True
                    print("The entered data could not be processed. Try again...")
                    continue
                if not err:
                    initialization_class_parameters[attr_name] = value
                    break
        clothes_obj = clothes_class(data=initialization_class_parameters)
        clothes_objects.append(clothes_obj)
        res = shipilov.input_(str_numbers="",
                              text_dialog="Want to add clothes? (Y - add, N - calculate fabric consumption)")
        if "n" in res.lower():
            break
    return clothes_objects

class Clothes:
    name = "без названия"
    width = 0
    height = 0

    def __init__(self, data):
        self.name = data.get("name")
        self.width = data.get("width")
        self.height = data.get("height")

    def calculation(self):
        return round(self.width * self.height)

    @classmethod
    def types(cls):
        res = []
        for el in Clothes.__subclasses__():
            res.append(el.__name__)
        return res


class Coat(Clothes):
    size = 0

    def calculation(self):
        return round(self.size/6.5 + 0.5)

    def __init__(self, data):
        super().__init__(data=data)
        self.size = data.get("size")


class Suit(Clothes):
    height = 0

    def calculation(self):
        return round(2*self.height+0.3)

    def __init__(self, data):
        super().__init__(data=data)
        self.height = data.get("height")


if __name__ == '__main__':
    exec_subtask2()
