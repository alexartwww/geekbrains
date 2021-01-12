from common import input_value

task = '''
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем
месте. Для заполнения списка элементов необходимо использовать функцию input().
'''

if __name__ == '__main__':
    print(task)

    num = input_value('Input number of values: ', '^[0-9]+$', int)

    values = []
    while len(values) < num:
        value = input_value('Input value: ', '^.+$', str)
        values.append(value)

    print(values)

    for i in range(len(values) // 2):
        values[i * 2], values[i * 2 + 1] = values[i * 2 + 1], values[i * 2]

    print(values)
