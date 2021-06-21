class Road():
    cementKgPerOneCm = 25
    _length = 0
    _width = 0
    _h = 0

    def __init__(self, length, width, h):
        self._length = length
        self._width = width
        self._h = h

    def calculate(self):
        return Road.cementKgPerOneCm * self._length * self._width * self._h


road = Road(5000, 20, 5)
print(road.calculate())