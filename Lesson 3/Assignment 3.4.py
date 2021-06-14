def my_func (x, y):
    y *= -1
    i=0
    n=1
    while i < y:
        n *= x
        i +=1
        if i == y:
            return 1/n

print(my_func(int(input("enter positive integer: ")), int(input("enter negative integer: "))))