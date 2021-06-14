print("Задание 5")
my_list = [7, 5, 3, 3, 2]
m = int(input("enter the integer:"))

for i in range(len(my_list)):
    if m > my_list[i]:
        my_list.insert(i, m)
        break
print(my_list)