from common import input_value

task = '''
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При
нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
специальный символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
'''

def sum_symbols():
    summa = 0
    while True:
        words = input_value('Input numbers or ! to exit: ', '^.+$', str)
        current_number = ''
        for symbol in words:
            if ord(symbol) >= 48 and ord(symbol) <= 57:
                current_number = current_number + symbol
            if ord(symbol) == 32 or ord(symbol) == 33:
                summa = summa + int(current_number)
                print('Sub sum = ', summa)
                current_number = ''
                if ord(symbol) == 33:
                    return summa


if __name__ == '__main__':
    print(task)

    print('Sum = ', sum_symbols())
