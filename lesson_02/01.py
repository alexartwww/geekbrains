task = '''
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''

if __name__ == '__main__':
    print(task)

    data = [32, 3.14, True, 'string', [2,3,4], {'a': 1, 'b': 2, 3: 3}, (1,2,3), {1,2,3}, frozenset({2,3,4})]

    types = [int, float, bool, str, list, dict, tuple, set, frozenset]

    for i, value in enumerate(data):
        print("{} is {}".format(value, types[i]) if type(value) == types[i] else "{} is not {}".format(value, types[i]))
