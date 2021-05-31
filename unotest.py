print("Домашка 1")
####################
print("Задание 1")
name = input ("Please, enter your name")
fname = input("Please, enter your family name")
age = int(input("Please, enter your age "))

print(f"Congratulations,  {name} {fname}! Happy {age}!")

####################
print("Задание 2")
seconds = int(input("Enter time in seconds: "))
time_sec = seconds % 60
minutes = seconds // 60
time_min = minutes % 60
time_hou = minutes// 60
print(f" {time_hou}:{time_min}:{time_sec}")

####################
print("Задание 3")
r_numb = int(input("Enter a random number 1-9: "))
#we multiply the numbers and add them
res = r_numb + r_numb * r_numb + r_numb * r_numb * r_numb
print(f"result:{res}")

####################
print("Задание 4")
num_a = int(input("Enter last 4 digits of your phone number: "))
num_b = 1
num_max = 1

while True:
    num_b = num_a % 10
    num_a = num_a // 10
    if num_b >= num_max:
        num_max = num_b
    break

print (f"Bigest number is {num_max}")

####################
print("Задание 5")
revenue = int(input("Enter the revenue of the company in Euro"))
costs = int(input("Enter the costs of the company in Euro"))
profit = revenue - costs

if revenue > costs:
    print("Congrats, your company gets profit")
    print(f"Your profitability of proceeds equals {profit/revenue} Euro")
else:
    print("You better take a look on your company finances - your business seems to be unprofitable ")

employees = int(input("How many people are employed?"))
print(f"The approximate revenue per employee is {profit/employees} Euro")

####################
print("Задание 6")

km_day_a = float(input("Enter the distance you run on Day 1"))
distance = float(input("Which distance would you like to run (in km)?"))
days = 1
while km_day_a <= distance:
    km_day_a = km_day_a * 1.1
    days += 1
print(f"You will run {distance} km in {days} days. Good luck!")