from math import factorial
n = int(input("Enter the number: "))
def my_fact(num):
    factor = 1;
    for i in range(1,n):
        factor *= i
        yield factor

for i in my_fact(n):
    print (i)
