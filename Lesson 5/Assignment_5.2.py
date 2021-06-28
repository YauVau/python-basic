
f = open('File_2')
line = 0
for i in f:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i, 'In the following line:', len(i), 'letters.', word, 'words.')

print('TOTAL: ', line, 'lines.')
f.close()