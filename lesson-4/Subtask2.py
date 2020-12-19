def exec_subtask2():
    data = [6, 14, 563, 1316, 54, 3435, 4545, 444, 545]
    res = [data[i] for i in range(1, len(data)) if data[i] > data[i - 1]]
    print(f'Результат: {res}')


if __name__ == '__main__':
    exec_subtask2()
