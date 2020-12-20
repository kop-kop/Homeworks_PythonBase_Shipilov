import sys


def exec_subtask6():
    path = sys.path[0] + "\\" + 'schedule.txt'
    try:
        current_file = open(path, "r")
    except:
        print("Не удалось открыть файл " + path)
        quit()
    str_numbers = '1234567890'
    lessons = {}
    for line in current_file:
        l = float(0)
        lab = float(0)
        pr = float(0)
        i = 0
        lesson = line[:line.find(":")]
        while True:
            line_copy = line[i:]

            num_in_line_copy = False
            for character in str_numbers:
                num_in_line_copy = line_copy.find(character)>-1
                if num_in_line_copy:
                    break
            if num_in_line_copy == False:
                break

            i_sym = -1
            current_sum_str = ""
            for character in line_copy:
                i_sym += 1
                if character in str_numbers or (not current_sum_str == "" and character == "."):
                    current_sum_str = current_sum_str + character
                elif not current_sum_str == "" and (character == " " or character == "("):
                    line_fragment = line_copy[i_sym:i_sym + 4]
                    flags = {"l": line_fragment.find("(л)") > -1, "lab": line_fragment.find("(ла") > -1,
                             "pr": line_fragment.find("(п") > -1}
                    if flags.get("l"):
                        l += float(current_sum_str)
                    elif flags.get("lab"):
                        lab += float(current_sum_str)
                    elif flags.get("pr"):
                        pr += float(current_sum_str)
                    i = i + i_sym
                    break
        lessons[lesson] = l + lab + pr + (0 if lessons.get(lesson) == None else lessons.get(lesson))

    current_file.close()
    print(lessons)


if __name__ == '__main__':
    exec_subtask6()
