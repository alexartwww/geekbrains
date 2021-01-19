from itertools import count, cycle
import sys
import common

task = '''
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
'''


if __name__ == '__main__':
    print(task)

    if len(sys.argv) < 3:
        print('Type 2 params:')
        print('first number')
        print('last number')
        sys.exit(1)

    first = common.format_value(sys.argv[1], '^[0-9]+$', int)
    last = common.format_value(sys.argv[2], '^[0-9]+$', int)

    if first == None or last == None:
        print('Wrong format!:')
        print('first number must be int')
        print('last number must be int')
        sys.exit(2)

    for i in count(first, 1):
        print(i)
        if i >= last:
            break
