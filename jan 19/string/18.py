def char(s):
    dic = {}
    for n in s:
        keys = dic.keys()
        if n in keys:
            dic[n] += 1
        else:
            dic[n] = 1
    return dic
a=input("string")
print(char(a))