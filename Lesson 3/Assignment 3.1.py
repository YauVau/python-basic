def my_f (s_1, s_2):
   try:
       sub= s_1 / s_2
       return sub
   except ZeroDivisionError:
       print("Error! No zero division possible")


print(my_f(int(input("Enter numerator: ")), int(input("Enter denumenator: "))))
