import re

task = '''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''


class Date:
    instances = []

    def __init__(self, date_string):
        self.date_string = date_string
        self.__class__.instances.append(self)

    @classmethod
    def extract_date(cls):
        for instance in cls.instances:
            test = re.findall('^(\d{4})-(\d{2})-(\d{2})$', instance.date_string)
            if test:
                return int(test[0][0]+test[0][1]+test[0][2])

    @staticmethod
    def validate_date():
        for instance in Date.instances:
            test = re.findall('^(\d{4})-(\d{2})-(\d{2})$', instance.date_string)
            if test:
                year = int(test[0][0])
                month = int(test[0][1])
                day = int(test[0][2])
                correct_days = {
                    1: 31,
                    2: 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28,
                    3: 31,
                    4: 30,
                    5: 31,
                    6: 30,
                    7: 31,
                    8: 31,
                    9: 30,
                    10: 31,
                    11: 30,
                    12: 31,
                }
                if month < 1 or month > 12 or day < 1 or day > correct_days[month]:
                    return False
        return True


if __name__ == '__main__':
    print(task)

    dt = Date('2020-02-29')
    print(Date.extract_date())
    print(Date.validate_date())
