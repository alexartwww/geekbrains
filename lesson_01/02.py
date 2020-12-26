from common import input_value

task = '''
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''

if __name__ == '__main__':
    print(task)
    seconds = input_value('Input seconds: ', '^[0-9]+$', int)
    time = ':'.join(
        map(
            lambda x: str(x) if x >= 10 else '0' + str(x),
            (seconds // 3600,
             seconds % 3600 // 60,
             seconds % 3600 % 60)
        ))
    print(time)
