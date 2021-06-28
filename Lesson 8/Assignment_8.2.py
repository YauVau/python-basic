class ZeroDivision(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'ZeroDivision, {0} '.format(self.message)
        else:
            return 'ZeroDivision has been raised'



try:
  1/0
except ValueError:
  raise ZeroDivision()