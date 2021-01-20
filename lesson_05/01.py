from common import input_value, readfile

task = '''
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''

if __name__ == '__main__':
    print(task)

    with open('01.file.txt', 'w') as file:
        while True:
            string = input_value('Type a string: ', '^.*$', str)
            if string == '':
                break
            file.write(string + '\n')

    print('================')
    print(readfile('01.file.txt'))
