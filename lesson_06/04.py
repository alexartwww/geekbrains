task = '''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False

    def go(self):
        print('Car ', self.name, ' color ', self.color, ' is_police', self.is_police, ' is going now')

    def stop(self):
        print('Car ', self.name, ' color ', self.color, ' is_police', self.is_police, ' stops now')

    def turn(self, direction):
        print('Car ', self.name, ' color ', self.color, ' is_police', self.is_police, ' turns on ', direction,
              ' direction')

    def show_speed(self):
        print('Car ', self.name, ' color ', self.color, ' is_police', self.is_police, ' speed = ', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Car ', self.name, ' color ', self.color, ' is_police', self.is_police, ' BREAKS SPEED LIMIT!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Car ', self.name, ' color ', self.color, ' is_police', self.is_police, ' BREAKS SPEED LIMIT!')


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)
        self.is_police = True


if __name__ == '__main__':
    print(task)

    police_car = PoliceCar('Полиция', 'Синий', 120)
    work_car = WorkCar('Рабочая', 'Серебристый', 39)
    town_car = TownCar('Городская', 'Черная', 65)
    sport_car = SportCar('Спортивная', 'Красная', 320)

    police_car.go()
    police_car.turn('Left')
    police_car.stop()
    police_car.show_speed()

    work_car.go()
    work_car.turn('Right')
    work_car.stop()
    work_car.show_speed()

    town_car.go()
    town_car.turn('Left')
    town_car.stop()
    town_car.show_speed()

    sport_car.go()
    sport_car.turn('Right')
    sport_car.stop()
    sport_car.show_speed()

