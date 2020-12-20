import sys
import shipilov


def exec_subtask2():
    path = shipilov.input_(str_numbers='',text_dialog="Введите название файла с расширением")
    path = sys.path[0] + "\\" + path
    try:
        current_file = open(path, "r")
    except:
        print("Не удалось открыть файл "+path)
        quit()
    count_words = 0
    count_lines = 0
    for line in current_file:
        count_lines = count_lines + 1
        count_words = count_words + len(line.split(" "))
    current_file.close()
    print(f'Количество строк: {count_lines}; Количество слов {count_words}');


if __name__ == '__main__':
    exec_subtask2()
