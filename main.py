from csv import reader

list1 = []
sum1 = 0
elf_id = 0
# open file in read mode
with open('calories.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        if len(row) > 0:
            list1.append(row)
        else:
            elf_id += 1
            print("Elf:" + str(elf_id))
            for i in list1:
                print(i)
            list1.clear()