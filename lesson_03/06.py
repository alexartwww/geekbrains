from common import input_value

task = '''
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой.

Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''

def int_func(word):
    return (chr(ord(word[0:1]) - 32) if ord(word[0:1]) >= 97 and ord(word[0:1]) <= 122 else word[0:1]) + word[1:]

if __name__ == '__main__':
    print(task)

    print('abc', '=>', int_func('abc'))
    print('Abc', '=>', int_func('Abc'))
    print('klm', '=>', int_func('klm'))
    print('Klm', '=>', int_func('Klm'))
    print('zyx', '=>', int_func('zyx'))
    print('Zyx', '=>', int_func('Zyx'))

    words = input_value('Input [a-z ]+: ', '^[a-z ]+$', str)
    print(' '.join([int_func(word) for word in words.split()]))
