task = '''
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
'''


class Storage(list):
    def append(self, value):
        if isinstance(value, Technics):
            super().append(value)

    def append_num(self, value, num):
        if isinstance(value, Technics) and isinstance(num, int):
            for _ in range(num):
                super().append(value)

    def __str__(self):
        return '; '.join([str(item) for item in self])

    def get_stats(self):
        result = {}
        for item in self:
            if item.get_type() in result:
                result[item.get_type()] += 1
            else:
                result[item.get_type()] = 1
        return result


class Technics:
    def __init__(self, brand, name):
        self.type = 'Unknown'
        self.brand = brand
        self.name = name

    def get_type(self):
        return self.type

    def __str__(self):
        return self.type + ' ' + self.brand + ' ' + self.name


class Printer(Technics):
    def __init__(self, brand, name, paper_amount):
        super().__init__(brand, name)
        self.type = 'Printer'
        self.paper_amount = paper_amount

    def __str__(self):
        return self.type + ' ' + self.brand + ' ' + self.name + ' paper_amount = ' + str(self.paper_amount)


class Scanner(Technics):
    def __init__(self, brand, name, color_depth):
        super().__init__(brand, name)
        self.type = 'Scanner'
        self.color_depth = color_depth

    def __str__(self):
        return self.type + ' ' + self.brand + ' ' + self.name + ' paper_amount = ' + str(self.color_depth)


class Copier(Technics):
    def __init__(self, brand, name, speed):
        super().__init__(brand, name)
        self.type = 'Copier'
        self.speed = speed

    def __str__(self):
        return self.type + ' ' + self.brand + ' ' + self.name + ' paper_amount = ' + str(self.speed)


if __name__ == '__main__':
    print(task)

    storage = Storage()
    printer = Printer('HP', 'LaserJet P1005', 500)
    scanner = Scanner('Canon', 'Lide 110', 24)
    copier = Copier('HP', 'LaserJet Pro M521dn', 2.5)
    copier2 = Copier('HP', 'LaserJet Pro 2321', 1.5)
    storage.append(printer)
    storage.append_num(scanner, 32)
    storage.append_num(copier, 23)
    storage.append(copier2)
    print(storage)

    print(storage.get_stats())
