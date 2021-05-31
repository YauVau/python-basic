print("Задание 6")

km_day_a = float(input("Enter the distance you run on Day 1"))
distance = float(input("Which distance would you like to run (in km)?"))
days = 1
while km_day_a <= distance:
    km_day_a = km_day_a * 1.1
    days += 1
print(f"You will run {distance} km in {days} days. Good luck!")