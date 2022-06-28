def dictionary(data):
    temp={}
    for a in data:
        if a=="":
            a = "spasi"
        temp[a]=1
        if temp[a] in temp.keys():
            temp[a]+=1
    print(temp)

    for b in temp.keys():
        return temp[b]
kalimat='salmatul farida'
print(dictionary(kalimat))