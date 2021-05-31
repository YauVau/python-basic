print("Домашка 2")

####################
print("Задание 1")

my_list = [ 3, 14, 8.98, "Python", True, "Love my dog", [16, 8, 4] ]
print(my_list)
i = 0
while i < len(my_list):
    print(type(my_list[i]))
    i += 1

####################
print("Задание 2")
(my_list.append(input("Enter any value:")))
i = 0
print("reversed:")
while i < len(my_list) - 1:
    tmp = my_list[i]
    my_list[i] = my_list[i+1]
    my_list[i+1] = tmp
    i += 2

print(my_list)


####################
print("Задание 3")

#dict
usnum = int(input("Please, enter the number of the month:"))
m_dict =  { 1:"Зима", 12:"Зима", 2:"Зима", 3:"Весна", 4:"Весна", 5:"Весна", 6:"Лето", 7:"Лето", 8:"Лето", 9:"Осень", 10:"Осень", 11:"Осень"}
print(m_dict[usnum])

#list
m = int(input("Введите номер месяца: "))
n = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
i=m-1
print (n[i])

####################
print("Задание 4")

words = input("Enter any word(s): ")
wrd = words.split( )

for count, word in enumerate(wrd, 1):
    print(count, word[:9])

####################
print("Задание 5")
my_list = [7, 5, 3, 3, 2]
mm = int(input("enter the integer:"))

for i in range(len(my_list)):
    if mm > my_list[i]:
        my_list.insert(i, mm)
        break
print(my_list)
