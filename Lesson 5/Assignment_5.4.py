#тут тоже не сразу поняла
d = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open("File_4.1", "r", encoding="utf-8") as f:
    with open("File_4.2", "w", encoding="utf-8") as f2:
        for line in f:
            en, *num = line.split()
            ru = d[en]
            f2.writelines(' '.join([ru] + num) + '\n')

