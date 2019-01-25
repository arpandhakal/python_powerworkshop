a = input("a dog's age in human year")
age = 0
for i in range(1, int(a)+1):
    if not i<=2:
        age = age+4
    else:
        age = age+10.5
print("The dogs age in dogs year is", age)
