from common import input_value

task = '''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
'''


class MyZeroDivisionError(ZeroDivisionError):
    def __str__(self):
        return 'MyZeroDivisionError'


class NewInt(int):
    def __truediv__(self, value):
        if value == NewInt(0):
            raise MyZeroDivisionError
        return NewInt(int.__truediv__(self, value))


if __name__ == '__main__':
    print(task)

    while True:
        try:
            a = input_value('Input int A: ', '^[0-9]+$', NewInt)
            b = input_value('Input int B: ', '^[0-9]+$', NewInt)

            print(a / b)
            break
        except MyZeroDivisionError as e:
            print(e)
