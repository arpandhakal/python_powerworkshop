import string
import re
a = input("enter a string")
f1=0
while True:
    if (len(a)<=4) or (len(a)>=16):
        f1=-1
        break
    elif not re.search("[a-z]",a):
        f1=-1
        break
    elif not re.search("[A-Z]",a):
        f1=-1
        break
    elif not re.search("[0-9]",a):
        f1=-1
        break
    elif not re.search("[@#$]",a):
        f1=-1
        break
    else:
        f1=0
        print("password is valid")
        break
if f1==-1:
    print("password is not valid")

