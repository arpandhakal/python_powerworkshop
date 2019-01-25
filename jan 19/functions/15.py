def count(string):
    low = 0
    up = 0

    for s in string:
        if s.isupper():
            up += 1
        elif s.islower():
            low += 1

    print ("No. of Upper case characters :",up)
    print("No. of lower case characters :", low)

a=input("string")
count(a)
