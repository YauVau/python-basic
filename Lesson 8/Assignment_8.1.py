import datetime

class Date:
  @staticmethod
  def isValidDate(date):
    day,month,year = date.split('-')
    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False

    if(isValidDate) :
        print ("Input date is valid .")
    else :
        print ("Input date is not valid.")

Date.isValidDate('12-33-2022')