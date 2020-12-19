def exec_subtask4():
    data = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    res = [data[i] for i in range(len(data)) if not data.count(data[i]) > 1]
    print(f'Результат: {res}')


if __name__ == '__main__':
    exec_subtask4()
