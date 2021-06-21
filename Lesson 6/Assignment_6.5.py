class Stationery:
  _title = ''
  def __init__(self, title):
    self._title = title

  def draw(self):
    raise NotImplementedError("Please Implement this method")


class Pen(Stationery):

  def __init__(self, title):
    super().__init__(title)

  def draw(self):
    print('hi, Im pen and Im blue')

class Handle(Stationery):

  def __init__(self, title):
    super().__init__(title)

  def draw(self):
    print('hi, Im Handle and Im fat')

class Pencil(Stationery):

  def __init__(self, title):
    super().__init__(title)

  def draw(self):
    print('hi, Im pencil and I can be erased')


stationery1 = Pen('pen')
stationery2 = Handle('handle')
stationery3 = Pencil('pencil')

stationery1.draw()
stationery2.draw()
stationery3.draw()