def createList (size):
    datalist = []
    for i in range (size):
        print('Masukkan datalist ke - ',i,end=' : ')
        datalist.append(int(input()))
    return datalist

def avgList (size):
    return sum(size)/len(size)

def addList(x,y):
    if len(x) != len(y):
        return 'size List Tidak Sama'
    else:
        hasil = []
        for i in range(len(x)):
            hasil.append(x[i] + y[i])
        return hasil
data1 = createList(4)
print('Data - 1 = ',data1,'; rata-rata list = ',avgList(data1))
data2 = createList(5)
print('Data - 2 = ',data2,'; rata-rata list = ',avgList(data2))
hasil = addList(data1,data2)
print(data1,'+',data2,'=',hasil)