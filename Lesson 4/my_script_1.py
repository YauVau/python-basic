def workers_salary():
    x = int(input("enter hours: "))
    y = int(input("rate per hour: "))
    z = int(input("bonus: "))
    return x * y + z
print(workers_salary())