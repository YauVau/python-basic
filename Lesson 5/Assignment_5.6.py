import re

dict = {}
with open('File_6', 'r', encoding='utf-8') as file :
    for line in file:
        # print(line)
        line_array = line.split(' ')
        summa = 0
        for i in line_array[1: ]:
            summa += int(re.search(r'\d+', i).group())
        print(summa)
        dict [line_array[0]] = summa
print(dict)
