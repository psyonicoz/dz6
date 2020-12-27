from time import sleep


class Trafficlight:
    def __init__(self):
        self.color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 7}

    def running(self):
        while True:
            for key in self.color.keys():
                print(f'Сейчас горит {key}')
                sleep(self.color[key])


Trafficlight = Trafficlight()
Trafficlight.running()
