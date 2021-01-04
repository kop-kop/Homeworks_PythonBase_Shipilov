import shipilov
from random import randint
from datetime import datetime
from collections import UserList

Items = []
EnterpriseStructure = {}
Leftovers_in_warehouses = {}  # Warehouse->{Division: {Item: Count}}


def exec_subtask4():
    # init
    global List_Documents_On_Receipt_Of_Equipment
    List_Documents_On_Receipt_Of_Equipment = Documents_On_Receipt_Of_Equipment()
    createBaseEnterpriseStructure()
    createBaseObjectsOfficeTechnics()

    # body
    while True:
        operation_number = select_operations()
        if operation_number == 1:
            TakeOrMoveTheGoodsToTheWarehouse()
        elif operation_number == 2:
            ReportGoods()
        elif operation_number == 3:
            quit()

def ReportGoods():

    names = {}
    for warehouse in EnterpriseStructure['Warehouses']:
        for division in EnterpriseStructure['Divisions']+[None]:
            available_count = Stock_balance.remains_of_the_warehouse(warehouse,division)
            for element in available_count:
                names[element.item.name] = element.count if names.get(element.item.name) is None else names[element.item.name] + element.count

    strings = []
    for key, value in names.items():
        strings.append("{}: {}".format(key, value))
    result = "-------------------------------\n"+\
                 ("\n".join(strings))+"\n"+ \
             "-------------------------------\n"
    print(result)


def TakeOrMoveTheGoodsToTheWarehouse():
    tech_types = Office_technic.techic_types()

    while True:
        warehouse_supplier = shipilov.select_value_from_list(
            ["<External supplier>"] + [Stock_balance(warehouse=warehouse) for warehouse in
                                       EnterpriseStructure['Warehouses']],
            text_dialog="Enter the number of the SENDING warehouse")
        warehouse_supplier = warehouse_supplier.warehouse if not type(warehouse_supplier) == type('') else None
        if not warehouse_supplier is None:
            division_supplier = shipilov.select_value_from_list(
                [f'<Without division> ({Stock_balance(warehouse=warehouse_supplier, division=None).count})'] + [
                    Stock_balance(warehouse=warehouse_supplier, division=division) for division in
                    EnterpriseStructure['Divisions']],
                text_dialog="Enter the number of the SENDING department")
            division_supplier = division_supplier.division if not type(division_supplier) == type('') else None
        else:
            division_supplier = None

        if not warehouse_supplier is None:
            available_stock = Stock_balance.remains_of_the_warehouse(warehouse_supplier, division_supplier)
            if len(available_stock) == 0:
                print(
                    f'There is no equipment available for moving in the {str(warehouse_supplier)}{"" if division_supplier is None else "-" + str(division_supplier)}')
                print("Select a different sender...")
                continue

        warehouse_recipient = shipilov.select_value_from_list(
            [Stock_balance(warehouse=warehouse) for warehouse in EnterpriseStructure['Warehouses']],
            text_dialog="Enter the number of the RECEIVING warehouse").warehouse
        division_recipient = shipilov.select_value_from_list(
            [f'<Without division> ({Stock_balance(warehouse=warehouse_recipient, division=None).count})'] + [
                Stock_balance(warehouse=warehouse_recipient, division=division) for division in
                EnterpriseStructure['Divisions']],
            text_dialog="Enter the number of the RECEIVING division")
        division_recipient = division_recipient.division if not type(division_recipient) == type('') else None
        break

    while True:

        crit_err = False
        item = None

        # if we know supplier -> select tech from it
        if not warehouse_supplier is None:
            available_stock = Stock_balance.remains_of_the_warehouse(warehouse=warehouse_supplier,
                                                                     division=division_supplier)
            if len(available_stock) == 0:
                print(
                    f'There is no equipment available for moving in the {str(warehouse_supplier)}{"" if division_supplier is None else "-" + str(division_supplier)}')
                crit_err = True
                break
            item = shipilov.select_value_from_list(available_stock,
                                                   text_dialog=f'Enter the number of equipment available in the {str(warehouse_supplier)}{"" if division_supplier is None else "-" + str(division_supplier)}').item
        else:
            # we describe the product ourselves
            question = "Type of equipment delivered to the warehouse:\n"
            for i in range(len(tech_types)):
                tech_type = tech_types[i]
                question += f'{i + 1}: {tech_type}\n'
            while True:
                err = False
                res = shipilov.input_(str_numbers="", text_dialog=question)
                try:
                    type_index = int(res) - 1
                except:
                    err = True
                    print("The vehicle type number is entered incorrectly. Please try again...")
                if not err:
                    break
            select_class = [this_class for this_class in Office_technic.__subclasses__() if
                            this_class.__name__ == tech_types[type_index]][0]
            initialization_class_parameters = {}
            for attr_name, type_of_value in shipilov.attrs_of_class_with_types(select_class).items():
                while True:
                    err = False
                    # if type_of_value is list -> check selected method
                    if type_of_value == type('') and hasattr(select_class, f'list_{attr_name}'):
                        value = shipilov.select_value_from_list(getattr(select_class, f'list_{attr_name}')(),
                                                                text_dialog=f'Enter the value number of the "{attr_name}" property')
                    else:
                        value_str = shipilov.input_(str_numbers="", text_dialog=f'Enter the value of the "{attr_name}"')
                        try:
                            if type_of_value == type(''):
                                value = value_str
                            elif type_of_value == type(False):
                                value = True if value_str.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup'] else False
                            else:
                                value = type_of_value(eval(value_str))
                        except:
                            err = True
                            print("The entered data could not be processed. Try again...")
                            continue
                    if not err:
                        initialization_class_parameters[attr_name] = value
                        break
                    else:
                        continue

        if crit_err:
            break

        if item is None:
            item = select_class(**initialization_class_parameters)
            Items.append(item)

        count = int(shipilov.input_(str_numbers='1234567890',
                                    text_dialog="Enter the quantity of equipment to be delivered to the warehouse"))
        try:
            List_Documents_On_Receipt_Of_Equipment.append(item=item, count=count, warehouse_supplier=warehouse_supplier,
                                                          division_supplier=division_supplier,
                                                          warehouse_recipient=warehouse_recipient,
                                                          division_recipient=division_recipient)
        except Exception as err_data:
            print(err_data)

        item = None

        if "n" in shipilov.select_value_from_list(["Yes", "No"],
                                                  text_dialog="Repeat the operation of receiving equipment ?").lower():
            break


def select_operations():
    text = f'Enter the number of the command you want to run:\n' \
           f'1. Take/Move the goods to the warehouse\n' \
           f'2. View the report on goods\n' \
           f'3. Exit the program\n' \
           f':'
    while True:
        err = False
        res = shipilov.input_(str_numbers="", text_dialog=text)
        try:
            operation_number = int(res)
            if operation_number < 1 or operation_number > 4:
                raise
        except:
            err = True
            print("The command could not be determined from the data entered. Please try again.")
        if not err:
            return operation_number


def createBaseEnterpriseStructure():
    Divisions = []
    ElementsStructure = ["Sales Department", 'Purchasing Department', 'Directorate']
    for element in ElementsStructure:
        Divisions.append(Division(element))
    EnterpriseStructure['Divisions'] = Divisions

    Warehouses = []
    ElementsStructure = ["Shipping Warehouse", 'Warehouse office', 'Main Warehouse',
                         "Sales Department storage warehouse"]
    for element in ElementsStructure:
        Warehouses.append(Warehouse(element))
    EnterpriseStructure['Warehouses'] = Warehouses


def createBaseObjectsOfficeTechnics():
    listWarehouses = EnterpriseStructure['Warehouses']
    listDivisions = EnterpriseStructure['Divisions']

    PrinterTypes = Printer.list_type_printer()
    PrinterNames = ["Canon XF400", "Epson SX4300"]
    for i in range(len(PrinterTypes)):
        printer_type = PrinterTypes[i]
        printer_name = PrinterNames[i]
        item = Printer(name=printer_name, weight=randint(1, 5), storage_cells_occupied=randint(1, 2),
                       type_printer=printer_type)
        Items.append(item)
        random_warehouse = listWarehouses[randint(0, len(listWarehouses) - 1)]
        random_division = listDivisions[randint(0, len(listDivisions) - 1)]
        List_Documents_On_Receipt_Of_Equipment.append(item=item, count=1, warehouse_recipient=random_warehouse,
                                                      division_recipient=random_division, dont_print_data=True)
    PrinterNames = ["HP StylePrint 400", "HP KP07"]
    for i in range(len(PrinterTypes)):
        printer_type = PrinterTypes[i]
        printer_name = PrinterNames[i]
        item = Printer(name=printer_name, weight=randint(1, 5), storage_cells_occupied=randint(1, 2),
                       type_printer=printer_type)
        Items.append(item)
        List_Documents_On_Receipt_Of_Equipment.append(item=item, count=1, warehouse_recipient=random_warehouse,
                                                      division_recipient=random_division, dont_print_data=True)
    for i in range(len(PrinterTypes)):
        printer_type = PrinterTypes[i]
        printer_name = PrinterNames[i]
        item = Printer(name=printer_name, weight=randint(1, 5), storage_cells_occupied=randint(1, 2),
                       type_printer=printer_type)
        Items.append(item)
        List_Documents_On_Receipt_Of_Equipment.append(item=item, count=1, warehouse_recipient=random_warehouse,
                                                      division_recipient=random_division, dont_print_data=True)
    ScanerResolutions = Scaner.list_scan_resolution()
    ScanerTypesMatricies = Scaner.list_type_matrix()
    ScanerNames = ["Epson SlimScan", "Canon P4000"]
    for i in range(len(ScanerNames)):
        scaner_name = ScanerNames[i]
        resolution = ScanerResolutions[randint(1, len(ScanerResolutions) - 1)]
        type_matrix = ScanerTypesMatricies[randint(1, len(ScanerTypesMatricies) - 1)]
        item = Scaner(name=scaner_name, weight=randint(1, 5), storage_cells_occupied=randint(1, 2),
                      type_matrix=type_matrix, scan_resolution=resolution)
        Items.append(item)
        random_warehouse = listWarehouses[randint(0, len(listWarehouses) - 1)]
        random_division = listDivisions[randint(0, len(listDivisions) - 1)]
        List_Documents_On_Receipt_Of_Equipment.append(item=item, count=1, warehouse_recipient=random_warehouse,
                                                      division_recipient=random_division, dont_print_data=True)
    double_sided_print_variables = [True, False]
    Copy_machines_Names = ["Kyocera ECOSYS M2233", "Kyocera FS-106H"]
    for i in range(len(Copy_machines_Names)):
        Copy_machine_Name = Copy_machines_Names[i]
        double_sided_print = double_sided_print_variables[randint(1, len(double_sided_print_variables) - 1)]
        item = Copy_machine(name=Copy_machine_Name, weight=randint(1, 5), storage_cells_occupied=randint(1, 2),
                            double_sided_print=double_sided_print)
        Items.append(item)
        random_warehouse = listWarehouses[randint(0, len(listWarehouses) - 1)]
        random_division = listDivisions[randint(0, len(listDivisions) - 1)]
        List_Documents_On_Receipt_Of_Equipment.append(item=item, count=1, warehouse_recipient=random_warehouse,
                                                      division_recipient=random_division, dont_print_data=True)


##########################################################################
##############TECHNIC

class Office_technic:
    name = ""
    weight = 0.2
    storage_cells_occupied = 1

    @staticmethod
    def select_from_list(l):
        pass

    @staticmethod
    def techic_types():
        res = []
        for el in Office_technic.__subclasses__():
            res.append(el.__name__)
        return res

    def __str__(self):
        return self.name


class Printer(Office_technic):
    type_printer = ""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def list_type_printer():
        return ["laser", "inkjet"]


class Scaner(Office_technic):
    type_matrix = ""
    scan_resolution = ""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def list_scan_resolution():
        return ["1920x1080", "3840×2160", "4096×3072", "8600x6000"]

    @staticmethod
    def list_type_matrix():
        return ["CCD", "CMOS", "CID"]


class Copy_machine(Office_technic):
    double_sided_print = False

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


##########################################################################
##############COMPANY

class Enterprise_structure:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Warehouse(Enterprise_structure):

    def __init__(self, name):
        super().__init__(name)


class Division(Enterprise_structure):

    def __init__(self, name):
        super().__init__(name)


##########################################################################
##############OPERATIONS

class Documents_On_Receipt_Of_Equipment(UserList):

    def append(self, **kwargs):

        item = kwargs.get("item")
        count = kwargs.get("count")
        warehouse_supplier = kwargs.get("warehouse_supplier")
        division_supplier = kwargs.get("division_supplier")
        warehouse_recipient = kwargs.get("warehouse_recipient")
        division_recipient = kwargs.get("division_recipient")

        dont_print_data = True if kwargs.get("dont_print_data") == True else False
        print_data = not dont_print_data

        if not warehouse_supplier is None:

            current_remains = Leftovers_in_warehouses.get(warehouse_supplier)
            if current_remains is None:
                raise Exception(MoveError(warehouse_supplier))
            else:
                current_remains_division = current_remains.get(division_supplier)
                if current_remains_division is None:
                    raise Exception(MoveError(warehouse_supplier, division_supplier))
                else:
                    current_item_count = current_remains_division.get(item.name)
                    if current_item_count is None or current_item_count == 0:
                        raise Exception(
                            MoveError(warehouse_supplier, division_supplier, f'\nThe {item.name} is out of stock'))
                    else:
                        new_count_for_warehouse_supplier = current_item_count - count
                        if new_count_for_warehouse_supplier >= 0:
                            current_remains_division[item.name] = new_count_for_warehouse_supplier
                        elif new_count_for_warehouse_supplier < 0:
                            raise Exception(MoveError(warehouse_supplier, division_supplier,
                                                      f'\nThe {item.name} is not enough in stock for the operation. Now {current_item_count}; {str(-new_count_for_warehouse_supplier)} pieces are missing'))

        current_balances_of_the_recipient = Leftovers_in_warehouses.get(warehouse_recipient)
        if current_balances_of_the_recipient is None:
            Leftovers_in_warehouses[warehouse_recipient] = {}
            current_balances_of_the_recipient = Leftovers_in_warehouses[warehouse_recipient]
        current_balances_of_the_recipient_division = current_balances_of_the_recipient.get(division_recipient)
        if current_balances_of_the_recipient_division is None:
            current_balances_of_the_recipient[division_recipient] = {}
            current_balances_of_the_recipient_division = current_balances_of_the_recipient[division_recipient]
        current_balances_of_the_recipient_item = current_balances_of_the_recipient_division.get(item.name)
        if current_balances_of_the_recipient_item is None:
            current_balances_of_the_recipient_division[item.name] = count
        else:
            current_item_recipient_count = current_balances_of_the_recipient_division[item.name] + count
            current_balances_of_the_recipient_division[item.name] = current_item_recipient_count

        data_fragment_supplier = f'{"External supplier" if warehouse_supplier is None else str(warehouse_supplier)}{"" if division_supplier is None else "-" + str(division_supplier)}'
        data = f'Time: {datetime.now().strftime("%Y-%m-%d %H-%M-%S")}; Item: {item}; Count: {count}; From {data_fragment_supplier} to {warehouse_recipient}{" (without linking to a division)" if division_recipient is None else "-" + str(division_recipient)}'
        super(Documents_On_Receipt_Of_Equipment, self).append(data)
        if print_data:
            print(data)


class Stock_balance:

    def __init__(self, **kwargs):
        item = kwargs.get("item")
        self.warehouse = kwargs.get("warehouse")
        self.division = kwargs.get("division")
        if not item is None:
            self.item = item
            self.count = kwargs.get("count")
        else:
            warehouse = kwargs.get("warehouse")
            check_only_warehouse_balance = True
            try:
                division = kwargs["division"]
            except:
                pass
            else:
                check_only_warehouse_balance = False
            if check_only_warehouse_balance:
                count = 0
                for division in EnterpriseStructure['Divisions'] + [None]:
                    for element in Stock_balance.remains_of_the_warehouse(warehouse, division):
                        count += element.count
                self.count = count
            else:
                count = 0
                for element in Stock_balance.remains_of_the_warehouse(warehouse, division):
                    count += element.count
                self.count = count

    def __str__(self):
        representation_item = True
        if hasattr(self, "item"):
            if not self.item is None:
                return f'{self.item.name} ({self.count})'
            else:
                representation_item = False
        else:
            representation_item = False
        if not representation_item:
            if self.division is None:
                return f'{str(self.warehouse)} ({self.count})'
            else:
                return f'{str(self.division)} ({self.count})'

    @staticmethod
    def remains_of_the_warehouse(warehouse, division):
        items = []
        current_remains = Leftovers_in_warehouses.get(warehouse)
        if not current_remains is None:
            current_remains_division = current_remains.get(division)
            if not current_remains_division is None:
                for item_name, value in current_remains_division.items():
                    current_item_count = value
                    if not (current_item_count is None or current_item_count == 0):
                        item = [item for item in Items if item.name == item_name][0]
                        items.append(Stock_balance(warehouse=warehouse, division=division, item=item,
                                                   count=current_item_count))
        return items


class MoveError(Exception):

    def __init__(self, warehouse, division=None, additional_info=""):
        if division is None:
            self.message = f'You can\'t transfer an item from the {warehouse.name}.'
        else:
            self.message = f'You can\'t transfer an item from the {warehouse.name}-{division.name}.'
        self.message += "" if additional_info == "" else "\n" + additional_info

    def __str__(self):
        return self.message


if __name__ == '__main__':
    exec_subtask4()
