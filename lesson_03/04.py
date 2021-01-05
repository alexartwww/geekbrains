from common import input_value

task = '''
Программа принимает действительное положительное число x и целое отрицательное
число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо
реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись
без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень
с помощью оператора **. Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
'''


def my_func(x, y):
    ''' second variant '''

    def prod(vars):
        ''' there is not build-in function like sum :('''
        result = 1
        for var in vars:
            result = result * var
        return result

    if y == 0:
        return 1

    return prod([x if y > 0 else 1 / x for _ in range(abs(y))])


if __name__ == '__main__':
    print(task)

    x = input_value('Input x: ', '^\-?[0-9]+(\.[0-9]+)?$', float)
    y = input_value('Input y: ', '^\-?[0-9]+$', int)
    print(my_func(x, y))
