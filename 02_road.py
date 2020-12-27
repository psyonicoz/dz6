class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.thickness = 5

    def roadbed_weight(self):
        rb_weight = self._length * self._width * self.weight * self.thickness / 1000
        print(f'Вам понадобится {rb_weight:.0f} тон асфальта')


tarmac_weight = Road(5000, 20)
tarmac_weight.roadbed_weight()
