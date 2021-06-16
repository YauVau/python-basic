primary_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

secondary_list = [j for i, j in enumerate(primary_list) if j > primary_list[i-1] and i > 0 ]
print (secondary_list)