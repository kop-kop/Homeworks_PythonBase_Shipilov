def exec_subtask3():
    res = [i for i in range(21, 240) if i / 20 == i // 20 or i / 21 == i // 21]
    print(f'Результат: {res}')


if __name__ == '__main__':
    exec_subtask3()
