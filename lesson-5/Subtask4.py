import sys
import shipilov
from num2t4ru import num2text
from os import path as filepath


def exec_subtask4():
    path = shipilov.input_(str_numbers='', text_dialog="Введите название файла с расширением")
    path = sys.path[0] + "\\" + path
    try:
        current_file = open(path, "r")
    except:
        print("Не удалось открыть файл " + path)
        quit()

    # path for new file
    fragments_name_file = filepath.splitext(filepath.basename(current_file.name))
    full_path_new_file = sys.path[0] + "\\" + fragments_name_file[0] + "_ru"
    if len(fragments_name_file) > 1:
        full_path_new_file = full_path_new_file + fragments_name_file[1]
    new_file = open(full_path_new_file, "w", encoding="utf-8")

    str_numbers = '1234567890'
    marker = "—"
    for line in current_file:
        current_sum_str = ""
        index_start_sum = -1
        en_word = ""
        i = -1
        for character in line:
            i += 1
            if character in str_numbers or (not current_sum_str == "" and character == "."):
                index_start_sum = index_start_sum if index_start_sum > -1 else i
                current_sum_str = current_sum_str + character
            elif character == marker and en_word == "":
                en_word = line[:i]
        sum_ru_str = num2text(float(current_sum_str))
        sum_ru_str = sum_ru_str[:1].upper()+sum_ru_str[1:]
        content = f'{sum_ru_str} - {current_sum_str}'
        new_file.write(content + "\n")

    Result_write = True
    try:
        current_file.close()
        new_file.close()
    except:
        Result_write = False

    if Result_write:
        print(f'Операция завершена, проверьте файл {filepath.basename(full_path_new_file)}')
    else:
        print(f'При записи файла {filepath.basename(full_path_new_file)} что-то пошло не так')


if __name__ == '__main__':
    exec_subtask4()
