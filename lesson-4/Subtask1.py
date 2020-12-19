from sys import argv

def exec_subtask1(start_data):
    time = start_data[:1][0]
    rate = start_data[1:2][0]
    bonus = start_data[2:3][0]
    res = time * rate + bonus
    print(f'Результат: {res}')

if __name__ == '__main__':
    if not len(argv) == 4:
        quit()
    start_data = []
    for param in argv[1:]:
        try:
            start_data.append(float(param))
        except:
            quit()
    exec_subtask1(start_data)