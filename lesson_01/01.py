from common import input_value

task = '''
Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.
'''

if __name__ == '__main__':
    print(task)
    a = 1
    b = 2.3445
    c = 'hello'
    d = True

    a = input_value('Input int: ', '^[0-9]+$', int)
    print(a)

    b = input_value('Input float: ', '^[0-9]+(\.[0-9]+)?$', float)
    print(b)

    c = input_value('Input str: ', '^.+$', str)
    print(c)

    d = input_value('Input bool: ', '^.*$', bool)
    print(d)
