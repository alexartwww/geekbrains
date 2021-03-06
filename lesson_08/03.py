from common import input_value
import re

task = '''
Создайте собственный класс-исключение, который должен проверять содержимое
списка на наличие только чисел. Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например,
команду “stop”. При этом скрипт завершается, сформированный список
выводится на экран.

Подсказка: для данного задания примем, что пользователь может вводить
только числа и строки. При вводе пользователем очередного элемента
необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить
пользователю ввести текст (не число) и отобразить соответствующее
сообщение. При этом работа скрипта не должна завершаться.
'''


class NonIntListError(Exception):
    def __str__(self):
        return 'NonIntListError: please add only numbers value!'


class ExtraList(list):
    def append(self, value):
        if not re.search('^[0-9]+$', value):
            raise NonIntListError
        super().append(value)


if __name__ == '__main__':
    print(task)

    values = ExtraList()
    while True:
        try:
            value = input_value('Input value: ', '^.*$', str)
            if value == 'stop':
                print(values)
                break
            values.append(value)
        except NonIntListError as e:
            print(e)
