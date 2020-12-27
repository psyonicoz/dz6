class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


a = Stationery('канцелярия')
a.draw()
b = Pen('карандаш')
b.draw()
c = Pencil('ручка')
c.draw()
d = Handle('маркер')
d.draw()
