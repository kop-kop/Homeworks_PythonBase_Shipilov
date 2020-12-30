import subprocess
import sys
from itertools import cycle

EndColor = '\033[0m'


class TrafficLight:

    def __init__(self, colorvalue=None):
        self.__color = colorvalue

    @classmethod
    def yellow(cls=None):
        return "\033[93m", "Yellow", "2"

    @classmethod
    def green(cls=None):
        return "\033[92m", "Green", "3"

    @classmethod
    def red(cls=None):
        return "\033[91m", "Red", "7"

    @classmethod
    def text_color(cls, color_data):
        return color_data[0] + color_data[1] + EndColor

    def __iter__(self):
        for color in (TrafficLight.red(), TrafficLight.yellow(), TrafficLight.green()):
            yield color

    def running(self):

        #time.sleep использовать слишком скучно
        bat_path = sys.path[0] + "\\" + "expect.bat"
        bat_content_template = "ping -n SEC 127.0.0.1 >nul"

        for color_data in cycle(self):
            self.__color = color_data[1]

            bat_file_pause = open(bat_path, "w")
            bat_file_pause.write(bat_content_template.replace("SEC", color_data[2]))
            bat_file_pause.close()
            subprocess.call(bat_path, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

            print(TrafficLight.text_color(color_data))

def exec_subtask1():
    main_traffic_light = TrafficLight()
    main_traffic_light.running()


if __name__ == '__main__':
    exec_subtask1()
