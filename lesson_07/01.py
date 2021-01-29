task = '''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31  22
37  43
51  86

 3   5  32
 2   4   6
-1  64  -8

3  5  8  3
8  3  7  1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки
второй матрицы и т.д.
'''


class MatrixSizeMismatchException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.width = len(matrix[0])
        self.height = len(matrix)

    def __str__(self):
        result = ''
        for line in self.matrix:
            for num in line:
                result += '%4s' % num
            result += '\n'
        return result

    def __add__(self, other):
        if self.width != other.width or self.height != other.height:
            raise MatrixSizeMismatchException('Matrix Size Mismatch! ' + ' Original: ' + str(self.width) + 'x' + str(
                self.height) + ' != Other: ' + str(other.width) + 'x' + str(other.height))

        new_matrix = Matrix([[0 for _ in range(self.width)] for j in range(self.height)])
        for i, _ in enumerate(self.matrix):
            for j, _ in enumerate(self.matrix[i]):
                new_matrix.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return new_matrix


if __name__ == '__main__':
    print(task)

    a = Matrix([
        [31, 22],
        [37, 43],
        [51, 86]
    ])

    b = Matrix([
        [3, 2],
        [1, 4],
        [5, 7]
    ])

    print('A =')
    print(a)
    print('B =')
    print(b)

    print('A + B =')
    print(a + b)
