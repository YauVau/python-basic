from functools import reduce
first_list = [el for el in range(100, 1001) if el % 2 == 0]
print(first_list)

# если требовалось перемножить 
multiply_all = reduce(lambda x,y: x * y, first_list)
print(multiply_all)

# на случай если имелось в виду сумировать а не перемножить
sum_all = reduce(lambda x,y: x + y, first_list)
print(sum_all)