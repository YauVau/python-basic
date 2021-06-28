dictionary = {}
with open('File_7', 'r', encoding="utf-8") as f:
    average_profit = 0
    firm_count = 0
    for line in f:
        tmp_income = float(line.split()[2])-float(line.split()[3])
        dictionary[line.split()[0]] = tmp_income
        if tmp_income > 0:
            firm_count += 1
            average_profit += tmp_income
    average_profit = average_profit // firm_count

    print(dictionary)
    print("average profit: ", average_profit)

file = open('File_7.1.json', 'w', encoding="utf-8")
with open('File_7.1.json', 'w+', encoding="utf-8") as f:
    f.write(f"{[dictionary, {'average profit' : average_profit}]}\n")