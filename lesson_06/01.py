task = '''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''


class TrafficLight:
    def __init__(self):
        self.__color = 'красный'

    def running(self, second):
        if second < 7:
            self.__color = 'красный'
        elif second >= 7 and second < 9:
            self.__color = 'желтый'
        else:
            self.__color = 'зеленый'

    def get_color(self):
        return self.__color


if __name__ == '__main__':
    print(task)

    traffic_light = TrafficLight()

    for second in range(0,20):
        traffic_light.running(second)
        print('Second = ',second, ' Color = ', traffic_light.get_color())

