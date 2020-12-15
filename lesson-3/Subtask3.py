def exec_subtask3():
    val1 = -3
    val2 = 13
    val3 = 4
    val_result = my_func(val1, val2, val3)
    print(val_result)


def my_func(val1, val2, val3):
    num = [val1, val2, val3]
    main = []
    minus = []
    plus = []

    for i in num:
        if (i < 0):
            minus.append(i)
        else:
            plus.append(i)

    minus.sort()
    plus.sort()

    main.extend(minus)
    main.extend(plus)

    return main[1] + main[2]


if __name__ == '__main__':
    exec_subtask3()
