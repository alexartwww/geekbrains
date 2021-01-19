import sys
import common

task = '''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

if __name__ == '__main__':
    print(task)

    if len(sys.argv) < 4:
        print('Type 3 params:')
        print('выработка в часах')
        print('ставка в час')
        print('премия')
        sys.exit(1)

    hours = common.format_value(sys.argv[1], '^[0-9]+$', int)
    price = common.format_value(sys.argv[2], '^[0-9]+(\.[0-9]+)?$', float)
    bonus = common.format_value(sys.argv[3], '^[0-9]+(\.[0-9]+)?$', float)

    if hours == None or price == None or bonus == None:
        print('Wrong format!:')
        print('выработка в часах must be int')
        print('ставка в час must be float')
        print('премия must be float')
        sys.exit(2)

    print('Заработная плата: ', (hours * price) + bonus)
