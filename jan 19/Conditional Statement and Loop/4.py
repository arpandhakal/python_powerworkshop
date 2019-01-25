numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
o=0
e=0
for i in range(0,12):
    if (numbers[i] % 2 ==0):
        e=e+1
    else:
        o=o+1

print("the number of even numbers are",e)
print("the number of odd numbers are",o)
