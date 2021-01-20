task = '''
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
количества строк, количества слов в каждой строке.
'''


if __name__ == '__main__':
    print(task)

    try:
        with open('02.file.txt') as f:
            num = 0
            for line in f:
                num += 1
                print('Строка: ', line[:-1], '; Слов: ', len(line.split()))
            print('Строк всего: ', num)
    except IOError as err:
        print(f'Ошибка {err}!')
