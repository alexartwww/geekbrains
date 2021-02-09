task = '''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).

В базовом классе определить параметры, общие для приведенных типов.

В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''


class Storage(list):
    def append(self, value):
        if isinstance(value, Technics):
            super().append(value)

    def __str__(self):
        return '; '.join([str(item) for item in self])


class Technics:
    def __str__(self):
        return self.brand + ' ' + self.name

    def __init__(self, brand, name):
        self.brand = brand
        self.name = name


class Printer(Technics):
    def __init__(self, brand, name, paper_amount):
        super().__init__(brand, name)
        self.paper_amount = paper_amount

    def __str__(self):
        return 'Printer ' + self.brand + ' ' + self.name


class Scanner(Technics):
    def __init__(self, brand, name, color_depth):
        super().__init__(brand, name)
        self.color_depth = color_depth

    def __str__(self):
        return 'Scanner ' + self.brand + ' ' + self.name


class Copier(Technics):
    def __init__(self, brand, name, speed):
        super().__init__(brand, name)
        self.speed = speed

    def __str__(self):
        return 'Copier ' + self.brand + ' ' + self.name


if __name__ == '__main__':
    print(task)

    storage = Storage()
    printer = Printer('HP', 'LaserJet P1005', 500)
    scanner = Scanner('Canon', 'Lide 110', 24)
    copier = Copier('HP', 'LaserJet Pro M521dn', 2.5)
    storage.append(printer)
    storage.append(scanner)
    storage.append(copier)
    print(storage)
