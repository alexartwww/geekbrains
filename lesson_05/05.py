task = '''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

if __name__ == '__main__':
    print(task)

    numbers = [10, 20, 30, 11, 22, 33, 21, 22, 23, 45, 65, 89, 94]

    try:
        with open('05.file.txt', 'w') as f_out:
            f_out.write(' '.join([str(num) for num in numbers]))

        with open('05.file.txt', 'r') as f_out:
            line = next(f_out)
            print('SUM From script ', sum([num for num in numbers]))
            print('SUM From file ', sum([int(num) for num in line.split()]))

    except IOError as err:
        print(f'Ошибка {err}!')
