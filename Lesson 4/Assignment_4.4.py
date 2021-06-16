primary_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

#убираем повторы
# primary_list.sort()
secondary_list = [ j for i, j in enumerate(primary_list) if j != primary_list[i-1] and i > 0 ]

print(secondary_list)

#убираем все цифры, которые имели повторения
secondary_list = [j for i, j in enumerate(primary_list) if j not in primary_list[i+1:] and j not in primary_list[:i]]

print(secondary_list)