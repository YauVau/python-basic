# one row solution
first_gen = (num for num in range(20,240) if num % 20 == 0 or num % 21 == 0 )
# вывод
for num in first_gen:
    print(num)