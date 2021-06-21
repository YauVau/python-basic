import time

class TrafficLight():
  __color = 'red'

  def running(self):
    self.__color = 'red'
    self.__printStatus()
    time.sleep(7)
    self.__color = 'yellow'
    self.__printStatus()
    time.sleep(2)
    self.__color = 'green'
    self.__printStatus()
    time.sleep(10)
    self.__color = 'red'


  def __printStatus(self):
    print('Traffic light is ' + self.__color)


traf = TrafficLight();
traf.running()