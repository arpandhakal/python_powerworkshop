num = int(input("Enter number of items in the list: "))
list_1 = []
for each in range(num):
    item = input("Enter item: ")
    list_1.append(item)
count = 0
for each in list_1:
    if len(each) >= 2 and each[0] == each[len(each)-1]:
        count += 1
print("{count}")