task = '''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func(var1, var2, var3):
    vars = [var1, var2, var3]
    vars.sort(reverse=True)
    return sum(vars[0:2])

if __name__ == '__main__':
    print(task)
    print(my_func(1, 2, 3))
