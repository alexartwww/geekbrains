task = '''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.

Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
полученного результата.
'''


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        new_coplex = Complex(0, 0)
        new_coplex.real = self.real + other.real
        new_coplex.img = self.img + other.img
        return new_coplex

    def __sub__(self, other):
        new_coplex = Complex(0, 0)
        new_coplex.real = self.real - other.real
        new_coplex.img = self.img - other.img
        return new_coplex

    def __mul__(self, other):
        new_coplex = Complex(0, 0)
        new_coplex.real = self.real * other.real - self.img * other.img
        new_coplex.img = self.img * other.real + self.real * other.img
        return new_coplex

    def __truediv__(self, other):
        new_coplex = Complex(0, 0)
        new_coplex.real = (self.real * other.real + self.img * other.img) / (other.real ** 2 + other.img ** 2)
        new_coplex.img = (self.img * other.real - self.real * other.img) / (other.real ** 2 + other.img ** 2)
        return new_coplex

    def __str__(self):
        if self.real == 0 and self.img == 0:
            return '0'
        elif self.real == 0:
            return str(self.img) + 'i'
        elif self.img == 0:
            return str(self.real)
        else:
            return str(self.real) + ' + ' + str(self.img) + 'i'


if __name__ == '__main__':
    print(task)

    a = Complex(1, 2)
    b = Complex(2, 2)

    print(a / b)
