from functools import reduce

def exec_subtask5():
    res = reduce(lambda x, y: x * y, [x for x in range(100, 1001) if x % 2 == 0])
    print(f'Результат: {res}')

if __name__ == '__main__':
    exec_subtask5()
