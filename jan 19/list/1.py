num = int(input("Enter number of items in the list: "))
list_1 = []
for i in range(num):
    item = int(input("Enter item: "))
    list_1.append(item)
sum_items = 0
for i in list_1:
    sum_items += i
print("the sum of all the items in the list {list_1} is : {sum_items}")