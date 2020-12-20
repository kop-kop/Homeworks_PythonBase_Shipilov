import sys
import random


def exec_subtask5():
    path = sys.path[0] + "\\set of numbers.txt"
    current_file = open(path, "w", encoding="utf-8")
    # random list
    l = range(1, random.randint(2, 10000))
    l = random.sample(l, random.randint(1, len(l)))
    current_file.write(str(l).strip('[]').replace(",", ""))
    current_file.close()
    print("Операция завершена, проверьте файл 'set of numbers.txt'")


if __name__ == '__main__':
    exec_subtask5()
