file = open('File_5.txt', 'w', encoding="utf-8")
with open('File_5.txt', 'w+', encoding="utf-8") as f:
    text = input("Enter any numbers split by space: ")
    f.write(f"{text}\n")
    summed = 0
    numb = text.split(" ")
    for i in numb:
        print(i)
        summed += int(i)
    print(summed)
