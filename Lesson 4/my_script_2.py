from itertools import count
from itertools import cycle

a = int(input("Enter the number to start with: "))
b = int(input("Enter the step count: "))

for el in count(a,b):
    if el >= 30000:
        break
    print(el)



c = 0
for choice in cycle(" END "):
    if c > 14:
        break
    print(choice)
    c +=1