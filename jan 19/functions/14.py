def digit_sum(x):
    t=0
    for i in range(0,len(str(x))):
        t=t+(x%10)
        x=x//10
        if x ==0:
            break
    return t
a=int(input("number"))
print("sum of the digits",digit_sum(a))
