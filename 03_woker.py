class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход с учётом премии: {sum(self._income.values())}')


a = Position('Кирилл', 'Кириллов', 'менеджер', 22500, 500)
a.get_full_name()
a.get_total_income()
