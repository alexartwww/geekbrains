from common import input_value

task = '''
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
'''

if __name__ == '__main__':
    print(task)

    season_list = [
        'Winter',
        'Winter',
        'Spring',
        'Spring',
        'Spring',
        'Summer',
        'Summer',
        'Summer',
        'Autumn',
        'Autumn',
        'Autumn',
        'Winter']
    season_dict = {
        0: 'Winter',
        1: 'Winter',
        2: 'Spring',
        3: 'Spring',
        4: 'Spring',
        5: 'Summer',
        6: 'Summer',
        7: 'Summer',
        8: 'Autumn',
        9: 'Autumn',
        10: 'Autumn',
        11: 'Winter',
    }

    month = input_value('Input month: ', '^(1|2|3|4|5|6|7|8|9|10|11|12)$', int)

    print('Season by list: ', season_list[month-1])
    print('Season by dict: ', season_dict[month-1])
