from common import input_value

task = '''
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
'''

if __name__ == '__main__':
    print(task)

    n = input_value('Input n: ', '^[0-9]{1}$', str)

    print(int(n * 1) + int(n * 2) + int(n * 3))
