task = '''
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
“Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод
для каждого экземпляра.
'''


class Stationery:
    def __init__(self):
        self.title = 'Stationery'

    def draw(self):
        print(self.title, ' is drawing')


class Pen(Stationery):
    def __init__(self):
        super().__init__()
        self.title = 'Pen'

    def draw(self):
        print('Pen is drawing')


class Pencil(Stationery):
    def __init__(self):
        super().__init__()
        self.title = 'Pencil'

    def draw(self):
        print('Pencil is drawing')


class Handle(Stationery):
    def __init__(self):
        super().__init__()
        self.title = 'Handle'

    def draw(self):
        print('Handle is drawing')


if __name__ == '__main__':
    print(task)

    stationery = Stationery()
    pen = Pen()
    pencil = Pencil()
    handle = Handle()

    stationery.draw()
    pen.draw()
    pencil.draw()
    handle.draw()
