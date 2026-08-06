def majorityelement(n):
    c={}
    for num in n:
        if num in c:
            c[num]+=1
        else:
            c[num]=1
    for key in c:
        if c[key]>len(n)//2:
            return key
n=[3,3,3,3,5,5,5,5,5,5,5,5]
print("majority element: ", majorityelement(n))                    