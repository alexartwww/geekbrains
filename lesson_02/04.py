from common import input_value

task = '''
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово
с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только
первые 10 букв в слове.
'''

if __name__ == '__main__':
    print(task)

    string = input_value('Input str: ', '^.+$', str)

    print('\n'.join(map(lambda x: x if len(x) <= 10 else x[0:10], string.split())))
