class Worker():
  _name = ''
  _surname = ''
  _position = ''
  _income = { 'wage': 0, 'bonus': 0}
  def __init__(self, name, surname, position, income):
    self._name = name
    self._surname = surname
    self._position = position
    self._income = income

class Position(Worker):
  def __init__(self, name, surname, position, income):
    super().__init__(name, surname, position, income)

  def get_full_name(self):
    return 'Full name:' + self._name + ' ' + self._surname

  def get_total_income(self):
    return 'Total income is ' + str(self._income['wage'] + self._income['bonus'])



worker = Position('Jane', 'Volchok', 'Wife', { 'wage': 100000, 'bonus': 50000})

print(worker.get_full_name())
print(worker.get_total_income())