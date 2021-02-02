task = '''
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании.

Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру,
например словарь.
'''


class Storage(list):
    def append(self, value):
        if isinstance(value, Technics):
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
    storage.append(scanner)
    storage.append(copier)
    storage.append(copier2)
    print(storage)

    print(storage.get_stats())
