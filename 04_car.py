class Car:
    def __init__(self, speed, color, name, is_police: bool = None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police is True:
            self.is_police = 'Полиция'
        else:
            self.is_police = 'Гражданская'

    def go(self):
        if self.speed > 0:
            print('Машина едет')
        else:
            print('Машина не едет')

    def stop(self, stop):
        if stop == 'Стоп':
            self.speed = 0
            print('Останавливаем машину')
        else:
            print('Продолжаем движение')

    def turn_directions(self, direction):
        if direction in ('Налево', 'Направо'):
            print(f'Машина поворачивает {direction}')
        else:
            print(f'Направление непонятно')

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed}км/ч')

    def print(self):
        print(f'{self.speed} {self.color} {self.name} {self.is_police}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости: на {self.speed - 60}км/ч')
        else:
            print(f'Скорость в данный момент: {self.speed}км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости: на {self.speed - 40}км/ч')
        else:
            print(f'Скорость в данный момент: {self.speed}км/ч')


class PoliceCar(Car):
    pass


a = TownCar(70, 'жёлтый', 'приус', True)
a.print()
a.go()
a.show_speed()
a.turn_directions('Направо')
a.turn_directions('пиу')
a.stop('Стоп')
a.show_speed()
a.go()
