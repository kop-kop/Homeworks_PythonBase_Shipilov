from time import sleep as waiting_for_an_update

class Stationery:

    def draw(self, title="Взяли в руки художественный инструмент."):
        print("Запуск отрисовки. "+title)

class Pen(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Ух ты, у нас для рисования имеется "+self.title)
        waiting_for_an_update(0.3)
        print("Напишем что нибудь... например отрывок стихотворения Лермонтова")
        waiting_for_an_update(2.5)
        print("....."
              +"Вдали я видел сквозь туман,\n"
                +"В снегах, горящих, как алмаз,\n"
                +"Седой незыблемый Кавказ.....\n")


class Pencil(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("                ")
        print("Вау а это " + self.title)
        waiting_for_an_update(2)
        print("Нарисуем мишку")
        print("   ▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄   \n"
        +"   █▒▒░░░░░░░░░▒▒█   \n"
        +"    █░░█░░░░░█░░█    \n"
        +" ▄▄  █░░░▀█▀░░░█  ▄▄ \n"
        +"█░░█ ▀▄░░░░░░░▄▀ █░░█")

class Handle(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("                ")
        print("Что вы взяли в руки... а это " + self.title+". Только на стенах чур не рисовать!")
        waiting_for_an_update(1.3)
        print("\33[33m"+"               \n"+"          ███  \n"+"             ██\n"+"    ███       █\n"+"    ███    ████\n"+"            ███\n"+"    ███       █\n"+"    ███       █\n"+"          █████"+'\033[0m')


def exec_subtask5():

    instr = Stationery()
    instr.draw()

    pen = Pen("синяя ручка")
    pen.draw()

    waiting_for_an_update(5)

    pencil = Pencil("волшебный карандаш")
    pencil.draw()

    waiting_for_an_update(3)

    handle = Handle("желтый маркер")
    handle.draw()

if __name__ == '__main__':
    print("Доброго времени суток")
    print(".∧＿∧                   \n"+"( ･ω･｡)つ━☆・*。           \n"+"⊂  ノ    ・゜+.            \n"+"しーＪ   °。+ *´¨)         \n"+"         .· ´¸.·*´¨)     \n"+"          (¸.·´ (¸.·'* ☆")
    exec_subtask5()