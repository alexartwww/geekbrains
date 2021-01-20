import json

task = '''
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю
прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее
в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''


if __name__ == '__main__':
    print(task)
    firms = {}
    result = {}
    try:
        with open('07.file.txt', 'r') as f:
            for line in f:
                line_sep = line.split()
                name = line_sep[0]
                form = line_sep[1]
                revenue = int(line_sep[2])
                spend = int(line_sep[3])
                if name not in firms:
                    firms[name] = revenue - spend
                else:
                    firms[name] += firms[name] + (revenue - spend)
        profit_list = [firms[name] for name in firms if firms[name] > 0]
        result = [firms, {"average_profit": sum(profit_list) / len(profit_list)}]
        print(json.dumps(result))
        with open('07.file.out.json', 'w') as f:
            json.dump(result, f)
    except IOError as err:
        print(f'Ошибка {err}!')
