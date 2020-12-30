from random import randint
from itertools import cycle
from time import sleep as waiting_for_an_update
import os

cars = []
end_color = '\033[0m'


class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False;

    def __init__(self, **kwargs):
        for s, v in kwargs.items():
            setattr(self, s, v)

    def go(self):
        if self.speed - 20 <= 0:
            i_start = 1
        else:
            i_start = -20
        i = randint(i_start, 40)
        start = self.speed
        finish = self.speed + i
        if start < finish:
            self.speed = randint(start, finish)
        else:
            self.speed = randint(finish, start)
        Car.gen_message()

    def turn(self, direction):
        if self.speed - 30 <= 0:
            i_start = 1
        else:
            i_start = 30
        self.speed = self.speed - randint(self.speed - i_start, self.speed)
        Car.gen_message(mode='directions', obj_direction=self, direction=direction)
        waiting_for_an_update(1)

    def stop(self):
        self.speed = 0
        Car.gen_message()
        waiting_for_an_update(0.3)

    def show_speed(self):
        Car.gen_message()

    @classmethod
    def directions(cls):
        return ("разворот назад ▼", "← ← ← ←  поворот налево", "поворот направо → → → → ")

    @classmethod
    def gen_message(cls, obj_speed_60=None, obj_direction=None, mode='speed', direction=None):

        os.system("cls")

        auto_str = "  ______\n" + " /|_||_\`.__\n" + "(   _    _ _|\n" + "=`-(_)--(_)-'"
        Message = ""

        available_colors = get_available_colors()
        for car in cars:

            # автомобиль
            fragment = "POLICE " if car.is_police else ""
            Message = Message + "\n" + available_colors.get(car.color) + auto_str +"   " + fragment + car.name + end_color

            #скорость
            if car.speed == 0:
                fragment = available_colors.get("Белый") + "машина остановлена" + end_color
            elif car.speed < 5:
                fragment = available_colors.get("Зеленый") + ("/" * 5) + end_color
            elif car.speed < 20:
                fragment = available_colors.get("Зеленый") + ("/" * car.speed) + end_color
            elif 20 < car.speed < 60:
                fragment = available_colors.get("Зеленый") + ("/" * 20) + end_color + available_colors.get(
                    "Желтый") + ("/" * (car.speed - 20)) + end_color
            elif car.speed >= 60:
                fragment = available_colors.get("Зеленый") + ("/" * 20) + end_color + available_colors.get(
                    "Желтый") + ("/" * (car.speed - 40)) + end_color + available_colors.get("Красный") + (
                                             "/" * (car.speed - 60)) + end_color
            fragment = " Скорость: " + str(car.speed) + " "+fragment

            if mode == "directions" and car == obj_direction:  # направление и скорость
                fragment = " "+direction + fragment

            if not obj_speed_60 == None and obj_speed_60 == car and mode == 'speed':
                fragment = available_colors.get("Красный")+"Превышение скорости. "+end_color+ fragment

            Message = Message + fragment

        print(Message, end='')


def exec_subtask4():
    cars.clear()

    available_colors = get_available_colors()

    for i in range(1, randint(3, 7)):
        color_car = list(available_colors.keys())[i]
        class_index = randint(1, 12)
        name = rand_name()
        if class_index == 1:
            car = Car(color=color_car, name=name)
        elif class_index == 2:
            car = SportCar(color=color_car, name=name)
        elif class_index == 3:
            car = PoliceCar(color=color_car, name=name)
        elif 4<=class_index<10:
            car = TownCar(color=color_car, name=name)
        elif 10<=class_index<=12:
            car = WorkCar(color=color_car, name=name)
        cars.append(car)

    for index_car in cycle(range(len(cars))):
        car = cars[index_car-1]
        operation_index = randint(1, 10)
        if operation_index == 1:
            car.stop()
        elif operation_index == 2:
            car.turn(direction=Car.directions()[randint(0, 2)])
        elif operation_index == 3:
            car.show_speed()
        elif operation_index >= 4:
            car.go()
        waiting_for_an_update(1)


class TownCar(Car):

    def __init__(self, **kwargs):
        Car.__init__(self,**kwargs)

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            # сообщение о превышении скорости
            Car.gen_message(obj_speed_60=self)


class WorkCar(Car):

    def __init__(self, **kwargs):
        Car.__init__(self,**kwargs)

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            # сообщение о превышении скорости
            Car.gen_message(obj_speed_60=self)


class SportCar(Car):

    def __init__(self, **kwargs):
        Car.__init__(self,**kwargs)

    def go(self):
        Car.go(self)
        if self.speed > 0:
            self.speed = self.speed + 6
        Car.gen_message()


class PoliceCar(Car):

    def __init__(self,**kwargs):
        Car.__init__(self,**kwargs)
        self.is_police = True

def rand_name():
    bc = "bcdfghjklmnpqrstvwxz"
    ae = "aeiouy"
    res = ""
    max_index_bc = len(bc) - 1
    max_index_ae = len(ae) - 1
    for i in range(randint(4, 10)):
        k = randint(0, 2)
        if k > 0:
            res = res + bc[randint(1, max_index_bc)]
        else:
            res = res + ae[randint(1, max_index_ae)]
    res = bc[randint(1, max_index_bc)].upper() + ae[randint(1, max_index_ae)] + res
    return res


def get_available_colors():
    return {
        "Красный":
            "\33[31m",

        "Зеленый":
            "\33[32m",

        "Желтый":
            "\33[33m",

        "Синий":
            "\33[34m",

        "Фиолетовый":
            "\33[35m",

        "Бирюзовый":
            "\33[36m",

        "Белый":
            "\33[37m"
    }


if __name__ == '__main__':
    exec_subtask4()
