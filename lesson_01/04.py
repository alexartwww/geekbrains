from common import input_value

task = '''
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

if __name__ == '__main__':
    print(task)
    number = input_value('Input number: ', '^[0-9]+$', int)

    max = 0
    current = 10
    while number > 0:
        if number % 10 > max:
            max = number % 10
        number = number // 10

    print(max)
