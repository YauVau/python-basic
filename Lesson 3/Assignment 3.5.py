
summary = 0

def my_func():
    global summary
    while True:
        str = input("Enter numbers split by space: ")
        str = str.split()

        for i in str:
            try:
                i = int(i)
            except ValueError:
                print(summary)
                return
            summary += i


my_func()