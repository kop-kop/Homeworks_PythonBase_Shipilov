import sys
import shipilov


def exec_subtask3():
    path = shipilov.input_(str_numbers='', text_dialog="Введите название файла с расширением")
    path = sys.path[0] + "\\" + path
    try:
        current_file = open(path, "r")
    except:
        print("Не удалось открыть файл " + path)
        quit()
    str_numbers = '1234567890'
    count_lines = 0
    sum = 0
    workers_less_than_20th = []
    for line in current_file:
        count_lines = count_lines + 1
        current_sum_str = ""
        index_start_sum = -1
        i = -1
        for character in line:
            i += 1
            if character in str_numbers or (not current_sum_str == "" and character == "."):
                index_start_sum = index_start_sum if index_start_sum > -1 else i
                current_sum_str = current_sum_str + character
        current_sum = float(current_sum_str)
        sum += current_sum
        if current_sum < 20000:
            workers_less_than_20th.append(line[:index_start_sum])
    current_file.close()

    print(workers_less_than_20th)
    print(f'Средний оклад по сотрудникам {sum / count_lines}')


if __name__ == '__main__':
    exec_subtask3()
