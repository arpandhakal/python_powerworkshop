def max(a,b,c):
    if a>b and a>c :
        print("maximum Number=",a)
    elif b>a and b>c:
        print("maximum Number=",b)
    elif a==b:
        print(a,"=",b)
    elif a==c:
         print(a,"=",c)
    elif b==c:
        print(b,"=",c)
    else:
        print("maximum Number=",c)
max(2,3,8)