class Car:
    _speed = 0
    _color = ''
    _name = ''
    _is_police = False

    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self):
        print(self._name + ' started')

    def stop(self):
        print(self._name + ' stopped')

    def turn(self, direction):
        print(self._name + ' turned ' + direction)

    def show_speed(self):
        print(self._name + ' speed is ' + str(self._speed))


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if (self._speed > 60):
            print(self._name + ' is over speed limit - ' + str(self._speed))
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if (self._speed > 60):
            print(self._name + ' is over speed limit - ' + str(self._speed))
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


car = SportCar(300, 'red', 'lamba')

car.go()
car.show_speed()

car = WorkCar(100, 'red', 'chevrolet')

car.go()
car.show_speed()
car.stop()
car.turn('left')