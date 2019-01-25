i = input("rows")
j = input("columns")
y=[]
for a in range(0, int(i)):
    x = []
    for b in range(0, int(j)):
        x.append(a*b)
    y.append(x)

print(y)


