import sys
import shipilov


def exec_subtask1():
    path = sys.path[0] + "\\data_write.txt"
    current_file = open(path, "a", encoding="utf-8")
    while True:
        content = shipilov.input_(str_numbers='', text_dialog="Данные для добавления")
        if not content == '':
            current_file.write(content+"\n")
        else:
            current_file.close()
            quit()


if __name__ == '__main__':
    exec_subtask1()
