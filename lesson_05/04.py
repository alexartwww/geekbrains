task = '''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
'''

if __name__ == '__main__':
    print(task)

    dictionary = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восемь',
        'Nine': 'Девять',
        'Ten': 'Десять',
        'Eleven': 'Одиннадцать',
        'Twelve': 'Двенадцать',
        'Thirteen': 'Тринадцать',
        'Fourteen': 'Четырнадцать',
        'Fifteen': 'Пятнадцать',
        'Sixteen': 'Шестнадцать',
        'Seventeen': 'Семнадцать',
        'Eightteen': 'Восемнадцать',
        'Nineteen': 'Девятнадцать',
        'Twenty': 'Двадцать',
        'Thirty': 'Тридцать',
        'Fourty': 'Сорок',
        'Fifty': 'Пятьдесят',
        'Sixty': 'Шестьдесят',
        'Seventy': 'Семьдесят',
        'Eightty': 'Восемьдесят',
        'Ninety': 'Девяносто',
    }

    try:
        with open('04.file.txt', 'r') as f_in:
            with open('04.file.out.txt', 'w') as f_out:
                for line in f_in:
                    for eng in dictionary:
                        line = line.replace(eng, dictionary[eng])
                    f_out.write(line)
    except IOError as err:
        print(f' {err}')
