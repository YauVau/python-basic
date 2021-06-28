file = open('File_1.txt', 'w', encoding="utf-8")
with open('File_1.txt', 'w+', encoding="utf-8") as f:
    while True:
        line = input("Enter any text, if not - enter space: ")
        if line == " ":
            break
        elif not line:
            break
        f.write(f"{line}\n")
        print(line)
print ("stopped")
