import sys
import json


def exec_subtask7():
    path = sys.path[0] + "\\" + 'company.txt'
    try:
        current_file = open(path, "r")
    except:
        print("Не удалось открыть файл " + path)
        quit()
    firms_data = {}
    unique_firms = []
    sum_profit = 0
    for line in current_file:
        fragments = line.split(" ")
        firm = fragments[0]
        proceeds = float(fragments[2])
        outlay = float(fragments[3])
        if not firm in unique_firms:
            unique_firms.append(firm)
        profit = proceeds - outlay
        sum_profit = sum_profit + profit
        firms_data[firm] = profit + (0 if firms_data.get(firm) == None else firms_data.get(firm))

    obj = []
    obj.append(firms_data)
    obj.append({"average_profit": sum_profit/len(unique_firms)})
    data_json = json.dumps(obj, ensure_ascii=False)

    current_file.close()

    path = sys.path[0] + "\\company_json.json"
    json_file = open(path, "w", encoding="utf-8")
    json_file.write(data_json)
    json_file.close()


if __name__ == '__main__':
    exec_subtask7()
