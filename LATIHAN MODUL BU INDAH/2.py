def mat(data):
    temp=[]
    if len(data)==len(data[0]):
        for a in range (len(data)):
            temp.append(data[a][a])
        return temp
    else:
        return False
bilangan=[[1,2,3],[4,5,6],[7,8,9]]
print(mat(bilangan))
        