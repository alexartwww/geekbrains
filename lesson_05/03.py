task = '''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''

if __name__ == '__main__':
    print(task)

    data = []
    try:
        with open('03.file.tsv') as f:
            for line in f:
                name, salary = line[:-1].split('\t')
                data.append({'name': name, 'salary': int(salary)})
    except IOError as err:
        print(f'Ошибка {err}!')

    less_then_20000 = [employee['name'] for employee in data if employee['salary'] < 20000]
    print(less_then_20000)

    print('Avarage salary: ', sum([employee['salary'] for employee in data]) / len(data))
