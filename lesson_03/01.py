from common import input_value

task = '''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления
на ноль.
'''


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


if __name__ == '__main__':
    print(task)

    a = input_value('Input a: ', '^[0-9]+(\.[0-9]+)?$', float)
    b = input_value('Input b: ', '^[0-9]+(\.[0-9]+)?$', float)

    print(divide(a, b))
